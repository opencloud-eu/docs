---
sidebar_position: 4
id: bare-metal
title: Quickstart Bare - Metal
---
<br/><br/>

## User Guide for Installing OpenCloud
Follow the steps below to install and configure OpenCloud on your system.
<br/><br/>

---

### Step 1: Install Git and clone the repository

1. Open a terminal.
2. Update your package list:
   ```bash
   sudo apt update
   ```
3. Install Git using the following command:
   ```bash
   sudo apt install git
   ```
4. Clone the OpenCloud repository:
   ```bash
   git clone https://github.com/opencloud-eu/opencloud.git
   ```
<br/><br/>

---

### Step 2: Update system and install required packages

1. Install the golang package:
   ```bash
   sudo apt install golang -y
   ```

2. Install npm (Node Package Manager):
   ```bash
   sudo apt install npm -y
   ```

3. Install corepack globally:
   ```bash
   sudo npm install -g corepack
   ```

4. Enable `pnpm` using corepack:
   ```bash
   corepack enable pnpm
   ```
<br/><br/>

---

### Step 3: Build process and OpenCloud initialization

1. Navigate to the OpenCloud directory:
   ```bash
   cd opencloud
   ```

2. Run the clean generate process:
   ```bash
   make clean generate
   ```

3. Build OpenCloud:
   ```bash
   make clean build
   ```

4. Initialize OpenCloud with insecure configuration and set an admin password:
   ```bash
   ./bin/opencloud init --insecure true --admin-password admin
   ```

5. Start the OpenCloud server:
   ```bash
   ./bin/opencloud server
   ```
<br/><br/>

---

### 4. Login

Login with your browser:
- [https://cloud.opencloud.test](https://cloud.opencloud.test)
- user: **admin**
- password: **admin**

Congratulations! You’ve successfully set up and launched OpenCloud! Happy hacking!

<img src={require("./img/bare-metal/login.png").default} alt="Admin general" width="1920"/>
<br/><br/>

--- 

### Conclusion

Your OpenCloud server is now running and ready for use 🚀