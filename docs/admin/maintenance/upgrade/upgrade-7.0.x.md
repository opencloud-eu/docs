---
sidebar_position: 4
id: upgrade-7.0.x
title: Upgrade 7.0.x
description: Upgrading to 7.0.x
draft: false
---

import Tabs from '@theme/Tabs'
import TabItem from '@theme/TabItem'

# Upgrading to OpenCloud 7.0.x

This guide explains how to upgrade an existing OpenCloud deployment to the 7.0.x release.
It includes all required migration steps, configuration changes, and search index updates introduced in this release.

The upgrade applies to deployments using:

- Docker Compose
- Docker Named Volumes
- Bind Mounts

Following this guide ensures a safe migration to OpenCloud 7.0.x.

## Before starting the upgrade

- Ensure you have OpenCloud 4.0.7 installed
- Create a complete backup of your configuration and data.
- Ensure you have access to your current opencloud.yaml.
- Verify that your current deployment is healthy before upgrading.

## Backup Config and Data

:::important
Always create a backup before upgrading to prevent data loss.
:::

- Using Bind Mounts

<Tabs> <TabItem value="bind-mounts" label="Using Bind Mounts">
If your config and data are stored in host directories (bind mounts), create a direct copy of these folders.

- Example (adjust paths to match your setup)

```bash
cp -a /mnt/opencloud/config /mnt/opencloud/config-backup
cp -a /mnt/opencloud/data /mnt/opencloud/data-backup
```

</TabItem>

<TabItem value="named-volumes" label="Using Named Volumes">

- Using Docker Named Volumes
- Create Backup Directory

```bash
mkdir -p ~/opencloud-backups
```

- Backup Config and Data

```bash
docker cp opencloud_full-opencloud-1:/var/lib/opencloud ~/opencloud-backups/data-backup
docker cp opencloud_full-opencloud-1:/etc/opencloud ~/opencloud-backups/config-backup
```

- Pull the latest OpenCloud Compose

If you are using Docker Compose with the `opencloud-compose` repository, update your local checkout before pulling the new container image:

```bash
cd /opencloud-compose
git pull
```

Skip this step if you run OpenCloud with plain Docker (`docker run`).

</TabItem>

</Tabs>

- Stop OpenCloud

First, gracefully stop your currently running OpenCloud instance:

<Tabs>

<TabItem value="docker" label="docker">

```bash
docker stop opencloud
```

</TabItem>

<TabItem value="docker compose" label="docker compose">

```bash
docker compose stop
```

</TabItem>

</Tabs>

## Configuration Migration Breaking Change

OpenCloud 7.0.x introduces a breaking configuration change.

Reference: [Migration PR](https://github.com/opencloud-eu/opencloud/pull/2760)

- Verify Configuration Changes

- Go inside the opencloud container.

- Using Bind Mounts

- Replace **your-home-directory** with your actual directory.

```bash
docker run --rm -it --entrypoint /bin/sh -v "your-home-directory-path":/etc/opencloud opencloudeu/opencloud:7.0.x
```

- Using Docker Named Volumes

- Replace **your-named-volume** with your actual volume name.

```bash
docker run --rm -it --entrypoint /bin/sh -v "your-named-volume-path":/etc/opencloud opencloudeu/opencloud:7.0.x
```

- Generate the Configuration Diff
  - Inside the container run:

  ```bash
  opencloud init --diff
  ```

  - Example output:

  ```bash
  diff -u /etc/opencloud/opencloud.yaml /etc/opencloud/opencloud.yaml.tmp
  --- /etc/opencloud/opencloud.yaml
  +++ /etc/opencloud/opencloud.yaml.tmp
  @@ -90,6 +90,9 @@
  sharing:
   events:
     tls_insecure: false
  ```

- service_account:
- service_account_id: 05bca760-ff47-44e3-9532-de8568e097bc
- service_account_secret: NavT+c9okb.AD+170x3..!W78EVXJtSM
  storage_users:
  events:
  tls_insecure: false

diff written to /etc/opencloud/opencloud.config.patch

- A patch file will automatically be created:

```bash
/etc/opencloud/opencloud.config.patch
```

- Apply the Configuration Patch
  - Go to the configuration directory:

  ```bash cd /etc/opencloud

  ```

  - Verify the generated files:

  Example:

  ```bash
  ls
  banned-password-list.txt
  csp.yaml
  opencloud.config.patch
  opencloud.yaml
  opencloud.yaml.2026-05-19-15-45-44.backup
  ```

- Testing the patch:
  - Run the following command:

  ```bash
  patch --dry-run opencloud.yaml < opencloud.config.patch
  ```

  - Expecting output:

  ```bash
  checking file opencloud.yaml
  ```

- Apply the patch:
  - Run the following command:

  ```bash
  patch opencloud.yaml < opencloud.config.patch
  ```

  - Expected output:

  ```bash
  patching file opencloud.yaml
  ```

## The following configuration entries must exist in opencloud.yaml

```bash
service_account:
service_account_id: 62b789c9-0dd0-4647-afd3-d6969eab03b8
service_account_secret: wAiwglE93^S-y3hm0bo5FS9sFj^rzQ&i
```

## Web Breaking Changes

OpenCloud Web also includes breaking changes in this release.

Review the official OpenCloud 7.0.x release notes carefully:

- Verification  
  Your OpenCloud instance should now be running on 7.0.x.
  - Essential Checks
  - User Accounts — Verify all users can log in
  - Shared Folders — Confirm shares remain functional
  - Public Links — Test public links
  - Search — Verify search works correctly after reindexing
  - Project Spaces — Check members and permissions
  - Service Health — Review logs for warnings or errors
  - Troubleshooting

- If issues occur during or after the upgrade:
  - Review container logs
  - Verify opencloud.yaml
  - Re-run the configuration diff if necessary
  - Restore from backup if required
  - Consult the troubleshooting documentation
  - Open an issue on GitHub if needed

- Useful resources:
  - OpenCloud Troubleshooting Guide
  - OpenCloud GitHub Issues

## Updating Web Extensions for OpenCloud 7.0.x

OpenCloud 7.0.x introduces breaking changes in the web client architecture.
Because of these changes, older web extension versions are no longer compatible with OpenCloud 7.0.x and must be updated.

New extension versions are available in the App Store inside the OpenCloud UI or on [GitHub](https://github.com/opencloud-eu/web-extensions/releases). To update your extensions, download their latest version and follow the [app installation guide](../../configuration/web-applications.md).
