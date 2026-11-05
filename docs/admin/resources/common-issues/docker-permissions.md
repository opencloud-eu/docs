---
sidebar_position: 4
id: docker-permissions
title: Docker Compose fails with permission denied
description: Fix Docker permission issues
draft: false
hide_table_of_contents: true
---

# Docker Compose fails with permission denied

## Problem

The Docker Compose setup fails to start and the logs contain messages such as `permission denied`.

Example log output:

```bash
opencloud-1 | {"level":"fatal","service":"nats","time":"2025-04-08T09:59:59Z","line":"github.com/opencloud-eu/opencloud/services/nats/pkg/logging/nats.go:33","message":"Can't start JetStream: could not create storage directory - mkdir /var/lib/opencloud/nats: permission denied"}
```

## Cause

The mounted directories may be owned by the wrong user, such as `root`, instead of the standard Docker user (`UID 1000`).

Incorrect directory ownership:

```bash
drwxr-xr-x  3 root root 4096 Apr  8 09:59 opencloud-data
```

Correct directory ownership:

```bash
drwxr-xr-x  9 1000 1000 4096 Apr  7 07:57 opencloud-data
```

## Solution

Adjust the ownership of the directory using the `chown` command:

```bash
chown -R 1000:1000 opencloud-data
```

:::caution Security warning
The user with UID 1000 on your host system will have full access to these mounted directories. Any local user account with this ID can read, modify, or delete OpenCloud configuration and data.

This can pose a security risk in shared or multi-user environments. Implement appropriate user and permission management and consider isolating access to these directories.
:::

Apply the ownership change to all relevant directories mounted into the containers.
