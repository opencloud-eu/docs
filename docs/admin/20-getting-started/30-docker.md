---
sidebar_position: 3
id: docker
title: Docker
description: "Classic docker setup."
---

# Docker


## Spin up a temporary local instance of OpenCloud using **Docker**.


---

### **Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Docker**](https://docs.docker.com/compose/install/)


---

###  1. Create Required Directories for Bind Mounts

```Shell
mkdir -p $HOME/opencloud/opencloud-config
mkdir -p $HOME/opencloud/opencloud-data
```


---

### 2. Pull OpenCloud Image

```Shell
docker pull opencloudeu/opencloud-rolling:latest
```


---

### 3.  Initialize OpenCloud (First-time Setup)

```Shell
docker run --rm -it \
    -v $HOME/opencloud/opencloud-config:/etc/opencloud \
    -v $HOME/opencloud/opencloud-data:/var/lib/opencloud \
    -e IDM_ADMIN_PASSWORD=admin \
    opencloudeu/opencloud-rolling:latest init
```

You can set your own password using `IDM_ADMIN_PASSWORD=your_password`. If not set, a password will be auto-generated

<img src={require("./img/quick-guide/docker-opencloud-init.png").default} alt="Admin general" width="1920"/>


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
    opencloudeu/opencloud-rolling:latest
```


---

### 5. Login

Login with your browser:
- [https://localhost:9200](https://localhost:9200)
- user: **admin**
- password: **admin**

<img src={require("./img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>


---

### 6. Conclusion

Your OpenCloud server is now running and ready to use 🚀


--- 

### Troubleshooting

If you encounter any issues or errors, try finding a solution here: 

- [Common Issues & Help](./../50-resources/30-common-issues.md)
