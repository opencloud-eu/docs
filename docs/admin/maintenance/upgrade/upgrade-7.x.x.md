---
sidebar_position: 20
id: upgrade-7.x.x
title: Upgrade 7.x.x
description: Upgrading to OpenCloud 7.x.x
draft: false
---

import Tabs from '@theme/Tabs'
import TabItem from '@theme/TabItem'

# Upgrading to OpenCloud 7.x.x

This guide describes how to upgrade an existing OpenCloud deployment to OpenCloud 7.x.x.

The guide applies to upgrades from:

- OpenCloud 6.x rolling
- OpenCloud 4.0.x stable

It covers the required configuration migration, optional OpenSearch index rebuild, and web extension updates introduced with OpenCloud 7.x.x.

## Before You Start

- Make sure your current deployment is running on OpenCloud 6.x (rolling) or OpenCloud 4.0.x (stable).
- Create a complete backup of your configuration and data.
- Make sure you have access to your current `opencloud.yaml`.
- Verify that your current deployment is healthy before upgrading.
- Review the OpenCloud 7.x.x [release notes](https://github.com/opencloud-eu/opencloud/releases) before starting the upgrade.

## Back Up Configuration and Data

<Tabs>
  <TabItem value="bind-mounts" label="Using Bind Mounts">

If your configuration and data are stored in directories on the host, create a copy of these directories.

Example:

```bash
cp -a /mnt/opencloud/config /mnt/opencloud/config-backup
cp -a /mnt/opencloud/data /mnt/opencloud/data-backup
```

Replace the paths with the directories used by your deployment.

  </TabItem>

  <TabItem value="named-volumes" label="Using Named Volumes">

Create a backup directory and copy the configuration and data from the OpenCloud container.

```bash
mkdir -p ~/opencloud-backups
docker cp opencloud-compose-opencloud-1:/etc/opencloud ~/opencloud-backups/config-backup
docker cp opencloud-compose-opencloud-1:/var/lib/opencloud ~/opencloud-backups/data-backup
```

Replace `opencloud-compose-opencloud-1` with the name of your OpenCloud container if it differs.

  </TabItem>
</Tabs>

## Update the `opencloud-compose` Checkout

If you use the `opencloud-compose` repository, update your local copy of the repository.

```bash
cd /opencloud-compose
git pull
```

Skip this step if you run OpenCloud with plain Docker.

## Stop OpenCloud

Stop the currently running OpenCloud instance.

<Tabs>
  <TabItem value="docker-compose" label="Docker Compose">

```bash
docker compose stop
```

  </TabItem>

  <TabItem value="docker" label="Docker">

```bash
docker stop opencloud
```

  </TabItem>
</Tabs>

## Pull the OpenCloud 7.x.x Image

Pull the OpenCloud 7.x.x image.

```bash
docker pull opencloudeu/opencloud:7.x.x
```

Replace `7.x.x` with the exact OpenCloud version you want to upgrade to.

## Apply the Configuration Migration

OpenCloud 7.x.x includes a breaking configuration change that must be applied before starting the upgraded instance.

### Open a Temporary OpenCloud Container

Open a shell in a temporary OpenCloud 7.x.x container and mount your OpenCloud configuration directory or configuration volume to `/etc/opencloud`.

<Tabs>
  <TabItem value="named-volumes" label="Using Named Volumes">

```bash
docker run --rm -it --entrypoint /bin/sh -v "<opencloud-config-volume>:/etc/opencloud" opencloudeu/opencloud:7.x.x
```

Replace `<opencloud-config-volume>` with the Docker volume or bind mount that contains your OpenCloud configuration.

  </TabItem>

  <TabItem value="bind-mounts" label="Using Bind Mounts">

```bash
docker run --rm -it --entrypoint /bin/sh -v "<path-to-your-config-directory>:/etc/opencloud" opencloudeu/opencloud:7.x.x
```

Replace `<path-to-your-config-directory>` with the host directory that contains your `opencloud.yaml`.

  </TabItem>
</Tabs>

### Generate the Configuration Diff

Inside the temporary container, run:

```bash
opencloud init --diff
```

Example output:

```diff
diff -u /etc/opencloud/opencloud.yaml /etc/opencloud/opencloud.yaml.tmp
--- /etc/opencloud/opencloud.yaml
+++ /etc/opencloud/opencloud.yaml.tmp
@@ -90,6 +90,9 @@
 sharing:
   events:
     tls_insecure: false
+service_account:
+  service_account_id: 00000000-0000-0000-0000-000000000000
+  service_account_secret: example-service-account-secret
 storage_users:
   events:
     tls_insecure: false

diff written to /etc/opencloud/opencloud.config.patch
```

The command creates the following patch file:

```bash
/etc/opencloud/opencloud.config.patch
```

### Apply the Configuration Patch

Change to the configuration directory:

```bash
cd /etc/opencloud
```

Verify that the patch file was created:

```bash
ls
```

Example output:

```bash
banned-password-list.txt
csp.yaml
opencloud.config.patch
opencloud.yaml
opencloud.yaml.2026-05-19-15-45-44.backup
```

Test the patch before applying it:

```bash
patch --dry-run opencloud.yaml < opencloud.config.patch
```

Expected output:

```bash
checking file opencloud.yaml
```

Apply the patch:

```bash
patch opencloud.yaml < opencloud.config.patch
```

Expected output:

```bash
patching file opencloud.yaml
```

Verify that the following configuration entries exist in `opencloud.yaml`:

```yaml
service_account:
  service_account_id: 00000000-0000-0000-0000-000000000000
  service_account_secret: example-service-account-secret
```

### Exit the Temporary Container

Exit the temporary container after applying the configuration patch.

```bash
exit
```

## Start OpenCloud

Start OpenCloud with the upgraded image.

<Tabs>
  <TabItem value="docker-compose" label="Docker Compose">

```bash
docker compose up -d
```

  </TabItem>

  <TabItem value="docker" label="Docker">

```bash
docker start opencloud
```

  </TabItem>
</Tabs>

### ⏳ First Startup After Upgrading to OpenCloud 7.x.x

After upgrading to OpenCloud 7.x.x, the first startup may take several minutes before all Spaces become fully available.

During this period, some Space-related functionality is temporarily restricted:

- Space member lists may be incomplete or incorrect.
- Space memberships cannot be modified.
- Creating or deleting Spaces is not possible.
- Share-related operations may be unavailable until the migration has completed.

#### Background

OpenCloud 7.x.x introduced a new backend mechanism for managing Space memberships. When upgrading from an earlier release, the `sharing` service automatically migrates existing memberships to the new format.

Depending on the number of Spaces and members in your installation, this process may take several minutes to complete.

#### Monitoring Migration Progress

To monitor the migration progress, configure the sharing service log level to `info` before starting the upgrade:

```bash
OC_LOG_LEVEL=info
```

or

```bash
SHARING_LOG_LEVEL=info
```

With the log level set to `info`, the sharing service writes migration progress information to the logs while the migration is running.

#### Migration Completed

Once the migration has finished successfully, the sharing service writes a completion message to the logs indicating that the migration has been completed.

> **Note:** Migration progress and completion messages are only available when the sharing service log level is configured to `info`.

After the completion message appears in the logs, all Space functionality, including member management, sharing operations, and Space creation or deletion, is available again.

#### Required Configuration Changes

The upgrade also requires a configuration change for the `sharing` service.

Please follow the instructions in the Upgrade Guide and apply the required configuration updates before starting the upgraded version of OpenCloud.

## Rebuild the OpenSearch Index

:::note

This step is only required for instances that use OpenSearch.

:::

OpenCloud 7.x.x introduces a new OpenSearch index structure.

Reference: [OpenSearch Index PR](https://github.com/opencloud-eu/opencloud/pull/2514)

After upgrading, rebuild the search index.

<Tabs>
  <TabItem value="docker" label="Docker">

```bash
docker exec -it opencloud opencloud search index --all-spaces
```

  </TabItem>

  <TabItem value="docker-compose" label="Docker Compose">

```bash
docker compose exec opencloud opencloud search index --all-spaces
```

  </TabItem>
</Tabs>

The indexing process can take longer on larger installations.

## Update Web Extensions

OpenCloud 7.x.x introduces breaking changes in the web client architecture.

Older web extension versions are no longer compatible with OpenCloud 7.x.x and must be updated.

New extension versions are available from:

- The App Store inside the OpenCloud web interface
- [OpenCloud Web Extensions on GitHub](https://github.com/opencloud-eu/web-extensions/releases)

Download the latest extension versions and follow the [web applications installation guide](../../configuration/web-applications.md).

## Verify the Upgrade

After starting OpenCloud, verify that the instance works as expected.

- Users can log in.
- Existing shares are still available.
- Public links work as expected.
- Project spaces show the correct members and permissions.
- Search returns expected results after rebuilding the OpenSearch index.
- The container logs do not show upgrade-related errors.

## Troubleshooting

If issues occur during or after the upgrade:

- Review the OpenCloud container logs.
- Verify the generated changes in `opencloud.yaml`.
- Re-run the configuration diff if required.
- Restore the backup if the instance cannot be recovered.
- Check the troubleshooting documentation.
- Open an issue on GitHub if the issue persists.

## Useful Resources

- [OpenCloud Troubleshooting Guide](../../resources/common-issues.md)
- [OpenCloud GitHub Issues](https://github.com/opencloud-eu/opencloud/issues)
- [OpenCloud Web Extensions Releases](https://github.com/opencloud-eu/web-extensions/releases)
