---
sidebar_position: 4
id: bare-metal
title: Quickstart Bare - Metal
---

**User Guide for Installing OpenCloud**

Follow the steps below to install and configure OpenCloud on your system.

---

### Step 1: Install Git and Clone the Repository

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

---

### Step 2: Update System and Install Required Packages

1. Install the Golang package:
   ```bash
   sudo apt install golang -y
   ```

2. Install Node.js:
   ```bash
   sudo apt install nodejs -y
   ```

3. Install npm (Node Package Manager):
   ```bash
   sudo apt install npm -y
   ```

4. Install Corepack globally:
   ```bash
   sudo npm install -g corepack
   ```

5. Enable `pnpm` using Corepack:
   ```bash
   corepack enable pnpm
   ```

---

### Step 3: Build Process and OpenCloud Initialization

1. Navigate to the OpenCloud directory:
   ```bash
   cd opencloud
   ```

2. Run the clean build process:
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

---

### Conclusion

Your OpenCloud server is now running and ready for use 🚀