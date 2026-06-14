---
sidebar_position: 31
id: onlyoffice
title: External OnlyOffice
description: Connect an external OnlyOffice Document Server to OpenCloud via WOPI
draft: false
---

# Connecting an External OnlyOffice Server

OpenCloud supports document editing and collaboration via the WOPI protocol using OnlyOffice Document Server. This guide explains how to connect an existing, external OnlyOffice server to your OpenCloud Docker Compose setup.

:::note Companion overlay
This guide assumes the `weboffice/onlyoffice.yml` compose overlay from the [opencloud-compose](https://github.com/opencloud-eu/opencloud-compose) repository is available in your deployment.
:::

## Prerequisites

- A running OpenCloud instance (for example, `https://cloud.example.test`).
- An external OnlyOffice Document Server (for example, `https://onlyoffice.example.test`).
- A dedicated public domain for the WOPI server (for example, `https://wopi.example.test`).
- A reverse proxy (for example, Traefik or Nginx) that terminates TLS for all three domains.

## Architecture overview

| Role | Example URL | Backend |
|------|-------------|---------|
| OpenCloud UI/API | `https://cloud.example.test` | OpenCloud container (port `9200`) |
| OnlyOffice Document Server | `https://onlyoffice.example.test` | External OnlyOffice host |
| WOPI endpoint | `https://wopi.example.test` | OpenCloud `collaboration` service (port `9300`) |

Editing flow: browser → OpenCloud → OnlyOffice editor (iframe) ↔ WOPI (`collaboration:9300`) ↔ OpenCloud storage.

## 1. Configure OnlyOffice Document Server

OnlyOffice supports the WOPI protocol, but it is disabled by default. Enable it on your Document Server instance:

1. Pass the following environment variables to your OnlyOffice container:

   ```env
   WOPI_ENABLED=true
   USE_UNAUTHORIZED_STORAGE=true
   ```

2. Retrieve the JWT secret from your OnlyOffice instance. Starting from version 7.2, JWT is enabled by default. To read the automatically generated secret, run:

   ```bash
   docker exec -it <onlyoffice-container-id> /var/www/onlyoffice/documentserver/npm/json \
     -f /etc/onlyoffice/documentserver/local.json \
     'services.CoAuthoring.secret.session.string'
   ```

   Save this value. You will need it as `ONLYOFFICE_JWT_SECRET` in OpenCloud.

3. Verify that OnlyOffice exposes its WOPI discovery endpoint:

   ```bash
   curl -sI https://onlyoffice.example.test/hosting/discovery
   ```

   Expected response: HTTP `200` with `Content-Type: text/xml`.

## 2. Configure OpenCloud

### Update environment variables

Add the following variables to your `.env` file in the OpenCloud Compose directory:

```env
OC_URL=https://cloud.example.test
ONLYOFFICE_URL=https://onlyoffice.example.test
WOPISERVER_URL=https://wopi.example.test
ONLYOFFICE_JWT_SECRET=<your-onlyoffice-jwt-secret>
```

Update your `COMPOSE_FILE` variable to include the OnlyOffice overlay and expose OpenCloud on your host:

```env
COMPOSE_FILE=docker-compose.yml:external-proxy/opencloud-exposed.yml:weboffice/onlyoffice.yml
```

:::tip Initial admin password
Ensure `INITIAL_ADMIN_PASSWORD` is set in `.env` before starting OpenCloud. An empty value can cause the `opencloud` container to restart continuously after initialization.
:::

### Expose the WOPI port

The `external-proxy/opencloud-exposed.yml` overlay publishes OpenCloud on port `9200`. The WOPI endpoint runs on the `collaboration` service at port `9300` and must be reachable by OnlyOffice through your reverse proxy.

Create a local compose override file (for example, `external-proxy/wopi-exposed.yml`):

```yaml
---
services:
  collaboration:
    ports:
      - "0.0.0.0:9300:9300"
```

Append it to `COMPOSE_FILE`:

```env
COMPOSE_FILE=docker-compose.yml:external-proxy/opencloud-exposed.yml:external-proxy/wopi-exposed.yml:weboffice/onlyoffice.yml
```

:::note
If you also run the built-in Collabora stack, you can reuse `external-proxy/collabora-exposed.yml` instead of creating `wopi-exposed.yml`.
:::

Apply the configuration:

```bash
docker compose up -d
```

If the `collaboration` service was recreated, restart it after OpenCloud is healthy:

```bash
docker compose restart collaboration
```

### Apply Content Security Policy (CSP)

To allow the OnlyOffice editor iframe to load, authorize your OnlyOffice domain in OpenCloud's Content Security Policy.

Open your OpenCloud CSP configuration (for example, `config/opencloud/csp.yaml` or the path referenced by `${OC_CONFIG_DIR}`) and add your OnlyOffice domain under the `frame-src` directive:

```yaml
frame-src:
  - '''self'''
  - 'blob:'
  - 'https://onlyoffice.example.test/'
```

If OpenCloud reads configuration from a runtime directory (for example, `/opt/opencloud/config/`), copy the updated file there and ensure ownership is `1000:1000`:

```bash
sudo cp config/opencloud/csp.yaml /opt/opencloud/config/csp.yaml
sudo chown 1000:1000 /opt/opencloud/config/csp.yaml
docker compose restart opencloud
```

## 3. Reverse proxy and routing

Configure your reverse proxy so that:

- `cloud.example.test` → OpenCloud host port `9200`
- `wopi.example.test` → OpenCloud host port `9300` (`collaboration` service)
- `onlyoffice.example.test` → your external OnlyOffice Document Server

### Example Nginx snippet for WOPI

```nginx
server {
  listen 443 ssl;
  server_name wopi.example.test;

  location / {
    proxy_pass http://127.0.0.1:9300;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  }
}
```

OnlyOffice must be able to reach `WOPISERVER_URL` (`https://wopi.example.test`) from its network location.

## 4. Verify the integration

| Check | Expected result |
|-------|-----------------|
| `curl -sI https://onlyoffice.example.test/hosting/discovery` | HTTP `200`, `text/xml` |
| `docker compose ps` | `opencloud` and `collaboration` are running; port `9300` is published |
| `docker compose logs collaboration` | No repeated discovery or WOPI errors |
| OpenCloud web UI | Office documents open in the OnlyOffice editor |

## Troubleshooting

### OnlyOffice discovery errors in collaboration logs

If `collaboration` logs show HTTP `404` or connection errors for `/hosting/discovery`, confirm that `WOPI_ENABLED=true` is set on OnlyOffice and that the discovery endpoint returns HTTP `200`.

### Editor iframe blocked

If the editor does not load, verify the CSP `frame-src` entry for `https://onlyoffice.example.test/` and restart the `opencloud` service after updating `csp.yaml`.

### JWT or WOPI authentication failures

Ensure `ONLYOFFICE_JWT_SECRET` in OpenCloud exactly matches the secret from OnlyOffice's `local.json`. Both sides must use the same JWT configuration.

## Related documentation

- [Collabora](./collabora/) — built-in Collabora Online integration
- [Running OpenCloud Behind an External Proxy](../getting-started/container/docker-compose/docker-external-proxy.md)
- [Collaboration service environment variables](../../dev/server/services/collaboration/info.mdx)
