---
sidebar_position: 7
id: ldap-invalid-credentials
title: Login fails with LDAP Result Code 49
description: Resolve invalid credentials caused by mismatched LibreIDM volumes
draft: false
hide_table_of_contents: true
---

# Login fails with LDAP Result Code 49 (Invalid Credentials)

## Problem

When using the built-in IDM (LibreIDM), login can fail with `Unexpected HTTP response: 500` in the browser, and the logs show the internal directory rejecting a bind:

```bash
opencloud-1 | {"level":"error","service":"idm","bind_dn":"uid=idp,ou=sysusers,o=libregraph-idm","op":"bind","message":"not found"}
opencloud-1 | {"level":"error","service":"idp","error":"ldap identifier backend logon connect error: LDAP Result Code 49 \"Invalid Credentials\": ","message":"identifier failed to logon with backend"}
```

## Cause

The built-in IDM seeds its service-account passwords once, at first start, into a bolt-store on the data volume (`idm.boltdb`), matching the values `opencloud init` writes into `opencloud.yaml` on the configuration volume.

The bind fails when the two volumes are no longer from the same `init`. The `idm` log entry reads either `not found` or `invalid credentials`; both indicate the same mismatch. This usually results from setting an internal LDAP password in the environment, or from reusing one volume, such as a restored or carried-over data volume, without the other.

## Solution

With the built-in IDM, do not set the internal LDAP or service passwords in `.env` or the environment. Let `opencloud init` generate them, and keep only `INITIAL_ADMIN_PASSWORD`.

Treat `opencloud.yaml` on the configuration volume and the data volume as one set. Keep them together and from the same point in time when you back up, restore, or move the instance.

If you do not need the existing data, remove both volumes so that `init` generates a matching set, then start again:

```bash
docker compose down
docker volume rm opencloud-compose_opencloud-config opencloud-compose_opencloud-data
docker compose up -d
```

:::caution
Deleting `idm.boltdb` alone may not be enough: it is re-seeded from the current configuration, but a bind password still set in the environment keeps the two sides out of sync.
:::

### Recommendation

The built-in IDM is intended for testing and small installations. For production, use an external identity provider, for example Keycloak with an external LDAP.
