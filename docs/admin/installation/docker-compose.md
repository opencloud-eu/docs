---
sidebar_position: 3
id: docker-compose
title: Quickstart with docker compose
---

# Docker Compose
<br/><br/>

## Spin up a temporary local instance of OpenCloud using **Docker Compose**.
<br/><br/>

---

### **Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [**Docker Compose**](https://docs.docker.com/compose/install/)
<br/><br/>

---

###  1. Download

Download the `opencloud_full` folder (this folder contains a multi-file Docker Compose configuration):

```Shell
git clone https://github.com/opencloud-eu/opencloud.git
```
<br/><br/>

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
<br/><br/>

---

### 3. Add local domains to /etc/hosts 

Edit the /etc/hosts file and add the following entries for local access:

```
127.0.0.1       cloud.opencloud.test
127.0.0.1       collabora.opencloud.test
127.0.0.1       wopiserver.opencloud.test
127.0.0.1       onlyoffice.opencloud.test
```
<br/><br/>

---

### 4. Login

Login with your browser:
- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: **admin**
- password: **admin**

<img src={require("./img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>

### 5. Conclusion

Your OpenCloud server is now running and ready to use 🚀
<br/><br/>

--- 

### Troubleshooting

If you encounter any issues or errors, try finding a solution here: 

- [Common Issues & Help](./../common-issues.md)
