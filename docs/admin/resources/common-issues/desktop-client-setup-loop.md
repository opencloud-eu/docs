---
sidebar_position: 8
id: desktop-client-setup-loop
title: Desktop Client setup loops during authentication
description: Allow Desktop Client WebFinger requests through NGINX Proxy Manager
draft: false
hide_table_of_contents: true
---

# Desktop Client setup loops during authentication

## Problem

When a user adds an account in OpenCloud Desktop Client 4.0.0, the browser does not open for authentication. The setup window may flicker and the client's memory usage continues to increase.

The request to `/.well-known/webfinger` returns HTTP status `403` instead of the server discovery response.

## Cause

Desktop Client 4.0 introduced WebFinger-based discovery of the server's OpenID Connect parameters. The request contains the following relation as a query parameter:

```text
http://openid.net/specs/connect/1.0/issuer
```

When “Block Common Exploits” is enabled for an OpenCloud proxy host in NGINX Proxy Manager, its file-injection rule can interpret the `http://` value as an unsafe query string and return `403`.

Desktop Client 4.0.0 contains a bug that causes it to repeatedly retry a failed WebFinger request instead of reporting the error. This causes the visible setup loop and increasing memory usage.

The retry behavior is fixed in Desktop Client 4.0.1. However, WebFinger discovery is still required in Desktop Client 4.0.1 and later, so the server or reverse proxy must allow the request to succeed.

## Solution

### Verify the WebFinger request

Replace `cloud.example.com` with the address of your OpenCloud instance and send the same request used by the Desktop Client:

```bash
curl --include 'https://cloud.example.com/.well-known/webfinger?resource=https://cloud.example.com/&rel=http://openid.net/specs/connect/1.0/issuer&platform=desktop'
```

The endpoint must return a successful response containing the OpenID Connect issuer relation. If it returns `403`, check the reverse proxy logs and configuration.

### Change the NGINX Proxy Manager setting

If NGINX Proxy Manager blocks the request:

1. Open “Proxy Hosts” in NGINX Proxy Manager.
2. Edit the proxy host for OpenCloud.
3. Disable “Block Common Exploits”.
4. Save the configuration.
5. Repeat the WebFinger request and confirm that it no longer returns `403`.

:::caution

Disabling “Block Common Exploits” disables the complete NGINX Proxy Manager ruleset for this proxy host. Review the security implications for your environment.

Do not edit NGINX Proxy Manager's generated configuration files directly because they can be overwritten. If you manage NGINX yourself, make sure that no query-string rule rejects the WebFinger request solely because a parameter contains `http://`.

:::

After correcting the proxy configuration, ask the user to restart the Desktop Client and add the account again.

### Review the required reverse proxy settings

Disabling “Block Common Exploits” is not a replacement for the required OpenCloud reverse proxy configuration. Compare your configuration with [Set Up the Final Nginx Reverse Proxy](../../getting-started/container/docker-compose/docker-external-proxy.md#set-up-the-final-nginx-reverse-proxy).

In particular, verify the documented forwarded headers, buffering settings, timeouts, keep-alive limits, and maximum upload size. If you use a reverse proxy other than Nginx, configure the equivalent settings for that proxy.

For details, see [Desktop issue #1077](https://github.com/opencloud-eu/desktop/issues/1077) and the corresponding [Desktop Client fix](https://github.com/opencloud-eu/desktop/pull/1090).
