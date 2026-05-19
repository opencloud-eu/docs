---
sidebar_position: 1
id: euro-office
title: Euro Office
description: Configuration guides for Euro Office integration in OpenCloud
draft: false
---

# Euro Office

[Euro Office](https://github.com/EURO-office/DocumentServer) is a sovereign document editing suite based on ONLYOFFICE that integrates with OpenCloud via the WOPI protocol.

:::warning
The Euro Office project is currently in its early stages and may have stability issues.
:::

## What you will find here

- Set up Euro Office with OpenCloud using Docker Compose.
- Configure Euro Office behind an external Nginx reverse proxy.

## Docker Compose Setup

Euro Office is available as a compose module in the [opencloud-compose](https://github.com/opencloud-eu/opencloud-compose) project.

### With Traefik (built-in reverse proxy)

Set the following in your `.env` file:

```env
COMPOSE_FILE=docker-compose.yml:weboffice/euroffice.yml:traefik/opencloud.yml:traefik/euroffice.yml

EURO_OFFICE_DOMAIN=euro-office.YOUR.DOMAIN
WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN
EURO_OFFICE_JWT_SECRET=YOUR.SECRET
```

### With an external proxy (Nginx, Caddy, etc.)

Set the following in your `.env` file:

```env
COMPOSE_FILE=docker-compose.yml:weboffice/euroffice.yml:external-proxy/opencloud.yml:external-proxy/euroffice.yml

EURO_OFFICE_DOMAIN=euro-office.YOUR.DOMAIN
WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN
EURO_OFFICE_JWT_SECRET=YOUR.SECRET
```

For the full Nginx configuration guide, see [Behind External Proxy](../../getting-started/container/docker-compose/external-proxy).



## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `EURO_OFFICE_DOMAIN` | `euro-office.opencloud.test` | Domain of the Euro Office document server |
| `EURO_OFFICE_JWT_SECRET` | `changeme` | JWT secret for Euro Office. **Change this for production!** |
| `EURO_OFFICE_DOCKER_IMAGE` | `ghcr.io/euro-office/documentserver` | Docker image for the document server |
| `EURO_OFFICE_DOCKER_TAG` | `latest` | Docker image tag |

## Exposed Ports (External Proxy)

When using an external reverse proxy, the following ports are exposed on the host:

| Service | Host Port | Description |
|---|---|---|
| Euro Office Document Server | `9900` | The document editing interface |
| Euro Office WOPI Server | `9300` | WOPI protocol endpoint (collaboration service) |

## DNS Entries

When deploying with custom domains, make sure DNS records point to your server for:

- `euro-office.YOUR.DOMAIN`
- `wopiserver.YOUR.DOMAIN`

For local testing with `.test` domains, add to `/etc/hosts`:

```text
127.0.0.1 euro-office.opencloud.test
127.0.0.1 wopiserver.opencloud.test
```
