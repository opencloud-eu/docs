---
sidebar_position: 3
id: production-setup-consideration
title: Production Setup Consideration
description: 'OpenCloud Production Setup Consideration'
draft: true
---

# Production Setup Consideration

:::caution Production Setup Recommended
By default, OpenCloud stores configuration and data inside internal Docker volumes.  
This works fine for local development or quick evaluations — but is not suitable for production environments.
:::

## Mount Persistent Volumes

For production deployments, you should mount persistent local directories for configuration and data. This ensures:

- Data durability
- Easier backups and recovery
- Full control over storage location and permissions

### Update your `.env` file with custom paths

```bash
OC_CONFIG_DIR=/your/local/path/opencloud/config
OC_DATA_DIR=/your/local/path/opencloud/data
```

### Set your email for SSL certification

```bash
TRAEFIK_ACME_MAIL=your@email.com
```

:::tip Folder Permissions

### Ensure these folders exist and are owned by user and group 1000:1000, which the Docker containers use by default

```bash
sudo mkdir -p /your/local/path/opencloud/{config,data}
sudo chown -R 1000:1000 /your/local/path/opencloud
```

:::

If these variables are not set, Docker will use internal volumes.
These volumes may be removed when containers are deleted, which means your configuration and data may be lost. This setup is therefore not recommended for production use.

:::caution Security Warning

The user with UID 1000 on your host system will have full access to these mounted directories. This means that any local user account with this ID can read, modify, or delete OpenCloud config and data files.

This can pose a security risk in shared or multi-user environments. Make sure to implement proper user and permission management and consider isolating access to these directories.

:::

## Use production release container

To avoid accidentally upgrading to versions that may contain breaking changes, you should explicitly specify the container image and version in your .env file.

```bash
OC_DOCKER_IMAGE=opencloudeu/opencloud
OC_DOCKER_TAG=2
```

This ensures that your deployment always uses a stable production release instead of automatically pulling newer versions.
