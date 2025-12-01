---
sidebar_position: 3
id: web-dav
title: WebDAV
description: Connect to a Space via WebDAV
draft: false
---

# Connect to a Space via WebDAV

With WebDAV, you can connect OpenCloud Spaces and Folders as network drives on your device and manage your files directly from your file manager — without using the browser.

## Prerequisites

- A valid OpenCloud account with WebDAV information enabled in the preferences
- Access to a resource in OpenCloud, either a Space, a Folder or the root of your account
- A WebDAV client (e.g. built-in OS support or [Mountain Duck](https://mountainduck.io/))
- (Optional but recommended) An App Token  
  → [How to create an App Token](/docs/user/admin/app-tokens)

## Step-by-Step Guide

### Enable WebDAV Info in the UI

To display WebDAV information for your Spaces:

- Go to Account Settings
- Enable "Show WebDAV info in details view"

  <img src={require("./img/webdav/preferences.png").default} alt="Enable WebDAV info" width="1920"/>

### Create an App Token (if required)

Some WebDAV clients (especially non-OIDC compatible ones like Mountain Duck) require an App Token for authentication.

:::note
We recommend using an App Token instead of your password for better security.
:::

- Go to Settings > App Tokens
- Click "+ New", give it a name, and set an expiration date
- Copy the token immediately – it will only be shown once  
  → [See App Token Guide](/docs/user/admin/app-tokens)

### Get the WebDAV URL

Open the info panel of the resource you want to access in the OpenCloud Web Interface.

You’ll see a section labeled WebDAV — copy the full WebDAV URL. It looks like:

`https://cloud.example.com/remote.php/dav/spaces/12345678-abcd-efgh-ijkl-987654321000/`

<img src={require("./img/webdav/webdav-url.png").default} alt="WebDAV URL" width="1920"/>

### Connect via WebDAV

Now connect your device using the WebDAV URL:

- Username: your OpenCloud username
- Password: your App Token (or password, if allowed)

You can use various clients depending on your operating system:

## Windows

- Open File Explorer → Click on “This PC” → Choose “Map network drive”
- Enter the WebDAV URL
- Authenticate with username and App Token

## macOS

- In Finder, choose “Go” > “Connect to Server…”
- Enter the WebDAV URL
- Login with your credentials or App Token

## Linux

- Use your file manager’s “Connect to Server” option
- Format the URL as:  
  `davs://cloud.example.com/remote.php/dav/spaces/<SPACE-ID>/`

:::note
Once connected, your Space will behave like a normal folder.
:::

:::note

- If your WebDAV client supports OIDC, you may not need an App Token
- Always use `https://` to ensure secure access
- App Tokens can be revoked anytime via your account settings

  :::
