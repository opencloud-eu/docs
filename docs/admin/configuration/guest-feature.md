---
sidebar_position: 160
id: guest-feature
title: Guest Feature
description: Set up the Guest Feature in OpenCloud
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

- A running OpenCloud deployment based on [`opencloud-compose`](https://github.com/opencloud-eu/opencloud-compose).
- OpenCloud version 9.0.0 or later.
- A working SMTP configuration for sending invitation emails.

If you are running an older OpenCloud version, follow the [Standard Upgrade Guide](../maintenance/upgrade/upgrade.md) and the [Upgrade 9.x.x](../maintenance/upgrade/upgrade-9.x.x.md) guide before enabling the Guest Feature.

:::important
Before upgrading, check whether a version-specific upgrade guide is available for your target version. These guides may contain additional migration steps, configuration changes, or breaking changes that must be considered.
:::

To configure email delivery, follow the [Mail Notifications](./mail-notifications.md) guide. Make sure that the `notifications` service is enabled.

All commands in this guide are run in the root directory of the `opencloud-compose` deployment.

## Check the Service Account Configuration

The `auth-guest` service requires a service account. Without it, the service does not start and the OpenCloud container keeps restarting.

Check whether your OpenCloud configuration contains the service account settings for the `auth-guest` service:

```bash
docker compose exec opencloud grep -A3 "auth_guest:" /etc/opencloud/opencloud.yaml
```

- **New installations of OpenCloud 9.0.0 or later:** The output shows the `service_account` settings. They are created automatically during the initial setup. No further action is required.
- **Installations upgraded from an earlier version:** If there is no output, migrate the configuration as described in the [Upgrade 9.x.x](../maintenance/upgrade/upgrade-9.x.x.md#guest-links) guide before you continue.

## Enable the Guest Feature

The Guest Feature settings must be passed to the OpenCloud container. Adding the variables to the `.env` file alone is not sufficient, because the `opencloud-compose` files do not forward them to the container.

Use a separate Compose file for the Guest Feature instead.

### Create the Compose File

Create the folder `custom` and the file `custom/guest.yml`:

```bash
mkdir -p custom
nano custom/guest.yml
```

Add the following content:

```yaml
services:
  opencloud:
    environment:
      OC_ENABLE_GUEST_LINKS: 'true'
```

### Add the File to `COMPOSE_FILE`

Add `custom/guest.yml` to the end of the existing `COMPOSE_FILE` variable in your `.env` file, for example:

```env
COMPOSE_FILE=docker-compose.yml:weboffice/collabora.yml:traefik/opencloud.yml:traefik/collabora.yml:radicale/radicale.yml:custom/guest.yml
```

Keep all files that are already part of your deployment.

:::note
Make sure that the `.env` file contains only one active `COMPOSE_FILE` line. If there are several lines, only the last one is used.
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
docker compose exec opencloud printenv OC_ENABLE_GUEST_LINKS
```

The output must be `true`.

Check that the `notifications` service is enabled:

```bash
docker compose exec opencloud printenv OC_ADD_RUN_SERVICES
```

The output must contain `notifications`.

Finally, test the Guest Feature in the web interface:

1. Share a file or folder with an external email address.
2. Select the recipient marked `(Guest)`.
3. Click `Share`.
4. Verify that the guest receives an invitation email and can access the shared content.

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

If the log contains `guestlinks: service_account_id must not be empty`, the service account settings for the `auth-guest` service are missing in the OpenCloud configuration. Migrate the configuration as described in [Check the Service Account Configuration](#check-the-service-account-configuration).

### Sharing with a Guest Fails

If users see the message `Failed to add share` when they share with a guest:

- Make sure that you are running OpenCloud version 9.0.0 or later.
- Verify that `OC_ENABLE_GUEST_LINKS` is set to `true` inside the container:

  ```bash
  docker compose exec opencloud printenv OC_ENABLE_GUEST_LINKS
  ```

  If there is no output, the variable is not passed to the container. Make sure that `custom/guest.yml` is part of `COMPOSE_FILE`.

### Guests Do Not Receive an Email

Check the log of the `notifications` service:

```bash
docker compose logs opencloud | grep '"service":"notifications"' | tail -10
```

Make sure that the `notifications` service is enabled and that your SMTP configuration is working. See [Mail Notifications](./mail-notifications.md) for configuration details and troubleshooting.

Invitations created while email delivery was not working are not sent again. Remove the guest share and invite the guest again.
