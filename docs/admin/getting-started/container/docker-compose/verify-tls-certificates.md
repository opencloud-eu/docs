---
sidebar_position: 5
id: docker-compose-verify-tls
title: Verify TLS/SSL Certificates
description: Validate SSL certificates and migrate from Let's Encrypt staging to production
---

# Verify TLS and SSL Certificates

After starting OpenCloud with Docker Compose and Traefik, verify that SSL certificates were issued correctly and switch from staging to production certificates when ready.

:::note
This guide applies to the [integrated Traefik deployment](./integrated-traefik.md). For external proxy setups, see [Behind External Proxy](./external-proxy.md).
:::

## Verify Staging Certificates

By default, the setup uses **Let's Encrypt staging certificates** for testing. These are not trusted by browsers but prove that the DNS and certificate generation workflow is correct.

### Open your domain in a web browser

Open the following URL:

```bash
https://cloud.YOUR.DOMAIN
```

Because the setup currently uses Let's Encrypt staging certificates, your browser will show a security warning. **This is expected and normal for the staging environment.**

The same warning may appear for the other configured domains.

### Example in Chrome

Click on the lock icon to view certificate details:

<img src={require("./../../img/docker-compose/certificate-details.png").default} alt="Certificate Details" width="500"/>

Expand the certificate information to confirm it was issued by "Let's Encrypt Staging":

<img src={require("./../../img/docker-compose/certificate-viewer.png").default} alt="Certificate Details" width="500"/>

<img src={require("./../../img/docker-compose/subordinate-ca's.png").default} alt="Certificate Details Subordinate CA" width="500"/>

:::success Staging Certificate Success
If you see "Let's Encrypt Staging" as the issuer, the certificate generation is working correctly. You can now safely switch to production certificates.
:::

## Apply a Real SSL Certificate

Once the staging certificate works correctly, you can switch to production SSL certificates from Let's Encrypt.

### Stop Docker Compose

```bash
docker compose down
```

### Remove old staging certificates

Delete the previously generated staging certificates:

```bash
rm -r certs
```

:::warning
If you changed volume names or paths in your `.env` file, adjust this command to match your certificate directory.
:::

### Disable staging mode in `.env`

Open the environment file:

```bash
nano .env
```

Comment out or remove the staging server line:

```bash
# TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory
```

Save the file.

### Restart OpenCloud with production certificates

Start the containers again:

```bash
docker compose up -d
```

Traefik will now request trusted production certificates from Let's Encrypt.

### Wait for certificate generation

Certificate generation may take a few moments. Check the logs:

```bash
docker compose logs traefik
```

Look for messages indicating successful certificate generation.

### Verify production certificates

After a short moment, visiting your domain should show a secure HTTPS connection:

<img src={require("./../../img/docker-compose/status-secure.png").default} alt="Secure Connection" width="1920"/>

The lock icon should show "Secure" (green lock) with "Let's Encrypt Authority X3" or similar as the issuer.

## Log into OpenCloud

Once certificates are verified:

1. Open your domain in a browser:

```bash
https://cloud.YOUR.DOMAIN
```

2. Log in with your admin credentials:
   - **Username:** `admin`
   - **Password:** (the password you configured in the `.env` file)

<img src={require("./../../img/docker-compose/login.png").default} alt="OpenCloud Login" width="1920"/>

## Troubleshooting

### Certificate generation fails

**Check Traefik logs:**

```bash
docker compose logs traefik
```

Look for error messages about ACME challenges.

### DNS issues

Ensure your domain correctly points to your server:

```bash
nslookup cloud.YOUR.DOMAIN
```

The result should match your server's IP address.

### Port 80/443 not accessible

Verify firewall rules allow:

- HTTP (port 80) – Required for ACME challenge
- HTTPS (port 443) – Required for OpenCloud access

### Certificate not updating

If Traefik fails to renew certificates:

1. Check available disk space
2. Verify ACME email is correct in `.env`
3. Review Traefik configuration in your Docker Compose setup

## Next Steps

- **[Production Considerations](./production-considerations.md)** – Persistent storage and production best practices
- **[Configure Keycloak](./keycloak-deployment.md)** (optional) – Add enterprise identity management
- **[Maintenance & Monitoring](../../maintenance/)** – System health and logging
