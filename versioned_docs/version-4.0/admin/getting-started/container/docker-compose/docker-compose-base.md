---
sidebar_position: 1
id: docker-compose-base
title: Docker Compose Base
description: Full-blown featureset including web office.
draft: false
---

# OpenCloud with Docker Compose + Integrated Traefik

Install an internet-facing OpenCloud instance with automatic SSL certificates using Docker Compose's integrated Traefik reverse proxy.

This is the **recommended deployment path** for most new OpenCloud installations. Traefik automatically manages Let's Encrypt SSL certificates, eliminating the need to manage a separate reverse proxy.

This installation guide is written for Ubuntu and Debian systems. The software can also be installed on other Linux distributions, but commands and package managers may differ.

:::note Not using Traefik?
If you already have an external reverse proxy (Nginx, HAProxy, etc.) or prefer to manage it separately, see [Deploy Behind External Proxy](./external-proxy.md) instead.
:::

## Prerequisites

- Four domains pointing to your server:
  - `cloud.YOUR.DOMAIN` → OpenCloud frontend
  - `collabora.YOUR.DOMAIN` → Collabora Online Server
  - `wopiserver.YOUR.DOMAIN` → WOPI server for document editing
  - `traefik.YOUR.DOMAIN` → Traefik dashboard

  Alternatively, you can use a wildcard domain (`*.YOUR.DOMAIN`)

- A hosted server (e.g., Hetzner, AWS, or your own VPS) with Linux and SSH access

## Connect to Your Server

Log into your server via SSH:

```bash
ssh root@YOUR.SERVER.IP
```

## Install Docker

Update your system and install Docker.

First, perform an update and upgrade:

```bash
apt update && apt upgrade -y
```

Install Docker following the [official Docker guide](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

Once Docker is installed, enable and start the service:

```bash
systemctl enable docker && systemctl start docker
```

## Clone the OpenCloud Repository

Download the necessary configuration files:

```bash
git clone https://github.com/opencloud-eu/opencloud-compose.git
```

## Configure the .env File for Staging Certificates

Before requesting real SSL certificates, it is recommended to test the setup using Let's Encrypt's staging environment.

### Navigate to the OpenCloud configuration folder

```bash
cd opencloud-compose
```

### Create environment file

```bash
cp .env.example .env
```

:::note
The repository includes .env.example as a template with default settings and documentation. Your actual .env file is excluded from version control (via .gitignore) to prevent accidentally committing sensitive information like passwords and domain-specific settings.
:::

## Modify these settings

### Edit the `.env` file with the editor of your choice

In our example we use nano

```bash
nano .env
```

### Disable insecure mode

```bash
# INSECURE=true
```

### Set your domain names

```bash
TRAEFIK_DOMAIN=traefik.YOUR.DOMAIN
OC_DOMAIN=cloud.YOUR.DOMAIN
COLLABORA_DOMAIN=collabora.YOUR.DOMAIN
WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN
```

### Set your admin password

```bash
INITIAL_ADMIN_PASSWORD=YourSecurePassword
```

### Set your email for SSL certification

```bash
TRAEFIK_ACME_MAIL=your@email.com
```

### Use Let's Encrypt staging certificates (for testing)

```bash
TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory
```

### Set your deployment options

Example configuration without Collabora:

```bash
COMPOSE_FILE=docker-compose.yml:traefik/opencloud.yml
```

Save the file and exit the editor.

## Start OpenCloud

Launch OpenCloud using Docker Compose:

```bash
docker compose up -d
```

This will start all required services in the background.

## Verify Your Deployment

After starting OpenCloud, verify that services are running and SSL certificates were issued:

1. Check the [TLS/SSL certificates are valid](./verify-tls-certificates.md)
2. Log in to OpenCloud: `https://cloud.YOUR.DOMAIN`
   - Username: `admin`
   - Password: (the password you set in `.env`)

## Next Steps

- **[Verify TLS Certificates](./verify-tls-certificates.md)** – Validate staging certificates and switch to production
- **[Production Setup Considerations](./production-considerations.md)** – Persistent storage, backups, and production best practices
- **[Configure Keycloak](./keycloak-deployment.md)** (optional) – Add Keycloak for enterprise identity management
- **[Configure Authentication](../../../configuration/authentication-and-user-management/)** – User management and identity provider integration

## Troubleshooting

If you encounter issues:

1. Check Docker logs: `docker compose logs`
2. Verify domain DNS records point to your server
3. Ensure firewall allows HTTP (80) and HTTPS (443)
4. See [Common Issues & Help](../../../resources/common-issues)
