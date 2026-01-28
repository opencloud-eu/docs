---
sidebar_position: 3
id: release-notes
title: Release Notes
description: Release Notes
draft: false
---

# Release Notes: Migration from v4.x.x to v5.0.0

- Version: 5.0.0
- Type: Major Release (Breaking Change in Service Architecture)
- [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v5.0.0)

## Who Is Affected?

If you use the official Docker Compose setup, no migration is typically required.

## Key Changes

The OCDAV is no longer initialized as its own service, it was moved from the backend services into the frontend service

:::compatibility note
Legacy env variable names (OCDAV\_\*) still work. They just need to be set on the frontend service now
:::

# Release Notes: Migration from v2.x.x to v3.0.0

- Version: 3.0.0
- Type: Major Release (Breaking Changes in the GraphAPI)
- [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v3.0.0)

## Who Is Affected?

This release introduces a breaking change in the GraphAPI.  
If you are using OpenCloud only through official clients (Web, Desktop, or Mobile), no migration is needed.

If you're using any other software that utilizes the GraphAPI, that software might need to be adjusted to follow the new behavior of the GraphAPI.

## Key Changes

The following endpoints of the GraphAPI were changed in a way that is not backwards compatible with the previous releases:

```http
GET /v1.0/me/drives/
GET /v1.0/drives/
GET /v1beta1/drives/
GET /v1beta1/me/drives/
```

:::note
Due to performance optimizations, these endpoints no longer automatically expand all permissions on the drives root items. If needed, the permissions can be explicitly requested via the appropriate $expand query option.
:::
