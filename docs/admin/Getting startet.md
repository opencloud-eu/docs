---
sidebar_position: 2
---

# Quick-Guide
## OpenCloud in less than five minutes

## Prerequisites:
- [**Docker**](https://docs.docker.com/engine/install/) and [**Docker Compose**](https://docs.docker.com/compose/install/) must be installed.
- A **Unix-based system** (Linux or macOS) or **Windows with WSL2** is recommended.

---

#  1. Start OpenCloud Full Example Deployment with Docker

### 1. Get the OpenCloud Full Example Repository
```
git clone https://github.com/opencloud-eu/fullexample
cd opencloud-full-example
```

### 2. Start the deployment with Docker Compose

```
docker-compose up -d
````

This starts all necessary containers in the background.


### 3. Check whether the containers are running

```
docker ps
```

Several containers should be listed here, e.g., for ocis, traefik, redis, etc.

# 2. Access to oCIS

By default, oCIS can be accessed at **[http://cloud.opencloud.test](http://cloud.opencloud.test)**.

### Login:

- **Admin User:** `admin`
- **Password:** `admin`


