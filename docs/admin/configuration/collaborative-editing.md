---
sidebar_position: 75
id: collaborative-editing
title: Collaborative Editing with the Yjs Server
description: How to enable collaborative editing in OpenCloud with the Yjs server
draft: false
---

# Collaborative Editing

The built-in text editor supports collaborative editing via the Yjs server, meaning multiple users can edit the same file simultaneously.

The `opencloud-compose` deployment example contains all required pieces. This guide explains how to enable them.

:::note
This is not related to Collabora. Collabora brings its own collaborative editing for office documents, see the [Collabora documentation](./collabora/).
:::

## Setting up the Yjs Server

This guide assumes that you already have a running deployment based on the `opencloud-compose` deployment example.

### Configure the `.env` file to deploy the Yjs server

In the root directory of the `opencloud-compose` deployment example, add the yjs component to the `COMPOSE_FILE` variable in your `.env` file:

```bash
COMPOSE_FILE=docker-compose.yml:yjs/yjs.yml:traefik/opencloud.yml
```

### Proxy

The OpenCloud proxy needs to forward the `/yjs` route to the yjs container. This is automatically configured when using the `opencloud-compose` deployment example, you don't need to make any additional changes.

If you are using a custom proxy setup however, ensure that requests to `/yjs` are correctly routed to the yjs container. Alternatively, you can host the yjs server on a separate URL and configure the OpenCloud web frontend to use that URL by setting the `WEB_OPTION_YJS_SERVER_URL` variable accordingly. Remember that you also need to adjust your CSP configuration to allow connections to the new URL.

### Update the deployment

```bash
docker compose up -d
```

This launches an additional container (called `yjs`) using the `opencloudeu/yjs` container image.

## Configuration options

All options are set in the `.env` file. All of them are optional.

| Variable                       | Description                                                                                                        | Default                 |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| `YJS_DOCKER_IMAGE`             | Docker image for the yjs container.                                                                                | `opencloudeu/yjs`       |
| `YJS_DOCKER_TAG`               | Docker tag for the yjs container.                                                                                  | `1.0.0`                 |
| `YJS_OPENCLOUD_URL`            | URL the yjs server uses to reach OpenCloud. This is an internal address, so no TLS is used between the containers. | `http://opencloud:9200` |
| `YJS_SHUTDOWN_GRACE_PERIOD_MS` | Grace period in milliseconds for a graceful shutdown. Keep it below the `stop_grace_period` set in `yjs/yjs.yml`.  | `15000`                 |

The OpenCloud web frontend gets the address of the yjs server through the `WEB_OPTION_YJS_SERVER_URL` variable. The `yjs/yjs.yml` compose file sets this for you. Collaborative editing stays disabled as long as this variable is empty.

## Scaling

The yjs server keeps the documents in memory only. All users that edit the same file must reach the same instance. Therefore, run a single instance.
