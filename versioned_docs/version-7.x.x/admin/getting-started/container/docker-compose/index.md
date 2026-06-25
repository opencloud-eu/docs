---
sidebar_position: 1
id: docker-compose-overview
title: Docker Compose Overview
description: Choose your Docker Compose deployment architecture for OpenCloud
---

# Docker Compose Deployment

This section guides you through deploying OpenCloud using Docker Compose. We support two main deployment architectures, suitable for different infrastructure scenarios.

## Choose Your Deployment Path

### 1. Integrated Traefik (Recommended for most users)

Use the built-in Traefik reverse proxy and automatic Let's Encrypt SSL certificates. This is the standard, recommended path for new deployments.

Best for:

- Standalone servers
- No existing reverse proxy infrastructure
- Simple, self-contained setup

[Get Started with Integrated Traefik →](./docker-compose-base.md)

### 2. Behind External Proxy

Use this setup if you want to run OpenCloud behind your own reverse proxy instead of the integrated Traefik setup.

The guide includes the required OpenCloud settings and an example Nginx configuration.

Best for:

- Existing reverse proxy environments
- Custom TLS handling
- Separate proxy management

[Deploy Behind External Proxy →](./docker-external-proxy.md)

## Further Configuration

After choosing and completing your deployment:

- [Production Setup Considerations](./production-considerations.md) – Persistent storage, backups, image versions
- [Verify TLS Certificates](./docker-compose-base.md#verify-tls-certificates) – Validate your SSL setup
- [Configure Authentication](../../../configuration/authentication-and-user-management/) – Users, authentication, and optional Keycloak integration
