---
sidebar_position: 100
id: logging
title: Logging
description: Logging in OpenCloud
draft: false
---

# Logging in OpenCloud

Logging helps monitor OpenCloud’s health and diagnose issues. Log output varies by level, from minimal to detailed. By default, logs are written to `stderr`. In Docker deployments, logs are accessible via `docker logs`.

## Log Levels

Set the global log level in your `.env` file using `LOG_LEVEL`, which maps to `OC_LOG_LEVEL`. The default is `error`.

If you want to change the log level for individual services, define the corresponding service-specific variables in the `environment:` section of the relevant service in `docker-compose.yaml`, for example `PROXY_LOG_LEVEL=info` or `SHARING_LOG_LEVEL=info`.

## The log levels are

### FATAL

Critical issues that cause the application to shut down — such as config errors or missing dependencies.

### ERROR

Severe problems that block proper operation and require admin attention.

### WARN

Unexpected conditions that don’t stop the app but may need investigation.

### INFO

Routine events that confirm expected behavior and operation.

### DEBUG

Highly detailed messages for diagnosing problems. Use cautiously in production due to verbosity.

## Request Correlation

### X-Request-ID

OpenCloud supports tracing using the `X-Request-ID` header. Clients send a UUID v4 with each request, which is included in backend logs for correlation.

To manually test with `curl`, add:

```bash
--header "X-Request-ID: <your-id>"
```
