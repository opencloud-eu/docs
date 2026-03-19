---
sidebar_position: 4
id: verify-SSL-certification
title: Verify SSL Certification
description: 'Verify SSL Certification in OpenCloud'
draft: true
---

# Verify SSL Certification

## After starting OpenCloud, verify that the SSL certificates were issued correctly

Open the following URL in your web browser:

```bash
https://cloud.YOUR.DOMAIN
```

Because the setup currently uses Let's Encrypt staging certificates, your browser will show a security warning. This is expected, as staging certificates are not trusted by browsers.

The same warning may appear for the other domains you configured.

Example in the Chrome browser:

<img src={require("./../../img/docker-compose/certificate-details.png").default} alt="Certificate Details" width="500"/>

- Check the certificate details to confirm that the certificate was issued by Let's Encrypt Staging.

  <img src={require("./../../img/docker-compose/certificate-viewer.png").default} alt="Certificate Details" width="500"/>
  <img src={require("./../../img/docker-compose/subordinate-ca's.png").default} alt="Certificate Details" width="500"/>

## Apply a Real SSL Certificate

Once the staging certificate works correctly, you can switch to a production SSL certificate.

### Stop Docker Compose

Stop the running containers:

```bash
docker compose down
```

### Remove old staging certificates

Delete the previously generated staging certificates:

```bash
rm -r certs
```

If you changed volume names or paths, adjust this command accordingly.

### Disable staging mode in `.env`

Open the environment file:

```bash
nano .env
```

Comment the staging server:

```bash
# TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory
```

### Restart OpenCloud with a real SSL certificate

Start the containers again:

```bash
docker compose up -d
```

OpenCloud will now request trusted production certificates from Let's Encrypt.

After a short moment, visiting the following URL should show a secure HTTPS connection:

<img src={require("./../../img/docker-compose/status-secure.png").default} alt="Certificate Details" width="1920"/>

## Log into OpenCloud

Open a browser and visit:

```bash
https://cloud.YOUR.DOMAIN
```

Login with:

Username: `admin`

Password: (the password you configured in the .env file)

<img src={require("./../../img/docker-compose/login.png").default} alt="Admin general" width="1920"/>

## Troubleshooting

If you encounter any issues during the setup process, check the troubleshooting guide:
[Common Issues & Help](../../../resources/common-issues)
