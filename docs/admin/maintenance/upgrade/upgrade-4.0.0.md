---
sidebar_position: 2
id: upgrade-4.0.0
title: Upgrade 4.0.0
description: Upgrading to 4.0.0
draft: false
---

import Tabs from '@theme/Tabs'
import TabItem from '@theme/TabItem'

# Update OpenCloud

This guide describes how to upgrade OpenCloud to the stable version
**v4.0.0** using the Git repository [opencloud-compose](https://github.com/opencloud-eu/opencloud-compose.git)
with externalized data and config directories.

# Stop OpenCloud

Stop the currently running OpenCloud instance:

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

## Backup Config and Data

We recommended to make a [backup](/docs/admin/maintenance/backup) before proceeding with the upgrade.

```bash
cp -r /mnt/opencloud/config /mnt/opencloud/config-backup
cp -r /mnt/opencloud/data /mnt/opencloud/data-backup
```

## Pull the 4.0.0 production release image

```bash
docker pull opencloudeu/opencloud:4.0.0
```

<Tabs>

<TabItem value="docker" label="docker">

</TabItem>

<TabItem value="docker compose" label="docker compose">

## Clone the opencloud-compose Repository

Clone the official opencloud-compose repository onto your server:

```bash
git clone https://github.com/opencloud-eu/opencloud-compose.git
cd opencloud
```

## Configure opencloud-compose

Migrate your environment variables to the new opencloud-compose structure.

To do this use this [documentation](/docs/admin/getting-started/container/docker-compose/docker-compose-base.md).

</TabItem>

</Tabs>

## Verify Configuration Changes

Go inside the containers

```bash
docker run --rm -it --entrypoint /bin/sh -v $HOME/opencloud/opencloud-config:/etc/opencloud opencloudeu/opencloud:4.0.0
```

Check for configuration changes:

```bash
opencloud init --diff
```

for example my result:

```bash
opencloud init --diff
Do you want to configure OpenCloud with certificate checking disabled?
 This is not recommended for public instances! [yes | no = default] yes
running in diff mode
diff -u /etc/opencloud/opencloud.yaml /etc/opencloud/opencloud.yaml.tmp
--- /etc/opencloud/opencloud.yaml
+++ /etc/opencloud/opencloud.yaml.tmp
@@ -1,9 +1,9 @@
 token_manager:
   jwt_secret: 9GyJ7NL^*91^xRkkyQ#3mXSm+IQVej^z
 machine_auth_api_key: G^Pj5yDYwpODM7mIBBpSeulf9OR^NQz%
-url_signing_secret: hSnW$M$1!chpCWD4@J&8dBTxVA9B6j5x
 system_user_api_key: WmS.GQ4.xc+5NS.^1lC-c3JGmHcZ0Q@p
 transfer_secret: Lz9tI.&-S$7@B!lTTBx5bBRDaV@&!Jc%
+url_signing_secret: hSnW$M$1!chpCWD4@J&8dBTxVA9B6j5x
 system_user_id: d4d7eac0-bd98-45cf-b134-55dc85f258e9
 admin_user_id: 8b4b020b-8ee6-469e-8ed6-69a33b5dc2b5
 graph:
```

replace `url_signing_secret` in the `/etc/opencloud/opencloud.yaml`

Update `opencloud.yaml` if required another changes.

## Start OpenCloud (v4.0.0)

<Tabs>

<TabItem value="docker" label="docker">
``` bash
docker run --rm -it --entrypoint /bin/sh -v $HOME/opencloud/opencloud-config:/etc/opencloud opencloudeu/opencloud:4.0.0
```
</TabItem>

<TabItem value="docker compose" label="docker compose">
``` bash
docker compose up -d
```
</TabItem>

</Tabs>

## Conclusion

Your OpenCloud instance should now be running on **v2.0.5** using
externalized config and data directories. Verify:

- Users\
- Shared folders\
- Public links\
- All data availability
