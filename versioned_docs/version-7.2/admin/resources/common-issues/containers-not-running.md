---
sidebar_position: 2
id: containers-not-running
title: OpenCloud containers are not running
description: Check whether the OpenCloud containers are running
draft: false
hide_table_of_contents: true
---

# OpenCloud containers are not running

## Problem

OpenCloud is unavailable or does not work as expected.

## Cause

One or more required containers may not be running.

## Solution

Check the running containers:

```bash
docker ps
```

<img src={require("../img/common-issues/quick-docker-running.png").default} alt="Admin general" width="1920"/>

Several containers should be listed, for example OpenCloud and Traefik.

If an expected container is missing or not running, check the logs for errors or warnings:

```bash
docker compose logs
```

To inspect a specific service, add its name:

```bash
docker compose logs <service-name>
```

Use the log messages to identify the affected service and continue troubleshooting the reported error.
