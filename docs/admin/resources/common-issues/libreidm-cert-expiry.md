---
sidebar_position: 5
id: libreidm-cert-expiry
title: Internal LibreIDM cert expires
description: Renew an expired internal IDM certificate
draft: false
---

# Internal LibreIDM cert expires

### 🔧 Renewing an expired certificate in internal IDM (OpenCloud)

When using the internal IDM (LibreIDM), the LDAP certificate may expire over time.
You can see similar errormessages in your logfiles:

```bash
opencloud-1      | 2026-03-10T14:10:36Z WRN core access token not set host.name=3133c92656c8 pkg=rhttp service=frontend traceid=2da2886cf47f0143876953ee33f814a9
opencloud-1      | 2026-03-10T14:10:36Z ERR failed to build subject.session error="invalid key format" service=proxy
opencloud-1      | 2026-03-10T14:10:36Z ERR handleConnection ber.ReadPacket error="remote error: tls: bad certificate" service=idm
opencloud-1      | 2026-03-10T14:10:37Z ERR could not get ldap Connection error="LDAP Result Code 200 \"Network Error\": tls: failed to verify certificate: x509: certificate has expired or is not yet valid: current time 2026-03-10T14:10:37Z is after 2026-03-04T10:02:39Z" service=graph
opencloud-1      | 2026-03-10T14:10:37Z ERR failed to add user error="LDAP Result Code 200 \"Network Error\": tls: failed to verify certificate: x509: certificate has expired or is not yet valid: current time 2026-03-10T14:10:37Z is after 2026-03-04T10:02:39Z" request-id=3133c92656c8/LlC0SVlYb4-000023 service=graph
opencloud-1      | 2026-03-10T14:10:37Z ERR handleConnection ber.ReadPacket error="remote error: tls: bad certificate" service=idm
opencloud-1      | 2026-03-10T14:10:37Z ERR could not create user: backend error error="generalException: failed to add user" request-id=3133c92656c8/LlC0SVlYb4-000023 service=graph
opencloud-1      | 2026-03-10T14:10:37Z WRN Error Response OData Error="failed to add user" service=proxy
opencloud-1      | 2026-03-10T14:10:37Z ERR Error creating user error="500 Internal Server Error" service=proxy
opencloud-1      | 2026-03-10T14:10:37Z ERR Autoprovisioning user failed error="500 Internal Server Error" service=proxy
```

#### 🛠️ Solution

Navigate to the IDM directory

```bash
cd .opencloud/idm
```

Delete the old certificates

```bash
rm ldap.crt ldap.key
```

Directory structure:

```text
.opencloud/idm
├── idm.boltdb
├── ldap.crt
└── ldap.key
```

Restart the OpenCloud container

```bash
docker compose restart
```

➡️ The certificates will be automatically regenerated on restart.

#### ⚠️ Recommendation

Admins should avoid using LibreIDM in production and use OpenLDAP instead.
