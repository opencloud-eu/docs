---
sidebar_position: 50
id: configure-open-cloud-mesh
title: Configure Open Cloud Mesh
description: Configure Open Cloud Mesh to connect users and share resources between two OpenCloud instances.
draft: false
---

# Configure Open Cloud Mesh

Open Cloud Mesh, abbreviated as OCM, enables users from separate OpenCloud instances to connect and share files or folders.

OCM must be configured on every participating OpenCloud instance.

This guide uses the following example instances:

```text
https://cloud.anja.opencloud.rocks
https://cloud.heiko.opencloud.rocks
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

Example configuration:

```json
[
  {
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

Use the same provider configuration on both OpenCloud instances.

Validate the JSON file:

```bash
python3 -m json.tool /mnt/oc/config/ocmproviders.json
```

## Enable the OCM web application

Create the following file in the `opencloud-compose` directory:

```text
config/opencloud/web.yaml
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

## Mount the web configuration

Open `docker-compose.yml` and locate the `volumes` section of the `opencloud` service.

Add the following mount:

```yaml
- ./config/opencloud/web.yaml:/etc/opencloud/web.yaml
```

Example:

```yaml
services:
  opencloud:
    volumes:
      - ./config/opencloud/csp.yaml:/etc/opencloud/csp.yaml
      - ./config/opencloud/apps.yaml:/etc/opencloud/apps.yaml
      - ./config/opencloud/banned-password-list.txt:/etc/opencloud/banned-password-list.txt
      - ./config/opencloud/web.yaml:/etc/opencloud/web.yaml
      - ${OC_CONFIG_DIR:-opencloud-config}:/etc/opencloud
      - ${OC_DATA_DIR:-opencloud-data}:/var/lib/opencloud
      - ${OC_APPS_DIR:-./config/opencloud/apps}:/var/lib/opencloud/web/assets/apps
```

The individual `web.yaml` mount must be present in addition to the general `/etc/opencloud` configuration mount.

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

## Verify connectivity

From the first instance, check the endpoints of the second instance:

```bash
curl -I https://cloud.heiko.opencloud.rocks/ocm/
curl -I https://cloud.heiko.opencloud.rocks/sciencemesh/
curl -I https://cloud.heiko.opencloud.rocks/dav/
```

Run the corresponding tests in the other direction:

```bash
curl -I https://cloud.anja.opencloud.rocks/ocm/
curl -I https://cloud.anja.opencloud.rocks/sciencemesh/
curl -I https://cloud.anja.opencloud.rocks/dav/
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

On the first instance:

1. Open the OCM application.
2. Create a new invitation.
3. Copy the generated invitation link.
4. Send the link to the user on the second instance.

On the second instance:

1. Open the invitation link.
2. Sign in to OpenCloud.
3. Accept the invitation.

After the invitation has been accepted, the remote user becomes available as an OCM connection.

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

Also verify the mount in the resolved Compose configuration:

```bash
docker compose config | grep -A 5 -B 5 'web.yaml'
```

Recreate the container after every change:

```bash
docker compose up -d --force-recreate opencloud
```

Reload OpenCloud Web without using the browser cache.

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

The users must also have completed the OCM invitation process before they appear as sharing recipients.

### An invitation cannot be accepted

Check that:

- Both domains are listed in `ocmproviders.json`.
- The domains do not include `https://`.
- Both instances can access each other over HTTPS.
- The ScienceMesh endpoints are reachable.
- The invitation has not expired.
- The user is signed in to the receiving OpenCloud instance.

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
  | grep -Ei 'ocm|provider|sciencemesh|error|failed'
```

```

```
