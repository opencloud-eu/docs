---
sidebar_position: 70
id: collabora
title: Collabora additional fonts
description: How to add additional fonts to Collabora.
draft: false
---

# Installing Additional Fonts for Collabora

By default, Collabora Online provides only a limited set of fonts.  
To ensure proper document rendering — especially for Microsoft Office documents — you may want to install additional font packages such as `ttf-mscorefonts` or other TrueType/OpenType fonts on your server.

## 1. Access the Server and Update System Packages

Before installing new fonts, make sure your system packages are up to date:

```bash
apt update
```

## 2. Install Microsoft Core Fonts

Install the Microsoft Core Fonts package to add common fonts such as Arial or Comic Sans MS:

```bash
apt install ttf-mscorefonts-installer
```

During the installation, you will be prompted to accept the EULA (End User License Agreement).

<img src={require("./img/collabora/accept-eula.png").default} alt="Accept EULA" width="1920"/>

## 3. Restart Collabora

After the installation is complete, restart your docker-compose setup to apply the changes:

```bash
docker compose restart
```

Once restarted, Collabora will recognize the newly installed fonts, and they will be available when editing documents.

<img src={require("./img/collabora/new-fonts.png").default} alt="New Fonts added" width="1920"/>
