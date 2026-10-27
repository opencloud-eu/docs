---
sidebar_position: 14
id: upgrade-9.x.x
title: Upgrade 9.x.x
description: Upgrading to OpenCloud 9.x.x
draft: false
---

# Upgrading to OpenCloud 9.x.x

OpenCloud 9.x.x adds guest links and moves thumbnail generation into the webdav service. Complete the regular upgrade first by following the [Standard Upgrade Guide](./upgrade.md).

:::important

OpenCloud 9.x.x is a Rolling release and is not intended for production environments. For more information, see the [Release Lifecycle](../../resources/lifecycle.md).

:::

## Quick upgrade

Set the new version in your `.env` (`OC_DOCKER_TAG`) and restart:

```bash
docker compose pull opencloud
docker compose up -d
```

OpenCloud 9.x.x starts with the existing 8.x.x configuration. Guest links stay disabled until you enable them.

## Thumbnails

Nothing to configure. Existing previews keep working.

- The cache moves to `thumbnails/cache` and is created automatically. The old `thumbnails/files` folder is no longer used and can be removed:

  ```bash
  docker compose exec opencloud sh -c 'rm -r "$OC_BASE_DATA_PATH/thumbnails/files"'
  ```

- Sizes are edge lengths, rounded up per axis, with a maximum of 2048 px.
- Old `THUMBNAILS_*` variable names are still read. Removed ones are ignored.
- If services run in separate containers, set `WEBDAV_THUMBNAILS_GENERATOR_URL=http://thumbnails:9186`.

Details: [webdav MIGRATION.md](https://github.com/opencloud-eu/opencloud/blob/main/services/webdav/MIGRATION.md).

## Guest links

Guest links are disabled by default. To enable them, migrate the configuration first. Open a shell in the config volume:

```bash
docker run --rm -it --user 1000:1000 --entrypoint /bin/sh \
  -v opencloud-compose_opencloud-config:/etc/opencloud \
  opencloudeu/opencloud:9.0.0
```

Inside the container, create and apply the patch:

```bash
cd /etc/opencloud
opencloud init --diff
patch opencloud.yaml < opencloud.config.patch
```

The patch adds `auth_guest.service_account` and removes `thumbnails.thumbnail`.

Then set `OC_ENABLE_GUEST_LINKS=true`, configure SMTP for the notifications service and restart OpenCloud. Guests get their link and PIN by email.


## Space quota

If `GRAPH_SPACES_DEFAULT_QUOTA` is set, rename it to `OC_SPACES_DEFAULT_QUOTA`. The `spaces.default_quota` capability reads only the new name, so clients see the default 1 GB otherwise.
