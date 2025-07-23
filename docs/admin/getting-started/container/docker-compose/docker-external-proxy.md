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
  - `collabora.YOUR.DOMAIN`
  - `wopiserver.YOUR.DOMAIN`
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
git clone https://github.com/opencloud-eu/opencloud.git
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

Paste the following config and adjust the URLs:

```nginx
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

Enable and reload Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/certbot-challenge /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

## Obtain SSL Certificates

Use `certbot` to get your TLS certificates with adjusted URLs:

```bash
sudo certbot certonly --webroot \
  -w /var/www/certbot \
  -d cloud.YOUR.DOMAIN \
  -d collabora.YOUR.DOMAIN \
  -d wopiserver.YOUR.DOMAIN \
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

WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN
```

The initial Admin password is mandatory for security reasons.

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

Paste the following configuration and adjust the URLs:

```nginx
# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name cloud.YOUR.DOMAIN collabora.YOUR.DOMAIN wopiserver.YOUR.DOMAIN;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

# OpenCloud
server {
    listen 443 ssl;
    server_name cloud.YOUR.DOMAIN;

    ssl_certificate /etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem;

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
    listen 443 ssl;
    server_name collabora.YOUR.DOMAIN;

    ssl_certificate /etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem;

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

# WOPI Server
server {
    listen 443 ssl;
    server_name wopiserver.YOUR.DOMAIN;

    ssl_certificate /etc/letsencrypt/live/cloud.YOUR.DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/cloud.YOUR.DOMAIN/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:9300;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Thanks to [mitexleo](https://github.com/mitexleo) for the Ngnix example configuration on GitHub

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
