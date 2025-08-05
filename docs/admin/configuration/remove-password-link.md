---
sidebar_position: 13
id: remove-password-from-link
title: Remove mandatory password from public link
description: Remove mandatory password from public link
draft: true
---

# Disable Mandatory Password for Public Links

By default, OpenCloud requires a password for public shares. If you'd like to disable this requirement, follow the steps below.

## Edit the `.env` File

Open the environment configuration file located in your `opencloud-compose` directory:

```bash
nano opencloud-compose/.env
```

Add the following environment variable to disable the password requirement for public links:

```env
OC_SHARING_PUBLIC_SHARE_MUST_HAVE_PASSWORD=false
```

## Restart Docker Services

After saving the file, shut down and restart the Docker containers to apply the changes:

```bash
docker compose down
docker compose up -d
```

## Result

The system no longer enforces a password when creating public share links.

:::note
This change applies globally to all public shares created after the restart.
:::