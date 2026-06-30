---
sidebar_position: 3
id: external-proxy
title: Behind External Proxy
description: How to run OpenCloud behind an external Nginx proxy with Certbot (manual setup).
draft: false
---

# Running OpenCloud Behind an External Proxy (Nginx + Certbot Setup)

This guide walks you through setting up OpenCloud behind an external Nginx reverse proxy with Let's Encrypt certificates using `certbot certonly --webroot`.

:::note Using Traefik Instead?
If you don't have an existing reverse proxy or prefer to let Traefik manage certificates automatically, see [Docker Compose with Integrated Traefik](./docker-compose-base.md) instead.
:::

## Requirements

- A public server with a static IP
- Proper DNS records for your domain:
  - `cloud.YOUR.DOMAIN`
  - `collabora.YOUR.DOMAIN`
- Installed software:
  - [Docker & Docker Compose](https://docs.docker.com/engine/install/)
  - `nginx`
  - `certbot`

## Connect to Your Server

Log into your server via SSH:

```bash
ssh root@YOUR.SERVER.IP
```

## Install Docker

Update your system and install Docker.

## Install Nginx & Certbot

Now install Nginx & Certbot

## Create a Webroot Directory for Certbot

```bash
sudo mkdir -p /var/www/certbot
sudo chown -R www-data:www-data /var/www/certbot
```

## Temporary Nginx Config for HTTP Challenge

Create a temporary config to allow HTTP validation:

```bash
sudo nano /etc/nginx/sites-available/certbot-challenge
```

Paste the following config and adjust the URLs:

```nginx
server {
    listen 80;
    server_name cloud.YOUR.DOMAIN collabora.YOUR.DOMAIN;

    root /var/www/certbot;

    location /.well-known/acme-challenge/ {
        allow all;
        try_files $uri =404;
    }
}
```

Enable and reload Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/certbot-challenge /etc/nginx/sites-enabled/certbot-challenge
sudo nginx -t && sudo systemctl reload nginx
```

## Obtain SSL Certificates

Use `certbot` to get your TLS certificates with adjusted URLs:

```bash
sudo certbot certonly --webroot \
  -w /var/www/certbot \
  -d cloud.YOUR.DOMAIN \
  -d collabora.YOUR.DOMAIN \
  --email your@email.com \
  --agree-tos \
  --no-eff-email
```

Your certificates will be saved under:

- `/etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem`
- `/etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem`

## Configure and start OpenCloud

Clone the OpenCloud Compose repo and set your environment:

```bash
git clone https://github.com/opencloud-eu/opencloud-compose.git
cd opencloud-compose
cp .env.example .env
nano .env
```

Set the following environment variables:

```env
# INSECURE=true

COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:external-proxy/opencloud.yml:external-proxy/collabora.yml

OC_DOMAIN=cloud.YOUR.DOMAIN

INITIAL_ADMIN_PASSWORD=YOUR.SECRET.PASSWORD

COLLABORA_DOMAIN=collabora.YOUR.DOMAIN
```

The initial Admin password is mandatory for security reasons.

:::note
The WOPI endpoint is served by OpenCloud on the OpenCloud domain. It is available through the OpenCloud proxy under `/wopi` and `/collaboration`.

A separate `wopiserver` domain, reverse proxy block, or exposed WOPI port is not required.
:::

Start the docker compose setup

```bash
docker compose up -d
```

## Further Configuration

For production deployments, review [Production Considerations](./production-considerations.md) for:

- Persistent volumes and data recovery
- Using the appropriate stable branch
- Permission and ownership best practices

## Set Up the Final Nginx Reverse Proxy

### Remove the temporary certbot config

```bash
sudo rm /etc/nginx/sites-enabled/certbot-challenge
```

### Create a new proxy config

```bash
sudo nano /etc/nginx/sites-available/opencloud
```

Paste the following configuration and adjust the URLs:

```nginx
# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name cloud.YOUR.DOMAIN collabora.YOUR.DOMAIN;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

# OpenCloud
server {
    listen 443 ssl http2;
    server_name cloud.YOUR.DOMAIN;

    ssl_certificate /etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    # Increase max upload size (required for Tus — without this, uploads over 1 MB fail)
    client_max_body_size 10M;

    # Disable buffering - essential for SSE
    proxy_buffering off;
    proxy_request_buffering off;

    # Extend timeouts for long connections
    proxy_read_timeout 3600s;
    proxy_send_timeout 3600s;
    keepalive_requests 100000;
    keepalive_timeout 5m;
    http2_max_concurrent_streams 512;

    # Prevent nginx from trying other upstreams
    proxy_next_upstream off;

    location / {
        proxy_pass http://127.0.0.1:9200;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# Collabora
server {
    listen 443 ssl http2;
    server_name collabora.YOUR.DOMAIN;

    ssl_certificate /etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    client_max_body_size 10M;

    location / {
        proxy_pass http://127.0.0.1:9980;

        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Real-IP $remote_addr;

        proxy_read_timeout 36000s;
        proxy_send_timeout 36000s;
    }

    location ~ ^/cool/(.*)/ws$ {
        proxy_pass http://127.0.0.1:9980;

        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";

        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Real-IP $remote_addr;

        proxy_read_timeout 36000s;
        proxy_send_timeout 36000s;
    }
}
```

:::info Version Differences
Starting from nginx 1.25.0, the `http2` directive syntax changed from: `listen 443 ssl http2;` to `listen 443 ssl; http2 on;`
:::

:::note
We enabled HTTP/2 and increased keep-alive limits to prevent large syncs from failing and ensure stable client connections, since nginx closes connections after ~1,000 requests by default.
:::

Thanks to [mitexleo](https://github.com/mitexleo) for the Nginx example configuration on GitHub and [zerox80](https://github.com/zerox80) for the adjustments.

Enable and reload Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/opencloud /etc/nginx/sites-enabled/opencloud
sudo nginx -t && sudo systemctl reload nginx
```

Verify that Nginx is listening on port `443`:

```bash
sudo ss -tulpn | grep ':443'
```

Verify that Collabora is reachable through the external proxy:

```bash
curl -k https://collabora.YOUR.DOMAIN/hosting/discovery | head
```

## Test Certificate Renewal

```bash
sudo certbot renew --dry-run
```

Your OpenCloud instance is now running securely behind a fully configured external Nginx reverse proxy with HTTPS.

## Timeout Considerations

When using a reverse proxy other than the documented Nginx example, make sure that request and response timeouts are configured for long-running uploads.

Slow uploads or large file uploads can take longer than the default timeout of some reverse proxies. If the timeout is too low, uploads may fail with `502 Bad Gateway` after about 60 seconds.

For custom reverse proxy setups, configure the equivalent of the relevant Nginx options, such as:

- `proxy_read_timeout`
- `proxy_send_timeout`
- `proxy_request_buffering off`
- `proxy_buffering off`

The exact option names depend on the reverse proxy in use.
