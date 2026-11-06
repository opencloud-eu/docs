---
sidebar_position: 6
id: raspberry-pi
title: Raspberry Pi
description: OpenCLoud on a Raspberry Pi
draft: false
---

# OpenCloud on a Raspberry Pi

:::note
The installation of OpenCloud on a Raspberry Pi is intended for private or non-production use only.  
It is not recommended for enterprise or critical environments due to the hardware's limited resources and potential performance constraints.
:::

## Hardware requirements

- Minimum Raspberry Pi 4B with at least 4 GB RAM connected via LAN or WLAN
- Micro SD card with at least 32 GB storage space
- External hard disk or USB stick (optional) for additional storage space

## Install operating system

- Install Raspberry Pi OS  
  A very detailed and understandable guide is available at:  
  [Raspberry Pi Getting Started](https://pimylifeup.com/raspberry-pi-getting-started/)

- SSH must be enabled if you want to access the machine remotely.

  This is usually required when your Raspberry Pi is running without a connected keyboard and display.

- If the Raspberry Pi is to be connected to WLAN, the login data for the WLAN must be entered.

## Connecting with SSH

Start the Raspberry Pi with the SD card and connect via SSH.  
The IP for this can be viewed in your router.

<img src={require("./../img/raspberrypi/ip-router.png").default} alt="find ip from raspberry-pi in router" width="500"/>

### Establish connection via SSH

```bash
ssh pi@YOUR-IP
```

After the first login, you should change the password for security reasons:

```bash
passwd
```

## Installing Docker and Docker Compose

Detailed installation instructions for Docker can be found here:  
[Install Docker on Raspberry Pi](https://pimylifeup.com/raspberry-pi-docker/)

- Perform update and upgrade:

```bash
sudo apt update && sudo apt upgrade -y
```

- Install Docker via script:

The Docker convenience script installs from the stable release channel and is intended for testing and development. For maintained installations, follow the [official Docker installation instructions](https://docs.docker.com/engine/install/). Check that your Raspberry Pi OS version and architecture are supported.

```bash
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
```

- Add current user to the Docker group:

```bash
sudo usermod -aG docker ${USER}
```

- Check if it's working:

```bash
groups ${USER}
```

<img src={require("./../img/raspberrypi/docker-user-check.png").default} alt="Check docker user" width="500"/>

- Reboot the Raspberry Pi:

```bash
sudo shutdown -r now
```

## Clone OpenCloud repository

```bash
git clone https://github.com/opencloud-eu/opencloud-compose.git
```

## Start the Docker Compose setup

```bash
cd opencloud-compose
```

Copy the `.env.example` file:

```bash
cp .env.example .env
```

Edit the `.env` file:

```bash
nano .env
```

Activate the minimal OpenCloud setup by un-commenting this line:

```bash
COMPOSE_FILE=docker-compose.yml:traefik/opencloud.yml
```

Look for the following line and set here your admin password:

```bash
INITIAL_ADMIN_PASSWORD=YourSecurePassword
```

:::tip Using external storage?
If you plan to use an external drive, mount it and configure
`OC_DATA_DIR` as described below **before the first OpenCloud startup**.
Skip the next startup command and complete the external storage instructions first. Start OpenCloud only after setting `OC_DATA_DIR`.
:::

If you are using the default Docker data volume, start OpenCloud now:

```bash
docker compose up
```

Once started, OpenCloud runs locally on your Raspberry Pi.

We will describe how to mount an external disk or USB stick and make OpenCloud available outside the local network using No-IP.

## Mount external hard disk or USB stick

### Find your external drive

```bash
lsblk
```

<img src={require("./../img/raspberrypi/find-external-hd.png").default} alt="find the external hd" width="500"/>

### Format the drive to ext4

:::danger Data loss warning
Formatting a partition permanently erases its existing data. Back up any important files before proceeding.

The device path `/dev/sda1` below is only an example. Use `lsblk -f` to identify your external drive and verify the correct partition, size, and mount points before formatting. Do not format a partition containing data you want to keep.
:::

```bash
sudo mkfs.ext4 /dev/sda1 -L DATA
```

<img src={require("./../img/raspberrypi/format-drive.png").default} alt="format drive" width="500"/>

### Add fstab entry for auto-mounting

Open `fstab`:

```bash
sudo nano /etc/fstab
```

Add this line:

```bash
LABEL=DATA /mnt/data ext4 auto,defaults 0 0
```

### Create the mount point

```bash
sudo mkdir -p /mnt/data
```

### Mount the drive

```bash
sudo mount -a
```

If an error occurs:

<img src={require("./../img/raspberrypi/error-mounting.png").default} alt="error mounting" width="500"/>

Run:

```bash
systemctl daemon-reload
```

And try mounting again.

### Verify the mount and set permissions

Before changing ownership, verify that the external filesystem is mounted at `/mnt/data`:

```bash
findmnt --mountpoint /mnt/data
```

If the expected filesystem is not mounted, correct the mount configuration before proceeding.

For a new, empty data filesystem, set ownership of its root directory:

```bash
sudo chown 1000:1000 /mnt/data
```

Verify that UID and GID `1000:1000` are appropriate for your deployment. Do not recursively change ownership of an existing drive without checking its contents and required permissions.

## Mount external storage in Docker

:::caution Existing installations
Changing `OC_DATA_DIR` does not migrate existing data from the
previous Docker volume. Before switching storage on an existing
installation, back up your OpenCloud data and configuration and
follow a verified migration procedure. Otherwise, existing files
may appear missing.
:::

If OpenCloud is already running, stop its Compose services:

```bash
docker compose down
```

Open the `.env` file:

```bash
nano .env
```

Set the `OC_DATA_DIR` variable to your mounted storage path, e.g.:

```env
OC_DATA_DIR=/mnt/data
```

<img src={require("./../img/raspberrypi/change-env-for-storage.png").default} alt="change env for storage" width="500"/>

Start OpenCloud with the configured data directory:

```bash
docker compose up
```

## Make OpenCloud externally available

### Create DynDNS hostname

Register at [No-IP](https://www.noip.com/) and create a hostname, e.g. `opencloud.webhop.me`.

<img src={require("./../img/raspberrypi/noip.png").default} alt="noip hostname input" width="500"/>

### Configure DynDNS in your router

Use your router’s web interface to:

- Locate the Dynamic DNS settings
- Select **No-IP** as provider
- Enter your No-IP credentials
- Use the created hostname (e.g. `opencloud.webhop.me`)
- Save and test the settings

More help: [No-IP Support](https://www.noip.com/support/knowledgebase/how-to-configure-ddns-in-router)

### Configure port forwarding

1. Ensure your Raspberry Pi always has the same IP address:
   - Either via static IP or DHCP assignment in the router

2. In your router settings, look for **Port Forwarding**, **NAT**, or **Port Sharing**

3. Forward the following ports to your Raspberry Pi:

- TCP Port 80 (HTTP)
- TCP Port 443 (HTTPS)

<img src={require("./../img/raspberrypi/portforwarding.png").default} alt="portforwarding in router" width="500"/>

### Update OC_DOMAIN

SSH into your Pi and update the domain:

```bash
cd opencloud-compose
docker compose down
nano .env
```

Edit the `OC_DOMAIN` value:

```env
OC_DOMAIN=opencloud.webhop.me
```

<img src={require("./../img/raspberrypi/oc-domain.png").default} alt="change the OC_DOMAIN variable" width="500"/>

Restart Docker:

```bash
docker compose up
```

Now your OpenCloud should be reachable via your URL.

<img src={require("./../img/raspberrypi/reachable-via-URL.png").default} alt="reachable-via-URL" width="1920"/>
