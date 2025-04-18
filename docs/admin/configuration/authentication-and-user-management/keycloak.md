---
sidebar_position: 3
id: keycloak
title: Keycloak Integration
---

# Keycloak Integration

OpenCloud supports using Keycloak as an external identity provider, providing enterprise-grade identity management capabilities. This guide explains how to set up and configure Keycloak with OpenCloud.

## Setting Up Keycloak with Docker Compose

OpenCloud includes a pre-configured Keycloak setup in the Docker Compose examples. To enable Keycloak:

1. Navigate to your OpenCloud deployment directory
2. Edit the `.env` file and uncomment the Keycloak line:
   ```
   KEYCLOAK=:keycloak.yml
   ```
3. Configure the following environment variables in the same file:
   ```
   KEYCLOAK_DOMAIN=your-domain.example.com
   KEYCLOAK_REALM=openCloud
   KEYCLOAK_ADMIN_USER=admin
   KEYCLOAK_ADMIN_PASSWORD=your-secure-password
   ```
4. Start the deployment with Keycloak:
   ```bash
   docker-compose up -d
   ```
   
   > **Note**: This simplified command works because of the `COMPOSE_FILE` variable in the `.env` file. When you uncomment the `KEYCLOAK=:keycloak.yml` line, the colon-prefixed value is automatically appended to the `COMPOSE_FILE` variable in the last line of the `.env` file, making it unnecessary to specify the configuration files explicitly.

## OpenCloud Configuration for Keycloak

When using Keycloak as the identity provider, you need to configure OpenCloud with the following settings:

```
PROXY_AUTOPROVISION_ACCOUNTS=true
PROXY_ROLE_ASSIGNMENT_DRIVER=oidc
OC_OIDC_ISSUER=https://your-domain.example.com/realms/openCloud
PROXY_OIDC_REWRITE_WELLKNOWN=true
PROXY_USER_OIDC_CLAIM=preferred_username
GRAPH_ASSIGN_DEFAULT_USER_ROLE=false
GRAPH_USERNAME_MATCH=none
OC_EXCLUDE_RUN_SERVICES=idp
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
   - If you previously used the built-in IdP and switched to Keycloak, you may need to remove the client configuration files and reinstall the desktop client
   - On Windows: Delete configuration at `%APPDATA%/OpenCloud/opencloud.cfg`
   - On macOS: Delete configuration at `~/Library/Preferences/OpenCloud/opencloud.cfg`
   - On Linux: Delete configuration at `~/.config/OpenCloud/opencloud.cfg`

## User and Group Management

When Keycloak is enabled:

1. Users and groups are primarily managed in Keycloak
2. Groups are passed via OIDC tokens in the "groups" claim
3. OpenCloud maps external groups to internal representations

For more details on user management with Keycloak, refer to the [Keycloak documentation](https://www.keycloak.org/documentation).
