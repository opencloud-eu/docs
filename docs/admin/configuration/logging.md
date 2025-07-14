---
sidebar_position: 13
id: logging
title: Logging
---

# Logging in OpenCloud

---

## Introduction

Logging helps monitor OpenCloud’s health and diagnose issues. Log output varies by level, from minimal to detailed. By default, logs are written to `stderr`. In Docker deployments, logs are accessible via `docker logs`.

---

## Log Levels

Set the global log level using the `OPEN_CLOUD_LOG_LEVEL` environment variable. You can also override it per service using service-specific variables. Default is `error`.

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

---

## Request Correlation

### X-Request-ID

OpenCloud supports tracing using the `X-Request-ID` header. Clients send a UUID v4 with each request, which is included in backend logs for correlation.

To manually test with `curl`, add:

```bash
--header "X-Request-ID: <your-id>"
```
