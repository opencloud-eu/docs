---
sidebar_position: 10
id: upgrade-9.1.x
title: Upgrade 9.1.x
description: Upgrading from OpenCloud 7.2.x to the Production release 9.1.x
draft: false
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Upgrading to OpenCloud 9.1.x

OpenCloud 9.1.x is the new Production release. This guide describes the direct upgrade from the previous Production release 7.2.x to 9.1.x.

An interim upgrade to the Rolling release 8.x.x is not required. This guide includes all changes from 8.x.x and 9.x.x that are relevant for the upgrade.

## Upgrade Paths

| Current version | Upgrade path                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| 7.2.x           | Upgrade directly to 9.1.x with this guide.                                                                         |
| 4.x             | Upgrade to 7.2.x first as described in [Upgrade 7.2.x](./upgrade-7.x.x.md). Then upgrade to 9.1.x with this guide. |

:::important

A direct upgrade from 4.x to 9.1.x is not supported. Upgrade to 7.2.x first and verify that the deployment works before you continue with 9.1.x.

:::

Use this guide together with the [Standard Upgrade Guide](../upgrade.md), which describes the general upgrade procedure. For more information about the release channels, see the [Release Lifecycle](../../../resources/lifecycle.md).

:::note

If you run the Rolling release 8.x.x, follow the [Upgrade 9.x.x](../rolling/upgrade-9.x.x.md) guide instead.

:::

## Before You Start

- Make sure that your deployment runs OpenCloud 7.2.x. If you run 4.x, see [Upgrade Paths](#upgrade-paths). Check the version that is currently running:

  ```bash
  docker compose images opencloud
  ```

- Create a complete backup of your configuration and data, see [Back Up Configuration and Data](../upgrade.md#back-up-configuration-and-data).
- Review the [OpenCloud release notes](https://github.com/opencloud-eu/opencloud/releases).
- Read the [breaking changes](#step-6-apply-the-breaking-changes) if you use custom settings in `opencloud.yaml`, custom thumbnail settings, custom email templates, web extensions, or an external reverse proxy.

## Step 1: Update the `opencloud-compose` Checkout

Update your local copy of the `opencloud-compose` repository as described in [Update the opencloud-compose Checkout](../upgrade.md#update-the-opencloud-compose-checkout).

## Step 2: Set the New Version

Set the Production image and the new version in your `.env` file:

```env
OC_DOCKER_IMAGE=opencloudeu/opencloud
OC_DOCKER_TAG=9.1.x
```

Replace `9.1.x` with the exact image tag of the version you want to install. Available tags are listed on [Docker Hub](https://hub.docker.com/r/opencloudeu/opencloud/tags).

Pull the new image:

```bash
docker compose pull opencloud
```

## Step 3: Migrate the Configuration

OpenCloud 9.1.x adds new settings to `opencloud.yaml`. Create and apply the configuration patch with the 9.1.x image before you start OpenCloud.

Stop OpenCloud:

```bash
docker compose down
```

Open a shell in a temporary container with your configuration volume:

<Tabs groupId="volume-type">
  <TabItem value="named-volumes" label="Using Named Volumes" default>

```bash
docker run --rm -it --user 1000:1000 --entrypoint /bin/sh \
  -v <opencloud-config-volume>:/etc/opencloud \
  opencloudeu/opencloud:9.1.x
```

Replace `<opencloud-config-volume>` with the Docker volume that contains your OpenCloud configuration.

  </TabItem>
  <TabItem value="bind-mounts" label="Using Bind Mounts">

```bash
docker run --rm -it --user 1000:1000 --entrypoint /bin/sh \
  -v <path-to-your-config-directory>:/etc/opencloud \
  opencloudeu/opencloud:9.1.x
```

Replace `<path-to-your-config-directory>` with the host directory that contains your `opencloud.yaml`.

  </TabItem>
</Tabs>

Inside the container, create the patch, test it, and apply it:

```bash
cd /etc/opencloud
opencloud init --diff
patch --dry-run opencloud.yaml < opencloud.config.patch
patch opencloud.yaml < opencloud.config.patch
exit
```

Review the patch before you apply it, especially if you use custom settings in `opencloud.yaml`. Among other changes, the patch adds the `auth_guest.service_account` settings that are required for guest links.

For a detailed description of these steps, see [Verify Configuration Changes](../upgrade.md#verify-configuration-changes).

## Step 4: Start OpenCloud

Start OpenCloud with the new version:

```bash
docker compose up -d --remove-orphans
```

Check that OpenCloud is running:

```bash
docker compose ps opencloud
```

## Step 5: Rebuild the Search Index

As of OpenCloud 8.x.x, OpenCloud uses a new, versioned search index. After the upgrade, files that existed before are not found until you rebuild the index.

<Tabs groupId="search-backend">
  <TabItem value="bleve" label="Bleve (default)" default>

Rebuild the index:

```bash
docker compose exec opencloud opencloud search index --all-spaces --force-rescan --insecure
```

Verify that older files can be found in the Web Client. Then remove the old, unversioned Bleve index:

```bash
docker compose exec opencloud rm -r /var/lib/opencloud/search/bleve
```

If you configured a custom `SEARCH_ENGINE_BLEVE_DATA_PATH`, replace `/var/lib/opencloud/search` with the configured path.

  </TabItem>
  <TabItem value="opensearch" label="OpenSearch">

Rebuild the index:

```bash
docker compose exec opencloud opencloud search index --all-spaces --force-rescan --insecure
```

Verify that older files can be found in the Web Client. Then list the existing indexes and remove the old one:

```bash
curl "http://localhost:9200/_cat/indices/opencloud-resources*?v"
curl -X DELETE "http://localhost:9200/opencloud-resources"
```

  </TabItem>
</Tabs>

Re-indexing runs in the background while OpenCloud keeps working. On large installations, it can take some time. For details, see [Upgrade 8.x.x](../rolling/upgrade-8.x.x.md).

## Step 6: Apply the Breaking Changes

Check the following list and apply the changes that are relevant for your deployment:

| If you …                                                                | See                                                                    |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| use an external Nginx reverse proxy                                     | [Reverse Proxy](#reverse-proxy)                                        |
| set thumbnail settings via environment variables or YAML                | [Thumbnails](../rolling/upgrade-9.x.x.md#thumbnails)                   |
| run the OpenCloud services in separate containers                       | [Separate Containers](../rolling/upgrade-9.x.x.md#separate-containers) |
| want to enable guest links                                              | [Guest Links](../rolling/upgrade-9.x.x.md#guest-links)                 |
| set `GRAPH_SPACES_DEFAULT_QUOTA`                                        | [Space Quota](../rolling/upgrade-9.x.x.md#space-quota)                 |
| rely on the search results for personal space roots or `.space` folders | [Search](../rolling/upgrade-9.x.x.md#search)                           |
| use customized email templates                                          | [Email Templates](../rolling/upgrade-9.x.x.md#email-templates)         |
| use apps or web extensions                                              | [Web Extensions](../rolling/upgrade-9.x.x.md#web-extensions)           |

If none of these apply, no further changes are required.

### Reverse Proxy

Real-time collaborative editing in the OpenCloud Editor requires the Yjs service. If you have enabled Yjs and use an external Nginx reverse proxy, forward the `/yjs` WebSocket route.

Also check that WebDAV and the Office integration are still forwarded correctly.

For the required Nginx configuration, see [Proxy Config](../../../getting-started/container/docker-compose/docker-external-proxy.md#create-a-new-proxy-config).

## Step 7: Verify the Upgrade

Check that OpenCloud is running and that no errors are logged:

```bash
docker compose ps
docker compose logs --tail=200 opencloud
```

Then test the following functions:

- Sign in to the Web Client.
- Open, upload, and download files.
- Open Spaces, shares, and public links.
- Search for existing files.
- Check that previews are displayed.
- If enabled, invite a guest and check that the invitation email is delivered.

## Troubleshooting

### The OpenCloud Container Keeps Restarting

Check the logs:

```bash
docker compose logs --tail=40 opencloud
```

If the log contains `guestlinks: service_account_id must not be empty`, guest links are enabled but the configuration has not been migrated. Migrate the configuration as described in [Step 3: Migrate the Configuration](#step-3-migrate-the-configuration).

### Older Files Are Not Found by the Search

Rebuild the search index as described in [Step 5: Rebuild the Search Index](#step-5-rebuild-the-search-index).

### Previews Are Not Displayed

See [Previews Are Not Displayed](../rolling/upgrade-9.x.x.md#previews-are-not-displayed) in the Upgrade 9.x.x guide.

### The Upgrade Cannot Be Completed

Restore your backup and start OpenCloud 7.2.x again. If the issue persists, check the [common issues](../../../resources/common-issues/index.md) or open an issue on [GitHub](https://github.com/opencloud-eu/opencloud/issues).
