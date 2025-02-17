---
sidebar_position: 2
id: quickstart
title: Quickstart
---

# Quickstart
**Docker Compose**

Spin up a temporary local instance of OpenCloud using **Docker Compose**.


**Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [**Docker Compose**](https://docs.docker.com/compose/install/)


---

##  1. Download

Download the `opencloud_full` folder (this folder contains a multi-file Docker Compose configuration):

```Shell
git clone https://github.com/opencloud-eu/opencloud/tree/main/deployments/examples/opencloud_full
```



## 2. Start

cd into the Docker Compose configuration folder:

```Shell
cd opencloud/deployments/examples/opencloud_full
```


Start the depoyment with Docker Compose:

```
docker-compose up -d
```

<img src={require("./img/quick-guide/quick-docker-compose-up.png").default} alt="Admin general" width="1920"/>

This starts all necessary containers in the background.

## 3. Login

Login with your browser:
- [https://cloud.opencloud.test](http://cloud.opencloud.test)
- user: **admin**
- password: **admin**

Congratulations! You’ve successfully set up and launched OpenCloud! Happy hacking!

<img src={require("./img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>

## Common Issues & Help

### Check whether the containers are running

```
docker ps
```

<img src={require("./img/quick-guide/quick-docker-running.png").default} alt="Admin general" width="1920"/>

Several containers should be listed here, e.g., for opencloud, traefik, etc.


### Accept Self-Signed Certificates:

As the local environment is self-signed, you must accept the security risk in your browser.

For Firefox:

You need to klick on **Advanced**

<img src={require("./img/quick-guide/quick-advanced.png").default} alt="Admin general" width="500"/>

Confirm the risk with **Accept the risk and Contiune**

<img src={require("./img/quick-guide/quick-accept-security-risk.png").default} alt="Admin general" width="500"/>

