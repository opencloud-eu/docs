---
sidebar_position: 12
id: radicale-integration
title: Calendar and Contacts Integration with Radicale
description: "How to enable Calendar and Contacts integration via Radicale in OpenCloud."
---

OpenCloud is able to act as an authenticating reverse proxy for the open-source
CalDAV and CardDAV Server[Radicale](https://radicale.org).

The `opencloud_full` deployment example already contains all the required pieces to
setup the integration. This guide explains the required steps to achieve that.

---

## Setting up Calendar and Contacts Integration with Radicale

To use this feature you need at least OpenCloud Version 2.3.0. Earlier releases lack
some of the required features. This guide assumes that you already have a running
deployment based on the `opencloud_full` deployment example.

### 1. Configure the `.env` file to deploy Radicale

In the root directory of the `opencloud_full` deployment example, usually `opencloud/deployments/examples/opencloud_full`, 
remove the `#` symbol from the line:

```
#RADICALE=:radicale.yml
```

### 2. Update the deployment

```
docker compose up -d
```

This will launch an additional container (called `radicale`) using the
`opencloudeu/radicale` container image and reconfigure the OpenCloud instance
to automatically forward all authenticated traffic on
`https://<your.opencloud.domain>/caldav` and
`https://<your.opencloud.admin>/carddav` to the radicale container adding
information about the authenticated users.

Radicale is configured to automatically create a default calendar and addressbook for every authenticated user.

## Accessing the Calendar and Addressbook

Users should now be able to access their Addressbook and Calendar with any
capable CalDAV/CardDAV software (OpenCloud does currently not provide any UI
to access them).

As very few clients currently support authentication via OpenID Connect you can use
the "App Token" feature in the user's settings page to generate an application specific
password that can be used for authentication in most existing CalDAV/CardDAV clients.

Many clients support the automatic discovery of existing Calendars and
Addressbooks via the so-called `.well-known` endpoints. In that case the only
thing that is needed for the client to work is to set
`https://<your.opencloud.domain>` as the target URL for calendars and
addressbooks together with the OpenCloud username as the username and the
generated app token as the password for authentication.
