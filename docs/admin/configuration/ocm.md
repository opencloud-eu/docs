---
sidebar_position: 50
id: ocm
title: Configure OpenCloud Mesh OCM
description: Configure OpenCloud Mesh OCM to connect users and share resources between two OpenCloud instances.
draft: false
---

# Configure OpenCloud Mesh

OpenCloud Mesh, abbreviated as OCM, enables users from separate OpenCloud instances to connect and share files or folders.

OCM uses an invitation-based workflow. A user on one OpenCloud instance creates an invitation, and a user on another OpenCloud instance accepts it. After the invitation has been accepted, both users are connected through OCM and can share resources across instances.

OCM must be configured on every participating OpenCloud instance.

This guide uses the following example instances:

```text
cloud.anja.opencloud.rocks
cloud.heiko.opencloud.rocks
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

Open `docker-compose.yml` and locate the `environment` section of the `opencloud` service.

Add the following variables:

```yaml
OC_ENABLE_OCM: 'true'
GRAPH_INCLUDE_OCM_SHAREES: 'true'
```

Example:

```yaml
services:
  opencloud:
    environment:
      OC_DEFAULT_LANGUAGE: ${DEFAULT_LANGUAGE}
      OC_ENABLE_OCM: 'true'
      GRAPH_INCLUDE_OCM_SHAREES: 'true'
```

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
    "name": "OpenCloud Anja",
    "full_name": "OpenCloud Anja",
    "organization": "OpenCloud",
    "domain": "cloud.anja.opencloud.rocks",
    "homepage": "https://cloud.anja.opencloud.rocks",
    "description": "OpenCloud instance Anja",
    "services": [
      {
        "endpoint": {
          "type": {
            "name": "OCM",
            "description": "OpenCloud Anja OCM API"
          },
          "name": "OpenCloud Anja OCM API",
          "path": "https://cloud.anja.opencloud.rocks/ocm/",
          "is_monitored": true
        },
        "api_version": "0.0.1",
        "host": "https://cloud.anja.opencloud.rocks"
      },
      {
        "endpoint": {
          "type": {
            "name": "Webdav",
            "description": "OpenCloud Anja WebDAV API"
          },
          "name": "OpenCloud Anja WebDAV API",
          "path": "https://cloud.anja.opencloud.rocks/dav/",
          "is_monitored": true
        },
        "api_version": "0.0.1",
        "host": "https://cloud.anja.opencloud.rocks"
      }
    ]
  },
  {
    "name": "OpenCloud Heiko",
    "full_name": "OpenCloud Heiko",
    "organization": "OpenCloud",
    "domain": "cloud.heiko.opencloud.rocks",
    "homepage": "https://cloud.heiko.opencloud.rocks",
    "description": "OpenCloud instance Heiko",
    "services": [
      {
        "endpoint": {
          "type": {
            "name": "OCM",
            "description": "OpenCloud Heiko OCM API"
          },
          "name": "OpenCloud Heiko OCM API",
          "path": "https://cloud.heiko.opencloud.rocks/ocm/",
          "is_monitored": true
        },
        "api_version": "0.0.1",
        "host": "https://cloud.heiko.opencloud.rocks"
      },
      {
        "endpoint": {
          "type": {
            "name": "Webdav",
            "description": "OpenCloud Heiko WebDAV API"
          },
          "name": "OpenCloud Heiko WebDAV API",
          "path": "https://cloud.heiko.opencloud.rocks/dav/",
          "is_monitored": true
        },
        "api_version": "0.0.1",
        "host": "https://cloud.heiko.opencloud.rocks"
      }
    ]
  }
]
```

The `domain` values must not include a protocol.

Correct:

```json
"domain": "cloud.heiko.opencloud.rocks"
```

Incorrect:

```json
"domain": "https://cloud.heiko.opencloud.rocks"
```

Validate the JSON file:

```bash
python3 -m json.tool /mnt/oc/config/ocmproviders.json
```

## Enable the OCM web application

The OCM web application must be enabled in the OpenCloud Web configuration.

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

The `ocm` entry enables the OCM application in OpenCloud Web.

:::important

Do not remove web applications that are required by your deployment. If your existing `web.yaml` already contains an `apps` list, add `ocm` to the existing list instead of replacing it completely.

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

On the Anja instance, check the Heiko instance:

```bash
docker compose exec opencloud curl -I https://cloud.heiko.opencloud.rocks/ocm/
docker compose exec opencloud curl -I https://cloud.heiko.opencloud.rocks/sciencemesh/
docker compose exec opencloud curl -I https://cloud.heiko.opencloud.rocks/dav/
```

On the Heiko instance, check the Anja instance:

```bash
docker compose exec opencloud curl -I https://cloud.anja.opencloud.rocks/ocm/
docker compose exec opencloud curl -I https://cloud.anja.opencloud.rocks/sciencemesh/
docker compose exec opencloud curl -I https://cloud.anja.opencloud.rocks/dav/
```

The following responses are expected:

- `/ocm/` can return `404` because no generic endpoint is available at the base path.
- `/sciencemesh/` should return `401` without authentication.
- `/dav/` should return `401` without authentication.

A `401` response confirms that the endpoint is reachable and requires authentication.

Errors such as `502 Bad Gateway`, DNS failures, TLS failures, or connection timeouts indicate a connectivity or reverse proxy problem.

## Open the OCM application

After recreating the container:

1. Sign out of OpenCloud Web.
2. Reload the page without using the browser cache or open a private browser window.
3. Sign in again.
4. Open the application switcher.
5. Select the OCM application.

The application provides the interface for creating and accepting OCM invitations.

## Connect users

Before users can share resources between instances, they must establish an OCM connection.

:::important

Create the invitation on one OpenCloud instance and accept it on the other OpenCloud instance.

Do not accept an invitation on the same instance where it was created.

:::

On the first instance:

1. Open the OCM application.
2. Create a new invitation.
3. Copy the generated invitation link or token.
4. Send the invitation link or token to the user on the second instance.

On the second instance:

1. Open the invitation link or open the OCM application.
2. Sign in to OpenCloud.
3. Accept the invitation.

After the invitation has been accepted, the remote user becomes available as an OCM connection.

:::note

Copy the full invitation link or token. Do not use the shortened token text that may be displayed in the invitation table.

By default, invitation tokens expire after 24 hours. If an invitation cannot be accepted because it has expired, create a new invitation.

:::

## Share a file or folder

After both users are connected:

1. Open the Files application.
2. Select a file or folder.
3. Open the sharing panel.
4. Search for the connected remote user.
5. Select the remote user.
6. Configure the permissions.
7. Create the share.

The remote user should now receive the shared resource on the other OpenCloud instance.

## Troubleshooting

### The OCM application is not visible

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

### An invitation cannot be accepted

Check that:

- Both domains are listed in `ocmproviders.json`.
- The domains in `ocmproviders.json` do not include `https://`.
- Both instances can access each other over HTTPS.
- The ScienceMesh endpoints are reachable.
- The invitation has not expired.
- The user is signed in to the receiving OpenCloud instance.
- The invitation is accepted on the other OpenCloud instance, not on the instance where it was created.
- The full invitation link or token was copied.

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
