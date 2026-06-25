---
sidebar_position: 30
id: default-user-quota
title: Set default user quota
description: How to set default user quota
draft: false
---

# Set Default Quota per User Role

You can define default storage quotas for specific user roles in OpenCloud by configuring the proxy service. This ensures that any newly created user with a given role automatically receives the specified quota.

## Define Role-Based Quotas in `proxy.yaml`

To configure quotas, edit the `opencloud.proxy.yaml` file and add the `role_quotas` section with role IDs and the desired quota in bytes:

```bash
nano opencloud-compose/config/opencloud/proxy.yaml
```

Example configuration:

```yaml
role_quotas:
  'd7beeea8-8ff4-406b-8fb6-ab2dd81e6b11': 1073741824
```

This assigns a 1 GiB quota to all new users with the "User" role.

## Role IDs

Use the following role IDs to configure different quotas:

- User:  
  `d7beeea8-8ff4-406b-8fb6-ab2dd81e6b11`

- SpaceAdmin:  
  `2aadd357-682c-406b-8874-293091995fdd`

- Admin:  
  `71881883-1768-46bd-a24d-a356a2afdf7f`

:::note
Quota values are defined in bytes.
:::

## Mount the Configuration in Docker

To apply the configuration, mount the updated `proxy.yaml` into your Docker container.

1. Open the `docker-compose.yaml` file:

```bash
nano opencloud-compose/docker-compose.yaml
```

2. Add the following line under the `volumes` section for the proxy container:

```yaml
- ./config/opencloud/proxy.yaml:/etc/opencloud/proxy.yaml
```

## Apply the Changes

Restart the OpenCloud container to apply the new configuration:

```bash
docker compose up -d
```

## Result

All newly created users who receive a role defined in the `role_quotas` section will automatically have the specified quota assigned.

:::info
This configuration does **not** affect existing users. Only new users will receive the default quota.
:::
