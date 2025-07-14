---
sidebar_position: 5
id: bare-metal
title: Bare-Metal
description: 'Manual, minimalist setup with essential features.'
---

## User Guide for Installing OpenCloud

Follow the steps below to install and configure OpenCloud on your system.<br/> This example is on Linux Ubuntu 24.04
distribution!

:::danger[Disclaimer] Bare-metal deployments are not officially supported by OpenCloud. They are great for quick
evaluation but are undocumented and have a minimalist feature set. If you choose this setup, you are on your own. With
great power comes great responsibility. :::

---

### 1. Install Git and clone the repository

- Open a terminal.

- Update your package list:

  ```shell
  sudo apt update && apt upgrade
  ```

- Install Git using the following command:

  ```shell
  sudo apt install git
  ```

  <img src={require("./../img/bare-metal/install-git.png").default} alt="install git" width="1920"/>

- Clone the OpenCloud repository:

  ```shell
  git clone https://github.com/opencloud-eu/opencloud.git
  ```

  <img src={require("./../img/bare-metal/git-clone.png").default} alt="git clone" width="1920"/>

---

### 2. Install the required packages

- Download and install Go by following the official guide: 🔗[**go.dev/doc/install**](https://go.dev/doc/install)

- Install npm (Node Package Manager):

  ```shell
  sudo apt install npm -y
  ```

  <img src={require("./../img/bare-metal/install-npm.png").default} alt="install npm" width="1920"/>

- Install corepack globally:

  ```shell
  sudo npm install -g corepack
  ```

  <img src={require("./../img/bare-metal/install-corepack.png").default} alt="install corepack" width="1920"/>

- Enable `pnpm` using corepack:

  ```shell
  corepack enable pnpm
  ```

  <img src={require("./../img/bare-metal/corepack-enable.png").default} alt="corepack enable" width="1920"/>

---

### 3. Build process and OpenCloud initialization

- Navigate to the OpenCloud directory:

  ```shell
  cd opencloud
  ```

  <img src={require("./../img/bare-metal/cd-opencloud.png").default} alt="cd opencloud" width="1920"/>

- Run the build generate process:

  ```shell
  make clean generate
  make -C opencloud build
  ```

- Initialize OpenCloud with insecure configuration and set an admin password:

  ```shell
  ./bin/opencloud init --insecure true --admin-password admin
  ```

  <img src={require("./../img/bare-metal/opencloud-init.png").default} alt="opencloud init" width="1920"/>

- Start the OpenCloud server:

  ```shell
  ./bin/opencloud server
  ```

  <img src={require("./../img/bare-metal/opencloud-server.png").default} alt="opencloud server" width="1920"/>

---

### 4. Login

Login with your browser:

- [https://localhost:9200](https://localhost:9200)
- user: **admin**
- password: **admin**

<img src={require("./../img/bare-metal/login.png").default} alt="login" width="1920"/>

---

### 5. Conclusion

Your OpenCloud server is now running and ready to use 🚀

---

### If you encounter any issues or errors, try finding a solution here

- [Common Issues & Help](./../../resources/common-issues.md)
