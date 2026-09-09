---
sidebar_position: 4
id: common-issues
title: Common Issues & Help
description: Common issues & help
draft: false
toc_max_heading_level: 2
---

# Common Issues & Help

## Desktop Client cannot connect through an external reverse proxy

### Problem

After a user enters the OpenCloud server address, the browser does not open. The Desktop Client window may flicker and its memory usage may increase. The proxy or client logs may show a `403` response to a `/.well-known/webfinger` request.

### Cause

The Desktop Client uses the WebFinger endpoint for server discovery. Security filters or other connection handling settings on an external reverse proxy can reject or alter this request. In [issue #1077](https://github.com/opencloud-eu/desktop/issues/1077), the reporter restored the connection after changing an optional Nginx Proxy Manager security filter, but this may not be the cause in every setup.

### Solution

Check the reverse proxy logs and verify that `/.well-known/webfinger` requests, including their query parameters, are forwarded to OpenCloud without being rejected or modified.

Review the [external proxy documentation](../getting-started/container/docker-compose/docker-external-proxy.md) and compare it with your setup. In addition to security filters, check HTTP/2, keep-alive handling, proxy timeouts, buffering, and upload limits. These settings are relevant for stable Desktop Client connections and long-running or larger sync operations.

## OpenCloud containers are not running

### Problem

OpenCloud is unavailable or does not work as expected.

### Cause

One or more required containers may not be running.

### Solution

Check the running containers:

```bash
docker ps
```

<img src={require("./img/common-issues/quick-docker-running.png").default} alt="Admin general" width="1920"/>

Several containers should be listed, for example OpenCloud and Traefik.

## Browser rejects a self-signed certificate

### Problem

The browser displays a security warning when you access a local OpenCloud environment.

### Cause

The local environment uses a self-signed certificate that the browser does not trust automatically.

### Solution

Accept the security risk in your browser. In Firefox, select **Advanced**:

<img src={require("./img/common-issues/quick-advanced.png").default} alt="Admin general" width="500"/>

Then select **Accept the Risk and Continue**:

<img src={require("./img/common-issues/quick-accept-security-risk.png").default} alt="Admin general" width="500"/>

## Docker Permission Issues

### Problem

If your Docker Compose setup fails to start and the logs contain messages such as `permission denied`, it's likely due to incorrect ownership of local directories used by the containers.

Example log output:

```bash
opencloud-1 | {"level":"fatal","service":"nats","time":"2025-04-08T09:59:59Z","line":"github.com/opencloud-eu/opencloud/services/nats/pkg/logging/nats.go:33","message":"Can't start JetStream: could not create storage directory - mkdir /var/lib/opencloud/nats: permission denied"}
```

### Cause

This error typically occurs when the mounted directories are owned by the wrong user, such as `root`, instead of the standard Docker user (`UID 1000`).

Incorrect directory ownership:

```bash
drwxr-xr-x  3 root root 4096 Apr  8 09:59 opencloud-data
```

Correct ownership should be:

```bash
drwxr-xr-x  9 1000 1000 4096 Apr  7 07:57 opencloud-data
```

### Solution

To resolve this issue, adjust the ownership of the directory using the `chown` command:

```bash
chown -R 1000:1000 opencloud-data
```

:::caution
Security Warning

The user with UID 1000 on your host system will have full access to these mounted directories. This means that any local user account with this ID can read, modify, or delete OpenCloud config and data files.

This can pose a security risk in shared or multi-user environments. Make sure to implement proper user and permission management and consider isolating access to these directories.

:::

Ensure you apply this to all relevant folders that are mounted into your containers. This will grant the Docker container the necessary permissions to access and write to these directories.

## Change Admin Password Set in `.env`

### Problem

Changing the OpenCloud admin password in the `.env` file has no effect after the container has been initialized, or the current password has been forgotten.

### Cause

The `.env` value is used to set the initial admin password. Once the container is running, password changes must be made through the Web UI or terminal.

### Solution

#### Option 1: Change via Web UI

If the current admin password is known:

1. Log in to the OpenCloud Web Interface.
2. Navigate to Settings > Security.
3. Enter your current password and choose a new one.

> If the admin password is forgotten or you prefer command-line tools, use the terminal method below.

#### Option 2: Change via Terminal

If the admin password is forgotten or needs to be changed via the terminal:

##### Stop the Docker container

First, stop your OpenCloud container:

```bash
docker compose stop opencloud
```

##### Run the password reset command

Use the following command to reset the password:

```bash
sudo docker run -it --rm -v <opencloud-data-path>:/var/lib/opencloud -v <opencloud-config-path>:/etc/opencloud opencloudeu/opencloud:<opencloud-version> idm resetpassword
```

##### Replace

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

##### Example for standard setup

```bash
sudo docker run -it --rm -v opencloud-compose_opencloud-data:/var/lib/opencloud -v opencloud-compose_opencloud-config:/etc/opencloud opencloudeu/opencloud:latest idm resetpassword
```

##### Start the container again

```bash
docker compose up -d
```

## Internal LibreIDM cert expires

### Problem

In OpenCloud releases earlier than 7.3, an expired internal LibreIDM certificate can interrupt communication with the directory service.

### Cause

These older releases do not automatically renew the internal LibreIDM certificate before it expires.

### Solution

Starting with OpenCloud 7.3, internal LibreIDM certificates are renewed automatically before they expire.

No manual certificate removal or container restart is required.

For affected older releases, see the remediation instructions for
[OpenCloud 7.2](https://docs.opencloud.eu/docs/7.2/admin/resources/common-issues/#internal-libreidm-cert-expires)
or [OpenCloud 4.0](https://docs.opencloud.eu/docs/4.0/admin/resources/common-issues/#internal-libreidm-cert-expires).

## Login fails with LDAP Result Code 49 (Invalid Credentials)

### Problem

When using the built-in IDM (LibreIDM), login can fail with `Unexpected HTTP response:
500` in the browser, and the logs show the internal directory rejecting a bind:

```bash
opencloud-1 | {"level":"error","service":"idm","bind_dn":"uid=idp,ou=sysusers,o=libregraph-idm","op":"bind","message":"not found"}
opencloud-1 | {"level":"error","service":"idp","error":"ldap identifier backend logon connect error: LDAP Result Code 49 \"Invalid Credentials\": ","message":"identifier failed to logon with backend"}
```

### Cause

The built-in IDM seeds its service-account passwords once, at first start, into a
bolt-store on the data volume (`idm.boltdb`), matching the values `opencloud init`
writes into `opencloud.yaml` on the config volume. The bind fails when the two volumes
are no longer from the same `init`. The `idm` line reads either `not found` or
`invalid credentials`; both mean the same mismatch. This usually comes from setting an
internal LDAP password in the environment, or from reusing one volume (for example a
restored or carried-over data volume) without the other.

### Solution

With the built-in IDM, do not set the internal LDAP or service passwords in `.env` or
the environment. Let `opencloud init` generate them, and keep only
`INITIAL_ADMIN_PASSWORD`.

Treat `opencloud.yaml` (config volume) and the data volume as one set. When you back
up, restore, or move the instance, keep them together and from the same point in time.

If you do not need the existing data, remove both volumes so `init` generates a
matching set, then start again:

```bash
docker compose down
docker volume rm opencloud-compose_opencloud-config opencloud-compose_opencloud-data
docker compose up -d
```

:::caution
Deleting `idm.boltdb` alone may not be enough: it is re-seeded from the current config,
but a bind password still set in the environment keeps the two sides out of sync.
:::

#### Recommendation

The built-in IDM is intended for testing and small installations. For production, use
an external identity provider, for example Keycloak with an external LDAP.
