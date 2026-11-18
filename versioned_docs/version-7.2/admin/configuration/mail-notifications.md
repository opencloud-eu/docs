---
sidebar_position: 40
id: mail-notifications
title: Mail Notifications
description: How to activate mail notifications in OpenCloud
draft: false
---

# Mail notifications in OpenCloud

This guide shows how to configure your OpenCloud instance to send notification E-Mails by modifying the `.env` file in your OpenCloud setup

## Open the .env File

Edit the file with your preferred text editor:

```bash
nano .env
```

Or use vim, code, or gedit as you prefer.

## Add or modify these Environment Variables

Adjust the following lines in your `.env` file according to your SMTP provider and requirements.

SMTP Settings:

```env
SMTP_HOST=YOUR_SMTP_HOST
SMTP_PORT=1025
SMTP_SENDER=noreply@your.text
SMTP_USERNAME=YOUR_USERNAME
SMTP_PASSWORD=YOUR_PASSWORD
SMTP_TRANSPORT_ENCRYPTION=none
SMTP_INSECURE=true
SMTP_AUTHENTICATION=auto
```

For available configuration options and values, see the [Environment Variables](../../dev/server/services/notifications/env-vars.mdx) section in the developer documentation.

The variables used in the `.env` file of `opencloud-compose` are mapped to the corresponding OpenCloud environment variables in `docker-compose.yml`. Their names are not always identical.

For example, `SMTP_TRANSPORT_ENCRYPTION` in the `.env` file maps to `NOTIFICATIONS_SMTP_ENCRYPTION` in OpenCloud, not `NOTIFICATIONS_SMTP_TRANSPORT_ENCRYPTION`.

When configuring OpenCloud directly without `opencloud-compose`, use the environment variable names listed in the developer documentation.

By default, the `notifications` service is disabled. To send notifications, enable the service in the `.env` file:

```env
START_ADDITIONAL_SERVICES=notifications
```

In the OpenCloud Compose setup, `START_ADDITIONAL_SERVICES` is mapped to `OC_ADD_RUN_SERVICES` inside the OpenCloud container.

## Save and exit

For nano, press Ctrl + O to save and Ctrl + X to exit.

## Restart OpenCloud

Apply the changes by restarting the OpenCloud services:

```bash
docker compose down
docker compose up -d
```

OpenCloud is now successfully configured to deliver notification emails, including those triggered by actions such as file sharing.
