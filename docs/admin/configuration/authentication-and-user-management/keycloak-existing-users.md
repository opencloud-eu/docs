---
sidebar_position: 4
id: keycloak-existing-users
title: Keycloak with existing users
---

# Keycloak with existing users Integration

OpenCloud supports two authentication modes when using Keycloak with existing users.

## Shared User Directory Mode

In this mode, a readable LDAP Directory with existing users serves as a central user directory for both Keycloak and OpenCloud.

**Key characteristics:**
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

**Example LDAP Structure:**
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

### Example Docker Compose Configuration

OpenCloud provides complete example deployments using Docker Compose:

1. Navigate to `deployments/examples/opencloud_full`
2. Edit the `.env` file to enable the Shared Directory Mode:

**For Shared Directory Mode:**
```bash
# Enable services
LDAP=:ldap.yml
KEYCLOAK=:keycloak.yml
# Comment out the autoprovisioning configuration
# KEYCLOAK_AUTOPROVISIONING=:keycloak-autoprovisioning.yml
```

The Docker Compose files `keycloak.yml`, `ldap.yml` contain the complete configuration for each component.

Keycloak is configured during startup by importing the `keycloak-realm.dist.json` file. This file contains the configuration for the OpenCloud realm, including client settings, roles, and user federation. This file is located in the `deployments/examples/opencloud_full/config/keycloak` directory.

:::warning

Keycloak can import the realm configuration file **only once** during the first startup. If you need to change the configuration, you must delete the Keycloak container and volume and restart it. This will reset Keycloak to its initial state.

:::
## Autoprovisioning Mode

In this mode, Keycloak is holding all users and OpenCloud autoprovisions new users during first login.
This mode is suitable in scenarios where the OpenIDConnect provider is external and not under control of the OpenCloud admin. To mitigate that lack of control, OpenCloud will use an LDAP server which is fully under the control of the OpenCloud admin to store the users and groups and additional attributes.

- Keycloak manages the users, groups, and roles
- The openCloud Clients and Sessions are configured in Keycloak
- Simplified user management with "just-in-time" provisioning
- Federation with external identity providers is supported (e.g., Google, GitHub, Facebook, Microsoft)
- In this case, we need to provide an LDAP server which is fully controlled by OpenCloud and needs a custom [LDAP Schema](https://github.com/opencloud-eu/opencloud/blob/main/deployments/examples/shared/config/ldap/schemas/10_opencloud_schema.ldif).

### Configuration for Autoprovisioning Mode

Keycloak,OpenCloud and OpenLDAP can be configured using environment variables:

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

### Example Docker Compose Configuration

OpenCloud provides complete example deployments using Docker Compose:

1. Navigate to `deployments/examples/opencloud_full`
2. Edit the `.env` file to enable the Autoprovisioning Mode:

**For Autoprovisioning Mode:**
```bash
# Enable services
LDAP=:ldap.yml
KEYCLOAK=:keycloak.yml
KEYCLOAK_AUTOPROVISIONING=:keycloak-autoprovisioning.yml
```

The Docker Compose files `keycloak.yml`, `ldap.yml`, and `keycloak-autoprovisioning.yml` contain the complete configuration for each component. The file `10_opencloud_ldap_schema.ldif` contains the OpenCloud LDAP schema and is loaded during the startup of the OpenLdap container.

Keycloak is configured during startup by importing the `keycloak-autoprovisioning-realm.dist.json` file. This file contains the configuration for the OpenCloud realm, including client settings, roles, users and groups. This file is located in the `deployments/examples/opencloud_full/config/keycloak` directory.

:::warning

Keycloak can import the realm configuration file **only once** during the first startup. If you need to change the configuration, you must delete the Keycloak container and volume and restart it. This will reset Keycloak to its initial state.

:::

### Troubleshooting

Common issues and solutions:

- **User cannot log in**: Check LDAP connectivity and user existence and check if each user has an OpenCloud Role assigned
- **Groups not synchronized**: Verify group mappings in Keycloak
- **Authentication errors**: Check Keycloak logs for OIDC-related issues
- **User creation fails**: Ensure LDAP has write permissions in Autoprovisioning Mode
