---
sidebar_position: 2
id: quick-guide
title: OpenCloud in under five minutes
---

# Quick-Guide
## OpenCloud in less than five minutes

## Prerequisites:
- A **Unix-based system** (Linux or macOS) or [**Windows with WSL2**](https://learn.microsoft.com/en-us/windows/wsl/install) is recommended.
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) must be installed
- [**Docker**](https://docs.docker.com/engine/install/) and [**Docker Compose**](https://docs.docker.com/compose/install/) must be installed.


---

#  1. Start OpenCloud Full Example Deployment with Docker

### 1. Get the OpenCloud Full Example Repository
```
git clone https://github.com/opencloud-eu/opencloud/tree/main/deployments/examples/opencloud_full

cd opencloud/deployments/examples/opencloud_full
```



### 2. Start the deployment with Docker Compose

```
docker-compose up -d
```

<img src={require("./img/quick-guide/quick-docker-compose-up.png").default} alt="Admin general" width="1920"/>

This starts all necessary containers in the background.


### 3. Check whether the containers are running

```
docker ps
```

<img src={require("./img/quick-guide/quick-docker-running.png").default} alt="Admin general" width="1920"/>

Several containers should be listed here, e.g., for opencloud, traefik, etc.

# 2. Access to oCIS

By default, oCIS can be accessed at [http://cloud.opencloud.test](http://cloud.opencloud.test)

### Accept security risk:

As the local environment is self-signed, you must accept the security risk in your browser.

For Firefox:

You need to klick on **Advanced**

<img src={require("./img/quick-guide/quick-advanced.png").default} alt="Admin general" width="500"/>

Confirm the risk with **Accept the risk and Contiune**

<img src={require("./img/quick-guide/quick-accept-security-risk.png").default} alt="Admin general" width="500"/>

### Login:

Now the login screen appears and you can login with following credentials:

- **Admin User:** `admin`
- **Password:** `admin`

<img src={require("./img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>

Now you can explore OpenCloud and get started! 

