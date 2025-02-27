---
sidebar_position: 1
id: bare-metal
title: Quickstart Bare - Metal
---
<br/><br/>

## User Guide for Installing OpenCloud
Follow the steps below to install and configure OpenCloud on your system.<br/>
This example is on Linux Ubuntu 24.04 distribution!
<br/><br/>

---

### 1. Install Git and clone the repository

- Open a terminal.

- Update your package list:
   ```bash
   sudo apt update && upgrade
   ```
   <img src={require("./img/bare-metal/apt-update-&&-upgrade.png").default} alt="sudo apt" width="1920"/>
<br/><br/>

- Install Git using the following command:
   ```bash
   sudo apt install git
   ```
   <img src={require("./img/bare-metal/install-git.png").default} alt="enter URL" width="1920"/>
<br/><br/>

- Clone the OpenCloud repository:
   ```bash
   git clone https://github.com/opencloud-eu/opencloud.git
   ```
   <img src={require("./img/bare-metal/git-clone.png").default} alt="enter URL" width="1920"/>
<br/><br/>

---

### 2. Update system and install required packages

- Install the golang package:
   ```bash
   sudo apt install golang -y
   ```
   <img src={require("./img/bare-metal/install-golang.png").default} alt="enter URL" width="1920"/>
<br/><br/>

- Install npm (Node Package Manager):
   ```bash
   sudo apt install npm -y
   ```
   <img src={require("./img/bare-metal/install-npm.png").default} alt="enter URL" width="1920"/>
<br/><br/>

- Install corepack globally:
   ```bash
   sudo npm install -g corepack
   ```
   <img src={require("./img/bare-metal/install-corepack.png").default} alt="enter URL" width="1920"/>
<br/><br/>

- Enable `pnpm` using corepack:
   ```bash
   corepack enable pnpm
   ```
   <img src={require("./img/bare-metal/corepack-enable.png").default} alt="enter URL" width="1920"/>
<br/><br/>

---

### 3. Build process and OpenCloud initialization

- Navigate to the OpenCloud directory:
   ```bash
   cd opencloud
   ```
   <img src={require("./img/bare-metal/cd-opencloud.png").default} alt="enter URL" width="1920"/>
<br/><br/>

- Run the generate process:
   ```bash
   make clean generate
   ```
   <img src={require("./img/bare-metal/make-clean-generate.png").default} alt="enter URL" width="1920"/>
<br/><br/>

- Navigate to the OpenCloud subdirectory:
   ```bash
   cd opencloud
   ``` 
   <img src={require("./img/bare-metal/cd-opencloud-subdirectory.png").default} alt="enter URL" width="1920"/>
<br/><br/>

- Build OpenCloud:
   ```bash
   make clean build
   ```
   <img src={require("./img/bare-metal/make-clean-build.png").default} alt="enter URL" width="1920"/>
<br/><br/>

- Initialize OpenCloud with insecure configuration and set an admin password:
   ```bash
   ./bin/opencloud init --insecure true --admin-password admin
   ```
   <img src={require("./img/bare-metal/opencloud-init.png").default} alt="enter URL" width="1920"/>
<br/><br/>

- Start the OpenCloud server:
   ```bash
   ./bin/opencloud server
   ```
   <img src={require("./img/bare-metal/opencloud-server.png").default} alt="enter URL" width="1920"/>
<br/><br/>

---

### 4. Login

Login with your browser:
- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: **admin**
- password: **admin**

<img src={require("./img/bare-metal/login.png").default} alt="Admin general" width="1920"/>
<br/><br/>

--- 

### 5. Conclusion

Your OpenCloud server is now running and ready to use 🚀
<br/><br/>

---

### If you encounter any issues or errors, try finding a solution here: 
- [Common Issues & Help](./common-issues.md)