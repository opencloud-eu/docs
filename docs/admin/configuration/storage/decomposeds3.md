---
sidebar_position: 3
id: storage-decomposeds3
title: 'Decomposeds3'
description: Decomposeds3 Storage Driver
draft: false
---

# Decomposeds3 Storage Driver

Decomposeds3 is a storage driver for OpenCloud that uses MinIO — an S3-compatible object storage — to store files efficiently. This setup combines the scalability of S3 with seamless integration into OpenCloud.

## Setup

Navigate to the folder containing the Docker Compose configuration:

```bash
cd opencloud-compose
```

Open the `.env` file and enable the required configuration files:

```bash
nano .env
```

Uncomment the following line to enable MinIO in the S3 Storage configuration block:

```env
#DECOMPOSEDS3_MINIO=:minio.yml
```

Add `storage/decomposeds3.yml` to the `COMPOSE_FILE` variable
or include it directly in the startup command:

```bash
docker compose -f docker-compose.yml -f storage/decomposeds3.yml up
```

Start all containers in the background:

```bash
docker compose up -d
```

## Add Local Domains to /etc/hosts

To enable local access, add the following lines to your `/etc/hosts` file:

```bash
127.0.0.1       cloud.opencloud.test
127.0.0.1       minio.opencloud.test
```

## Login

Open your browser and visit:

- [https://cloud.opencloud.test](https://cloud.opencloud.test)

After logging in, you should see the OpenCloud interface:

<img src={require("./../img/login-page.png").default} alt="Login Page" width="1920"/>

<img src={require("./../img/decomposeds3-with-minio.png").default} alt="OpenCloud with decomposeds3 and MinIO" width="1920"/>

## Troubleshooting

If you run into any issues or errors, check the following resource:

- [Common Issues & Help](../../resources/common-issues.md)
