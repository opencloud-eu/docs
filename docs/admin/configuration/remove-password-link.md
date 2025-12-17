---
sidebar_position: 80
id: remove-password-from-link
title: Remove mandatory password from public link
description: Remove mandatory password from public link
draft: false
---

# Disable Mandatory Password for Public Links

By default, OpenCloud requires a password for public shares. If you'd like to disable this requirement, follow the steps below.

## Edit the `.env` File

Open the environment configuration file located in your `opencloud-compose` directory:

```bash
nano opencloud-compose/.env
```

Add the following environment variables to configure password requirements for public links:

```env
# Disable password requirement for all public links (read-only and writable)
OC_SHARING_PUBLIC_SHARE_MUST_HAVE_PASSWORD=false

# Optional: Enforce password only for writable public links
# Note: This setting only applies when OC_SHARING_PUBLIC_SHARE_MUST_HAVE_PASSWORD is set to false
OC_SHARING_PUBLIC_WRITEABLE_SHARE_MUST_HAVE_PASSWORD=true
```

## Restart Docker Services

After saving the file, shut down and restart the Docker containers to apply the changes:

```bash
docker compose down
docker compose up -d
```

## Result

- **`OC_SHARING_PUBLIC_SHARE_MUST_HAVE_PASSWORD=false`**: The system no longer enforces a password when creating public share links (both read-only and writable).
- **`OC_SHARING_PUBLIC_WRITEABLE_SHARE_MUST_HAVE_PASSWORD=true`**: If the first variable is set to `false`, this option allows you to still enforce passwords specifically for writable public shares while keeping read-only shares password-free.

:::note
This change applies globally to all public shares created after the restart.
:::
