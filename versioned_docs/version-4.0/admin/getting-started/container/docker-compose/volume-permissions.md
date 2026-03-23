---
sidebar_position: 7
id: docker-compose-volume-permissions
title: Volume Permissions and UID/GID Management
description: Understanding and managing filesystem permissions for OpenCloud Docker volumes
---

# Volume Permissions and UID/GID Management

This guide explains how to properly configure filesystem permissions for OpenCloud's persistent volumes in Docker Compose deployments. Understanding UID/GID mappings is crucial for production deployments with mounted volumes.

## Default Container User

OpenCloud containers run as a non-root user with:

- UID (User ID): 1000
- GID (Group ID): 1000

This is the user that reads and writes to all data, configuration, and cache directories within the container.

## Mount Point Permissions

When you mount directories from your host system into the container, the container's UID 1000 must have proper read/write access.

### Correct Setup

```bash
# Create directories
sudo mkdir -p /your/local/path/opencloud/{config,data}

# Set ownership to UID/GID 1000:1000
sudo chown -R 1000:1000 /your/local/path/opencloud

# Set appropriate permissions (owner can read/write/execute, others cannot)
sudo chmod -R 0700 /your/local/path/opencloud
```

Directory structure should look like:

```bash
/your/local/path/opencloud/
├── config/          (UID 1000 owner, mode 0700)
│   ├── opencloud.config.php
│   ├── redis/
│   └── nginx/
└── data/             (UID 1000 owner, mode 0700)
    ├── database/
    ├── files/
    └── objectstorage/
```

### Verifying permissions

Check that directories are owned by 1000:1000:

```bash
ls -ln /your/local/path/opencloud/
# Example output:
# drwx------ 5 1000 1000 4096 Jan 15 10:30 config
# drwx------ 8 1000 1000 4096 Jan 16 14:22 data
```

## Understanding UID Mapping

### Host user with UID 1000

If your host system has a user with UID 1000 (e.g., the first non-root user created):

```bash
id myuser
# Output: uid=1000(myuser) gid=1000(myuser) groups=1000(myuser)
```

That user can directly access the mounted directories:

```bash
ls /your/local/path/opencloud/config
cd /your/local/path/opencloud/data
```

This is the most common case and requires minimal configuration.

### UID mismatch scenarios

Problem: Your host system's UID 1000 is assigned to a different user (or doesn't exist).

```bash
cat /etc/passwd | grep 1000
# (empty or shows different user)
```

Solution: Create a dedicated service user or adjust permissions:

```bash
# Option 1: Create a dedicated user for OpenCloud
sudo useradd -u 1000 -m -s /usr/sbin/nologin opencloud

# Then change ownership
sudo chown -R opencloud:opencloud /your/local/path/opencloud

# Option 2: Use numeric IDs in chown
sudo chown -R 1000:1000 /your/local/path/opencloud
```

## Permission Modes Explained

### Recommended: 0700 (rwx------)

```bash
sudo chmod -R 0700 /your/local/path/opencloud
```

- Owner (UID 1000): read, write, execute
- Group members: no access
- Others: no access

Use case: Maximum security; only the container user can access.

### More permissive: 0750 (rwxr-x---)

```bash
sudo chmod -R 0750 /your/local/path/opencloud
```

- Owner: read, write, execute
- Group members: read, execute
- Others: no access

Use case: Allows other group members to read (useful for backups, monitoring).

### Caution: 0755 (rwxr-xr-x)

```bash
sudo chmod -R 0755 /your/local/path/opencloud
```

- Everyone can read and list directories

Warning: Not recommended for data directories containing sensitive information.

## Bind Mounts vs Named Volumes

### Bind Mounts (Recommended for persistent data)

```bash
# In .env or docker-compose override
OC_CONFIG_DIR=/your/local/path/opencloud/config
OC_DATA_DIR=/your/local/path/opencloud/data
```

Advantages:

- Full control over permissions and ownership
- Easy to backup
- Direct host filesystem access

You must manually manage permissions.

### Named Volumes (Docker-managed)

If not set, Docker creates automatic volumes:

```bash
# Volumes are stored in /var/lib/docker/volumes/
docker volume ls
```

Advantages:

- Docker manages permissions automatically
- Docker handles backup/restore

Disadvantages:

- Harder to access directly
- Less control over ownership
- Not recommended for production

## Troubleshooting Permission Issues

### "Permission denied" errors in container

If OpenCloud container can't read/write:

```bash
# Check container can see files
docker compose exec opencloud ls -la /var/opencloud/config

# If permission denied, check host ownership
ls -ln /your/local/path/opencloud/config

# Fix: Change ownership
sudo chown -R 1000:1000 /your/local/path/opencloud
```

### Cannot write after mounting

```bash
# Error: "Read-only file system"
# Solution: Ensure directory is writable
sudo chmod u+w /your/local/path/opencloud/{config,data}
```

### Backup/restore permission issues

When restoring from backup:

```bash
# After extracting backup, fix permissions
sudo chown -R 1000:1000 /your/local/path/opencloud
sudo chmod -R 0700 /your/local/path/opencloud
```

## Security Considerations

:::caution
UID 1000 on your host system will have full read/write access to OpenCloud data.

In multi-user or shared hosting environments:

1. Isolate the host user (e.g., dedicated service account)
2. Restrict SSH/shell access appropriately
3. Use additional filesystem-level security (SELinux, AppArmor)
4. Regularly audit file access

   :::

## Environment Variables for Persistence

```bash
# In .env file
OC_CONFIG_DIR=/your/local/path/opencloud/config
OC_DATA_DIR=/your/local/path/opencloud/data
OC_LOG_DIR=/your/local/path/opencloud/logs

# Ensure these directories exist with correct permissions
```

If these variables are not set, Docker will use unnamed volumes that persist only as long as containers are not removed.

## See Also

- [Production Considerations](./production-considerations.md) – Volume mounting setup
- [Docker documentation on volumes](https://docs.docker.com/storage/volumes/)
- [Linux permission quick reference](https://en.wikipedia.org/wiki/File-system_permissions)
