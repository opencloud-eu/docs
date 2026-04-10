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
EURO_OFFICE_WOPISERVER_DOMAIN=wopiserver-eo.YOUR.DOMAIN
EURO_OFFICE_JWT_SECRET=YOUR.SECRET
```

### With an external proxy (Nginx, Caddy, etc.)

Set the following in your `.env` file:

```env
COMPOSE_FILE=docker-compose.yml:weboffice/euroffice.yml:external-proxy/opencloud.yml:external-proxy/euroffice.yml

EURO_OFFICE_DOMAIN=euro-office.YOUR.DOMAIN
EURO_OFFICE_WOPISERVER_DOMAIN=wopiserver-eo.YOUR.DOMAIN
EURO_OFFICE_JWT_SECRET=YOUR.SECRET
```

For the full Nginx configuration guide, see [Behind External Proxy](../../getting-started/container/docker-compose/external-proxy).

### Using both Collabora and Euro Office

Both office suites can run simultaneously. In this case, OpenDocument formats (`.odt`, `.ods`, `.odp`) open in Collabora while Microsoft Office formats (`.docx`, `.xlsx`, `.pptx`) open in Euro Office.

:::info
To avoid app interlocking issues, be aware that there is currently no cross-app file locking. If a file is opened in one app, the other app must wait for the lock to be released.
:::

With Traefik:

```env
COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:weboffice/euroffice.yml:traefik/opencloud.yml:traefik/collabora.yml:traefik/euroffice.yml
```

With external proxy:

```env
COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:weboffice/euroffice.yml:external-proxy/opencloud.yml:external-proxy/collabora.yml:external-proxy/euroffice.yml
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `EURO_OFFICE_DOMAIN` | `euro-office.opencloud.test` | Domain of the Euro Office document server |
| `EURO_OFFICE_WOPISERVER_DOMAIN` | `wopiserver-eo.opencloud.test` | Domain of the WOPI server for Euro Office |
| `EURO_OFFICE_JWT_SECRET` | `changeme` | JWT secret for Euro Office. **Change this for production!** |
| `EURO_OFFICE_DOCKER_IMAGE` | `ghcr.io/euro-office/documentserver` | Docker image for the document server |
| `EURO_OFFICE_DOCKER_TAG` | `latest` | Docker image tag |

## Exposed Ports (External Proxy)

When using an external reverse proxy, the following ports are exposed on the host:

| Service | Host Port | Description |
|---|---|---|
| Euro Office Document Server | `9900` | The document editing interface |
| Euro Office WOPI Server | `9302` | WOPI protocol endpoint (collaboration service) |

## DNS Entries

When deploying with custom domains, make sure DNS records point to your server for:

- `euro-office.YOUR.DOMAIN`
- `wopiserver-eo.YOUR.DOMAIN`

For local testing with `.test` domains, add to `/etc/hosts`:

```text
127.0.0.1 euro-office.opencloud.test
127.0.0.1 wopiserver-eo.opencloud.test
```
