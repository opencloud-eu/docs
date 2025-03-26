---
sidebar_position: 2
id: docker-compose
title: Docker Compose
description: "🌟 Full-blown featureset including web office and full-text search."
---

# Docker Compose



## **Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [**Docker Compose**](https://docs.docker.com/compose/install/)
- Four domains set up and pointing to your server
    - cloud.* for serving OpenCloud
    - collabora.* for serving Collabora
    - wopiserver.* for serving the WOPI server
    - traefik.* for serving the Traefik dashboard

    Alternatively you can register a wildcard domain with *.YOUR.DOMAIN
- Host service (we use in our example Hetzner as hostservice)

---

## 1. Login to a host-service / server:

In our case, we log in to our created Hetzner server via SSH via the terminal.

```Shell
ssh root@"ip of the server"
```

---

## 2. Install Docker

Perform an update and upgrad

```Shell
apt update && apt upgrade -y
```


Follow the instruction from the [official Docker website](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

After installing Docker, you need to enable and start it

```Shell
systemctl enable docker && systemctl start docker
```

## 3. Clone OpenCloud Repository

Download the `opencloud_full` folder (this folder contains a multi-file Docker Compose configuration):


```Shell
git clone https://github.com/opencloud-eu/opencloud.git
```

---

## 4. Adjust .env file to start the docker compose with staging certificates

Before applying a production Let's Encrypt certificate, you should first test whether the domain certification works correctly. To do this, modify the .env file and use the Let's Encrypt staging environment. The staging certificates allow you to verify your setup without hitting rate limits.

cd into the Docker Compose configuration folder:

```Shell
cd opencloud/deployments/examples/opencloud_full
```

```Shell
nano .env
```

Following variables should be adjusted:

- Comment insecure out:

`# INSECURE=true`

 It skips certificate validation for various parts of OpenCloud and is needed when self signed certificates are used.

- enter your traefik domain

`TRAEFIK_DOMAIN=traefik.YOUR.DOMAIN`

Domain of Traefik, where you can find the dashboard. Defaults to "traefik.opencloud.test"


- enter a valid e-mail adress

`TRAEFIK_ACME_MAIL=valid@mail.adress`

Email address for obtaining LetsEncrypt certificates.

- set the CA-Server to staging

`TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory`

With staging configured, there will be an SSL error in the browser.
When one of the certificates which are written on the lets encrypt website show up, the process went well.

https://letsencrypt.org/docs/staging-environment/

- set your OpenCloud Domain

`OC_DOMAIN=cloud.YOUR.DOMAIN`

Domain of openCloud, where you can find the frontend. Defaults to "cloud.opencloud.test"

- change your admin password 

`ADMIN_PASSWORD=Saf3PAssW0Rd`

OpenCloud admin user password. Defaults to "admin".

- set the Collabora domain

`COLLABORA_DOMAIN=collabora.YOUR.DOMAIN`

Domain of Collabora, where you can find the frontend. Defaults to "collabora.opencloud.test"

- set the WopiServer Domain

`WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN`

Domain of the wopiserver which handles OnlyOffice. Defaults to "wopiserver.opencloud.test"

## 5. Start

Start the deployment with Docker Compose:

```Shell
docker compose up -d
```


This starts all necessary containers in the background.

---

## 6. Check if the certification process works

In your browser enter your OpenCloud domain.

You should now have an insecure connection.

Check the certificate if it is one from the let´s encrypt staging server

https://letsencrypt.org/docs/staging-environment/

<img src={require("./img/docker-compose/certificate-details.png").default} alt="Certificate Details" width="500"/>
<img src={require("./img/docker-compose/certificate-viewer.png").default} alt="Certificate Details" width="500"/>
<img src={require("./img/docker-compose/subordinate-ca's.png").default} alt="Certificate Details" width="500"/>

--- 

## 7.  Make your OpenCloud SSL certificed 

Now that you know, that the signing porcess works, you can make your OpenCloud SSL certificed

You need to remove the `acme.json` file in the traefik container.

- Stop the docker compose

```Shell
docker compose down
```

- Remove the cert volume.

When you have nothing changed in the settings, you can use this command

```Shell
docker volume rm opencloud_full_certs
```

Otherwise you need to find out, how you volume is named and delete this one.

- Comment the staging server out in the .env

```Shell
cd opencloud/deployments/examples/opencloud_full
```

```Shell
nano .env
```

`# TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory`

- Start the docker compose again

```Shell
docker compose up -d
```


When you open your OpenCloud domain in the browser you should have a SSL certified connection

<img src={require("./img/docker-compose/status-secure.png").default} alt="Certificate Details" width="1920"/>


# 8. Login your OpenCloud

Login with your browser:
- https://"your domain of your .env file"
- user: **admin**
- password: **Saf3PAssW0Rd**

<img src={require("./img/docker-compose/login.png").default} alt="Admin general" width="1920"/>




## Troubleshooting

If you encounter any issues or errors, try finding a solution here: 

- [Common Issues & Help](./../50-resources/30-common-issues.md)
<br/>
---

## Guide for local installation
Spin up a temporary local instance of OpenCloud using **Docker Compose**.

## **Prerequisites:**
- **Linux**, **Mac** or **Windows** Subsystem for Linux [(WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
- [**Git**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [**Docker Compose**](https://docs.docker.com/compose/install/)

---

###  1. Download

Download the `opencloud_full` folder (this folder contains a multi-file Docker Compose configuration):

```Shell
git clone https://github.com/opencloud-eu/opencloud.git
```

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

---

### 3. Add local domains to /etc/hosts 

Edit the /etc/hosts file and add the following entries for local access:

```
127.0.0.1       cloud.opencloud.test
127.0.0.1       collabora.opencloud.test
127.0.0.1       wopiserver.opencloud.test
```

Open [https://collabora.opencloud.test](https://collabora.opencloud.test) and accept the self-signed certificate. This step is needed as you can not accept the self-signed certificate if you try to open a .odt document from within the OpenCloud Web UI as Collabora is embedded via an iframe.

<img src={require("./img/quick-guide/collabora-accept-self-signed-cert.png").default} alt="Accept self signed certificate" width="1920"/>


---

### 4. Login

Login with your browser:
- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: **admin**
- password: **admin**

<img src={require("./img/quick-guide/quick-login.png").default} alt="Admin general" width="1920"/>


### 5. Conclusion

Your OpenCloud server is now running and ready to use 🚀

--- 

### Troubleshooting

If you encounter any issues or errors, try finding a solution here: 

- [Common Issues & Help](./../50-resources/30-common-issues.md)