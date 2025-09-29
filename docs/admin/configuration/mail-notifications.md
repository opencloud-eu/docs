---
sidebar_position: 9
id: mail-notificatons
title: Mail Notifications
description: How to activate mail notifications in OpenCloud.
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
Note: `SMTP_TRANSPORT_ENCRYPTION` and `SMTP_INSECURE` may vary depending on your setup.

SMTP Settings:

```env
SMTP_HOST=YOUR_SMTP_HOST
SMTP_PORT=1025
SMTP_SENDER=noreply@your.text
SMTP_USERNAME=YOUR_USERNAME
SMTP_PASSWORD=YOUR_PASSWORD
SMTP_TRANSPORT_ENCRYPTION=none
SMTP_INSECURE=true
```

Per default the `notifications` service is disabled. To send out notifications, the service must be enabled via:

```env
START_ADDITIONAL_SERVICES="notifications"
```

:::warning
In the .env file, values should be written without quotation marks. Do not use 'single quotes' or "double quotes" — just enter the plain value.
:::

## Save and exit

For nano, press Ctrl + O to save and Ctrl + X to exit.

## Restart OpenCloud

Apply the changes by restarting the OpenCloud services:

```bash
docker compose down
docker compose up -d
```

OpenCloud is now successfully configured to deliver notification emails, including those triggered by actions such as file sharing.
