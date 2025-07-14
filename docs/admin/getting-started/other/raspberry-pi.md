---
sidebar_position: 6
id: raspberry-pi
title: Raspberry Pi
---

# OpenCloud on Raspberry Pi

:::note
The installation of OpenCloud on a Raspberry Pi is intended for private or non-production use only.  
It is not recommended for enterprise or critical environments due to the hardware's limited resources and potential performance constraints.
:::

## 1.1 Hardware requirements

- Minimum Raspberry Pi 4B with at least 4 GB RAM connected via LAN or WLAN
- Micro SD card with at least 32 GB storage space
- External hard disk or USB stick (optional) for additional storage space

## 1.2 Install operating system

- Install Raspberry Pi OS  
  A very detailed and understandable guide is available at:  
  [Raspberry Pi Getting Started](https://pimylifeup.com/raspberry-pi-getting-started/)

- SSH must be activated  
  <img src={require("./../img/raspberrypi/ssh-activate.png").default} alt="activate ssh" width="500"/>

- If the Raspberry Pi is to be connected to WLAN, the login data for the WLAN must be entered.

## 1.3 Connecting with SSH

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

## 1.4 Installing Docker and Docker Compose

Detailed installation instructions for Docker can be found here:  
[Install Docker on Raspberry Pi](https://pimylifeup.com/raspberry-pi-docker/)

- Perform update and upgrade:

```bash
sudo apt update && sudo apt upgrade -y
```

- Install Docker via script:

```bash
curl -fsSL test.docker.com -o get-docker.sh && sh get-docker.sh
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

## 1.5 Clone OpenCloud repository

```bash
git clone https://github.com/opencloud-eu/opencloud-compose.git
```

## 1.6 Start the Docker Compose setup

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

Add the minimal OpenCloud setup:

```env
COMPOSE_FILE=docker-compose.yml:traefik/opencloud.yml
```

Then start Docker:

```bash
docker compose up
```

Now OpenCloud is running locally on your Raspberry Pi, and you can adjust it to your needs.

We will describe how to mount an external disk or USB stick and make OpenCloud available outside the local network using No-IP.

## 1.7 Mount external hard disk or USB stick

### 1. Find your external drive

```bash
lsblk
```

<img src={require("./../img/raspberrypi/find-external-hd.png").default} alt="find the external hd" width="500"/>

### 2. Format the drive to ext4

```bash
sudo mkfs.ext4 /dev/sda1 -L DATA
```

<img src={require("./../img/raspberrypi/format-drive.png").default} alt="format drive" width="500"/>

### 3. Add fstab entry for auto-mounting

Open `fstab`:

```bash
sudo nano /etc/fstab
```

Add this line:

```bash
LABEL=DATA /mnt/data ext4 auto,defaults 0 0
```

### 4. Create the mount point and set permissions

```bash
sudo mkdir -p /mnt/data
sudo chown -R 1000:1000 /mnt/data
```

### 5. Mount the drive

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

## 1.8 Mount external storage in Docker

Stop Docker:

```bash
docker compose down
```

Open the `.env` file:

```bash
cd opencloud-compose
nano .env
```

Set the `OC_DATA_DIR` variable to your mounted storage path, e.g.:

```env
OC_DATA_DIR=/mnt/data
```

<img src={require("./../img/raspberrypi/change-env-for-storage.png").default} alt="change env for storage" width="500"/>

Restart Docker:

```bash
docker compose up
```

## 1.9 Make OpenCloud externally available

### 1. Create DynDNS hostname

Register at [No-IP](https://www.noip.com/) and create a hostname, e.g. `opencloud.webhop.me`.

<img src={require("./../img/raspberrypi/noip.png").default} alt="noip hostname input" width="500"/>

### 2. Configure DynDNS in your router

Use your router’s web interface to:

- Locate the Dynamic DNS settings
- Select **No-IP** as provider
- Enter your No-IP credentials
- Use the created hostname (e.g. `opencloud.webhop.me`)
- Save and test the settings

More help: [No-IP Support](https://www.noip.com/support/knowledgebase/how-to-configure-ddns-in-router)

### 3. Configure port forwarding

1. Ensure your Raspberry Pi always has the same IP address:
   - Either via static IP or DHCP assignment in the router

2. In your router settings, look for **Port Forwarding**, **NAT**, or **Port Sharing**

3. Forward the following ports to your Raspberry Pi:

- TCP Port 80 (HTTP)
- TCP Port 443 (HTTPS)

<img src={require("./../img/raspberrypi/portforwarding.png").default} alt="portforwarding in router" width="500"/>

### 4. Update OC_DOMAIN

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
