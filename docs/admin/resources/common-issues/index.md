---
sidebar_position: 1
id: common-issues-overview
title: Common Issues & Help
description: Common issues and help
draft: false
toc_max_heading_level: 2
---

# Common Issues & Help

Use this page to find troubleshooting guidance for common administration issues.

## Startup and permissions

- [OpenCloud containers are not running](./containers-not-running.md)
- [Docker Compose fails with permission denied](./docker-permissions.md)

## Browser and certificates

- [Browser rejects a self-signed certificate](./self-signed-certificates.md)

## Access and account recovery

- [Admin password cannot be changed in `.env`](./admin-password-reset.md)
- [Login fails with LDAP Result Code 49](./ldap-invalid-credentials.md)

## Desktop Client connections

- [Desktop Client setup loops during authentication](./desktop-client-setup-loop.md)

## IDM and certificates

- [Internal LibreIDM certificate expires](./libreidm-cert-expiry.md)

## Standalone Docker startup failures

The [standalone Docker guide](../../getting-started/container/docker.md)
uses `--rm` in the startup command. This removes the container when
it exits, making startup failures harder to investigate.

To troubleshoot:

1. Remove `--rm` from the startup command before retrying.
2. Run `docker ps -a` to check the container status.
3. Run `docker logs opencloud` to inspect startup errors.
4. Correct the problem. Remove a stopped container with
   `docker rm opencloud` before reusing the same container name.

Removing the container does not delete data stored in bind mounts
or named volumes.

On macOS, `extended attributes not supported` may indicate an
incompatible host bind mount. See the
[Docker guide](../../getting-started/container/docker.md)
for the named-volume workaround.
