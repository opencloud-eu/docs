---
sidebar_position: 3
id: storage-decomposeds3
title: 'Decomposeds3'
description: Decomposeds3 Storage Driver
draft: false
---

# Decomposeds3 Storage Driver

Decomposeds3 is a storage driver for OpenCloud that uses MinIO, an S3-compatible object storage, for handling file storage efficiently. This setup leverages S3’s scalability while integrating seamlessly with OpenCloud.

## Prerequisites

- Linux, Mac or Windows Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Docker](https://docs.docker.com/compose/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Start

Navigate to the Docker Compose configuration folder:

```bash
cd opencloud-compose
```

Enable `decomposeds3.yml` and `minio.yml` in the `.env` file:

```bash
nano .env
```

To activate the minio.yml, the following line must be uncommented.

```env
#DECOMPOSEDS3_MINIO=:minio.yml
```

To enable S3 storage, add `storage/decomposeds3.yml` to the COMPOSE_FILE variable or to
your startup command (`docker compose -f docker-compose.yml -f storage/decomposeds3.yml up`).

Start the deployment with Docker Compose:

```bash
docker compose up -d
```

This starts all necessary containers in the background.

## Add local domains to /etc/hosts

Edit the /etc/hosts file and add the following entries for local access:

```bash
127.0.0.1       cloud.opencloud.test
127.0.0.1       minio.opencloud.test
```

## Login

Login with your browser:

- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: admin
- password: admin

Congratulations! You’ve successfully set up and launched OpenCloud! Happy hacking!🚀

<img src={require("./../img/login-page.png").default} alt="Admin general" width="1920"/>

<img src={require("./../img/decomposeds3-with-minio.png").default} alt="Admin general" width="1920"/>

## Troubleshooting

If you encounter any issues or errors, try finding a solution here:

- [Common Issues & Help](../../resources/common-issues.md)
