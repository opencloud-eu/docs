---
sidebar_position: 140
id: ocm
title: Configure OpenCloud Mesh OCM
description: Configure OpenCloud Mesh OCM between two OpenCloud instances.
draft: false
---

# Configure OpenCloud Mesh

OpenCloud Mesh, abbreviated as OCM, enables users from separate OpenCloud instances to connect and share files or folders.

OCM uses an invitation-based workflow. A user on one OpenCloud instance creates an invitation, and a user on another OpenCloud instance accepts it. After the invitation has been accepted, both users are connected through OCM and can share resources across instances.

OCM must be configured on every participating OpenCloud instance.

This guide uses the following example instances:

```text
cloud1.opencloud.test
cloud2.opencloud.test
```

Replace these domains with the domains of your OpenCloud instances.

## Prerequisites

Before configuring OCM, make sure that:

- At least two OpenCloud instances are available.
- Both instances are reachable over HTTPS.
- Both instances use valid TLS certificates.
- Each instance can resolve and connect to the domain of the other instance.
- You have access to the `opencloud-compose` directory on both servers.
- The OpenCloud configuration directory is mounted to `/etc/opencloud`.
- The OpenCloud data directory is persistent.

The configuration must be applied to both instances.

## Enable OCM services

Create an `ocm.yml` file in the root of the `opencloud-compose` directory with the following content:

```yaml
services:
  opencloud:
    environment:
      OC_ENABLE_OCM: 'true'
      GRAPH_INCLUDE_OCM_SHAREES: 'true'
```

Add `ocm.yml` to the end of the existing `COMPOSE_FILE` value in the `.env` file. Keep all files that are already part of your deployment. For example:

```bash
COMPOSE_FILE=docker-compose.yml:traefik/opencloud.yml:ocm.yml
```

Using a separate Compose overlay keeps the OCM configuration independent of `docker-compose.yml` and avoids conflicts when updating the `opencloud-compose` repository.

`OC_ENABLE_OCM` enables the OCM backend services.

`GRAPH_INCLUDE_OCM_SHAREES` includes connected OCM users in the recipient search of the sharing dialog.

## Configure trusted OCM providers

Create an `ocmproviders.json` file in the mounted OpenCloud configuration directory.

For example, if the host directory `/mnt/oc/config` is mounted to `/etc/opencloud`, create:

```text
/mnt/oc/config/ocmproviders.json
```

The file is then available inside the container as:

```text
/etc/opencloud/ocmproviders.json
```

Use the same provider configuration on both OpenCloud instances.

Example configuration:

```json
[
  {
    "name": "OpenCloud 1",
    "full_name": "OpenCloud 1",
    "organization": "OpenCloud",
    "domain": "cloud1.opencloud.test",
    "homepage": "https://cloud1.opencloud.test",
    "description": "OpenCloud instance 1",
    "services": [
      {
        "endpoint": {
          "type": {
            "name": "OCM",
            "description": "OpenCloud 1 OCM API"
          },
          "name": "OpenCloud 1 OCM API",
          "path": "https://cloud1.opencloud.test/ocm/",
          "is_monitored": true
        },
        "api_version": "0.0.1",
        "host": "https://cloud1.opencloud.test"
      },
      {
        "endpoint": {
          "type": {
            "name": "Webdav",
            "description": "OpenCloud 1 WebDAV API"
          },
          "name": "OpenCloud 1 WebDAV API",
          "path": "https://cloud1.opencloud.test/dav/",
          "is_monitored": true
        },
        "api_version": "0.0.1",
        "host": "https://cloud1.opencloud.test"
      }
    ]
  },
  {
    "name": "OpenCloud 2",
    "full_name": "OpenCloud 2",
    "organization": "OpenCloud",
    "domain": "cloud2.opencloud.test",
    "homepage": "https://cloud2.opencloud.test",
    "description": "OpenCloud instance 2",
    "services": [
      {
        "endpoint": {
          "type": {
            "name": "OCM",
            "description": "OpenCloud 2 OCM API"
          },
          "name": "OpenCloud 2 OCM API",
          "path": "https://cloud2.opencloud.test/ocm/",
          "is_monitored": true
        },
        "api_version": "0.0.1",
        "host": "https://cloud2.opencloud.test"
      },
      {
        "endpoint": {
          "type": {
            "name": "Webdav",
            "description": "OpenCloud 2 WebDAV API"
          },
          "name": "OpenCloud 2 WebDAV API",
          "path": "https://cloud2.opencloud.test/dav/",
          "is_monitored": true
        },
        "api_version": "0.0.1",
        "host": "https://cloud2.opencloud.test"
      }
    ]
  }
]
```

The `domain` values must not include a protocol.

Correct:

```json
"domain": "cloud2.opencloud.test"
```

Incorrect:

```json
"domain": "https://cloud2.opencloud.test"
```

Validate the JSON file:

```bash
python3 -m json.tool /mnt/oc/config/ocmproviders.json
```

## Enable the OCM web application

The OCM web application, shown as ScienceMesh in OpenCloud Web, must be enabled in the OpenCloud Web configuration.

Create `web.yaml` in the mounted OpenCloud configuration directory.

For example, if `/mnt/oc/config` is mounted to `/etc/opencloud`, create:

```text
/mnt/oc/config/web.yaml
```

Inside the container, the file is available as:

```text
/etc/opencloud/web.yaml
```

Add the list of enabled web applications:

```yaml
# OpenCloud web configuration
web:
  config:
    apps:
      - files
      - search
      - text-editor
      - pdf-viewer
      - external
      - admin-settings
      - epub-reader
      - preview
      - app-store
      - ocm
```

The `ocm` entry enables the ScienceMesh application in OpenCloud Web.

:::important

Do not remove web applications that are required by your deployment. If your existing `web.yaml` already contains an `apps` list, add `ocm` to the existing list instead of replacing it completely. To find out what `apps` are currently loaded, you can execute the following command:

```bash
curl -sk https://cloud1.opencloud.test/config.json | jq .apps
[
  "files",
  "search",
  "text-editor",
  "pdf-viewer",
  "external",
  "admin-settings",
  "epub-reader",
  "preview",
  "app-store",
  "rclone-crypt"
]
```

:::

## Verify the configuration mount

If your OpenCloud configuration directory is already mounted to `/etc/opencloud`, no additional mount for `web.yaml` is required.

Example:

```yaml
services:
  opencloud:
    volumes:
      - ${OC_CONFIG_DIR:-opencloud-config}:/etc/opencloud
      - ${OC_DATA_DIR:-opencloud-data}:/var/lib/opencloud
      - ${OC_APPS_DIR:-./config/opencloud/apps}:/var/lib/opencloud/web/assets/apps
```

In this case, place both files in the mounted configuration directory:

```text
ocmproviders.json
web.yaml
```

If your deployment does not mount the complete OpenCloud configuration directory, mount `web.yaml` explicitly:

```yaml
services:
  opencloud:
    volumes:
      - ./config/opencloud/web.yaml:/etc/opencloud/web.yaml
```

## Recreate the OpenCloud container

Apply the configuration by recreating the OpenCloud container:

```bash
docker compose up -d --force-recreate opencloud
```

Run this command on both instances.

## Verify the configuration

Check that OCM is enabled in the running container:

```bash
docker compose exec opencloud printenv OC_ENABLE_OCM
```

Expected output:

```text
true
```

Check that remote OCM users are included in the sharing search:

```bash
docker compose exec opencloud printenv GRAPH_INCLUDE_OCM_SHAREES
```

Expected output:

```text
true
```

Check that the provider configuration is available:

```bash
docker compose exec opencloud \
  ls -la /etc/opencloud/ocmproviders.json
```

Check that the web configuration is available:

```bash
docker compose exec opencloud \
  cat /etc/opencloud/web.yaml
```

Check the resolved Compose configuration:

```bash
docker compose config | grep -A 10 -B 10 "OC_ENABLE_OCM"
```

## Verify OCM storage permissions

OCM stores invitation and sharing information below the OpenCloud data directory.

Check that the storage directory is available and writable by the OpenCloud container user:

```bash
docker compose exec opencloud sh -lc 'id && ls -ld /var/lib/opencloud /var/lib/opencloud/storage /var/lib/opencloud/storage/ocm 2>/dev/null || true'
```

If `/var/lib/opencloud/storage/ocm` does not exist yet, it may be created when the first OCM operation is performed.

If you use bind mounts, make sure that the mounted data directory is writable by the OpenCloud container user.

Example:

```bash
sudo chown -R 1000:1000 /mnt/oc/data
```

After changing permissions, recreate the container:

```bash
docker compose up -d --force-recreate opencloud
```

## Verify connectivity

Run the connectivity checks from inside the OpenCloud container.

On the first instance, check the second instance:

```bash
docker compose exec opencloud curl -I https://cloud2.opencloud.test/ocm/
docker compose exec opencloud curl -I https://cloud2.opencloud.test/sciencemesh/
docker compose exec opencloud curl -I https://cloud2.opencloud.test/dav/
```

On the second instance, check the first instance:

```bash
docker compose exec opencloud curl -I https://cloud1.opencloud.test/ocm/
docker compose exec opencloud curl -I https://cloud1.opencloud.test/sciencemesh/
docker compose exec opencloud curl -I https://cloud1.opencloud.test/dav/
```

The following responses are expected:

- `/ocm/` can return `404` because no generic endpoint is available at the base path.
- `/sciencemesh/` should return `401` without authentication.
- `/dav/` should return `401` without authentication.

A `401` response confirms that the endpoint is reachable and requires authentication.

Errors such as `502 Bad Gateway`, DNS failures, TLS failures, or connection timeouts indicate a connectivity or reverse proxy problem.

After configuring and verifying OCM, see [Connect and share through OpenCloud Mesh](../../user/sharing/opencloud-mesh.md) for the user workflow.

## Troubleshooting

### The ScienceMesh application is not visible

Check that `/etc/opencloud/web.yaml` exists inside the container:

```bash
docker compose exec opencloud \
  cat /etc/opencloud/web.yaml
```

Make sure that the application list contains:

```yaml
- ocm
```

Also verify the resolved Compose configuration:

```bash
docker compose config | grep -A 5 -B 5 "web.yaml"
```

Recreate the container after every change:

```bash
docker compose up -d --force-recreate opencloud
```

Reload OpenCloud Web without using the browser cache or open a private browser window.

### Remote users are not shown in the sharing dialog

Check the environment variable:

```bash
docker compose exec opencloud \
  printenv GRAPH_INCLUDE_OCM_SHAREES
```

Expected output:

```text
true
```

Also check that the users completed the OCM invitation process successfully.

Remote users only appear as sharing recipients after the OCM connection has been established.

For the user workflow, see [Connect and share through OpenCloud Mesh](../../user/sharing/opencloud-mesh.md).

### An invitation cannot be accepted

Check that:

- Both domains are listed in `ocmproviders.json`.
- The domains in `ocmproviders.json` do not include `https://`.
- Both instances can access each other over HTTPS.
- The ScienceMesh endpoints are reachable.

For checks that users can perform, see [Troubleshoot OpenCloud Mesh](../../user/sharing/opencloud-mesh.md#troubleshooting).

### The provider configuration is not loaded

Check the file location:

```bash
docker compose exec opencloud \
  ls -la /etc/opencloud/ocmproviders.json
```

Validate the JSON syntax:

```bash
python3 -m json.tool /mnt/oc/config/ocmproviders.json
```

Check the OpenCloud logs:

```bash
docker compose logs --since=15m opencloud \
  | grep -Ei "ocm|provider|sciencemesh|error|failed"
```

### An error message is shown in the web interface

If OpenCloud Web shows an error message, expand the details and copy the `X-Request-Id`.

Search for the request ID in the OpenCloud logs:

```bash
docker compose logs --since=30m opencloud \
  | grep -F "<X-Request-Id>" -C 20
```

Replace `<X-Request-Id>` with the request ID shown in the web interface.

You can also search for OCM-related log entries:

```bash
docker compose logs --since=30m opencloud \
  | grep -Ei "ocm|sciencemesh|invite|provider|federat|error|failed"
```

### OCM storage is not writable

Check the storage permissions:

```bash
docker compose exec opencloud sh -lc 'id && ls -ld /var/lib/opencloud /var/lib/opencloud/storage /var/lib/opencloud/storage/ocm 2>/dev/null || true'
```

If you use bind mounts, make sure that the mounted data directory is writable by the OpenCloud container user.

Example:

```bash
sudo chown -R 1000:1000 /mnt/oc/data
```

Recreate the container afterwards:

```bash
docker compose up -d --force-recreate opencloud
```
