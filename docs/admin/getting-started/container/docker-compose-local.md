---
sidebar_position: 3
id: docker-compose-local
title: Docker Compose local
description: '🌟 Full-blown featureset including web office and full-text search.'
---

## Guide for local installation

Spin up a temporary local instance of OpenCloud using **Docker Compose**.

## **Prerequisites:**

- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [**Docker Compose**](https://docs.docker.com/compose/install/)

---

## 1. Download

Clone the OpenCloud repository:

```Shell
git clone https://github.com/opencloud-eu/opencloud-compose.git
```

---

## 2. Start

### cd into the Docker Compose configuration folder:

```Shell
cd opencloud-compose
```

### Create environment file:

```Shell
cp .env.example .env
```

> **Note:** The repository includes .env.example as a template with default settings and documentation. Your actual .env file is excluded from version control (via .gitignore) to prevent accidentally committing sensitive information like passwords and domain-specific settings.

### Configure deployment options:

You can deploy using explicit -f flags:

```Shell
docker compose -f docker-compose.yml -f weboffice/collabora.yml -f traefik/opencloud.yml -f traefik/collabora.yml up -d
```

Or by uncomment or adding the COMPOSE_FILE variable in .env:

```Shell
COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:traefik/opencloud.yml:traefik/collabora.yml
```

Set you initial admin password in the .env

```Shell
INITIAL_ADMIN_PASSWORD=YOUR.SECRET.PASSWORD
```

This is mandatory for security reasons. Otherwise the OpenCloud container will not start.

Start the deployment with Docker Compose:

```Shell
docker compose up -d
```

<img src={require("./../img/quick-guide/quick-docker-compose-up.png").default} alt="Admin general" width="1920"/>

This starts all necessary containers in the background.

---

## 3. Add local domains to /etc/hosts

Edit the /etc/hosts file and add the following entries for local access:

```
127.0.0.1       cloud.opencloud.test
127.0.0.1       collabora.opencloud.test
127.0.0.1       wopiserver.opencloud.test
```

Open [https://collabora.opencloud.test](https://collabora.opencloud.test) and accept the self-signed certificate. This step is needed as you can not accept the self-signed certificate if you try to open a .odt document from within the OpenCloud Web UI as Collabora is embedded via an iframe.

<img src={require("./../img/quick-guide/collabora-accept-self-signed-cert.png").default} alt="Accept self signed certificate" width="1920"/>

---

## 4. Login

Login with your browser:

- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: **admin**
- password: YOUR.SECRET.PASSWORD

<img src={require("./../img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>

## 5. Conclusion

Your OpenCloud server is now running and ready to use 🚀

---

## Troubleshooting

If you encounter any issues or errors, try finding a solution here:

- [Common Issues & Help](./../../resources/common-issues.md)
