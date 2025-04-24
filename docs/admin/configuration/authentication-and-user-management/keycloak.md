---
sidebar_position: 3
id: keycloak
title: Keycloak Integration
---

# Keycloak Integration

OpenCloud supports using Keycloak as an external identity provider, providing enterprise-grade identity management capabilities. This guide explains how to set up and configure Keycloak with OpenCloud.

## OpenCloud Configuration for Keycloak

When using Keycloak as the identity provider, you need to configure OpenCloud with the following settings:

```
PROXY_AUTOPROVISION_ACCOUNTS=true|false # that depends on your setup
PROXY_ROLE_ASSIGNMENT_DRIVER=oidc
OC_OIDC_ISSUER=https://your-domain.example.com/realms/openCloud
WEB_OPTION_ACCOUNT_EDIT_LINK_HREF=https://your-domain.example.com/realms/openCloud/account
PROXY_OIDC_REWRITE_WELLKNOWN=true
PROXY_USER_OIDC_CLAIM=preferred_username|sub|uuid # this depends on your setup
# admin and demo accounts must be created in Keycloak
OC_ADMIN_USER_ID: ""
SETTINGS_SETUP_DEFAULT_ASSIGNMENTS: "false"
GRAPH_ASSIGN_DEFAULT_USER_ROLE: "false"
GRAPH_USERNAME_MATCH=none
OC_EXCLUDE_RUN_SERVICES=idp,idm # it is not supported to run keycloak with the built-in idm
```

Look [here](./external-idp.md#opencloud-configuration) for some more details about these settings.

## Client Configuration

The [OIDC clients](./external-idp.md#client-configuration) required by OpenCloud are pre-configured in the Docker Compose setup and match the clients used by the built-in IdP.

## Advanced Configuration

### Backchannel Logout

OpenCloud supports Keycloak's backchannel logout feature, which allows Keycloak to notify OpenCloud when a user logs out. This ensures that all sessions are properly terminated:

- **Backchannel Logout URL**: `https://your-domain.example.com/backchannel_logout`
- **Backchannel Logout Session Required**: `true`

### Manual Client Configuration

If you need to manually configure the clients in Keycloak:

1. Log in to the Keycloak admin console
2. Select the OpenCloud realm
3. Navigate to Clients and click Create
4. Configure each client according to the specifications above
5. Ensure all clients have the appropriate scopes:
   - web-origins
   - profile
   - roles
   - groups
   - basic
   - email

## Troubleshooting

### Common Issues

1. **Authentication Fails**:
   - Verify that the client IDs and redirect URIs match exactly
   - Ensure the clients are properly configured as public clients
   - Check that the backchannel logout URL is correct

2. **Mobile App Authentication Fails**:
   - Verify the custom URI schemes (oc://) are correctly configured
   - Ensure the post logout redirect URIs are set correctly

3. **Desktop Client Authentication Fails**:
   - Verify localhost and 127.0.0.1 redirect URIs are correctly configured

## User and Group Management

When Keycloak is enabled:

1. Users and groups are primarily managed in Keycloak
2. Groups are passed via OIDC tokens in the "groups" claim
3. OpenCloud maps external groups to internal representations

For more details on user management with Keycloak, refer to the [Keycloak documentation](https://www.keycloak.org/documentation).

## Existing User Integration with Keycloak

To integrate with already existing users from an Identity management OpenCloud supports two authentication modes:

1. **Shared User Directory Mode**: LDAP serves as a central user directory for both Keycloak and OpenCloud
2. **Autoprovisioning Mode**: The Identity Provider (Keycloak) manages users, groups, and roles, while OpenCloud autoprovisions new users during first login in its own user directory. This is the case when the Identity Provider is "read only" or if the users are coming from a federated Identity Provider (e.g., Google, GitHub, Facebook, Microsoft).

For detailed configuration and setup instructions, see the [Keycloak with existing users](./keycloak-existing-users.md) guide.
