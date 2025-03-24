---
sidebar_position: 2
id: docker-compose
title: Docker Compose
description: "🌟 Full-blown featureset including web office and full-text search."
---

# Docker Compose



## **Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [**Docker Compose**](https://docs.docker.com/compose/install/)
- Four domains set up and pointing to your server
    - opencloud.* for serving OpenCloud
    - collabora.* for serving Collabora
    - wopiserver.* for serving the WOPI server
    - traefik.* for serving the Traefik dashboard
- Host service (we us in our example Hetzner as hoster)

---

## 1. Login to a host-service / server:

In our case, we log in to our created Hetzner server via SSH via the terminal.

```Shell
ssh root@"ip of the server"
```

---

## 2. Install Docker Compose

```Shell
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```Shell
sudo chmod +x /usr/local/bin/docker-compose
```

```Shell
sudo apt install docker-compose
```

## 3. Clone OpenCloud Repository

Download the `opencloud_full` folder (this folder contains a multi-file Docker Compose configuration):


```Shell
git clone https://github.com/opencloud-eu/opencloud.git
```

---

## 4. Changes .env File

In den folgenden Screenshots beschreiben wir welche Änderungen in der .env vorgenommen werden müssen um OpenCloud von aussen erreichbar zu machen.

<img src={require("./img/docker-compose/traefik-domain.png").default} alt="Insecure Option and Traefik Domain" width="1920"/>

<img src={require("./img/docker-compose/opencloud-domain.png").default} alt="OC Domain" width="1920"/>

<img src={require("./img/docker-compose/collabora-and-wopiserver-domain.png").default} alt="Collabora and Wopi Domain" width="1920"/>

## 5. Start

cd into the Docker Compose configuration folder:

```Shell
cd opencloud/deployments/examples/opencloud_full
```

Start the deployment with Docker Compose:

```Shell
docker compose up -d
```

<img src={require("./img/quick-guide/quick-docker-compose-up.png").default} alt="Admin general" width="1920"/>

This starts all necessary containers in the background.

---

## 6. Login

Login with your browser:
- https://"your domain of your .env file"
- user: **admin**
- password: **admin**

<img src={require("./img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>


## 7. Conclusion

Your OpenCloud server is now running and ready to use 🚀

--- 

## Troubleshooting

If you encounter any issues or errors, try finding a solution here: 

- [Common Issues & Help](./../50-resources/30-common-issues.md)
<br/>
---

## Guide for local installation
Spin up a temporary local instance of OpenCloud using **Docker Compose**.

## **Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [**Docker Compose**](https://docs.docker.com/compose/install/)

---

###  1. Download

Download the `opencloud_full` folder (this folder contains a multi-file Docker Compose configuration):

```Shell
git clone https://github.com/opencloud-eu/opencloud.git
```

---

### 2. Start

cd into the Docker Compose configuration folder:

```Shell
cd opencloud/deployments/examples/opencloud_full
```

Start the deployment with Docker Compose:

```Shell
docker compose up -d
```

<img src={require("./img/quick-guide/quick-docker-compose-up.png").default} alt="Admin general" width="1920"/>

This starts all necessary containers in the background.

---

### 3. Add local domains to /etc/hosts 

Edit the /etc/hosts file and add the following entries for local access:

```
127.0.0.1       cloud.opencloud.test
127.0.0.1       collabora.opencloud.test
127.0.0.1       wopiserver.opencloud.test
```

Open [https://collabora.opencloud.test](https://collabora.opencloud.test) and accept the self-signed certificate. This step is needed as you can not accept the self-signed certificate if you try to open a .odt document from within the OpenCloud Web UI as Collabora is embedded via an iframe.

<img src={require("./img/quick-guide/collabora-accept-self-signed-cert.png").default} alt="Accept self signed certificate" width="1920"/>


---

### 4. Login

Login with your browser:
- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: **admin**
- password: **admin**

<img src={require("./img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>


### 5. Conclusion

Your OpenCloud server is now running and ready to use 🚀

--- 

### Troubleshooting

If you encounter any issues or errors, try finding a solution here: 

- [Common Issues & Help](./../50-resources/30-common-issues.md)