---
sidebar_position: 2
id: docker
title: Quickstart with docker
---

# Docker
<br/><br/>

## Spin up a temporary local instance of OpenCloud using **Docker**.
<br/><br/>

---

### **Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Docker**](https://docs.docker.com/compose/install/)
<br/><br/>

---

###  1. Create Required Directories for Bind Mounts

```Shell
mkdir -p $HOME/opencloud/opencloud-config
mkdir -p $HOME/opencloud/opencloud-data
```
<br/><br/>

---

### 2. Pull OpenCloud Image

```Shell
docker pull opencloud-eu/opencloud:latest
```
<br/><br/>

---

### 3.  Initialize OpenCloud (First-time Setup)

```Shell
docker run --rm -it \
    -v $HOME/opencloud/opencloud-config:/etc/opencloud \
    -v $HOME/opencloud/opencloud-data:/var/lib/opencloud \
    -e IDM_ADMIN_PASSWORD=admin \
    opencloud-eu/opencloud:latest init
```

You can set your own password using `IDM_ADMIN_PASSWORD=your_password`. If not set, a password will be auto-generated

<img src={require("./img/quick-guide/docker-opencloud-init.png").default} alt="Admin general" width="1920"/>
<br/><br/>

---

### 4. Start OpenCloud

```Shell
docker run \
    --name opencloud \
    --rm \
    -it \
    -p 9200:9200 \
    -v $HOME/opencloud/opencloud-config:/etc/opencloud \
    -v $HOME/opencloud/opencloud-data:/var/lib/opencloud \
    -e OC_INSECURE=true \
    -e PROXY_HTTP_ADDR=0.0.0.0:9200 \
    -e OC_URL=https://localhost:9200 \
    opencloud-eu/opencloud:latest
```
<br/><br/>

---

### 5. Login

Login with your browser:
- [https://localhost:9200](https://localhost:9200)
- user: **admin**
- password: **admin**

<img src={require("./img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>
<br/><br/>

---

### 6. Conclusion

Your OpenCloud server is now running and ready to use 🚀
<br/><br/>

--- 

### If you encounter any issues or errors, try finding a solution here: 
- [Common Issues & Help](./common-issues.md)