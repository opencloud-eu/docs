---
sidebar_position: 15
id: frontend-check-updates
title: Frontend Update check
description: How to disable the frontend check for updates in OpenCloud.
draft: false
---

# Disable frontend update check

## Disable Frontend Update Check

By default, OpenCloud performs a frontend check to verify if you are running the latest version.

TO DO add screenshot from the version

### Edit the `.env` File

Open the environment configuration file located in your `opencloud-compose` directory:

```bash
nano opencloud-compose/.env
```

Add the following environment variable to disable the frontend check for updates:

```env
FRONTEND_CHECK_FOR_UPDATES=false
```

## Restart Docker Services

After saving the file, shut down and restart the Docker containers to apply the changes:

```bash
docker compose down
docker compose up -d
```

## Result

The frontend will no longer display a message about newer versions being available.

TO DO add screenshot that the checker is no longer shown
