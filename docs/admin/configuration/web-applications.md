---
sidebar_position: 11
id: web-applications
title: Web Apps
description: How to enable web applications in OpenCloud.
draft: false
---

# Web Applications

Administrators have the ability to provide additional web applications to their users. This feature is especially useful for organizations that want to integrate third-party tools or provide internally developed apps within the OpenCloud environment.

## Installing a Web Application

You can install a web application in just a few steps:

### Open the App Store

Use the Application Switcher in the top navigation bar of OpenCloud and navigate to the App Store.

<img src={require("./img/app-store.png").default} alt="App Store" width="1920"/>

### Download the Application

Find and download the application you want to install.

### Extract and copy

Unzip the downloaded archive and copy the extracted folder into the web application directory.  
By default, this path is:

```bash
opencloud-compose/config/opencloud/apps
```

### Access in OpenCloud

Once the app is copied to the correct location, it will automatically appear in the OpenCloud interface.

## Configure a Web Application

Some OpenCloud apps require additional configuration — for example, the External Sites app.

These configurations can be managed in the following file:

```bash
opencloud-compose/config/opencloud/apps/external-sites/manifest.json
```

:::note
Configuration details vary between apps.
For specific setup instructions, please refer to the official documentation of the respective app.
:::
