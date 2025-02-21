---
sidebar_position: 1
id: decomposeds3
title: Decomposeds3
---

# Decomposeds3 Storage Driver

Decomposeds3 is a storage driver for OpenCloud that uses MinIO, an S3-compatible object storage, for handling file storage efficiently. This setup leverages S3’s scalability while integrating seamlessly with OpenCloud.

---

**Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Docker**](https://docs.docker.com/compose/install/)
- [**Docker Compose**](https://docs.docker.com/compose/install/)

---

##  1. Download

Download the `opencloud_full` folder (this folder contains a multi-file Docker Compose configuration):

```Shell
git clone https://github.com/opencloud-eu/opencloud.git
```

## 2. Start

Navigate to the Docker Compose configuration folder:

```Shell
cd opencloud/deployments/examples/opencloud_full
```

Enable `decomposeds3.yml` and `minio.yml` in the `.env` file:

```Shell
nano opencloud/deployments/examples/opencloud_full/.env
```

Find all required environment variables `env` here: [decomposeds3-envs](https://github.com/opencloud-eu/opencloud/blob/main/services/storage-users/pkg/config/config.go#L143-L176)

Start the deployment with Docker Compose:

```Shell
docker compose up -d
```

This starts all necessary containers in the background.

## 3. Add local domains to /etc/hosts 

Edit the /etc/hosts file and add the following entries for local access:

```
127.0.0.1       cloud.opencloud.test
127.0.0.1       minio.opencloud.test
```

## 4. Login

Login with your browser:
- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: **admin**
- password: **admin**

🎉 Congratulations! You’ve successfully set up and launched OpenCloud! Happy hacking!🚀

<img src={require("./img/login-page.png").default} alt="Admin general" width="1920"/>

<img src={require("./img/decomposeds3-with-minio.png").default} alt="Admin general" width="1920"/>

--- 

### Troubleshooting

If you encounter any issues or errors, try finding a solution here: 

- [Common Issues & Help](./../common-issues.md)
