---
sidebar_position: 4
id: desktop-client-setup-loop
title: Desktop Client setup loops and memory usage increases
description: Stop a failed Desktop Client setup that repeatedly retries authentication
draft: false
hide_table_of_contents: true
---

# Desktop Client setup loops and memory usage increases

## Problem

When adding an account in OpenCloud Desktop Client 4.0.0, the browser does not open for authentication. The setup window may flicker and the client's memory usage continues to increase.

## Cause

The Desktop Client cannot complete the server discovery request. If the server or a reverse proxy rejects this request, version 4.0.0 repeatedly retries it instead of displaying an error.

One known cause is an NGINX Proxy Manager configuration that blocks the required WebFinger request.

## Solution

1. Close the Desktop Client. If it no longer responds, use your operating system's process manager to stop it.
2. Contact your OpenCloud administrator and provide the server address.
3. Ask the administrator to check the [Desktop Client WebFinger request](../../admin/resources/common-issues/desktop-client-setup-loop.md).
4. After the server or reverse proxy configuration has been corrected, restart the Desktop Client and add the account again.

The indefinite retry has been fixed for Desktop Client 4.0.1. The server or reverse proxy must still allow the WebFinger request before authentication can start.

For technical details, see [Desktop issue #1077](https://github.com/opencloud-eu/desktop/issues/1077).
