---
sidebar_position: 4
id: common-issues
title: Common Issues & Help
description: Common issues & help
draft: false
---

# Common Issues & Help

## Check whether the containers are running

```bash
docker ps
```

<img src={require("./img/common-issues/quick-docker-running.png").default} alt="Admin general" width="1920"/>

Several containers should be listed here, e.g., for opencloud, traefik, etc.

## Accept Self-Signed Certificates

As the local environment is self-signed, you must accept the security risk in your browser.

For Firefox:

You need to click on Advanced

<img src={require("./img/common-issues/quick-advanced.png").default} alt="Admin general" width="500"/>

Confirm the risk with Accept the risk and Continue

<img src={require("./img/common-issues/quick-accept-security-risk.png").default} alt="Admin general" width="500"/>

## Docker Permission Issues

If your Docker Compose setup fails to start and the logs contain messages such as `permission denied`, it's likely due to incorrect ownership of local directories used by the containers.

Example log output:

```bash
opencloud-1 | {"level":"fatal","service":"nats","time":"2025-04-08T09:59:59Z","line":"github.com/opencloud-eu/opencloud/services/nats/pkg/logging/nats.go:33","message":"Can't start JetStream: could not create storage directory - mkdir /var/lib/opencloud/nats: permission denied"}
```

This error typically occurs when the mounted directories are owned by the wrong user, such as `root`, instead of the standard Docker user (`UID 1000`).

Incorrect directory ownership:

```bash
drwxr-xr-x  3 root root 4096 Apr  8 09:59 opencloud-data
```

Correct ownership should be:

```bash
drwxr-xr-x  9 1000 1000 4096 Apr  7 07:57 opencloud-data
```

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

## Internal LibreIDM cert expires

### 🔧 Renewing an expired certificate in internal IDM (OpenCloud)

When using the internal IDM (LibreIDM), the LDAP certificate may expire over time.
You can see similar errormessages in your logfiles:

```bash
opencloud-1      | 2026-03-10T14:10:36Z WRN core access token not set host.name=3133c92656c8 pkg=rhttp service=frontend traceid=2da2886cf47f0143876953ee33f814a9
opencloud-1      | 2026-03-10T14:10:36Z ERR failed to build subject.session error="invalid key format" service=proxy
opencloud-1      | 2026-03-10T14:10:36Z ERR handleConnection ber.ReadPacket error="remote error: tls: bad certificate" service=idm
opencloud-1      | 2026-03-10T14:10:37Z ERR could not get ldap Connection error="LDAP Result Code 200 \"Network Error\": tls: failed to verify certificate: x509: certificate has expired or is not yet valid: current time 2026-03-10T14:10:37Z is after 2026-03-04T10:02:39Z" service=graph
opencloud-1      | 2026-03-10T14:10:37Z ERR failed to add user error="LDAP Result Code 200 \"Network Error\": tls: failed to verify certificate: x509: certificate has expired or is not yet valid: current time 2026-03-10T14:10:37Z is after 2026-03-04T10:02:39Z" request-id=3133c92656c8/LlC0SVlYb4-000023 service=graph
opencloud-1      | 2026-03-10T14:10:37Z ERR handleConnection ber.ReadPacket error="remote error: tls: bad certificate" service=idm
opencloud-1      | 2026-03-10T14:10:37Z ERR could not create user: backend error error="generalException: failed to add user" request-id=3133c92656c8/LlC0SVlYb4-000023 service=graph
opencloud-1      | 2026-03-10T14:10:37Z WRN Error Response OData Error="failed to add user" service=proxy
opencloud-1      | 2026-03-10T14:10:37Z ERR Error creating user error="500 Internal Server Error" service=proxy
opencloud-1      | 2026-03-10T14:10:37Z ERR Autoprovisioning user failed error="500 Internal Server Error" service=proxy
```

#### 🛠️ Solution

Navigate to the IDM directory

```bash
cd .opencloud/idm
```

Delete the old certificates

```bash
rm ldap.crt ldap.key

Directory structure:

.opencloud/idm
├── idm.boltdb
├── ldap.crt
└── ldap.key
```

Restart the OpenCloud container

```bash
docker compose restart
```

➡️ The certificates will be automatically regenerated on restart.

#### ⚠️ Recommendation

Admins should avoid using LibreIDM in production and use OpenLDAP instead.

## Login fails with LDAP Result Code 49 (Invalid Credentials)

When using the built-in IDM (LibreIDM), login can fail with `Unexpected HTTP response:
500` in the browser, and the logs show the internal directory rejecting a bind:

```bash
opencloud-1 | {"level":"error","service":"idm","bind_dn":"uid=idp,ou=sysusers,o=libregraph-idm","op":"bind","message":"not found"}
opencloud-1 | {"level":"error","service":"idp","error":"ldap identifier backend logon connect error: LDAP Result Code 49 \"Invalid Credentials\": ","message":"identifier failed to logon with backend"}
```

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

### Recommendation

The built-in IDM is intended for testing and small installations. For production, use
an external identity provider, for example Keycloak with an external LDAP.

## Large uploads stuck in "processing" on storage with slow `fsync`

A large file (several GB) finishes uploading but then sits in **processing** and never
becomes available. The desktop client just hangs on it. The data itself is written to
disk fine; what fails is the finalization step after the upload.

While the file is finalizing, this shows up in the log every few seconds:

```bash
opencloud-1 | {"level":"error","service":"postprocessing","error":"context deadline exceeded","message":"failed to get consumer"}
opencloud-1 | {"level":"error","service":"search","error":"context deadline exceeded","message":"failed to get consumer"}
```

The cause is the way PosixFS and DecomposedFS store metadata. They run without a
database and rely on extended attributes and the embedded NATS JetStream event bus,
which calls `fsync` for every message it writes. Finalizing a large upload generates a
burst of these syncs against the same disk that holds the data. On most storage that
goes unnoticed, but if synchronous writes are slow it becomes the bottleneck. A typical
case is a VM backed by ZFS on consumer SSDs with no separate ZIL (SLOG) device, where
every `fsync` turns into a cache-flush round trip. The sync path saturates, the
`postprocessing` and `search` consumers miss their deadlines, the finalize event is
lost, and the upload is left stuck with nothing to recover it.

You can tell it apart from a CPU or memory problem because the machine is purely
I/O-bound during finalization: `cat /proc/pressure/io` reports `some avg10` close to
100% while CPU pressure stays near zero, and the blocked kernel threads are the
filesystem journal threads. A quick way to confirm the storage is slow at synchronous
writes:

```bash
dd if=/dev/zero of=testfile bs=4k count=1000 oflag=dsync
dd if=/dev/zero of=testfile bs=1M count=1000 oflag=direct
```

If the first command is dramatically slower than the second, the storage is sensitive
to `fsync` and plain bandwidth is not the issue.

To recover an upload that is already stuck, re-drive its postprocessing. The data is
still on disk, so this does not re-upload anything:

```bash
opencloud postprocessing resume -u <uploadID> -r
```

To avoid the problem, move the JetStream store onto a `tmpfs` so its syncs land in
memory instead of on the slow disk. Set `NATS_NATS_STORE_DIR` to a path you mount as
`tmpfs`:

```yaml
services:
  opencloud:
    environment:
      NATS_NATS_STORE_DIR: /run/opencloud-nats
    tmpfs:
      - /run/opencloud-nats:rw,size=1g,mode=1777
```

This is safe for a single-node instance. The JetStream store is a transient event bus
and a set of caches that OpenCloud rebuilds from the file system on startup, and app
tokens live on the data volume, not in NATS, so they survive a restart. The only thing
lost when the store is emptied is the activity log.

Keep in mind that a `tmpfs` store is held in RAM and cleared on every restart, so size
it for your event volume (1 GiB is a reasonable start) and make sure the host has the
memory for it. Don't use a `tmpfs` store with a clustered NATS setup, where the store
has to be durable.
