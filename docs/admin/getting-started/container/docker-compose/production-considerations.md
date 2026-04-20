---
sidebar_position: 4
id: docker-compose-production-considerations
title: Production Considerations
description: Best practices and recommendations for production OpenCloud deployments with Docker Compose
---

# Production Setup Considerations

This guide outlines essential best practices and configurations for running OpenCloud in a production environment with Docker Compose.

:::caution Production Setup Recommended
By default, OpenCloud stores configuration and data inside internal Docker volumes.  
This works fine for local development or quick evaluations — but is not suitable for production environments.
:::

## Mount Persistent Volumes

For production deployments, you should mount persistent local directories for configuration and data. This ensures:

- Data durability – Configuration and data persist across container restarts
- Easier backups and recovery – Access files directly from the host
- Full control over storage location and permissions – Meet organizational compliance requirements

### Update your `.env` file with custom paths

Edit your environment configuration to specify local mount points:

```bash
nano .env
```

Add or uncomment these variables:

```bash
OC_CONFIG_DIR=/your/local/path/opencloud/config
OC_DATA_DIR=/your/local/path/opencloud/data
```

Replace `/your/local/path/opencloud` with your desired location (e.g., `/opt/opencloud` or `/mnt/data/opencloud`).

### Ensure proper folder ownership and permissions

Create the directories and set correct ownership for the container user (UID/GID 1000:1000 by default):

```bash
sudo mkdir -p /your/local/path/opencloud/{config,data}
sudo chown -R 1000:1000 /your/local/path/opencloud
sudo chmod -R 0700 /your/local/path/opencloud
```

If these variables are not set, Docker will use internal volumes. These volumes may be removed when containers are deleted, which means your configuration and data may be lost. This setup is therefore not recommended for production use.

:::caution Security Warning

The user with UID 1000 on your host system will have full access to these mounted directories. This means that any local user account with this ID can read, modify, or delete OpenCloud config and data files.

This can pose a security risk in shared or multi-user environments. Make sure to implement proper user and permission management and consider isolating access to these directories.

For more details on volume permissions, see [Volume Permissions and UID/GID Management](./volume-permissions.md).

:::

## Use the appropriate repository branch

By default, the `main` branch of the `opencloud-compose` repository tracks the rolling release.

For production deployments, use the current `stable-*` branch instead, for example:

```bash
git checkout stable-4.0
```

Stable branch names change over time as new stable releases become available. Moving from one stable-\* branch to another is an update and should be handled accordingly.

## Backup and Recovery Strategy

With persistent volumes in place, you should implement a backup and recovery strategy for your OpenCloud deployment:

- Regular backups of `OC_CONFIG_DIR` and `OC_DATA_DIR`
- Off-site or remote storage for disaster recovery
- Regular verification and testing of restore procedures

For detailed backup guidance, see the [Backup documentation](../../../maintenance/backup.md).
