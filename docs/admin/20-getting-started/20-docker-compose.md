---
sidebar_position: 2
id: docker-compose
title: Docker Compose
description: "🌟 Full-blown featureset including web office and full-text search."
---

# Docker Compose


Spin up a temporary local instance of OpenCloud using **Docker Compose**.


## **Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [**Docker Compose**](https://docs.docker.com/compose/install/)

---

##  1. Download

Download the `opencloud_full` folder (this folder contains a multi-file Docker Compose configuration):

```Shell
git clone https://github.com/opencloud-eu/opencloud.git
```

---

## 2. Start

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

## 3. Add local domains to /etc/hosts 

Edit the /etc/hosts file and add the following entries for local access:

```
127.0.0.1       cloud.opencloud.test
127.0.0.1       collabora.opencloud.test
127.0.0.1       wopiserver.opencloud.test
127.0.0.1       onlyoffice.opencloud.test
```

---

## 4. Login

Login with your browser:
- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: **admin**
- password: **admin**

<img src={require("./img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>

## 5. Accept self signed certificates

As described in the [common issues](./../50-resources/30-common-issues.md) you need to accept the self signed certificates.

If you want to use collabora as well, you need to go on [https://collabora.opencloud.test](https://collabora.opencloud.test) and accept there the certifacte too. 
After this, you can work with Collabora in OpenCloud.

## 6. Conclusion

Your OpenCloud server is now running and ready to use 🚀

--- 

## Troubleshooting

If you encounter any issues or errors, try finding a solution here: 

- [Common Issues & Help](./../50-resources/30-common-issues.md)
