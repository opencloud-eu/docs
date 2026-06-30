---
sidebar_position: 3
id: keycloak
title: Keycloak Integration
description: Keycloak Integration
draft: false
---

# Keycloak Integration

OpenCloud supports using Keycloak as an external identity provider, providing enterprise-grade identity management capabilities.
For issuer variables, WebFinger client discovery, and Docker Compose requirements, see the [generic external IDP documentation](./external-idp.md).

This guide is divided into three main sections:

- [Keycloak Integration Overview](#opencloud-configuration-for-keycloak-general): A brief overview of the integration process.
- [Shared User Directory Mode](#configuration-for-shared-directory-mode): Keycloak and OpenCloud share a common LDAP directory for user management.
- [Autoprovisioning Mode](#configuration-for-autoprovisioning-mode): OpenCloud autoprovisions users in a separate LDAP directory managed by OpenCloud.

## OpenCloud Configuration for Keycloak (General)

When using Keycloak as the identity provider, keep the Keycloak-specific parts of the setup here:
realm, clients, scopes, mappers, and logout behavior.

The OpenCloud issuer, WebFinger discovery, and Docker Compose external IDP setup
are documented in the [generic external IDP guide](./external-idp.md).

### Client Configuration

If you use the official `opencloud-compose` Docker Compose setup with Keycloak
(see [Shared User Directory Mode](#shared-user-directory-mode) below), the
required OIDC clients are already pre-configured in Keycloak through the
`keycloak-realm.dist.json` import and match the client IDs and scopes
OpenCloud expects by default. You only need to configure the clients manually
if you are not using this Docker Compose setup or run a custom Keycloak
deployment.

Use the client IDs and scopes from the [generic external IDP guide](./external-idp.md)
when creating the Keycloak clients.

### Manual Client Configuration

Create one public OpenID Connect client in Keycloak for each OpenCloud client
type that should connect to this deployment: Web, Android, iOS, and Desktop.

The client IDs configured in Keycloak must match the client IDs configured in
OpenCloud through WebFinger. OpenCloud already ships with the following
defaults, so you only need to set the corresponding environment variables if
you want to use different client IDs:

```env
WEBFINGER_WEB_OIDC_CLIENT_ID=web
WEBFINGER_ANDROID_OIDC_CLIENT_ID=OpenCloudAndroid
WEBFINGER_IOS_OIDC_CLIENT_ID=OpenCloudIOS
WEBFINGER_DESKTOP_OIDC_CLIENT_ID=OpenCloudDesktop
```

Configure each client as a public OIDC client and enable the authorization code
flow with PKCE. Do not configure a client secret.

The scopes configured on the Keycloak clients must provide the claims required
by OpenCloud. Make sure the access token or UserInfo response contains the user,
email, profile, group, and role information required by your OpenCloud setup.
The WebFinger OIDC scopes configured in OpenCloud must exist in Keycloak and be
usable by the clients. These are already the OpenCloud defaults, so you only
need to set the corresponding environment variables if you want to use
different scopes:

```env
WEBFINGER_WEB_OIDC_CLIENT_SCOPES=openid profile email
WEBFINGER_ANDROID_OIDC_CLIENT_SCOPES=openid profile email offline_access
WEBFINGER_IOS_OIDC_CLIENT_SCOPES=openid profile email offline_access
WEBFINGER_DESKTOP_OIDC_CLIENT_SCOPES=openid profile email offline_access
```

Configure the required redirect URIs for each client according to the OpenCloud
client configuration used by your deployment.

Keycloak client scopes and mappers must provide the claims required for user
mapping, user provisioning if enabled, and role assignment when the `oidc`
driver is used.

For the generic OpenCloud external IDP requirements, including issuer
variables, WebFinger client discovery, required claims, and Docker Compose
setup, see [External OpenID Connect Identity Provider](./external-idp.md).

### Advanced Configuration

#### Backchannel Logout

OpenCloud supports Keycloak's backchannel logout feature, which allows Keycloak to notify OpenCloud when a user logs out. This ensures that all sessions are properly terminated:

- Backchannel Logout URL: `https://your-domain.example.com/backchannel_logout`
- Backchannel Logout Session Required: `true`

## Shared User Directory Mode

```mermaid
graph TD
    subgraph opencloud["OpenCloud Deployment"]
        OpenCloud["OpenCloud Server"]
        Keycloak("Keycloak<br>(OIDC Provider)")
    end
    subgraph existing["Existing Infrastructure"]
        LDAP[("LDAP Server<br>(Shared User Directory)")]
    end

    OpenCloud -->|"User and Groups are looked up for sharing"| LDAP
    OpenCloud -->|"Reads Roles from claims"| Keycloak
    Keycloak -->|"Verify credentials"| LDAP
    LDAP -->|"Import Users and Groups"| Keycloak

    classDef service fill:#3498db,stroke:#2c3e50,stroke-width:2px,rx:10px,ry:10px;
    classDef storage fill:#2ecc71,stroke:#27ae60,stroke-width:2px,rx:10px,ry:10px;
    classDef readonly fill:#87CEFA,stroke:#4682B4,stroke-width:3px,rx:10px,ry:10px;
    classDef general stroke-width:2px,rx:10px,ry:10px;

    class OpenCloud,Keycloak service;
    class LDAP storage;
    class existing,directory readonly;
    class opencloud general;
```

In this mode, a readable LDAP Directory with existing users serves as a central user directory for both Keycloak and OpenCloud.

Key characteristics:

- LDAP is the source of truth for user information
- The LDAP server uses standard attributes (uid, cn, sn, givenName, mail)
- A common unique identifier (e.g. `entryUUID` or `objectGUID`) guarantees stable user mapping even if users are changing
- Both Keycloak and OpenCloud read user data directly from LDAP
- User accounts must exist in LDAP before they can log in or receive shares
- LDAP is configured as read-only for OpenCloud
- OpenCloud can create custom groups only if a subtree of the read-only LDAP can be writable

### LDAP Assumptions for Shared Directory Mode

OpenCloud can work with any LDAP schema containing standard attributes:

- User attributes: `uid`, `cn`, `sn`, `givenName`, `mail`
- Groups are stored in a dedicated organizational unit
- Default configuration sets LDAP as read-only

Example LDAP Structure:

```bash
dc=example,dc=org              # Base DN
├── ou=users                   # User organizational unit
│   ├── uid=user1              # User entries
│   └── uid=user2
└── ou=groups                  # Group organizational unit
    ├── cn=admins              # Group entries
    ├── cn=users
    └── ou=custom (optional)   # Optional custom groups tree, writable by OpenCloud
        ├── cn=teamA           # Custom Group entries
        └── cn=teamB
```

:::tip

It is possible to use a writable subtree of the LDAP server for custom groups. This is useful if you want to create groups in OpenCloud that are not managed by Keycloak.

This feature is optional and can be disabled by setting `GRAPH_LDAP_GROUP_CREATE_BASE_DN` to an empty string.

:::

### Configuration for Shared Directory Mode

Keycloak and OpenCloud can be configured using environment variables:

```bash
# Basic Keycloak configuration
KEYCLOAK_DOMAIN=keycloak.example.org
KEYCLOAK_REALM=openCloud

# OpenCloud OIDC configuration
OC_OIDC_ISSUER=https://${KEYCLOAK_DOMAIN:-keycloak.opencloud.test}/realms/${KEYCLOAK_REALM:-openCloud}
WEB_OPTION_ACCOUNT_EDIT_LINK_HREF=https://${KEYCLOAK_DOMAIN:-keycloak.opencloud.test}/realms/${KEYCLOAK_REALM:-openCloud}/account
PROXY_OIDC_REWRITE_WELLKNOWN=true
PROXY_USER_OIDC_CLAIM=uuid # this claim needs to be configured in the keycloak realm to use the keycloak user id
PROXY_USER_CS3_CLAIM=userid
# admin and demo accounts must be created in Keycloak
OC_ADMIN_USER_ID=""
SETTINGS_SETUP_DEFAULT_ASSIGNMENTS=false
GRAPH_ASSIGN_DEFAULT_USER_ROLE=false
GRAPH_USERNAME_MATCH=none

# OpenCloud LDAP configuration
OC_LDAP_URI=ldaps://ldap-server:1636
OC_LDAP_SERVER_WRITE_ENABLED=false # assuming the external ldap main tree is not writable
# Disable non writable attributes in the OpenCloud Admin UI
FRONTEND_READONLY_USER_ATTRIBUTES="user.onPremisesSamAccountName,user.displayName,user.mail,user.passwordProfile,user.accountEnabled,user.appRoleAssignments"
OC_LDAP_INSECURE=true
OC_LDAP_BIND_DN=cn=admin,dc=opencloud,dc=eu
OC_LDAP_BIND_PASSWORD=admin-password
OC_LDAP_USER_BASE_DN=ou=users,dc=opencloud,dc=eu
OC_LDAP_USER_SCHEMA_ID=entryUUID
OC_LDAP_DISABLE_USER_MECHANISM=none
OC_LDAP_GROUP_BASE_DN=ou=groups,dc=opencloud,dc=eu
OC_LDAP_GROUP_SCHEMA_ID=entryUUID
# Custom groups feature when a writable subtree is available
GRAPH_LDAP_GROUP_CREATE_BASE_DN=ou=custom,ou=groups,dc=opencloud,dc=eu
GRAPH_LDAP_SERVER_UUID=true

```

### Example Docker Compose Configuration - Shared Directory Mode

OpenCloud provides complete example deployments using Docker Compose:

1. Navigate to the `opencloud-compose` repository
2. Edit the `.env` file to enable the Shared Directory Mode:

For Shared Directory Mode:

```bash
# Enable services
COMPOSE_FILE=docker-compose.yml:idm/ldap-keycloak.yml:traefik/opencloud.yml:traefik/ldap-keycloak.yml
# Your public keycloak domain without protocol
KEYCLOAK_DOMAIN=your-keycloak-domain.example.com
# Admin user login name. Defaults to "kcadmin".
KEYCLOAK_ADMIN=
# Admin user login password. Defaults to "admin".
KEYCLOAK_ADMIN_PASSWORD=
```

The Docker Compose file `idm/ldap-keycloak.yml` contains the complete configuration for each component.

Keycloak is configured during startup by importing the `keycloak-realm.dist.json` file. This file contains the configuration for the OpenCloud realm, including client settings, roles, and user federation. This file is located in the `config/keycloak` directory of the `opencloud-compose` repository.

:::warning

Keycloak can import the realm configuration file only once during the first startup. If you need to change the configuration, you must delete the Keycloak container and volume and restart it. This will reset Keycloak to its initial state.

:::

## Autoprovisioning Mode

In this mode, Keycloak is holding all users and OpenCloud autoprovisions new users during first login.
This mode is suitable in scenarios where the OpenIDConnect provider is external and not under control of the OpenCloud admin. To mitigate that lack of control, OpenCloud will use an LDAP server which is fully under the control of the OpenCloud admin to store the users and groups and additional attributes.

```mermaid
graph TD
    subgraph opencloud["OpenCloud Deployment"]
        LDAP[("`LDAP Server
            - managed by opencloud
            - custom schema`")]
        OpenCloud["`OpenCloud Server`"]
        Stop((("Block <br>disabled<br>Users")))
    end
    subgraph existing["Existing Infrastructure"]
        Keycloak("`Keycloak<br>(OIDC Provider)`")
        UserDirectory[("`Federated Identity Provider
        - Microsoft
        - Google
        - and others`")]
    end

    OpenCloud -->|"User and Groups are created during first user login"| LDAP
    OpenCloud <-->|"User and Groups are looked up for sharing"| LDAP
    OpenCloud -- "Reads Users, Attributes, Group memberships and Roles from OIDC claims" --> Stop --> Keycloak
    UserDirectory -->|"Import Users and Groups"| Keycloak

    classDef service fill:#3498db,stroke:#2c3e50,stroke-width:2px,rx:10px,ry:10px;
    classDef storage fill:#2ecc71,stroke:#27ae60,stroke-width:2px,rx:10px,ry:10px;
    classDef readonly fill:#87CEFA,stroke:#4682B4,stroke-width:3px,rx:10px,ry:10px;
    classDef general stroke-width:2px,rx:10px,ry:10px;

    class OpenCloud,Keycloak service;
    class LDAP storage;
    class existing,directory readonly;
    class opencloud general;
```

- Keycloak manages the users, groups, and roles
- The OpenCloud Clients and Sessions are configured in Keycloak
- Simplified user management with "just-in-time" provisioning
- Federation with external identity providers is supported (e.g., Google, GitHub, Facebook, Microsoft)
- In this case, we need to provide an LDAP server which is fully controlled by OpenCloud and needs a custom [LDAP Schema](https://github.com/opencloud-eu/opencloud-compose/blob/main/config/ldap/schemas/10_opencloud_schema.ldif).

### Configuration for Autoprovisioning Mode

Keycloak, OpenCloud and OpenLDAP can be configured using environment variables:

```bash
# Basic Keycloak configuration
KEYCLOAK_DOMAIN=keycloak.example.org
KEYCLOAK_REALM=openCloud

# OpenCloud OIDC configuration
OC_OIDC_ISSUER=https://${KEYCLOAK_DOMAIN:-keycloak.opencloud.test}/realms/${KEYCLOAK_REALM:-openCloud}
WEB_OPTION_ACCOUNT_EDIT_LINK_HREF=https://${KEYCLOAK_DOMAIN:-keycloak.opencloud.test}/realms/${KEYCLOAK_REALM:-openCloud}/account
PROXY_OIDC_REWRITE_WELLKNOWN=true
PROXY_USER_OIDC_CLAIM=sub
PROXY_AUTOPROVISION_CLAIM_USERNAME=sub
PROXY_USER_CS3_CLAIM=username
# admin and demo accounts must be created in Keycloak
OC_ADMIN_USER_ID=""
SETTINGS_SETUP_DEFAULT_ASSIGNMENTS=false
GRAPH_ASSIGN_DEFAULT_USER_ROLE=false
GRAPH_USERNAME_MATCH=none

# OpenCloud LDAP configuration
OC_LDAP_URI=ldaps://ldap-server:1636
OC_LDAP_SERVER_WRITE_ENABLED=true
# Disable non writable attributes in the OpenCloud Admin UI
FRONTEND_READONLY_USER_ATTRIBUTES="user.onPremisesSamAccountName,user.displayName,user.mail,user.passwordProfile,user.memberOf"
OC_LDAP_INSECURE=true
OC_LDAP_BIND_DN=cn=admin,dc=opencloud,dc=eu
OC_LDAP_BIND_PASSWORD=admin-password
OC_LDAP_USER_BASE_DN=ou=users,dc=opencloud,dc=eu
OC_LDAP_DISABLE_USER_MECHANISM=none
OC_LDAP_GROUP_BASE_DN=ou=groups,dc=opencloud,dc=eu
```

### Example Docker Compose Configuration - Autoprovisioning Mode

OpenCloud provides complete example deployments using Docker Compose:

1. Navigate to the `opencloud-compose` repository
2. Edit the `.env` file to enable the Autoprovisioning Mode:

For Autoprovisioning Mode:

```bash
# Enable services
COMPOSE_FILE=docker-compose.yml:idm/external-idp.yml:traefik/opencloud.yml
# Your public keycloak domain without protocol
IDP_DOMAIN=your-idp-domain.example.com
# The openCloud users need to be able to edit their account in the external IdP
IDP_ACCOUNT_URL=https://your-idp-domain.example.com/realms/openCloud/account
```

The Docker Compose file `idm/external-idp.yml` contains the complete configuration for each OpenCloud component. The file `10_opencloud_ldap_schema.ldif` contains the OpenCloud LDAP schema and is loaded during the startup of the OpenLdap container. In this mode, your IdP setup is not part of the OpenCloud Deployment.

:::warning

Your external IdP configuration must match the client IDs and scopes described in the
[generic external IDP guide](./external-idp.md).

Your external IdP must provide the required claims for user provisioning and role assignment.

Claims:

- `sub`: Unique identifier for the user (used as username in OpenCloud)
- `roles`: List of roles assigned to the user (used for role assignment in OpenCloud)
- `name`: User's full name (optional, used for display purposes)
- `preferred_username`: User's preferred username (optional, more intuitive during login)
- `email`: User's email address (optional, used for notifications)
- `groups`: List of groups the user belongs to (optional, used for group assignments in OpenCloud)

:::

## Troubleshooting

Common issues and solutions:

- User cannot log in:
  - Check LDAP connectivity and user existence
  - Check if each user has an OpenCloud Role assigned
  - Verify that the client IDs and redirect URIs match exactly
- Groups not synchronized: Verify group mappings in Keycloak
- User creation fails (autoprovisioning mode): Ensure LDAP has write permissions in Autoprovisioning Mode
