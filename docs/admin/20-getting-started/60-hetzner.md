---
sidebar_position: 6
id: hetzner
title: Hetzner Cloud
draft: false
---

# OpenCloud on Hetzner Cloud

This guide will walk you through deploying OpenCloud on a Hetzner Cloud server using Docker Compose with Let's Encrypt SSL certificates.

## Prerequisites

1. A Hetzner Cloud account
2. A domain or subdomain pointing to your Hetzner Cloud server's IP address
3. Basic knowledge of Linux, SSH, and Docker

## Server Setup

1. Create a new server in the Hetzner Cloud Console:
   - Select a server plan (we recommend at least CPX21 with 4GB RAM)
   - Choose Ubuntu 22.04 as the operating system
   - Add your SSH key for access
   - Create the server

2. Once your server is created, note its IP address and update your domain's DNS records to point to this IP address.

3. SSH into your server:
   ```bash
   ssh root@your-domain.com
   ```

4. Update the system and install required packages:
   ```bash
   apt update && apt upgrade -y
   apt install -y docker.io docker-compose git curl
   systemctl enable docker && systemctl start docker
   ```

## OpenCloud Installation

1. Clone the OpenCloud repository with Hetzner-specific configuration:
   ```bash
   mkdir -p /opt/opencloud
   cd /opt/opencloud
   git clone https://github.com/opencloud-eu/opencloud.git .
   git remote add fork https://github.com/YOUR_USERNAME/YOUR_FORK.git  # Optional: Add your fork
   git checkout hetzner-deployment  # Use the hetzner-deployment branch
   cd deployments/examples/opencloud_hetzner
   ```

   > Note: If you want to customize the deployment, consider creating your own fork of the OpenCloud repository with a hetzner-deployment branch.

2. Create the environment file:
   ```bash
   cat > .env << 'EOF'
   # Domain configuration
   OC_DOMAIN=your-domain.com
   TRAEFIK_DOMAIN=traefik.your-domain.com
   TRAEFIK_ACME_MAIL=admin@your-domain.com

   # Admin setup
   ADMIN_PASSWORD=CHANGE_ME_BEFORE_FIRST_STARTUP

   # Production-ready settings
   INSECURE=false
   DEMO_USERS=false
   PROXY_ENABLE_BASIC_AUTH=true

   # Enable web apps - uncomment these if you want to use Collabora/OnlyOffice
   #COLLABORA_DOMAIN=collabora.your-domain.com
   #ONLYOFFICE_DOMAIN=onlyoffice.your-domain.com

   # Logging configuration
   LOG_LEVEL=info
   LOG_PRETTY=false
   TRAEFIK_LOG_LEVEL=INFO

   # Optional: SMTP configuration for email notifications
   #SMTP_HOST=smtp.example.com
   #SMTP_PORT=587
   #SMTP_USERNAME=user
   #SMTP_PASSWORD=password
   #SMTP_SENDER=OpenCloud <opencloud@your-domain.com>
   #SMTP_INSECURE=false
   EOF
   ```

3. Edit the `.env` file to set your actual domain and a secure admin password:
   ```bash
   nano .env
   ```

4. Start OpenCloud:
   ```bash
   docker-compose -f docker-compose.yml -f opencloud.yml up -d
   ```

5. Check that the containers are running correctly:
   ```bash
   docker-compose -f docker-compose.yml -f opencloud.yml ps
   ```

6. View the logs to monitor the startup process:
   ```bash
   docker-compose -f docker-compose.yml -f opencloud.yml logs -f
   ```

## Accessing Your OpenCloud Instance

After a few minutes (to allow Let's Encrypt to generate certificates), your OpenCloud instance should be accessible at `https://your-domain.com`.

Log in with:
- Username: `admin`
- Password: The value you set for `ADMIN_PASSWORD` in the `.env` file

## Adding Office Document Editing

To enable document editing with Collabora or OnlyOffice:

1. Uncomment the corresponding lines in the `.env` file:
   ```
   COLLABORA_DOMAIN=collabora.your-domain.com
   ```
   or
   ```
   ONLYOFFICE_DOMAIN=onlyoffice.your-domain.com
   ```

2. Add the corresponding service to your deployment:

   For Collabora:
   ```bash
   docker-compose -f docker-compose.yml -f opencloud.yml -f ../opencloud_full/collabora.yml up -d
   ```

   For OnlyOffice:
   ```bash
   docker-compose -f docker-compose.yml -f opencloud.yml -f ../opencloud_full/onlyoffice.yml up -d
   ```

## Maintenance

### Updating OpenCloud

To update your OpenCloud instance to the latest version:

```bash
cd /opt/opencloud
git pull
cd deployments/examples/opencloud_hetzner
docker-compose -f docker-compose.yml -f opencloud.yml pull
docker-compose -f docker-compose.yml -f opencloud.yml up -d
```

### Viewing Logs

To view the logs of your OpenCloud instance:

```bash
cd /opt/opencloud/deployments/examples/opencloud_hetzner
docker-compose -f docker-compose.yml -f opencloud.yml logs -f
```

### Backing Up Data

For a simple backup of OpenCloud data, you can back up the Docker volumes:

```bash
docker run --rm -v opencloud_hetzner_opencloud-config:/source -v /backup:/backup busybox tar -cf /backup/opencloud-config-$(date +%Y%m%d).tar /source
docker run --rm -v opencloud_hetzner_opencloud-data:/source -v /backup:/backup busybox tar -cf /backup/opencloud-data-$(date +%Y%m%d).tar /source
```

## Troubleshooting

### Permission Issues

If you encounter permission issues with the config or data directories, you can fix them by setting the correct ownership:

```bash
docker-compose -f docker-compose.yml -f opencloud.yml down
docker volume rm opencloud_hetzner_opencloud-config opencloud_hetzner_opencloud-data
docker-compose -f docker-compose.yml -f opencloud.yml up -d
```

### SSL Certificate Issues

If Let's Encrypt fails to generate certificates, ensure:
1. Your domain is correctly pointing to your server's IP address
2. Ports 80 and 443 are not blocked by a firewall
3. Check the Traefik logs for specific error messages:
   ```bash
   docker-compose -f docker-compose.yml -f opencloud.yml logs traefik
   ```