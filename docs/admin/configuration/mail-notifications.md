---
sidebar_position: 9
id: mail-notificatons
title: Mail Notifications
description: "How to activate mail notifications in OpenCloud."
draft: true
---

# Mail notifications in OpenCloud

## This guide shows how to configure your OpenCloud instance to send notification E-Mails by modifying the `.env` file in your OpenCloud setup.

---

### 🛠️ Step 1: Open the .env File

Edit the file with your preferred text editor:

```bash
nano .env
```

Or use vim, code, or gedit as you prefer.

---

### 📝 Step 2: Add or Modify These Environment Variables

Change the following lines in the .env file.

SMTP Settings:

```env
SMTP_HOST=mailhog
SMTP_PORT=1025
SMTP_SENDER=noreply@your.text
SMTP_USERNAME=YOUR_USERNAME
SMTP_PASSWORD=YOUR_PASSWORD
SMTP_TRANSPORT_ENCRYPTION=none
SMTP_INSECURE=true
```
⚠️ In the .env file, values should be written without quotation marks. Do not use 'single quotes' or "double quotes" — just enter the plain value.

---

### 💾 Step 3: Save and Exit

For nano, press Ctrl + O to save and Ctrl + X to exit.

---

### 🔄 Step 4: Restart OpenCloud

Apply the changes by restarting the OpenCloud services:

```bash
docker compose down 
docker compose up -d
```

---

OpenCloud is now successfully configured to deliver notification emails, including those triggered by actions such as file sharing.