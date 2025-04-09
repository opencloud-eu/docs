---
sidebar_position: 3
id: keycloak
title: Keycloak Integration
---

# Keycloak Integration

OpenCloud supports using Keycloak as an external identity provider, providing enterprise-grade identity management capabilities. This guide explains how to set up and configure Keycloak with OpenCloud.

## Overview

OpenCloud employs a dual-track authentication strategy:

1. **Built-in IDP (Identity Provider)**: 
   - Based on LibreGraph Connect (lico)
   - Targeted at smaller installations (up to 500 users)
   - Designed for standalone or small deployments

2. **External Identity Providers**:
   - Keycloak as the recommended OIDC provider for larger installations
   - Support for Azure AD, EntraID, ADFS through Keycloak
   - Enterprise-focused solution

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

## Client Configuration

OpenCloud requires several OIDC clients to be configured in Keycloak. These clients are pre-configured in the Docker Compose setup and match the clients used by the built-in IdP:

### Web Client

The web client is used for browser-based access to OpenCloud:

- **Client ID**: `web`
- **Client Type**: Public client
- **Redirect URIs**: 
  - `https://your-domain.example.com/`
  - `https://your-domain.example.com/oidc-callback.html`
  - `https://your-domain.example.com/oidc-silent-redirect.html`

### Desktop Client

The desktop client is used for the OpenCloud desktop application:

- **Client ID**: `OpenCloudDesktop`
- **Client Type**: Public client
- **Redirect URIs**:
  - `http://127.0.0.1`
  - `http://localhost`

### Mobile App Clients

#### Android App

- **Client ID**: `OpenCloudAndroid`
- **Client Type**: Public client
- **Redirect URIs**: `oc://android.opencloud.eu`
- **Post Logout Redirect URIs**: `oc://android.opencloud.eu`

#### iOS App

- **Client ID**: `OpenCloudIOS`
- **Client Type**: Public client
- **Redirect URIs**: `oc://ios.opencloud.eu`
- **Post Logout Redirect URIs**: `oc://ios.opencloud.eu`

### Additional Clients

#### Cyberduck File Transfer Client

- **Client ID**: `Cyberduck`
- **Client Type**: Public client
- **Redirect URIs**:
  - `x-cyberduck-action:oauth`
  - `x-mountainduck-action:oauth`

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