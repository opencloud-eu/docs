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

<img src={require("./img/frontend-update-check/check-true.png").default} alt="check is true" width="520"/>

### Edit the `.env` File

Open the environment configuration file located in your `opencloud-compose` directory:

```bash
nano opencloud-compose/.env
```

Set the `FRONTEND_CHECK_FOR_UPDATES` environment variable to `false` to disable the frontend check for updates:

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

<img src={require("./img/frontend-update-check/check-false.png").default} alt="check is false" width="520"/>
