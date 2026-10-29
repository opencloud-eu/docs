---
sidebar_position: 14
id: upgrade-9.x.x
title: Upgrade 9.x.x
description: Upgrading to OpenCloud 9.x.x
draft: false
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Upgrading to OpenCloud 9.x.x

OpenCloud 9.x.x introduces guest links and a new thumbnail architecture. It also renames some settings and changes the default behavior of the search and the email templates. Some of these changes require manual steps during the upgrade.

This guide describes the version-specific steps for upgrading to OpenCloud 9.x.x. Use it together with the [Standard Upgrade Guide](./upgrade.md), which describes the general upgrade procedure.

:::important

OpenCloud 9.x.x is a Rolling release and is not intended for production environments. For more information, see the [Release Lifecycle](../../resources/lifecycle.md).

:::

## How to Use This Guide

The required steps depend on the version you are upgrading from:

| Current version | Upgrade path                                  | Guide                                   |
| --------------- | --------------------------------------------- | --------------------------------------- |
| 8.x.x           | Upgrade directly to 9.x.x.                    | [Upgrade from 8.x.x](#upgrade-from-8xx) |
| 7.x.x           | Upgrade to 8.x.x first, then upgrade to 9.x.x | [Upgrade from 7.x.x](#upgrade-from-7xx) |

1. Complete the steps in [Before You Start](#before-you-start).
2. Follow the upgrade guide for your current version.
3. Check the [Breaking Changes](#breaking-changes) that apply to your deployment.
4. [Verify the upgrade](#verify-the-upgrade).

## Before You Start

- Create a complete backup of your configuration and data, see [Back Up Configuration and Data](./upgrade.md#back-up-configuration-and-data).
- Check the version that is currently running:

  ```bash
  docker compose images opencloud
  ```

- Review the [OpenCloud 9.0.0 release notes](https://github.com/opencloud-eu/opencloud/releases).
- Read the [Breaking Changes](#breaking-changes) if you use custom settings in `opencloud.yaml`, custom thumbnail settings, custom email templates, web extensions, or an external reverse proxy.

## Upgrade from 7.x.x

We recommend not to skip OpenCloud 8.x.x. Upgrade to 8.x.x first, verify the deployment and the search, and then continue with 9.x.x.

### Step 1: Upgrade to 8.x.x

Set the latest 8.x.x version in your `.env` file, for example:

```env
OC_DOCKER_TAG=8.x.x
```

Replace `8.x.x` with the latest available 8.x.x version. Then pull the image and restart OpenCloud:

```bash
docker compose pull opencloud
docker compose up -d
```

### Step 2: Rebuild the Search Index

OpenCloud 8.x.x creates a new search index. Files that existed before the upgrade are not found until you rebuild the index:

```bash
docker compose exec opencloud opencloud search index --all-spaces --force-rescan --insecure
```

After you have verified that older files can be found in the Web Client, remove the old index. For the commands for Bleve and OpenSearch, see [Upgrade 8.x.x](./upgrade-8.x.x.md).

### Step 3: Check the Yjs Proxy Route

If you have enabled Yjs for real-time collaborative editing and use an external Nginx reverse proxy, forward the `/yjs` WebSocket route. For the required configuration, see [Proxy Config](../../getting-started/container/docker-compose/docker-external-proxy.md#create-a-new-proxy-config).

### Step 4: Continue With the Upgrade to 9.x.x

Check that OpenCloud 8.x.x is running without errors. Then follow the steps in [Upgrade from 8.x.x](#upgrade-from-8xx).

## Upgrade from 8.x.x

### Step 1: Upgrade to 9.x.x

Set the new version in your `.env` file:

```env
OC_DOCKER_TAG=9.0.0
```

Pull the new image and restart OpenCloud:

```bash
docker compose pull opencloud
docker compose up -d
```

OpenCloud 9.x.x starts with the existing 8.x.x configuration. Guest links stay disabled until you enable them.

### Step 2: Migrate the Configuration

OpenCloud 9.x.x adds new settings to `opencloud.yaml`. Create and apply the configuration patch with the 9.x.x image as described in [Verify Configuration Changes](./upgrade.md#verify-configuration-changes) in the Standard Upgrade Guide.

In short, open a shell in a temporary container with your configuration volume:

```bash
docker run --rm -it --user 1000:1000 --entrypoint /bin/sh \
  -v <opencloud-config-volume>:/etc/opencloud \
  opencloudeu/opencloud-rolling:9.0.0
```

Replace `<opencloud-config-volume>` with the Docker volume or bind mount that contains your OpenCloud configuration.

Inside the container, create the patch, test it, and apply it:

```bash
cd /etc/opencloud
opencloud init --diff
patch --dry-run opencloud.yaml < opencloud.config.patch
patch opencloud.yaml < opencloud.config.patch
```

The patch adds the `auth_guest.service_account` settings. Review the patch before you apply it, especially if you use custom thumbnail settings in `opencloud.yaml`.

:::important

The configuration migration is required before you enable guest links. Without the `auth_guest.service_account` settings, the `auth-guest` service does not start and the OpenCloud container keeps restarting.

:::

### Step 3: Apply the Breaking Changes

Check the following list and apply the changes that are relevant for your deployment:

| If you …                                                 | See                                         |
| -------------------------------------------------------- | ------------------------------------------- |
| set thumbnail settings via environment variables or YAML | [Thumbnails](#thumbnails)                   |
| run the OpenCloud services in separate containers        | [Separate Containers](#separate-containers) |
| want to enable guest links                               | [Guest Links](#guest-links)                 |
| set `GRAPH_SPACES_DEFAULT_QUOTA`                         | [Space Quota](#space-quota)                 |
| use customized email templates                           | [Email Templates](#email-templates)         |
| use apps or web extensions                               | [Web Extensions](#web-extensions)           |
| use an external reverse proxy with custom routes         | [Reverse Proxy](#reverse-proxy)             |

If none of these apply, no further changes are required.

### Step 4: Verify the Upgrade

Test your deployment as described in [Verify the Upgrade](#verify-the-upgrade).

## Breaking Changes

### Thumbnails

OpenCloud 9.x.x uses a new thumbnail architecture. The webdav service now handles thumbnail requests, selects the size, and manages the cache. The thumbnails service only generates the images.

Existing previews keep working. No action is required if you use the default settings.

#### Cache Directory

The cache moves from `thumbnails/files` to `thumbnails/cache` and is created automatically. The cache starts empty after the upgrade and is refilled as previews are requested.

The old `thumbnails/files` folder is no longer used. After you have verified that previews are displayed, you can remove it:

```bash
docker compose exec opencloud rm -r /var/lib/opencloud/thumbnails/files
```

If you configured a custom `OC_BASE_DATA_PATH`, replace `/var/lib/opencloud` with the configured path.

:::caution

If you mounted a separate volume directly at `thumbnails/files`, set `WEBDAV_THUMBNAILS_CACHE_DIR` to that mount point. Otherwise the new cache is written next to the volume.

:::

#### Environment Variables

Old `THUMBNAILS_*` variable names are still read. We recommend to switch to the new names:

| Old variable                           | New variable                              |
| -------------------------------------- | ----------------------------------------- |
| `THUMBNAILS_RESOLUTIONS`               | `WEBDAV_THUMBNAILS_RESOLUTIONS`           |
| `THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE` | `OC_THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE` |
| `THUMBNAILS_TXT_FONTMAP_FILE`          | `WEBDAV_THUMBNAILS_TXT_FONTMAP_FILE`      |
| `THUMBNAILS_FILESYSTEMSTORAGE_ROOT`    | `WEBDAV_THUMBNAILS_CACHE_DIR`             |

- If both `THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE` and `OC_THUMBNAILS_MAX_INPUT_IMAGE_FILE_SIZE` are set, the old variable takes precedence. Remove the old variable when you set the new one.
- `THUMBNAILS_FILESYSTEMSTORAGE_ROOT` pointed to the parent of the `files` folder. `WEBDAV_THUMBNAILS_CACHE_DIR` points to the cache directory itself.

The following variables are no longer used by the thumbnails service and are ignored:

- `THUMBNAILS_DATA_ENDPOINT`
- `THUMBNAILS_TRANSFER_TOKEN`
- `THUMBNAILS_WEBDAVSOURCE_INSECURE`
- `THUMBNAILS_CS3SOURCE_INSECURE`
- `THUMBNAILS_GRPC_ADDR`
- `THUMBNAILS_HTTP_ROOT`

Do not remove `OC_REVA_GATEWAY` or `OC_INSECURE`. These variables are no longer used by the thumbnails service, but other services still read them.

#### YAML Configuration

Thumbnail settings in `opencloud.yaml` are **not** read from the old location. Unknown keys are ignored without an error, so the default values are used instead. If you set thumbnail settings in `opencloud.yaml`, move them before restarting.

<Tabs groupId="thumbnail-yaml">
  <TabItem value="old" label="Old location (8.x.x)" default>

```yaml
thumbnails:
  thumbnail:
    resolutions: ['16x16', '32x32', '7680x4320']
    max_input_image_file_size: 50MB
    font_map_file: /etc/opencloud/fontmap.json
  filesystem_storage:
    root: /var/lib/opencloud/thumbnails
```

  </TabItem>
  <TabItem value="new" label="New location (9.x.x)">

```yaml
webdav:
  thumbnails:
    resolutions: ['16', '32', '2048']
    max_input_image_file_size: 50MB
    txt_fontmap_file: /etc/opencloud/fontmap.json
    cache_dir: /var/lib/opencloud/thumbnails/cache
thumbnails:
  thumbnail:
    max_input_image_file_size: 50MB
```

  </TabItem>
</Tabs>

`max_input_image_file_size` must be set in both places, because webdav and the thumbnail generator must use the same limit.

#### Resolutions

- Resolutions are now edge lengths. Each axis is rounded up separately, so the orientation of an image is preserved.
- The default maximum size is 2048 px instead of 8K. Larger requests receive a 2048 px preview.
- Legacy entries in the format `WidthxHeight` are still accepted. Each side is limited to 2048 px.
- For previews larger than 2048 px, add a plain length to the resolutions and raise `THUMBNAILS_MAX_OUTPUT_WIDTH` and `THUMBNAILS_MAX_OUTPUT_HEIGHT` on the thumbnails service accordingly.

#### Separate Containers

If the OpenCloud services run in separate containers, the webdav service must be able to reach the thumbnail generator and the cache directory.

By default, the thumbnails service listens on `127.0.0.1:9186` and can only be reached from the same container. Configure both services:

```env
# thumbnails service
THUMBNAILS_HTTP_ADDR=0.0.0.0:9186

# webdav service
WEBDAV_THUMBNAILS_GENERATOR_URL=http://thumbnails:9186
```

:::warning

The thumbnails service performs no authentication. Do not publish port 9186. Make it reachable only on an internal network.

:::

No action is required for the default single-container deployment.

#### HEIC, HEIF, and AVIF Previews

The Web Client can display previews of HEIC, HEIF, and AVIF images. The OpenCloud image cannot decode these formats. They require an external [imagor](https://github.com/cshum/imagor) instance as thumbnail generator.

If you use [opencloud-compose](https://github.com/opencloud-eu/opencloud-compose), update the repository and add `thumbnails/imagor.yml` to `COMPOSE_FILE` in your `.env` file. The module starts imagor on an internal network, sets `WEBDAV_THUMBNAILS_GENERATOR_URL`, and adds the image types to `OC_THUMBNAILS_ADDITIONAL_SOURCE_TYPES`.

For all thumbnail migration details, see the [webdav MIGRATION.md](https://github.com/opencloud-eu/opencloud/blob/main/services/webdav/MIGRATION.md).

### Guest Links

OpenCloud 9.x.x introduces the `auth-guest` service. It allows users to share files and folders with external people by email address.

Guest links are disabled by default. You can upgrade to 9.x.x without enabling them.

To enable guest links:

1. Migrate the configuration as described in [Step 2: Migrate the Configuration](#step-2-migrate-the-configuration).
2. Set `OC_ENABLE_GUEST_LINKS=true` for the OpenCloud container.
3. Configure SMTP for the notifications service and enable the notifications service. Guests receive their invitation link and PIN by email.
4. Restart OpenCloud.

Guest sessions are signed with a key derived from `OC_JWT_SECRET`. If you change `OC_JWT_SECRET`, all guest sessions become invalid.

For all configuration options, see the [auth-guest service documentation](../../../dev/server/services/auth-guest/index.md).

### Space Quota

If `GRAPH_SPACES_DEFAULT_QUOTA` is set, rename it to `OC_SPACES_DEFAULT_QUOTA`. The value is set in bytes:

```env
OC_SPACES_DEFAULT_QUOTA=10000000000
```

The old name is deprecated. The quota is still applied, but the `spaces.default_quota` capability reads only the new name. If you keep the old name, clients display the default of 1 GB instead of your configured value.

### Search

By default, search results no longer include the root folder of personal spaces and the `.space` folder of spaces. These resources stay in the search index, so no re-indexing is required.

The new setting `SEARCH_QUERY_TEMPLATE` defines the query filter that is applied to every search. The default value is:

```text
({{.QUERY}}) AND (NOT path:"./.space" AND NOT id:{{.SPACE_ROOT_PERSONAL}})
```

Change it only if you need a different search behavior.

### Email Templates

The HTML emails of the notifications service use a new layout. The templates are now split into `layout.html.tmpl`, `message.html.tmpl`, and `digest.html.tmpl` in `templates/html/`.

- Custom template folders that contain only `email.html.tmpl` keep working.
- If you use customized templates, check the emails after the upgrade.
- Times in daily and weekly digests are displayed in UTC.

### Web Extensions

Apps and web extensions can now declare the OpenCloud versions they support. If an installed extension does not support OpenCloud 9.x.x, its status is displayed in red in the admin overview.

After the upgrade, check your installed extensions and update them if required.

### Reverse Proxy

If you use an external reverse proxy with custom routes, check after the upgrade that WebDAV, Office integration, and, if enabled, the `/yjs` WebSocket route are still forwarded correctly. For the required Nginx configuration, see [Proxy Config](../../getting-started/container/docker-compose/docker-external-proxy.md#create-a-new-proxy-config).

## Verify the Upgrade

Check that OpenCloud is running and that no errors are logged:

```bash
docker compose ps
docker compose logs --tail=200 opencloud
```

Then test the following functions:

- Sign in to the Web Client.
- Open, upload, and download files.
- Open Spaces and shares.
- Search for existing files.
- Check that previews are displayed.
- If enabled, invite a guest and check that the invitation email is delivered.

## Troubleshooting

### The OpenCloud Container Keeps Restarting

Check the logs:

```bash
docker compose logs --tail=40 opencloud
```

If the log contains `guestlinks: service_account_id must not be empty`, guest links are enabled but the configuration has not been migrated. Migrate the configuration as described in [Step 2: Migrate the Configuration](#step-2-migrate-the-configuration), or disable guest links.

### Previews Are Not Displayed

- If you set thumbnail settings in `opencloud.yaml`, check that you moved them to `webdav: thumbnails:`.
- If the services run in separate containers, check `WEBDAV_THUMBNAILS_GENERATOR_URL`.
- Check that the webdav service can write to the cache directory.

### Clients Show a Default Space Quota of 1 GB

Rename `GRAPH_SPACES_DEFAULT_QUOTA` to `OC_SPACES_DEFAULT_QUOTA` and restart OpenCloud.

### Older Files Are Not Found by the Search

If you upgraded from 7.x.x, rebuild the search index as described in [Step 2: Rebuild the Search Index](#step-2-rebuild-the-search-index).
