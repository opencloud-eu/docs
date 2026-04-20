---
sidebar_position: 7
id: docker-compose-volume-permissions
title: Volume Permissions
description: Configure filesystem permissions for OpenCloud Docker volumes
---

# Volume Permissions

OpenCloud runs as a non-root user inside the container and requires read and write access to the mounted configuration and data directories.

When using bind mounts, ensure that the directories referenced by `OC_CONFIG_DIR` and `OC_DATA_DIR` are writable by the container user.

## Recommended permissions

Create the directories on the host and assign them to UID and GID `1000`:

```bash
sudo mkdir -p /your/local/path/opencloud/{config,data}
sudo chown -R 1000:1000 /your/local/path/opencloud
sudo chmod -R 0700 /your/local/path/opencloud
```

To verify the ownership on the host, run:

```bash
ls -ln /your/local/path/opencloud/
```

## Rootless Docker and UID Mapping

When Docker runs in rootless mode, bind-mounted directories do not always use the same ownership mapping you see in a regular Docker setup.

The OpenCloud container still runs as UID and GID `1000` inside the container, but rootless Docker maps that identity into the subordinate UID and GID range configured for your host user. As a result, a host directory owned by `1000:1000` may not be writable inside the container.

### Check subordinate IDs

You can inspect the subordinate UID and GID ranges on the host with:

```bash
grep "^$(whoami):" /etc/subuid
grep "^$(whoami):" /etc/subgid
```

If the output looks like this:

```text
youruser:100000:65536
youruser:100000:65536
```

then container UID `1000` maps to host UID `101000`.

### Adjust ownership

In that case, set the bind-mounted directories to the mapped host UID and GID:

```bash
sudo chown -R 101000:101000 /your/local/path/opencloud
sudo chmod -R 0700 /your/local/path/opencloud
```

### Verify access inside the container

Do not rely only on host-side ownership values in rootless mode. Verify that the OpenCloud container can actually read and write the mounted directories:

```bash
docker compose exec opencloud sh
ls -la /etc/opencloud
ls -la /var/lib/opencloud
touch /var/lib/opencloud/.write-test
```

If those commands succeed, the permissions are configured correctly.

### Prefer a simpler setup

If you do not want to manage mapped host UID and GID values manually, consider using Docker named volumes instead of bind mounts for rootless setups.

## Troubleshooting

If OpenCloud reports permission errors, verify the mounted directories from both the host and the container.

### Check on the host

```bash
ls -ln /your/local/path/opencloud/
```

### Check inside the container

```bash
docker compose exec opencloud ls -la /etc/opencloud
docker compose exec opencloud ls -la /var/lib/opencloud
```

If needed, re-apply ownership and permissions on the host:

```bash
sudo chown -R 1000:1000 /your/local/path/opencloud
sudo chmod -R 0700 /your/local/path/opencloud
```

## Further reading

For more information about Docker storage, see the official Docker documentation:

- [Volumes](https://docs.docker.com/storage/volumes/)
- [Bind mounts](https://docs.docker.com/engine/storage/bind-mounts/)

For backup recommendations, see [Backup and recovery](../../../maintenance/backup.md).
