---
sidebar_position: 160
id: guest-feature
title: Guest-Feature
description: Set up guest-feature in OpenCloud
draft: false
---

# Set Up the Guest Feature

The Guest Feature allows users to share files and folders with external people by email address. The invited guest receives an email with a personal link and can access the shared content in the web browser without an OpenCloud account.

This guide explains how to enable the Guest Feature in a deployment based on the `opencloud-compose` deployment example.

:::note
The Guest Feature is disabled by default. It requires OpenCloud version 9.0.0 or later and a working email configuration.
:::

## How the Guest Feature Works

The Guest Feature is provided by the `auth-guest` service.

- When a user shares a file or folder with an external email address, the `auth-guest` service creates a one-time invitation link.
- The `notifications` service sends the invitation link to the guest by email.
- When the guest opens the link, OpenCloud verifies it and creates a guest session in the browser.
- The guest can access only the shared file or folder, with the permissions assigned by the sharing user.

| Setting                         | Default                                   |
| ------------------------------- | ----------------------------------------- |
| Validity of the invitation link | 30 minutes, single use (not configurable) |
| Lifetime of a guest session     | 24 hours (`AUTH_GUEST_JWT_TTL`)           |

## Prerequisites

- A running OpenCloud deployment based on `opencloud-compose`.
- OpenCloud version 9.0.0 or later.
- Access to an SMTP mailbox that OpenCloud can use to send emails.

All commands in this guide are run in the root directory of the `opencloud-compose` deployment.

## Check the OpenCloud Version

Check whether your OpenCloud image contains the `auth-guest` service:

```bash
docker compose exec opencloud opencloud help | grep -i guest
```

If the output shows `auth-guest`, continue with the next step.

If there is no output, update OpenCloud. Set the image tag in your `.env` file, for example:

```env
OC_DOCKER_TAG=9.0.0
```

Then update the deployment:

```bash
docker compose pull opencloud
docker compose up -d
```

:::caution
Create a backup before you update OpenCloud.
:::

## Get the Service Account Credentials

The `auth-guest` service uses the OpenCloud service account. Without it, the service does not start.

Read the service account credentials from your existing OpenCloud configuration:

```bash
docker compose exec opencloud cat /etc/opencloud/opencloud.yaml | grep -m1 -A2 "service_account:"
```

The output looks similar to this:

```yaml
service_account:
  service_account_id: 1234abcd-...
  service_account_secret: ...
```

You need both values in the next step.

:::important
Treat the service account secret like a password. Do not share it.
:::

## Enable the Guest Feature

The Guest Feature settings must be passed to the OpenCloud container. Adding the variables to the `.env` file alone is not sufficient, because the `opencloud-compose` files do not forward them to the container.

Use a separate Compose file for the Guest Feature instead.

### Create the Compose File

Create the folder `custom` and the file `custom/guest.yml`:

```bash
mkdir -p custom
nano custom/guest.yml
```

Add the following content and replace the placeholders with the values from the previous step:

```yaml
services:
  opencloud:
    environment:
      OC_ENABLE_GUEST_LINKS: 'true'
      AUTH_GUEST_SERVICE_ACCOUNT_ID: 'YOUR-SERVICE-ACCOUNT-ID'
      AUTH_GUEST_SERVICE_ACCOUNT_SECRET: 'YOUR-SERVICE-ACCOUNT-SECRET'
```

:::caution
Docker Compose interprets the `$` character as the start of a variable. If the secret contains a `$`, write it as `$$`. Otherwise Docker Compose shows a warning such as `The "XY" variable is not set` and passes an incorrect secret to the container.
:::

### Add the File to `COMPOSE_FILE`

Add `custom/guest.yml` to the end of the `COMPOSE_FILE` variable in your `.env` file, for example:

```env
COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:traefik/opencloud.yml:traefik/collabora.yml:radicale/radicale.yml:custom/guest.yml
```

:::note
Make sure that the `.env` file contains only one active `COMPOSE_FILE` line. If there are several lines, only the last one is used.
:::

## Configure Email Delivery

Guests receive their invitation link by email. Configure the SMTP settings and enable the `notifications` service in your `.env` file:

```env
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_SENDER=OpenCloud <noreply@example.com>
SMTP_USERNAME=noreply@example.com
SMTP_PASSWORD=YOUR-PASSWORD
SMTP_TRANSPORT_ENCRYPTION=starttls
SMTP_INSECURE=false
SMTP_AUTHENTICATION=auto
START_ADDITIONAL_SERVICES=notifications
```

- `SMTP_SENDER` must usually match the mailbox that sends the email. Otherwise the mail server may reject the message.
- If `START_ADDITIONAL_SERVICES` already contains other services, add `notifications` separated by a comma.
- Use port `587` with `starttls` or port `465` with `ssltls`, depending on your mail provider.

For more information, see [Mail Notifications](./mail-notifications.md).

:::tip
Some hosting providers block outgoing connections on port `465`. If emails are not sent, check which port is reachable from your server:

```bash
nc -vz -w 5 smtp.example.com 465
nc -vz -w 5 smtp.example.com 587
```

:::

## Restart OpenCloud

Apply the changes:

```bash
docker compose up -d
```

## Verify the Configuration

Check that the OpenCloud container is running:

```bash
docker compose ps opencloud
```

The status must be `Up`. If the status is `Restarting`, see [Troubleshooting](#troubleshooting).

Check that the Guest Feature is enabled:

```bash
docker compose exec opencloud env | grep GUEST
```

The output must contain `OC_ENABLE_GUEST_LINKS=true`.

Check that the email settings are active:

```bash
docker compose exec opencloud env | grep -E "SMTP_HOST|ADD_RUN_SERVICES"
```

The output must contain your SMTP server and `notifications`.

Finally, test the Guest Feature in the web interface: share a folder with an external email address, select the entry marked **(Guest)**, and click **Share**. The guest should receive an invitation email.

## Optional Settings

You can adjust the behavior of the Guest Feature with additional environment variables in `custom/guest.yml`.

| Variable                          | Default | Description                                                                           |
| --------------------------------- | ------- | ------------------------------------------------------------------------------------- |
| `AUTH_GUEST_JWT_TTL`              | `24h`   | Lifetime of a guest session.                                                          |
| `AUTH_GUEST_PIN_AND_NONCE_TTL`    | `30m`   | Lifetime of the one-time PIN used to renew guest access.                              |
| `AUTH_GUEST_BACKOFF_MAX_ATTEMPTS` | `5`     | Number of failed PIN attempts before the PIN is invalidated.                          |
| `AUTH_GUEST_QUOTA_COOLDOWN`       | `1m`    | Minimum time between two renewals without a valid session for the same share.         |
| `AUTH_GUEST_QUOTA_DAILY_CAP`      | `50`    | Maximum number of renewals without a valid session per share within the quota window. |

For a complete list of settings, see the [auth-guest environment variables](../../dev/server/services/auth-guest/env-vars.mdx) in the developer documentation.

## Troubleshooting

### The OpenCloud Container Keeps Restarting

Check the logs:

```bash
docker compose logs --tail=40 opencloud
```

If the log contains `guestlinks: service_account_id must not be empty`, the service account credentials are missing. Add `AUTH_GUEST_SERVICE_ACCOUNT_ID` and `AUTH_GUEST_SERVICE_ACCOUNT_SECRET` to `custom/guest.yml` as described in [Enable the Guest Feature](#enable-the-guest-feature).

### Sharing with a Guest Fails

If users see the message `Failed to add share` when they share with a guest:

- Check that the OpenCloud image contains the `auth-guest` service, see [Check the OpenCloud Version](#check-the-opencloud-version).
- Check that `OC_ENABLE_GUEST_LINKS=true` is set inside the container:

  ```bash
  docker compose exec opencloud env | grep GUEST
  ```

  If there is no output, the variable is not passed to the container. Make sure that `custom/guest.yml` is part of `COMPOSE_FILE`.

### Guests Do Not Receive an Email

Check the log of the `notifications` service:

```bash
docker compose logs opencloud | grep '"service":"notifications"' | tail -10
```

- **No output:** The `notifications` service is not running. Set `START_ADDITIONAL_SERVICES=notifications` in your `.env` file.
- **`SMTP Connection timed out`:** OpenCloud cannot reach the mail server. Your hosting provider may block the configured port. Use port `587` with `starttls` instead of port `465`.
- **Authentication errors:** Check `SMTP_USERNAME`, `SMTP_PASSWORD`, and `SMTP_SENDER`.

Invitations created while email delivery was not working are not sent again. Remove the guest share and invite the guest again.
