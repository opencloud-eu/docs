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

```bash
cp -a /mnt/opencloud/config /mnt/opencloud/config-backup
cp -a /mnt/opencloud/data /mnt/opencloud/data-backup
```

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

- Stop OpenCloud
  - Docker

  ```bash
  docker stop opencloud
  ```

  - Docker Compose

  ```bash
  docker compose stop
  ```

  - Pull the New Release Image

  ```bash
  docker pull opencloudeu/opencloud:7.0.x
  ```

## Configuration Migration Breaking Change

OpenCloud 7.0.x introduces a breaking configuration change.

Reference: [Migration PR](https://github.com/opencloud-eu/opencloud/pull/2760)

- Verify Configuration Changes

- Go inside the opencloud container.

- Using Bind Mounts

- Replace **your-home-directory** with your actual directory.

```bash
docker run --rm -it --entrypoint /bin/sh \
  -v "your-home-directory"/opencloud/opencloud-config:/etc/opencloud \
  opencloudeu/opencloud:7.0.x
```

- Using Docker Named Volumes

- Replace **your-named-volume** with your actual volume name.

```bash
docker run --rm -it --entrypoint /bin/sh \
  -v "your-named-volume":/etc/opencloud \
  opencloudeu/opencloud:7.0.x
```

- Generate the Configuration Diff
  - Inside the container run:

  ```bash
  opencloud init --diff
  ```

  - Example output:

  ```bash
  diff -u /etc/opencloud/opencloud.yaml /etc/opencloud/opencloud.yaml.tmp
  ```

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

- Apply the patch:

```bash
patch < opencloud.config.patch
```

- Expected output:

```bash
patching file opencloud.yaml
Required Configuration Changes
```

## The following configuration entries must exist in opencloud.yaml

```bash
service_account:
service_account_id: 62b789c9-0dd0-4647-afd3-d6969eab03b8
service_account_secret: wAiwglE93^S-y3hm0bo5FS9sFj^rzQ&i
```

## Verify that these values were added successfully after applying the patch

- Start OpenCloud 7.0.x

```bash
docker run \
    --name opencloud \
    --rm \
    -d \
    -p 9200:9200 \
    -v $HOME/opencloud/opencloud-config:/etc/opencloud \
    -v $HOME/opencloud/opencloud-data:/var/lib/opencloud \
    -e OC_INSECURE=true \
    -e PROXY_HTTP_ADDR=0.0.0.0:9200 \
    -e OC_URL=https://localhost:9200 \
    opencloudeu/opencloud:7.0.x
Docker Compose
```

# If you previously used the project name opencloud_full, continue using the same project name to preserve

```bash
Docker networks
Existing volumes
Service compatibility
Option 1 — Temporary
docker compose -p opencloud_full up -d
Option 2 — Permanent
```

- Add to .env:

```bash
COMPOSE_PROJECT_NAME=opencloud_full
```

- Then start normally:

```bash
docker compose up -d
Verify the Migration
```

- After startup, monitor the logs:

```bash
docker logs -f opencloud
```

or:

```bash
docker compose logs -f
```

## Watch for migration messages and ensure no errors occur

- Verify Project Spaces

- After the migration completes:
  - Open all existing project spaces
  - Verify that all members still exist
  - Check permissions and shared access

## Reindex OpenSearch Breaking Change

This step is important because the migration changes internal member handling.
OpenCloud 7.0.x introduces a new OpenSearch index structure.  
Reference: [OpenSearch Index PR](https://github.com/opencloud-eu/opencloud/pull/2514)

Rebuild the search index after upgrading:

```bash
opencloud search index --all-spaces
```

Depending on the size of your installation, this process may take some time.

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
