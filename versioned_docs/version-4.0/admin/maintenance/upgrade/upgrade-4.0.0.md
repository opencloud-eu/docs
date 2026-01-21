---
sidebar_position: 2
id: upgrade-4.0.0
title: Upgrade 4.0.0
description: Upgrading to 4.0.0
draft: false
---

import Tabs from '@theme/Tabs'
import TabItem from '@theme/TabItem'

# Upgrading to OpenCloud 4.0.0

This guide explains how to upgrade from the previous stable opencloud_full Compose setup to the new
[opencloud-compose](https://github.com/opencloud-eu/opencloud-compose.git) repository structure.  
It covers both types of persistent storage used in earlier deployments:

- Bind mounts: host directories mapped into containers.
- Docker named volumes: volumes managed directly by Docker.

Following this guide, you can safely migrate to the stable v4.0.0 release of OpenCloud.

## Before You Begin

- Determine Your Deployment Type: This guide covers two common setups:
  - Bind Mounts: Config and data are stored in directories on the host machine (e.g., `/mnt/opencloud/config`).
  - Docker Named Volumes: Config and data are managed by Docker. You will need your `COMPOSE_PROJECT_NAME` to access them.
- Check Paths: If you are using bind mounts, ensure you know the correct paths on your host system. You can find them by inspecting your current container's `docker run` command or `docker-compose.yml` file (look for `volumes:` sections that map to host paths). For a running container, `docker inspect opencloud_full-opencloud-1` also exposes this information in the `Mounts` section.

## Backup Config and Data

:::important
Important: Always create a backup before upgrading to prevent data loss.  
We strongly recommend following the [backup documentation](../backup) and creating copies of your configuration and data directories.
:::

<Tabs> <TabItem value="bind-mounts" label="Using Bind Mounts">
If your config and data are stored in host directories (bind mounts), create a direct copy of these folders.

### Example (adjust paths to match your setup)

```bash
cp -a /mnt/opencloud/config /mnt/opencloud/config-backup
cp -a /mnt/opencloud/data /mnt/opencloud/data-backup
```

</TabItem>

<TabItem value="named-volumes" label="Using Named Volumes">

### Create backup directory

```bash
mkdir -p ~/opencloud-backups
```

### Backup config and data

```bash
docker cp opencloud_full-opencloud-1:/var/lib/opencloud ~/opencloud-backups/data-backup
docker cp opencloud_full-opencloud-1:/etc/opencloud ~/opencloud-backups/config-backup
```

</TabItem>

</Tabs>

## Stop OpenCloud

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

## Pull the 4.0.0 Production Release Image

```bash
docker pull opencloudeu/opencloud:4.0.0
```

## Update Deployment Configuration

<Tabs>

<TabItem value="docker compose" label="docker compose">

### Clone the opencloud-compose Repository

Clone the official opencloud-compose repository onto your server:

```bash
git clone https://github.com/opencloud-eu/opencloud-compose.git
cd opencloud-compose
```

### Migrate Environment Variables

Transfer your existing environment variables to the new opencloud-compose structure. Refer to the [Docker Compose configuration documentation](../../getting-started/container/docker-compose/docker-compose-base.md) for detailed instructions.

</TabItem>

</Tabs>

## Verify Configuration Changes

Go inside the container:

If your config is stored in host directories (change `<your-home-directory>` to your home directory. In our example it is `/mnt` ):

```bash
docker run --rm -it --entrypoint /bin/sh -v <your-home-directory>/opencloud/opencloud-config:/etc/opencloud opencloudeu/opencloud:4.0.0
```

or, if you use Docker Named Volumes (replace `<your-named-volume>`with your volume name. In our example it is `opencloud_full_opencloud-config`):

```bash
docker run --rm -it --entrypoint /bin/sh \
  -v <your-named-volume>:/etc/opencloud \
  opencloudeu/opencloud:4.0.0
```

Check for configuration changes:

```bash
opencloud init --diff
```

Example output:

```bash
opencloud init --diff
Do you want to configure OpenCloud with certificate checking disabled?
 This is not recommended for public instances! [yes | no = default] yes
running in diff mode
diff -u /etc/opencloud/opencloud.yaml /etc/opencloud/opencloud.yaml.tmp
--- /etc/opencloud/opencloud.yaml
+++ /etc/opencloud/opencloud.yaml.tmp
@@ -3,6 +3,7 @@
 machine_auth_api_key: k55Y7i3Djeeu4aPPNzM67Q39rf3ZHz^9
 system_user_api_key: GeTXN@Mj7-4n8Yhuwb&#oq8Gb1hF7Q%^
 transfer_secret: ANy#T5.IvknED9-Ud39+YmlXzN^TdaKi
+url_signing_secret: zB#FtAYid24Z^DkuBoTllnId=igo!tCO
 system_user_id: 8cc36d34-cd87-4434-b9e2-726e5553609c
 admin_user_id: 34a73600-a02c-4064-8aec-341cd1865a71
 graph:

diff written to /etc/opencloud/opencloud.config.patch
```

Apply any necessary changes to `/etc/opencloud/opencloud.yaml` based on the diff output. In this example, add `url_signing_secret` to your `opencloud.yaml`.

## Start OpenCloud (v4.0.0)

<Tabs>

<TabItem value="docker" label="docker">

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
    opencloudeu/opencloud:4.0.0
```

</TabItem>

<TabItem value="docker compose" label="docker compose">

## Important Note for Existing Deployments

If you previously deployed OpenCloud using the project name `opencloud_full` (our earlier example) and are now switching to the official [opencloud-compose](https://github.com/opencloud-eu/opencloud-compose) repository, you may need to specify the original project name to ensure:

- Network compatibility - for services like S3 that need to be on the same network
- Volume persistence - to access existing Docker volumes

Run the command with your original project name:

```bash
docker compose -p opencloud_full up -d
```

Alternatively, set the project name permanently in the .env file:

```bash
COMPOSE_PROJECT_NAME=opencloud_full
```

Then use the standard command:

```bash
docker compose up -d
```

</TabItem>

</Tabs>

## Verification

Your OpenCloud instance should now be running on `v4.0.0`.

### Essential Checks

- User Accounts — Confirm all users can log in successfully
- Shared Folders — Verify shared folder permissions and access
- Public Links — Test that public links remain functional
- Data Integrity — Ensure all files and folders are accessible
- Service Health — Check logs for any errors or warnings

## Troubleshooting

If you encounter issues during or after the upgrade:

1. Review the logs for error messages
2. Consult the [troubleshooting guide](../../resources/common-issues)
3. Restore from backup if necessary
4. Contact support or open an issue on [GitHub](https://github.com/opencloud-eu/opencloud/issues)
