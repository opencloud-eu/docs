---
sidebar_position: 10
id: upgrade-guide
title: Standard Upgrade Guide
description: Standard guide for upgrading OpenCloud
draft: false
slug: upgrade-guide
---

# Standard Upgrade Guide

import Tabs from '@theme/Tabs'
import TabItem from '@theme/TabItem'

This guide provides the standard steps to upgrade OpenCloud for both [docker](../../getting-started/container/docker.md) and [docker compose](../../getting-started/container/docker-compose/docker-compose-base.md)

## Stop OpenCloud

Stop the currently running OpenCloud instance:

<Tabs groupId="deployment">
  <TabItem value="docker" label="docker">
    ```Shell
    docker stop opencloud
    ```
  </TabItem>
  <TabItem value="docker-compose" label="docker compose">
    ```Shell
    docker compose stop
    ```
  </TabItem>
</Tabs>

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

## Pull the new Opencloud version

```bash
docker pull opencloudeu/opencloud-rolling:{tag} # or opencloudeu/opencloud:{tag} depending on the version you're using
```

## Verify Configuration Changes

If upgrading from an older release, check for required configuration changes:

### Open a Temporary OpenCloud Container

Open a shell in a temporary OpenCloud container and mount your OpenCloud configuration directory or configuration volume to `/etc/opencloud`.

<Tabs>
  <TabItem value="named-volumes" label="Using Named Volumes">

```bash
docker run --rm -it --entrypoint /bin/sh -v "<opencloud-config-volume>:/etc/opencloud" opencloudeu/opencloud (or opencloud-rolling):"version-tag"
```

Replace `<opencloud-config-volume>` with the Docker volume or bind mount that contains your OpenCloud configuration.

  </TabItem>

  <TabItem value="bind-mounts" label="Using Bind Mounts">

```bash
docker run --rm -it --entrypoint /bin/sh -v "<path-to-your-config-directory>:/etc/opencloud" opencloudeu/opencloud (or opencloud-rolling):"version-tag"
```

Replace `<path-to-your-config-directory>` with the host directory that contains your `opencloud.yaml`.

  </TabItem>
</Tabs>

### Generate the Configuration Diff

Inside the temporary container, run:

```bash
opencloud init --diff
```

If you see `no changes, your config is up to date`, no further action is needed.

<img src={require("../img/init-diff.png").default} alt="init -diff" width="1920"/>

In that case, [exit the temporary container](#exit-the-temporary-container) and start OpenCloud.

Otherwise, update your `opencloud.yaml` file accordingly and [apply the patch](#apply-the-configuration-patch).

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

## Start OpenCloud with updated image

<Tabs groupId="deployment">
  <TabItem value="docker" label="docker">
    ```Shell
    docker run \
    --name opencloud \
    --rm \
    -it \
    -p 9200:9200 \
    -v $HOME/opencloud/opencloud-config:/etc/opencloud \
    -v $HOME/opencloud/opencloud-data:/var/lib/opencloud \
    -e OC_INSECURE=true \
    -e PROXY_HTTP_ADDR=0.0.0.0:9200 \
    -e OC_URL=https://localhost:9200 \
    opencloudeu/opencloud-rolling:{tag}
    ```
  </TabItem>
  <TabItem value="docker-compose" label="docker compose">
    ```Shell
    docker compose up -d
    ```
  </TabItem>
</Tabs>

## Conclusion

Make sure that all previously created data, users, shared files, public links exist.
