---
sidebar_position: 4
id: common-issues
title: Common Issues & Help
---

---

### Check whether the containers are running

```Shell
docker ps
```

<img src={require("./img/common-issues/quick-docker-running.png").default} alt="Admin general" width="1920"/>

Several containers should be listed here, e.g., for opencloud, traefik, etc.

---

### Accept Self-Signed Certificates

As the local environment is self-signed, you must accept the security risk in your browser.

For Firefox:

You need to click on **Advanced**

<img src={require("./img/common-issues/quick-advanced.png").default} alt="Admin general" width="500"/>

Confirm the risk with **Accept the risk and Continue**

<img src={require("./img/common-issues/quick-accept-security-risk.png").default} alt="Admin general" width="500"/>


---

### Docker Permission Issues

If your Docker Compose setup fails to start and the logs contain messages such as `permission denied`, it's likely due to incorrect ownership of local directories used by the containers.

**Example log output:**

```
opencloud-1 | {"level":"fatal","service":"nats","time":"2025-04-08T09:59:59Z","line":"github.com/opencloud-eu/opencloud/services/nats/pkg/logging/nats.go:33","message":"Can't start JetStream: could not create storage directory - mkdir /var/lib/opencloud/nats: permission denied"}
```

This error typically occurs when the mounted directories are owned by the wrong user, such as `root`, instead of the standard Docker user (`UID 1000`).

**Incorrect directory ownership:**

```
drwxr-xr-x  3 root root 4096 Apr  8 09:59 opencloud-data
```

**Correct ownership should be:**

```
drwxr-xr-x  9 1000 1000 4096 Apr  7 07:57 opencloud-data
```

To resolve this issue, adjust the ownership of the directory using the `chown` command:

```bash
chown -R 1000:1000 opencloud-data
```

:::caution Security Warning

The user with UID 1000 on your host system will have full access to these mounted directories. This means that any local user account with this ID can read, modify, or delete OpenCloud config and data files.

This can pose a security risk in shared or multi-user environments. Make sure to implement proper user and permission management and consider isolating access to these directories.

:::

Ensure you apply this to all relevant folders that are mounted into your containers. This will grant the Docker container the necessary permissions to access and write to these directories.

---

## 🔐 Change Admin Password Set in `.env`

If you initially set the OpenCloud **admin password** using the `.env` file, please note:

> ⚠️ **You cannot simply change the password again by editing the `.env` file.**  
> Once the container is running, password changes must be made via the Web UI or terminal.

---

### ✅ Option 1: Change via Web UI

If the current admin password is known:

1. Log in to the OpenCloud **Web Interface**.
2. Navigate to **Settings > Security**.
3. Enter your current password and choose a new one.

> If the admin password is forgotten or you prefer command-line tools, use the terminal method below.

---

### 🖥️ Option 2: Change via Terminal

If the admin password is forgotten or needs to be changed via the terminal:

#### Step 1: Stop the Docker container

First, stop your OpenCloud container:

```bash
docker compose stop opencloud
```

#### Step 2: Run the password reset command

Use the following command to reset the password:

```bash
sudo docker run -it --rm -v <opencloud-data-path>:/var/lib/opencloud -v <opencloud-config-path>:/etc/opencloud opencloudeu/opencloud:<opencloud-version> idm resetpassword
```
Replace:

`<opencloud-data-path>` – Docker volume for OpenCloud data

`<opencloud-config-path>` – Docker volume for OpenCloud config

`<opencloud-version>` – Use latest or your specific version

🔍 How to find the volume names
You can list your current Docker volumes with:

```bash
docker volume ls
```

Look for volumes like:

`opencloud_full_opencloud-data`

`opencloud_full_opencloud-config`

💡 Example for standard setup:

```bash
sudo docker run -it --rm -v opencloud_full_opencloud-data:/var/lib/opencloud -v opencloud_full_opencloud-config:/etc/opencloud opencloudeu/opencloud:latest idm resetpassword
```

#### Step 3: Start the container again

```bash
docker compose up -d
``` 
