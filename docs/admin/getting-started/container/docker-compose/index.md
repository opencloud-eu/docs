---
sidebar_position: 1
id: docker-compose-overview
title: Docker Compose Overview
description: Choose your Docker Compose deployment architecture for OpenCloud
---

# Docker Compose Deployment

This section guides you through deploying OpenCloud using Docker Compose. We support two main deployment architectures, suitable for different infrastructure scenarios.

## Choose Your Deployment Path

### 1. **Integrated Traefik** (Recommended for most users)

Use the built-in Traefik reverse proxy and automatic Let's Encrypt SSL certificates. This is the standard, recommended path for new deployments.

**Best for:**

- Standalone servers
- No existing reverse proxy infrastructure
- Simple, self-contained setup

[Get Started with Integrated Traefik →](./integrated-traefik.md)

### 2. **Behind External Proxy** (For existing infrastructure)

Deploy OpenCloud behind your own Nginx, HAProxy, or other reverse proxy. Choose this if you already have a reverse proxy in place or prefer to manage it separately.

**Best for:**

- Multi-service environments
- Existing reverse proxy infrastructure
- Complex networking requirements

[Deploy Behind External Proxy →](./external-proxy.md)

## Next Steps

After choosing and completing your deployment:

- **[Production Setup Considerations](./production-considerations.md)** – Persistent storage, backups, image versions
- **[Verify TLS Certificates](./verify-tls-certificates.md)** – Validate your SSL setup
- **[Configure Authentication](../../../configuration/authentication-and-user-management/)** – Users, authentication, and optional Keycloak integration

## Project Structure

Both deployment paths use the same underlying composition of services:

- OpenCloud server
- Collabora Online Editor (optional)
- WOPI Server
- Database
- Object Storage (MinIO)
- Optional: Traefik (integrated path) or your external proxy (external path)

Choose the path that best matches your infrastructure and requirements.
