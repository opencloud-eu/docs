---
sidebar_position: 95
id: euro-office
title: Euro Office
description: Community supported Euro Office setup for OpenCloud.
draft: false
---

# Euro Office

:::note Community Documentation
This guide is provided as community documentation.

EuroOffice is not officially supported by OpenCloud. The configuration shown here is maintained as a community contribution and is not covered by official OpenCloud support.

Use this guide as a reference for community-based setups. For officially supported office integrations, use the officially documented OpenCloud options.
:::

[Euro Office](https://github.com/EURO-office/DocumentServer) is a sovereign document editing suite maintained by several european organisations as a joint effort. It integrates with OpenCloud via WOPI and the app provider mechanism.

:::warning
The Euro Office project is currently in its early stages and may have stability issues.
:::

Thanks to [zerox80](https://github.com/zerox80) for the initial Euro Office documentation.

## Docker Compose Setup

Euro Office is available as a compose module in the [opencloud-compose](https://github.com/opencloud-eu/opencloud-compose) project.

### With Traefik (built-in reverse proxy)

Set the following in your `.env` file:

```env
COMPOSE_FILE=docker-compose.yml:weboffice/euroffice.yml:traefik/opencloud.yml:traefik/euroffice.yml

EURO_OFFICE_DOMAIN=euro-office.YOUR.DOMAIN
EURO_OFFICE_JWT_SECRET=YOUR.SECRET
```

### With an external proxy (Nginx, Caddy, etc.)

Set the following in your `.env` file:

```env
COMPOSE_FILE=docker-compose.yml:weboffice/euroffice.yml:external-proxy/opencloud.yml:external-proxy/euroffice.yml

EURO_OFFICE_DOMAIN=euro-office.YOUR.DOMAIN
EURO_OFFICE_JWT_SECRET=YOUR.SECRET
```

## Nginx Configuration for External Proxy

When running Euro Office behind an external Nginx reverse proxy, add the following server blocks to your Nginx configuration.

For the general OpenCloud external proxy setup, see [Behind External Proxy](../getting-started/container/docker-compose/external-proxy).

### SSL Certificates

Make sure your SSL certificates also cover the Euro Office domain. Add it to your `certbot` command:

```bash
sudo certbot certonly --webroot \
  -w /var/www/certbot \
  -d euro-office.YOUR.DOMAIN \
  --email your@email.com \
  --agree-tos \
  --no-eff-email
```

### Euro Office Nginx Server Blocks

Add this server block to your Nginx configuration alongside the OpenCloud and Collabora blocks:

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
```

Make sure to also add `euro-office.YOUR.DOMAIN` to the `server_name` directive of your HTTP-to-HTTPS redirect block.

## Environment Variables

| Variable                   | Default                              | Description                                             |
| -------------------------- | ------------------------------------ | ------------------------------------------------------- |
| `EURO_OFFICE_DOMAIN`       | `euro-office.opencloud.test`         | Domain of the Euro Office document server               |
| `EURO_OFFICE_JWT_SECRET`   | `changeme`                           | JWT secret for Euro Office. Change this for production. |
| `EURO_OFFICE_DOCKER_IMAGE` | `ghcr.io/euro-office/documentserver` | Docker image for the document server                    |
| `EURO_OFFICE_DOCKER_TAG`   | `latest`                             | Docker image tag                                        |

## Exposed Ports (External Proxy)

When using an external reverse proxy, the following port is exposed on the host:

| Service                     | Host Port | Description                    |
| --------------------------- | --------- | ------------------------------ |
| Euro Office Document Server | `9900`    | The document editing interface |

## DNS Entries

When deploying with custom domains, make sure a DNS record points to your server for:

- `euro-office.YOUR.DOMAIN`

For local testing with `.test` domains, add to `/etc/hosts`:

```text
127.0.0.1 euro-office.opencloud.test
```
