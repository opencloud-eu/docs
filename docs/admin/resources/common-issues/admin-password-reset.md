---
sidebar_position: 5
id: admin-password-reset
title: Admin password cannot be changed in `.env`
description: Change or reset the OpenCloud admin password
draft: false
hide_table_of_contents: true
---

# Admin password cannot be changed in `.env`

## Problem

Changing the OpenCloud admin password in the `.env` file has no effect after the container has been initialized, or the current password has been forgotten.

## Cause

The `.env` value is used to set the initial admin password. Once the container is running, password changes must be made through the Web UI or terminal.

## Solution

### Option 1: Change via Web UI

If the current admin password is known:

1. Log in to the OpenCloud Web Interface.
2. Navigate to Settings > Security.
3. Enter your current password and choose a new one.

> If the admin password is forgotten or you prefer command-line tools, use the terminal method below.

### Option 2: Change via Terminal

If the admin password is forgotten or needs to be changed via the terminal:

#### Stop the Docker container

First, stop your OpenCloud container:

```bash
docker compose stop opencloud
```

#### Run the password reset command

Use the following command to reset the password:

```bash
sudo docker run -it --rm -v <opencloud-data-path>:/var/lib/opencloud -v <opencloud-config-path>:/etc/opencloud opencloudeu/opencloud:<opencloud-version> idm resetpassword
```

Replace:

- `<opencloud-data-path>` with the Docker volume for OpenCloud data.
- `<opencloud-config-path>` with the Docker volume for OpenCloud configuration.
- `<opencloud-version>` with `latest` or your specific version.

To find the volume names, list the current Docker volumes:

```bash
docker volume ls
```

Look for volumes such as:

- `opencloud-compose_opencloud-data`
- `opencloud-compose_opencloud-config`

#### Example for the standard setup

```bash
sudo docker run -it --rm -v opencloud-compose_opencloud-data:/var/lib/opencloud -v opencloud-compose_opencloud-config:/etc/opencloud opencloudeu/opencloud:latest idm resetpassword
```

#### Start the container again

```bash
docker compose up -d
```
