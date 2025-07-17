---
sidebar_position: 2
id: app-tokens
title: App Tokens
description: App Tokens in OpenCLoud
draft: false
---

# App Tokens

App Tokens allow you to connect external apps and services (such as WebDAV clients) securely without using your main password.

## Create the App Token

- Go to the App Tokens section in your OpenCloud account settings.
- Click on “+ New” to create a new token.
- Enter a name for the token (e.g., "WebDAV Client").
- Select an expiration date for added security.
- Click Create.

  <img src={require("./img/app-tokens/create.png").default} alt="Create App Token" width="400"/>

## Copy the App Token

- Once the token is created, it will be shown only once.
- Copy it immediately and store it in a secure place.

  <img src={require("./img/app-tokens/copy-token.png").default} alt="Copy Token" width="400"/>

:::note
If you lose the token, you’ll need to delete it and create a new one.
:::

## Use the App Token

You can now use the token in place of your password when connecting:

- WebDAV
- External apps
- Third-party services

## Delete the App Token

If a token is no longer needed:

- Go back to the App Tokens section.
- Click the trash icon next to the token to remove it.

This ensures unused tokens cannot be misused.

:::note
Use App Tokens for better security and control when connecting external services.
:::
