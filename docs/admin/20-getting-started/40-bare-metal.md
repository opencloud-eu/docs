---
sidebar_position: 4
id: bare-metal
title: Bare-Metal
description: "Manual, minimalist setup with essential features."
---

## User Guide for Installing OpenCloud
Follow the steps below to install and configure OpenCloud on your system.<br/>
This example is on Linux Ubuntu 24.04 distribution!

---

### 1. Install Git and clone the repository

- Open a terminal.

- Update your package list:
   ```bash
   sudo apt update && upgrade
   ```
   <img src={require("./img/bare-metal/apt-update-&&-upgrade.png").default} alt="sudo apt" width="1920"/>

- Install Git using the following command:
   ```bash
   sudo apt install git
   ```
   <img src={require("./img/bare-metal/install-git.png").default} alt="install git" width="1920"/>

- Clone the OpenCloud repository:
   ```bash
   git clone https://github.com/opencloud-eu/opencloud.git
   ```
   <img src={require("./img/bare-metal/git-clone.png").default} alt="git clone" width="1920"/>

---

### 2. Update system and install required packages

- Install the golang package:
   ```bash
   sudo apt install golang -y
   ```
   <img src={require("./img/bare-metal/install-golang.png").default} alt="install golang" width="1920"/>

- Install npm (Node Package Manager):
   ```bash
   sudo apt install npm -y
   ```
   <img src={require("./img/bare-metal/install-npm.png").default} alt="install npm" width="1920"/>

- Install corepack globally:
   ```bash
   sudo npm install -g corepack
   ```
   <img src={require("./img/bare-metal/install-corepack.png").default} alt="install corepack" width="1920"/>

- Enable `pnpm` using corepack:
   ```bash
   corepack enable pnpm
   ```
   <img src={require("./img/bare-metal/corepack-enable.png").default} alt="corepack enable" width="1920"/>

---

### 3. Build process and OpenCloud initialization

- Navigate to the OpenCloud directory:
   ```bash
   cd opencloud
   ```
   <img src={require("./img/bare-metal/cd-opencloud.png").default} alt="cd opencloud" width="1920"/>
   
- Run the generate process:
   ```bash
   make clean generate
   ```
   <img src={require("./img/bare-metal/make-clean-generate.png").default} alt="make clean generate" width="1920"/>

- Navigate to the OpenCloud subdirectory:
   ```bash
   cd opencloud
   ``` 
   <img src={require("./img/bare-metal/cd-opencloud-subdirectory.png").default} alt="cd opencloud subdirectory" width="1920"/>

- Build OpenCloud:
   ```bash
   make clean build
   ```
   <img src={require("./img/bare-metal/make-clean-build.png").default} alt="make clean build" width="1920"/>

- Initialize OpenCloud with insecure configuration and set an admin password:
   ```bash
   ./bin/opencloud init --insecure true --admin-password admin
   ```
   <img src={require("./img/bare-metal/opencloud-init.png").default} alt="opencloud init" width="1920"/>

- Start the OpenCloud server:
   ```bash
   ./bin/opencloud server
   ```
   <img src={require("./img/bare-metal/opencloud-server.png").default} alt="opencloud server" width="1920"/>

---

### 4. Login

Login with your browser:
- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: **admin**
- password: **admin**

<img src={require("./img/bare-metal/login.png").default} alt="login" width="1920"/>

--- 

### 5. Conclusion

Your OpenCloud server is now running and ready to use 🚀

---

### If you encounter any issues or errors, try finding a solution here: 
- [Common Issues & Help](./../50-resources/30-common-issues.md)