---
sidebar_position: 4
id: admin-password-reset
title: Change Admin Password Set in `.env`
description: Change the admin password set in `.env`
draft: false
---

# Change Admin Password Set in `.env`

If you initially set the OpenCloud admin password using the `.env` file, please note:

:::caution
You cannot simply change the password again by editing the `.env` file.  
Once the container is running, password changes must be made via the Web UI or terminal.
:::

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

#### Replace

`<opencloud-data-path>` – Docker volume for OpenCloud data

`<opencloud-config-path>` – Docker volume for OpenCloud config

`<opencloud-version>` – Use latest or your specific version

🔍 How to find the volume names
You can list your current Docker volumes with:

```bash
docker volume ls
```

Look for volumes like:

`opencloud-compose_opencloud-data`

`opencloud-compose_opencloud-config`

#### Example for standard setup

```bash
sudo docker run -it --rm -v opencloud-compose_opencloud-data:/var/lib/opencloud -v opencloud-compose_opencloud-config:/etc/opencloud opencloudeu/opencloud:latest idm resetpassword
```

#### Start the container again

```bash
docker compose up -d
```
