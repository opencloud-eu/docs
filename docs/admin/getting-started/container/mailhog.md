---
sidebar_position: 4
id: mailhog
title: Mailhog
description: "Integrating Mailhog into OpenCloud"
---

# Mailhog

## Integrating Mailhog into OpenCloud Using `docker-compose.yml`

This guide explains how to integrate Mailhog into an existing OpenCloud setup using Traefik and Docker Compose. This version uses a single `docker-compose.yml` file for simplicity and clarity.

---

## Prerequisites

* A running OpenCloud environment using Docker Compose
* A properly configured Traefik reverse proxy
* A working external network for Traefik (e.g., `opencloud_full_opencloud-net`)
* A DNS record for `mailhog.YOURDOMAIN`

---

## Step-by-step Instructions

### 1. Modify `docker-compose.yml`

Edit your existing `docker-compose.yml` and add the Mailhog service **within the `services:` block**, directly below the other services like `traefik`.

```yaml
services:
  mailhog:
    image: mailhog/mailhog
    container_name: mailhog
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.mailhog.rule=Host(`mailhog.YOUR.DOMAIN`)"
      - "traefik.http.routers.mailhog.entrypoints=https"
      - "traefik.http.routers.mailhog.tls.certresolver=http"
      - "traefik.http.services.mailhog.loadbalancer.server.port=8025"
    networks:
      - opencloud-net
```

### 2. Ensure the network is defined

At the bottom of your `docker-compose.yml`, verify that the `opencloud-net` network is defined as external:

```yaml
networks:
  opencloud-net:
    external: true
    name: opencloud_full_opencloud-net
```

### 3. Recreate the network (if necessary)

If the `opencloud_full_opencloud-net` network doesn't exist, create it manually:

```bash
docker network create opencloud_full_opencloud-net
```

### 4. Start the Mailhog service

Use Docker Compose to start Mailhog:

```bash
docker compose up -d mailhog
```

### 5. Verify Traefik routing

Check the Traefik dashboard (e.g., `traefik.YOURDOMAIN`) to ensure that the `mailhog` router appears under "HTTP Routers".

### 6. Access Mailhog

Navigate to:

```
https://mailhog.YOUR.DOMAIN
```

You should see the Mailhog web UI.

### 7. Configure OpenCloud to use Mailhog (Optional)

In your OpenCloud `.env` file, set the SMTP variables as follows:

```env
SMTP_HOST=mailhog
SMTP_PORT=1025
SMTP_SENDER=noreply@your.text
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_AUTHENTICATION=
SMTP_TRANSPORT_ENCRYPTION=none
SMTP_INSECURE=true
```

Save the file and restart OpenCloud:

```bash
docker compose up -d
```

---

Now your OpenCloud instance should send emails via Mailhog, and you can view them in the Mailhog web interface!
