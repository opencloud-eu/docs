---
sidebar_position: 1
id: docker-compose-base
title: Docker Compose
description: Full-blown featureset including web office.
draft: false
---

# OpenCloud with Docker Compose

Install an internet-facing OpenCloud with SSL certification using Docker Compose.

This installation documentation is for Ubuntu and Debian systems. The software can also be installed on other Linux distributions, but the commands and package managers may differ.

## Prerequisites

- Four domains pointing to your server:
  - `cloud.YOUR.DOMAIN` → OpenCloud frontend
  - `collabora.YOUR.DOMAIN` → Collabora Online Server
  - `wopiserver.YOUR.DOMAIN` → WOPI server for document editing
  - `traefik.YOUR.DOMAIN` → Traefik dashboard

  Alternatively, you can use a wildcard domain (`*.YOUR.DOMAIN`)

- A hosted server (e.g., Hetzner, AWS, or your own VPS) with Linux and SSH access

## Connect to Your Server

Log into your server via SSH:

```bash
ssh YOUR_ADMIN_USER@YOUR.SERVER.IP
```

:::note
Use a non-root user with `sudo` privileges. If you logged in as root, prepend `sudo` where appropriate or run the commands without `sudo`
:::

## Install Docker

Update your system and install Docker.

First, perform an update and upgrade:

```bash
sudo apt update && sudo apt upgrade -y
```

Install Docker following the [official Docker guide](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

Once Docker is installed, enable and start the service:

```bash
sudo systemctl enable docker && sudo systemctl start docker
```

## Create a dedicated user to run OpenCloud (recommended)

For security reasons, do not run the OpenCloud stack as `root`. Create a dedicated user (for example `opencloud`) and run the remaining steps as that user.

```bash
sudo adduser opencloud
sudo usermod -aG docker opencloud
```

Log out and log back in (or start a new login shell), then continue as `opencloud`.

Docker can be managed as a non-root user (e.g. via the `docker` group). Be aware that access to the Docker daemon is effectively equivalent to root access on the host. Limit group membership and restrict access accordingly.

## Clone the OpenCloud Repository

Download the necessary configuration files:

```bash
git clone https://github.com/opencloud-eu/opencloud-compose.git
```

## Configure the .env File for Staging Certificates

Before requesting real SSL certificates, test the setup with Let's Encrypt’s staging environment.

### Navigate to the OpenCloud configuration folder

```bash
cd opencloud-compose
```

### Create environment file

```bash
cp .env.example .env
```

:::note
The repository includes .env.example as a template with default settings and documentation. Your actual .env file is excluded from version control (via .gitignore) to prevent accidentally committing sensitive information like passwords and domain-specific settings.
:::

Edit the `.env` file with the editor of your choice:

### In our example we use nano

```bash
nano .env
```

## Modify these settings

### Disable insecure mode

```env
# INSECURE=true
```

### Set your domain names

```env
TRAEFIK_DOMAIN=traefik.YOUR.DOMAIN
OC_DOMAIN=cloud.YOUR.DOMAIN
COLLABORA_DOMAIN=collabora.YOUR.DOMAIN
WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN
```

### Set your admin password

```env
INITIAL_ADMIN_PASSWORD=YourSecurePassword
```

### Set your email for SSL certification

```env
TRAEFIK_ACME_MAIL=your@email.com
```

### Use Let's Encrypt staging certificates (for testing)

```env
TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory
```

### Set your deployment options

For example, without Collabora:

```env
COMPOSE_FILE=docker-compose.yml:traefik/opencloud.yml
```

Save and exit.

### Production Setup Consideration

:::caution Production Setup Recommended
By default, OpenCloud stores configuration and data inside internal Docker volumes.  
This works fine for local development or quick evaluations — but is not suitable for production environments.
:::

#### Mount Persistent Volumes

For production setups, mount persistent host directories for configuration and data. This gives you:

- Data durability
- Easier backups and recovery
- Full control over storage location and permissions

Update your `.env` file with custom paths:

```env
OC_CONFIG_DIR=/your/local/path/opencloud/config
OC_DATA_DIR=/your/local/path/opencloud/data
```

### UID/GID and volume permissions (important)

OpenCloud containers run as `1000:1000` by default.  
If your host user uses different IDs, set `OC_CONTAINER_UID_GID` in `.env` so file ownership matches your host user:

```env
OC_CONTAINER_UID_GID=1001:1001
```

You can check your UID/GID with:

```bash
id -u
id -g
```

:::tip Folder Permissions

Create the folders and assign ownership to the UID/GID used by the container (default `1000:1000`, or your `OC_CONTAINER_UID_GID` value):

```bash
sudo mkdir -p /your/local/path/opencloud/{config,data}
sudo chown -R $(id -u):$(id -g) /your/local/path/opencloud
```

:::

If `OC_CONFIG_DIR` and `OC_DATA_DIR` are not set, Docker uses internal volumes. Those are harder to manage for backups and are not recommended for production.

:::caution Security Warning

Any local account that matches the mapped UID/GID can access these mounted directories.  
In shared or multi-user environments, this can expose OpenCloud config and data files.

Use strict host-level permission management and isolate access to these paths where possible.

:::

#### Use production release container

To avoid accidentally updating to a version with breaking changes, you should specify the production container version to be used in your `.env` file:

```env
OC_DOCKER_IMAGE=opencloudeu/opencloud
OC_DOCKER_TAG=4.0.3
```

:::tip Keep the version up to date
The documentation may not always reference the latest available release. Before deploying (and when updating), check the available tags on Docker Hub and adjust OC_DOCKER_TAG to the most recent stable version:
<https://hub.docker.com/r/opencloudeu/opencloud/tags>

:::

## Start OpenCloud

Launch OpenCloud using Docker Compose:

```bash
docker compose up -d
```

This will start all required services in the background.

## Verify SSL Certification

In your web browser, visit:

```bash
https://cloud.YOUR.DOMAIN
```

You should see a security warning because the staging certificate is not fully trusted.
The same warning should appear for the other domains you are using.

Example with Chrome browser:

<img src={require("./../../img/docker-compose/certificate-details.png").default} alt="Certificate Details" width="500"/>

- Check the certificate details to confirm it’s from Let's Encrypt Staging.

  <img src={require("./../../img/docker-compose/certificate-viewer.png").default} alt="Certificate Details" width="500"/>
  <img src={require("./../../img/docker-compose/subordinate-ca's.png").default} alt="Certificate Details" width="500"/>

## Apply a Real SSL Certificate

Once the staging certificate works, switch to a production certificate.

### Stop Docker Compose

```bash
docker compose down
```

### Remove old staging certificates

```bash
rm -rf ./certs
```

(Run this in the `opencloud-compose` directory. If you changed volume names, adjust accordingly.)

### Disable staging mode in `.env`

```bash
nano .env
```

Comment the staging server:

```env
# TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory
```

### Restart OpenCloud with a real SSL certificate

```bash
docker compose up -d
```

Now, visiting `https://cloud.YOUR.DOMAIN` should show a secure connection with a valid SSL certificate.

<img src={require("./../../img/docker-compose/status-secure.png").default} alt="Certificate Details" width="1920"/>

## Log into OpenCloud

Open a browser and visit:

```bash
https://cloud.YOUR.DOMAIN
```

Login with:

Username: `admin`

Password: (your password)

<img src={require("./../../img/docker-compose/login.png").default} alt="Admin general" width="1920"/>

## Troubleshooting

If you encounter any issues, check the [Common Issues & Help](../../../resources/common-issues)
