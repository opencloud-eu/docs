---
sidebar_position: 2
id: external-proxy
title: Behind External Proxy
description: How to run OpenCloud behind an external Nginx proxy with Certbot (manual setup).
draft: false
---

# Running OpenCloud Behind an External Proxy (Nginx + Certbot Setup)

This guide walks you through setting up OpenCloud behind an external Nginx reverse proxy with Let's Encrypt certificates using `certbot certonly --webroot`.

## Requirements

- A public server with a static IP
- Proper DNS records for your domain:
  - `cloud.YOUR.DOMAIN`
  - `collabora.YOUR.DOMAIN` (if using Collabora)
  - `wopiserver.YOUR.DOMAIN` (if using Collabora)
  - `euro-office.YOUR.DOMAIN` (if using Euro Office)
  - `wopiserver-eo.YOUR.DOMAIN` (if using Euro Office)
- Installed software:
  - [Docker & Docker Compose](https://docs.docker.com/engine/install/)
  - `nginx`
  - `certbot`

:::tip Office Suite Choice
OpenCloud supports [Collabora](../../../configuration/collabora) and [Euro Office](../../../configuration/euro-office) as web office editors. You can use one or both. Adjust the DNS entries, certificates, and Nginx configuration below based on your choice.
:::

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

Paste the following config and adjust the URLs. Include the domains for the office suite(s) you are using:

```nginx
# Collabora only:
server {
    listen 80;
    server_name cloud.YOUR.DOMAIN collabora.YOUR.DOMAIN wopiserver.YOUR.DOMAIN;

    root /var/www/certbot;

    location /.well-known/acme-challenge/ {
        allow all;
        try_files $uri =404;
    }
}
```

If using Euro Office (alone or alongside Collabora), add the Euro Office domains to `server_name`:

```nginx
# Euro Office only:
server {
    listen 80;
    server_name cloud.YOUR.DOMAIN euro-office.YOUR.DOMAIN wopiserver-eo.YOUR.DOMAIN;
    # ...same location block as above...
}

# Both Collabora and Euro Office:
server {
    listen 80;
    server_name cloud.YOUR.DOMAIN collabora.YOUR.DOMAIN wopiserver.YOUR.DOMAIN euro-office.YOUR.DOMAIN wopiserver-eo.YOUR.DOMAIN;
    # ...same location block as above...
}
```

Enable and reload Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/certbot-challenge /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

## Obtain SSL Certificates

Use `certbot` to get your TLS certificates with adjusted URLs. Include all domains you need:

```bash
# Collabora only:
sudo certbot certonly --webroot \
  -w /var/www/certbot \
  -d cloud.YOUR.DOMAIN \
  -d collabora.YOUR.DOMAIN \
  -d wopiserver.YOUR.DOMAIN \
  --email your@email.com \
  --agree-tos \
  --no-eff-email
```

If using Euro Office, add the Euro Office domains:

```bash
# Euro Office only:
sudo certbot certonly --webroot \
  -w /var/www/certbot \
  -d cloud.YOUR.DOMAIN \
  -d euro-office.YOUR.DOMAIN \
  -d wopiserver-eo.YOUR.DOMAIN \
  --email your@email.com \
  --agree-tos \
  --no-eff-email

# Both Collabora and Euro Office:
sudo certbot certonly --webroot \
  -w /var/www/certbot \
  -d cloud.YOUR.DOMAIN \
  -d collabora.YOUR.DOMAIN \
  -d wopiserver.YOUR.DOMAIN \
  -d euro-office.YOUR.DOMAIN \
  -d wopiserver-eo.YOUR.DOMAIN \
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

Set the following environment variables based on your office suite choice:

**Collabora only:**

```env
# INSECURE=true

COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:external-proxy/opencloud.yml:external-proxy/collabora.yml

OC_DOMAIN=cloud.YOUR.DOMAIN

INITIAL_ADMIN_PASSWORD=YOUR.SECRET.PASSWORD

COLLABORA_DOMAIN=collabora.YOUR.DOMAIN

WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN
```

**Euro Office only:**

```env
# INSECURE=true

COMPOSE_FILE=docker-compose.yml:weboffice/euroffice.yml:external-proxy/opencloud.yml:external-proxy/euroffice.yml

OC_DOMAIN=cloud.YOUR.DOMAIN

INITIAL_ADMIN_PASSWORD=YOUR.SECRET.PASSWORD

EURO_OFFICE_DOMAIN=euro-office.YOUR.DOMAIN

EURO_OFFICE_WOPISERVER_DOMAIN=wopiserver-eo.YOUR.DOMAIN

EURO_OFFICE_JWT_SECRET=YOUR.EURO.OFFICE.SECRET
```

**Both Collabora and Euro Office:**

```env
# INSECURE=true

COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:weboffice/euroffice.yml:external-proxy/opencloud.yml:external-proxy/collabora.yml:external-proxy/euroffice.yml

OC_DOMAIN=cloud.YOUR.DOMAIN

INITIAL_ADMIN_PASSWORD=YOUR.SECRET.PASSWORD

COLLABORA_DOMAIN=collabora.YOUR.DOMAIN
WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN

EURO_OFFICE_DOMAIN=euro-office.YOUR.DOMAIN
EURO_OFFICE_WOPISERVER_DOMAIN=wopiserver-eo.YOUR.DOMAIN
EURO_OFFICE_JWT_SECRET=YOUR.EURO.OFFICE.SECRET
```

The initial Admin password is mandatory for security reasons.

For production releases, please refer to the considerations outlined in the Docker Compose base instructions:

[production setup consideration](./docker-compose-base#production-setup-consideration)

Start the docker compose setup

```bash
docker compose up -d
```

## Set Up the Final Nginx Reverse Proxy

### Remove the temporary certbot config

```bash
sudo rm /etc/nginx/sites-enabled/certbot-challenge
```

### Create a new proxy config

```bash
sudo nano /etc/nginx/sites-available/opencloud
```

Paste the following configuration and adjust the URLs. Include only the server blocks you need based on your office suite choice.

### Core blocks (always required)

```nginx
# Redirect HTTP to HTTPS
# Add all domains you use to server_name
server {
    listen 80;
    server_name cloud.YOUR.DOMAIN collabora.YOUR.DOMAIN wopiserver.YOUR.DOMAIN euro-office.YOUR.DOMAIN wopiserver-eo.YOUR.DOMAIN;

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
```

### Collabora blocks (if using Collabora)

```nginx
# Collabora
server {
  listen 443 ssl http2;
  server_name collabora.YOUR.DOMAIN;

  ssl_certificate /etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem;
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
  # Increase max upload size to collabora editor
  client_max_body_size 10M;

  location / {
      proxy_pass http://127.0.0.1:9980;
      proxy_set_header Host $host;
  }

  location ~ ^/cool/(.*)/ws$ {
      proxy_pass http://127.0.0.1:9980;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection "Upgrade";
      proxy_set_header Host $host;
  }

}

# Collabora WOPI Server
server {
  listen 443 ssl http2;
  server_name wopiserver.YOUR.DOMAIN;

  ssl_certificate /etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem;
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

  location / {
      proxy_pass http://127.0.0.1:9300;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
  }
}
```

### Euro Office blocks (if using Euro Office)

```nginx
# Euro Office Document Server
server {
    listen 443 ssl http2;
    server_name euro-office.YOUR.DOMAIN;

    ssl_certificate /etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    client_max_body_size 100M;

    location / {
        proxy_pass http://127.0.0.1:9900;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        # Required for WebSocket support
        proxy_set_header X-Forwarded-Proto https;
    }

    location ~ ^/(web-apps/apps/.*/(main|mobile|embed)/.*\.json|doc/.*/(c|s)/.*) {
        proxy_pass http://127.0.0.1:9900;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto https;
    }
}

# Euro Office WOPI Server
server {
    listen 443 ssl http2;
    server_name wopiserver-eo.YOUR.DOMAIN;

    ssl_certificate /etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    location / {
        proxy_pass http://127.0.0.1:9302;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

:::info Version Differences
Starting from nginx 1.25.0, the `http2` directive syntax changed from: `listen 443 ssl http2;` to `listen 443 ssl; http2 on;`
:::

:::note
We enabled HTTP/2 and increased keep-alive limits to prevent large syncs from failing and ensure stable client connections, since nginx closes connections after ~1,000 requests by default.
:::

Thanks to [mitexleo](https://github.com/mitexleo) for the Ngnix example configuration on GitHub and [zerox80](https://github.com/zerox80) for the adjustments

Enable and reload Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/opencloud /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

## Test Certificate Renewal

```bash
sudo certbot renew --dry-run
```

Your OpenCloud instance is now running securely behind a fully configured external Nginx reverse proxy with HTTPS.
