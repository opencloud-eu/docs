---
sidebar_position: 3
id: docker-permissions
title: Docker Permission Issues
description: Fix Docker permission issues
draft: false
---

# Docker Permission Issues

If your Docker Compose setup fails to start and the logs contain messages such as `permission denied`, it's likely due to incorrect ownership of local directories used by the containers.

Example log output:

```bash
opencloud-1 | {"level":"fatal","service":"nats","time":"2025-04-08T09:59:59Z","line":"github.com/opencloud-eu/opencloud/services/nats/pkg/logging/nats.go:33","message":"Can't start JetStream: could not create storage directory - mkdir /var/lib/opencloud/nats: permission denied"}
```

This error typically occurs when the mounted directories are owned by the wrong user, such as `root`, instead of the standard Docker user (`UID 1000`).

Incorrect directory ownership:

```bash
drwxr-xr-x  3 root root 4096 Apr  8 09:59 opencloud-data
```

Correct ownership should be:

```bash
drwxr-xr-x  9 1000 1000 4096 Apr  7 07:57 opencloud-data
```

To resolve this issue, adjust the ownership of the directory using the `chown` command:

```bash
chown -R 1000:1000 opencloud-data
```

:::caution
Security Warning

The user with UID 1000 on your host system will have full access to these mounted directories. This means that any local user account with this ID can read, modify, or delete OpenCloud config and data files.

This can pose a security risk in shared or multi-user environments. Make sure to implement proper user and permission management and consider isolating access to these directories.

:::

Ensure you apply this to all relevant folders that are mounted into your containers. This will grant the Docker container the necessary permissions to access and write to these directories.
