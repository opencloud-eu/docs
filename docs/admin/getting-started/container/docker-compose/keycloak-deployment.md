---
sidebar_position: 6
id: docker-compose-keycloak-deployment
title: Enable Keycloak Integration
description: Add Keycloak identity management to your Docker Compose OpenCloud deployment
draft: false
---

# Keycloak Integration with Docker Compose

This guide explains how to enable Keycloak as an identity provider (IdP) for your Docker Compose OpenCloud deployment. This provides enterprise-grade user and access management.

:::note
This page covers **deployment setup only**. For detailed Keycloak configuration, user management, and integration patterns, see the [Keycloak Configuration Guide](../../../configuration/authentication-and-user-management/keycloak.md).
:::

## Prerequisites

- An existing OpenCloud Docker Compose deployment
- Understanding of [Keycloak as an identity provider](../../../configuration/authentication-and-user-management/keycloak.md)

## Enable Keycloak in `.env`

Edit your environment configuration file:

```bash
cd opencloud-compose
nano .env
```

Add or uncomment the following lines to enable **Keycloak with integrated LDAP**:

```bash
# Enable Keycloak + LDAP services
COMPOSE_FILE=docker-compose.yml:idm/ldap-keycloak.yml:traefik/opencloud.yml:traefik/ldap-keycloak.yml

# Keycloak domain (without https://)
KEYCLOAK_DOMAIN=keycloak.YOUR.DOMAIN

# Keycloak admin credentials
KEYCLOAK_ADMIN=admin
KEYCLOAK_ADMIN_PASSWORD=ChangeMeToASecurePassword
```

### Available Docker Compose configurations

The `opencloud-compose` repository provides several idm (Identity Management) options:

| Configuration           | Use Case                                                       |
| ----------------------- | -------------------------------------------------------------- |
| `idm/ldap-keycloak.yml` | Keycloak with integrated OpenLDAP (recommended for new setups) |
| `idm/keycloak.yml`      | Keycloak standalone without LDAP                               |
| `idm/openldap.yml`      | OpenLDAP only (for external IdP integration)                   |

Choose the configuration that matches your authentication infrastructure.

## Start OpenCloud with Keycloak

After updating `.env`, start the deployment:

```bash
docker compose up -d
```

Docker will pull and start the Keycloak container along with OpenCloud services.

### Wait for services to initialize

Keycloak may take a minute or two to start. Monitor the logs:

```bash
docker compose logs keycloak
```

Look for messages indicating Keycloak is ready to accept connections.

## Access Keycloak

Once running, access the Keycloak admin console:

```bash
https://keycloak.YOUR.DOMAIN
```

Log in with the credentials you set in `.env`:

- **Username:** `admin` (or your `KEYCLOAK_ADMIN` value)
- **Password:** Your `KEYCLOAK_ADMIN_PASSWORD`

## Next Steps

### 1. Configure Keycloak for OpenCloud

The Docker Compose setup auto-imports a base configuration for OpenCloud via `keycloak-realm.dist.json`. However, you'll likely need to:

- Create users and assign roles
- Configure authentication flows
- Set up LDAP federation (if using `ldap-keycloak.yml`)
- Configure OIDC client settings

See [Keycloak Configuration & Integration Guide](../../../configuration/authentication-and-user-management/keycloak.md) for detailed instructions.

### 2. Create Users in Keycloak

Follow the guide [Adding Users with Keycloak](../../../configuration/authentication-and-user-management/keycloak-user.md) to:

- Assign admin roles
- Create users with standard or guest permissions
- Enable self-registration

### 3. Update OpenCloud Configuration

Configure OpenCloud to use Keycloak as the identity provider. This typically involves setting OIDC-related environment variables. See the [Keycloak Integration documentation](../../../configuration/authentication-and-user-management/keycloak.md) for details.

## Troubleshooting

### Keycloak won't start

Check container logs:

```bash
docker compose logs keycloak
```

Common issues:

- Insufficient disk space or memory
- Port conflicts (Keycloak uses port 8080 internally)
- Database connection issues

### Can't access Keycloak admin console

Verify:

1. The domain `keycloak.YOUR.DOMAIN` resolves to your server
2. Traefik has successfully assigned SSL certificates (check via `docker compose logs traefik`)
3. Keycloak container is running: `docker compose ps keycloak`

### LDAP federation issues

If using `idm/ldap-keycloak.yml`:

1. Verify OpenLDAP is running: `docker compose ps openldap`
2. Check Keycloak logs for LDAP connection errors
3. Verify LDAP user federation is configured correctly in Keycloak admin console

## See Also

- **[Full Keycloak Integration Guide](../../../configuration/authentication-and-user-management/keycloak.md)** – Configuration, modes, and advanced setup
- **[User Management with Keycloak](../../../configuration/authentication-and-user-management/keycloak-user.md)** – Creating users and managing roles
- **[Production Considerations](./production-considerations.md)** – Backup and production best practices
