---
sidebar_position: 1
id: docker-compose-base
title: Default Setup with Traefik
description: Full-blown featureset including web office.
draft: false
---

# OpenCloud with Docker Compose + Integrated Traefik

Install an internet-facing OpenCloud instance with automatic SSL certificates using Docker Compose's integrated Traefik reverse proxy.

This is the recommended deployment path for most new OpenCloud installations. Traefik automatically manages Let's Encrypt SSL certificates, eliminating the need to manage a separate reverse proxy.

This installation guide is written for Ubuntu and Debian systems. The software can also be installed on other Linux distributions, but commands and package managers may differ.

:::note Not using Traefik?
If you already have an external reverse proxy (Nginx, HAProxy, etc.) or prefer to manage it separately, see [Deploy Behind External Proxy](./docker-external-proxy.md) instead.
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

### Set the deployment option

Set the `COMPOSE_FILE` variable based on the components you want to deploy.

For an OpenCloud deployment without Collabora, use:

```bash
COMPOSE_FILE=docker-compose.yml:traefik/opencloud.yml
```

To deploy OpenCloud with Collabora, use:

```bash
COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:traefik/opencloud.yml:traefik/collabora.yml:radicale/radicale.yml
```

Save the file and exit the editor.

## Start OpenCloud

Launch OpenCloud using Docker Compose:

```bash
docker compose up -d
```

This will start all required services in the background.

## Verify TLS Certificates

After starting OpenCloud, verify that SSL certificates were issued correctly and switch from staging to production certificates when ready.

### Verify Staging Certificates

By default, the setup uses Let's Encrypt staging certificates for testing. These are not trusted by browsers but prove that the DNS and certificate generation workflow is correct.

Open the following URL:

```bash
https://cloud.YOUR.DOMAIN
```

Because the setup currently uses Let's Encrypt staging certificates, your browser will show a security warning. This is expected and normal for the staging environment.

The same warning may appear for the other configured domains.

### Example in Chrome

Click on the lock icon to view certificate details:

<img src={require("./../../img/docker-compose/certificate-details.png").default} alt="Certificate Details" width="500"/>

Expand the certificate information to confirm it was issued by "Let's Encrypt Staging":

<img src={require("./../../img/docker-compose/certificate-viewer.png").default} alt="Certificate Details" width="500"/>

<img src={require("./../../img/docker-compose/subordinate-ca's.png").default} alt="Certificate Details Subordinate CA" width="500"/>

:::success Staging Certificate Success
If you see "Let's Encrypt Staging" as the issuer, the certificate generation is working correctly. You can now safely switch to production certificates.
:::

## Switch to Production Certificates

Once the staging certificate works correctly, you can switch to production SSL certificates from Let's Encrypt.

### Stop Docker Compose

```bash
docker compose down
```

### Remove old staging certificates

Delete the previously generated staging certificates:

```bash
rm -r certs
```

:::warning
If you changed volume names or paths in your `.env` file, adjust this command to match your certificate directory.
:::

### Disable staging mode in `.env`

Open the environment file:

```bash
nano .env
```

Comment out or remove the staging server line:

```bash
# TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory
```

Save the file.

### Restart OpenCloud with production certificates

Start the containers again:

```bash
docker compose up -d
```

Traefik will now request trusted production certificates from Let's Encrypt.

### Wait for certificate generation

Certificate generation may take a few moments. Check the logs:

```bash
docker compose logs traefik
```

Look for messages indicating successful certificate generation.

### Verify production certificates

After a short moment, visiting your domain should show a secure HTTPS connection:

<img src={require("./../../img/docker-compose/status-secure.png").default} alt="Secure Connection" width="1920"/>

The lock icon should show "Secure" (green lock) with "Let's Encrypt Authority X3" or similar as the issuer.

## Log into OpenCloud

Once certificates are verified:

1. Open your domain in a browser:

```bash
https://cloud.YOUR.DOMAIN
```

2. Log in with your admin credentials:
   - Username: `admin`
   - Password: (the password you configured in the `.env` file)

<img src={require("./../../img/docker-compose/login.png").default} alt="OpenCloud Login" width="1920"/>

## Further Configuration

- [Production Setup Considerations](./production-considerations.md) – Persistent storage, backups, and production best practices
- [Configure Keycloak](./keycloak-deployment.md) (optional) – Add Keycloak for enterprise identity management
- [Configure Authentication](../../../configuration/authentication-and-user-management/) – User management and identity provider integration

## Troubleshooting

If you encounter issues:

1. Check Docker logs: `docker compose logs`
2. Verify domain DNS records point to your server
3. Ensure firewall allows HTTP (80) and HTTPS (443)
4. See [Common Issues & Help](../../../resources/common-issues.md)
