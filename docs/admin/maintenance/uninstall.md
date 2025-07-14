---
sidebar_position: 4
id: uninstall
title: 'Uninstall'
description: 'Guide to uninstall OpenCloud.'
---

# Uninstall OpenCloud with Docker Compose

> ⚠️ **Warning:** This guide will completely remove all OpenCloud data. Make sure to back up any important files before
> proceeding.

---

## Step 1: Stop and Remove Docker Containers

Navigate to your `opencloud-compose` directory (where your `docker-compose.yml` file is located), then run:

```shell
docker compose down
```

To also remove unnamed volumes and orphan containers:

```shell
docker compose down --volumes --remove-orphans
```

## Step 2: Remove Docker Volumes

To check your existing volumes:

```shell
docker volume ls
```

Typical OpenCloud volumes may include:

`opencloud_compose_opencloud-data`

`opencloud_compose_opencloud-config`

To delete specific volumes:

```shell
docker volume rm opencloud_compose_opencloud-data opencloud_compose_opencloud-config
```

Or to clean up all unused volumes (be careful!):

```shell
docker volume prune
```

## Step 3: Delete Mounted Directories (if used)

If your .env referenced local folders such as /mnt/opencloud/data, you should delete those manually:

```shell
sudo rm -rf /mnt/opencloud/data
sudo rm -rf /mnt/opencloud/config
```

Adjust the paths to match your setup.

## Step 4: Remove the Compose Project Folder (Optional)

If you want to delete the entire project directory:

```shell
cd ..
rm -rf opencloud-compose
```

## Result

After completing these steps, OpenCloud is fully removed, including:

- All Docker containers

- All persistent volumes

- Any local folders and mounts

- Optional project directory
