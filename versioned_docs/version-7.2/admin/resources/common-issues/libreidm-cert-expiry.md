---
sidebar_position: 6
id: libreidm-cert-expiry
title: Internal LibreIDM certificate expires
description: Renew an expired internal LibreIDM certificate
draft: false
hide_table_of_contents: true
---

# Internal LibreIDM certificate expires

## Problem

When using the internal IDM (LibreIDM), the LDAP certificate may expire. The logs may contain errors such as:

```bash
opencloud-1 | ERR handleConnection ber.ReadPacket error="remote error: tls: bad certificate" service=idm
opencloud-1 | ERR could not get ldap Connection error="LDAP Result Code 200 \"Network Error\": tls: failed to verify certificate: x509: certificate has expired or is not yet valid" service=graph
opencloud-1 | ERR Autoprovisioning user failed error="500 Internal Server Error" service=proxy
```

## Cause

OpenCloud 7.2 does not automatically renew the internal LibreIDM certificate before it expires.

## Solution

Navigate to the IDM directory:

```bash
cd .opencloud/idm
```

Delete the expired certificate and key:

```bash
rm ldap.crt ldap.key
```

The directory has the following structure:

```text
.opencloud/idm
├── idm.boltdb
├── ldap.crt
└── ldap.key
```

Restart the OpenCloud container:

```bash
docker compose restart
```

The certificate and key are regenerated automatically when the container restarts.

### Recommendation

The built-in IDM is intended for testing and small installations. For production, use an external identity provider, for example Keycloak with an external LDAP.
