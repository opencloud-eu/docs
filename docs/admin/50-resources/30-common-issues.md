---
sidebar_position: 3
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

Ensure you apply this to all relevant folders that are mounted into your containers. This will grant the Docker container the necessary permissions to access and write to these directories.