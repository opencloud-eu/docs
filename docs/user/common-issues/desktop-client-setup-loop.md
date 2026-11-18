---
sidebar_position: 4
id: desktop-client-setup-loop
title: Desktop Client setup loops and memory usage increases
description: Get help when Desktop Client setup does not open the browser
draft: false
hide_table_of_contents: true
---

# Desktop Client setup loops and memory usage increases

## Problem

When adding an account in the OpenCloud Desktop Client, the browser does not open for authentication. The setup window may flicker and the client's memory usage continues to increase.

## Cause

The Desktop Client cannot complete the server discovery request. The server or reverse proxy configuration may need to be adjusted by an administrator.

## Solution

1. Close the Desktop Client. If it no longer responds, use your operating system's process manager to stop it.
2. Contact your OpenCloud administrator and provide the server address.
3. Ask the administrator to follow the troubleshooting steps in [Desktop Client setup loops during authentication](../../admin/resources/common-issues/desktop-client-setup-loop.md).
4. After the server or reverse proxy configuration has been corrected, restart the Desktop Client and add the account again.
