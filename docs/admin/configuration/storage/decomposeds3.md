---
sidebar_position: 3
id: storage-decomposeds3
title: 'Decomposeds3'
description: Decomposeds3 Storage Driver
draft: false
---

# Decomposeds3 Storage Driver

Decomposeds3 is a storage driver for OpenCloud that uses MinIO — an S3-compatible object storage — to store files efficiently. This setup combines the scalability of S3 with seamless integration into OpenCloud.

:::warning

This setup includes **No Migration Path** from existing storage solutions. If you are already using another storage backend, you will need to migrate your data manually.

:::

## Configure an S3 Bucket

1. **Access your S3 Service**: Log in to your S3-compatible service (e.g., Hetzner S3, MinIO, AWS S3).
2. **Create a Bucket**: Create a new bucket named `opencloud` (or any name you prefer).
3. **Set Permissions**: Ensure the bucket has the necessary permissions for read and write operations
4. **Note the Endpoint and Credentials**: Make a note of the endpoint URL, access key, and secret key for your S3 service.
5. **CORS Configuration**: If your S3 service requires CORS configuration, ensure that it allows requests from your OpenCloud domain.
6. **Region**: Note the region where your bucket is created, as it may be required for configuration.

## Setup OpenCloud

Navigate to the folder containing the Docker Compose configuration:

```bash
cd opencloud-compose
```

Open the `.env` file and fill the required configuration variables:

```bash
nano .env
```

Now we need all the information about the S3 bucket we created earlier. Modify the following lines in your `.env` file:

```yaml
# Configure the S3 storage endpoint. Defaults to "http://minio:9000" for testing purposes.
DECOMPOSEDS3_ENDPOINT=https//your-s3-endpoint.example.com
# S3 region. Defaults to "default".
DECOMPOSEDS3_REGION=eu-central-1
# S3 access key. Defaults to "opencloud"
DECOMPOSEDS3_ACCESS_KEY=<your-access-key>
# S3 secret. Defaults to "opencloud-secret-key"
DECOMPOSEDS3_SECRET_KEY=<your-secret-key>
# S3 bucket. Defaults to "opencloud"
DECOMPOSEDS3_BUCKET=opencloud
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

## Login

Open your browser and log in.

After logging in, you should see the OpenCloud interface:

<img src={require("./../img/login-page.png").default} alt="Login Page" width="1920"/>

<img src={require("./../img/decomposeds3-with-minio.png").default} alt="OpenCloud with decomposeds3 and MinIO" width="1920"/>

## Troubleshooting

If you run into any issues or errors, check the following resource:

- [Common Issues & Help](../../resources/common-issues.md)
