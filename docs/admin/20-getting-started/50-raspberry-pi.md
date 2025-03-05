---
sidebar_position: 5
id: raspberry-pi
title: Raspberry Pi
---

# OpenCloud on Raspberry Pi


## 1.1 Hardware requirements

- Minimum Raspberry Pi 4B with at least 4 GB RAM connected via LAN or WLAN
- Micro SD card with at least 32 GB storage space
- External hard disk or USB-Stick (optional) for additional storage space

## 1.2 Install operating system

- Install Raspberry Pi OS
  A very detailed and understandable guide is available at:  
  [Raspberry Pi Getting Started](https://pimylifeup.com/raspberry-pi-getting-started/)
- SSH must be activated
<img src={require("./img/raspberrypi/ssh-activate.png").default} alt="activate ssh" width="500"/>

- If the Raspberry Pi is to be connected to WLAN, the login data for the WLAN must be entered.

## 1.3 Connecting with SSH

Start the Raspberry Pi with the SD card and connect via SSH.  
The IP for this can be viewed in your router.

<img src={require("./img/raspberrypi/ip-router.png").default} alt="find ip from raspberry-pi in router" width="500"/>

#### Establish connection via SSH:
```sh
ssh pi@YOUR-IP
```

After the first login, you should change the password for security reasons:
```sh
passwd
```

## 1.4 Installing Docker and Docker Compose

Detailed installation instructions for docker can be found here:  
[Install Docker on Raspberry Pi](https://pimylifeup.com/raspberry-pi-docker/)

- Perform update and upgrade

```sh
sudo apt update && sudo apt upgrade -y
```
- Install Docker via Script

```sh
curl -fsSL test.docker.com -o get-docker.sh && sh get-docker.sh
```

- Add current user to the Docker Group

```sh
sudo usermod -aG docker ${USER}
```
- Check if it`s running:

```sh
groups ${USER}
```
<img src={require("./img/raspberrypi/docker-user-check.png").default} alt="Check docker user" width="500"/>

- Reboot the Raspberry Pi to let the changes take effect

```sh
sudo shutdown -r now
```
- Install Docker-Compose

```sh
sudo apt install docker-compose
```

- Check the installation

```sh
docker-compose --version
```
<img src={require("./img/raspberrypi/docker-compose-check.png").default} alt="Check docker-compose" width="500"/>


## 1.5 Clone OpenCloud respository

```sh 
git clone https://github.com/opencloud-eu/opencloud.git
``` 


## 1.6 Start the docker compose setup

```sh 
cd opencloud/deployments/examples/opencloud_full
```

```sh 
docker compose up 
```


Now you have running OpenCloud locally on your RaspberryPi and you can adjust it to your needs.
We will describe how you can mount an external disk or USB-Stick and make your OpenCloud available outside of the local network with No-IP



## 1.7 Mount external hard disk or USB-Stick

#### 1. Find your external hard disk or USB-Stick on your Raspberry-Pi

```sh
lsblk
```
<img src={require("./img/raspberrypi/find-external-hd.png").default} alt="find the external hd" width="500"/>


#### 2. Format the drive to ext4 filesystem

```sh
sudo mkfs.ext4 PATH-TO-DRIVE -L DATA
```
PATH-TO-DRIVE is in this example `/dev/sda1` so the command would be

```sh
sudo mkfs.ext4 /dev/sda1 -L DATA
```
<img src={require("./img/raspberrypi/format-drive.png").default} alt="format drive" width="500"/>

#### 3. Add entry in fstab for automatic mounting when restarting

  - open fstab with sudo
```sh
  sudo nano /etc/fstab
```
  - add following line in the fstab file

```sh 
LABEL=DATA /mnt/data ext4 auto,defaults 0 0
```

#### 4. Create the `/mnt/data` directory and give the user 1000 access

```sh 
sudo mkdir -p /mnt/data
```
```sh 
sudo chown -R 1000:1000 /mnt/data
```

#### 5.  mount the drive automatically 

```sh 
sudo mount -a
```  

Maybe you get following error

<img src={require("./img/raspberrypi/error-mounting.png").default} alt="error mounting" width="500"/>

then please perform the recommended command
```sh 
systemctl daemon-reload
``` 
and try to mount again.

## 1.8 Mount external storage

Stop the running docker

```sh 
docker compose down
``` 

Go to the deployment folder and open the `.env` file with e.g. nano 

```sh 
cd opencloud/deployments/examples/opencloud_full
``` 
```sh 
nano .env
```

When you added an external hard disk or USB-Stick for the storage, you need to set the `OC_DATA_DIR` variable and adjust the path to your storage

<img src={require("./img/raspberrypi/change-env-for-storage.png").default} alt="change env for storage" width="500"/>


Here it is `/mnt/data`

Start the docker again

```sh 
docker compose up
``` 

## 1.9 Make your OpenCloud available from outside

#### 1. Create a DynDNS account and the hostname

To make your Raspberry Pi accessible from the outside, you need a DynDNS entry (dynamic DNS). This is necessary because Let's Encrypt only creates SSL certificates for domain names, not for IP addresses. A DynDNS service ensures that your Pi always remains accessible under a fixed domain, even if the IP address changes.

You can create a free DynDNS account at [No-IP](https://www.noip.com/), for example. After registering, log in to the No-IP web interface and create a new host name under “Create Hostname”. In this example, we use `opencloud.webhop.me` as the address for the Raspberry Pi.

<img src={require("./img/raspberrypi/noip.png").default} alt="noip hostname input" width="500"/>

#### 2. Configure DyDNS in your router

If your router supports integrated Dynamic DNS (DDNS), you can update your IP address directly via the router. This eliminates the need to install the Dynamic Update Client (DUC) from No-IP on your Raspberry Pi.
How to set up DDNS in the router:

- Log into your router's web interface (usually via 192.168.1.1 or a similar address).
- Search for the DDNS settings - these are usually located under Network, Internet or Dynamic DNS.
- Select No-IP as your provider from the list of supported DDNS services.
- Enter your No-IP credentials (username & password).
- Enter the hostname you previously created with No-IP (e.g. ocis-at-home.ddns.net).
- Save the settings and test the connection.

The router will now automatically update your public IP address at No-IP so that your Raspberry Pi always remains accessible under the selected subdomain.

You can also look in the documentation from [No-IP](https://www.noip.com/support/knowledgebase/how-to-configure-ddns-in-router)

#### 3. Configure port forwarding in your router

To make your Raspberry Pi accessible from the Internet, you must set up port forwarding in your router. This means that requests from outside to certain ports are automatically forwarded to your Raspberry Pi in the local network.

1. Make sure that your Raspberry Pi always has the same IP address:

- By making a fixed DHCP assignment in the router settings
- Or via a static IP address in the network settings of your Pi


2. In the router menu, search for “Port forwarding”, “NAT” or “Port sharing” (the name may vary depending on the router model)

3. Create a new portforwarding with TCP for 80 and 443

  Example from a Speedport 4
<img src={require("./img/raspberrypi/portforwarding.png").default} alt="portforwarding in router" width="500"/>

#### 4. Change the OpenCloud domain in the configuration

Now you need to change the environment variable `OC_DOMAIN` in the `.env` file

1. Connect via ssh on your Raspberry-Pi

2. Navigate to the correct folder 

  ```sh 
  cd opencloud/deployments/examples/opencloud_full
  ```
3. Stop running OpenCloud docker

```sh 
docker compose down
```

4. open the `.env` file with e.g. nano 

  ```sh 
  nano .env
  ```
5. Look for the `OC_DOMAIN` variable and enter your URL, here we used `opencloud.webhop.me`
<img src={require("./img/raspberrypi/oc-domain.png").default} alt="change the OC_DOMAIN variable" width="500"/>

6. Start the docker again

```sh 
docker compose up
``` 

Now your OpenCloud should be reachable via your URL.

<img src={require("./img/raspberrypi/reachable-via-URL.png").default} alt="reachable-via-URL" width="1920"/>