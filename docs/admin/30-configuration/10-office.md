---
sidebar_position: 1
id: office
title: Office
draft: true
---


# Collabora Online Integration

The OpenCloud Docker Compose setup includes an integrated [Collabora Online](https://www.collaboraoffice.com/collabora-online/) server, enabling real-time collaborative editing of office documents directly in the browser.

## Supported File Formats

Collabora Online supports a wide range of formats, including:

- **Microsoft Office**: `.docx`, `.xlsx`, `.pptx`, etc.
- **Open Document Format (ODF)**: `.odt`, `.ods`, `.odp`
- **Other formats**: such as **Visio** and **Publisher** (viewing only)

## Collabora CODE

By default, OpenCloud uses the [**Collabora Online Development Edition (CODE)**](https://www.collaboraonline.com/code/).  
CODE is feature-rich and designed for testing and small-scale deployments.

> ⚠️ **Note**: CODE receives frequent updates and may include experimental features.

## Enterprise Edition Recommendation

For **production environments** or **enterprise use cases**, we recommend using the **Collabora Online Enterprise Edition**. It provides:

- Long-term support (LTS)
- Enhanced performance and scalability
- Regular security updates and maintenance

A commercial subscription is required and can be obtained via mail@opencloud.eu

## Enable Collabora

To enable collabora in your productive docker compose setup you need following URLs pointed to your server:

- `collabora.YOUR.DOMAIN` → Collabora Online Server
- `wopiserver.YOUR.DOMAIN` → WOPI server for document editing

or like described in the [Docker Compose](./../../20-getting-started/20-docker/20-docker-compose.md) use a wildcard domain.

Set your domain names in the .env file

```bash
COLLABORA_DOMAIN=collabora.YOUR.DOMAIN
WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN
```