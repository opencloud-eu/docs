---
sidebar_position: 2
id: docker-compose
title: Docker Compose
description: "🌟 Full-blown featureset including web office."
---

# OpenCloud with Docker Compose

Install a internet facing OpenCloud with SSL certification with Docker Compose.

This installation documentation is for **Ubuntu and Debian** systems. The software can also be installed on other Linux distributions, but the commands and package managers may differ.

## **Prerequisites**

- **Four domains** pointing to your server:
  - `cloud.YOUR.DOMAIN` → OpenCloud frontend
  - `collabora.YOUR.DOMAIN` → Collabora Online Server
  - `wopiserver.YOUR.DOMAIN` → WOPI server for document editing
  - `traefik.YOUR.DOMAIN` → Traefik dashboard

  Alternatively, you can use a wildcard domain (`*.YOUR.DOMAIN`)
- A **hosted server** (e.g., Hetzner, AWS, or your own VPS) with Linux and SSH access

---

## 1. Connect to Your Server
Log into your server via SSH:

```bash
ssh root@YOUR.SERVER.IP
```

## 2. Install Docker
Update your system and install Docker.


First, perform an update and upgrade:

```bash
apt update && apt upgrade -y
```
Install Docker following the [official Docker guide](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

Once Docker is installed, enable and start the service:

```bash
systemctl enable docker && systemctl start docker
```

## 3. Clone the OpenCloud Repository
Download the necessary configuration files:

```bash
git clone https://github.com/opencloud-eu/opencloud.git
```

## 4. Configure the .env File for Staging Certificates
Before requesting real SSL certificates, test the setup with Let's Encrypt’s staging environment.

Navigate to the OpenCloud configuration folder:

```bash
cd opencloud/deployments/examples/opencloud_full
```

Edit the `.env` file with the editor of your choice:

In our example we use nano

```bash
nano .env
```

Modify these settings:

### ✅ Disable insecure mode
```bash
# INSECURE=true
```

### ✅ Set your domain names
```bash
TRAEFIK_DOMAIN=traefik.YOUR.DOMAIN
OC_DOMAIN=cloud.YOUR.DOMAIN
COLLABORA_DOMAIN=collabora.YOUR.DOMAIN
WOPISERVER_DOMAIN=wopiserver.YOUR.DOMAIN
```

### ✅ Set your admin password
```bash
ADMIN_PASSWORD=YourSecurePassword
```

### ✅ Set your email for SSL certification
```bash
TRAEFIK_ACME_MAIL=your@email.com
```

### ✅ Use Let's Encrypt staging certificates (for testing)
```bash
TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory
```

Save and exit.

### 🚨 Production Setup Consideration

:::caution Production Setup Recommended

By default, OpenCloud stores configuration and data inside internal Docker volumes.  
This works fine for local development or quick evaluations — **but is not suitable for production environments**.

:::

#### 📦 Mount Persistent Volumes

In production, you should mount persistent local directories for configuration and data to ensure:

- Data durability
- Easier backups and recovery
- Full control over storage location and permissions

Update your `.env` file with custom paths:

```env
OC_CONFIG_DIR=/your/local/path/opencloud/config
OC_DATA_DIR=/your/local/path/opencloud/data
```

:::tip Folder Permissions

Ensure these folders exist and are owned by user and group 1000:1000, which the Docker containers use by default:

```bash
sudo mkdir -p /your/local/path/opencloud/{config,data}
sudo chown -R 1000:1000 /your/local/path/opencloud
```
::: 

If these variables are left unset, Docker will use internal volumes, which **do not persist** if the containers are removed — not recommended for real-world use.

:::caution Security Warning

The user with UID 1000 on your host system will have full access to these mounted directories. This means that any local user account with this ID can read, modify, or delete OpenCloud config and data files.

This can pose a security risk in shared or multi-user environments. Make sure to implement proper user and permission management and consider isolating access to these directories.

:::


## 5. Start OpenCloud
Launch OpenCloud using Docker Compose:

```bash
docker compose up -d
```

This will start all required services in the background.

## 6. Verify SSL Certification

In your web browser, visit:

```bash
https://cloud.YOUR.DOMAIN
```

You should see a security warning because the staging certificate is not fully trusted.
Same should appear with the other domains you are using.

Example with Chrome browser:

<img src={require("./../img/docker-compose/certificate-details.png").default} alt="Certificate Details" width="500"/>


✅ Check the certificate details to confirm it’s from Let's Encrypt Staging. 

<img src={require("./../img/docker-compose/certificate-viewer.png").default} alt="Certificate Details" width="500"/>
<img src={require("./../img/docker-compose/subordinate-ca's.png").default} alt="Certificate Details" width="500"/>

## 7. Apply a Real SSL Certificate
Once the staging certificate works, switch to a production certificate.

### Steps:
#### 1️⃣ Stop Docker Compose
```bash
docker compose down
```

#### 2️⃣ Remove old staging certificates
```bash
docker volume rm opencloud_full_certs
```

(If you changed volume names, adjust accordingly.)

#### 3️⃣ Disable staging mode in `.env`
```bash
nano .env
```

Comment the staging server:
```bash
# TRAEFIK_ACME_CASERVER=https://acme-staging-v02.api.letsencrypt.org/directory
```

#### 4️⃣ Restart OpenCloud with a real SSL certificate
```bash
docker compose up -d
```

✅ Now, visiting `https://cloud.YOUR.DOMAIN` should show a secure connection with a valid SSL certificate.

<img src={require("./../img/docker-compose/status-secure.png").default} alt="Certificate Details" width="1920"/>

## 8. Log into OpenCloud
Open a browser and visit:

```bash
https://cloud.YOUR.DOMAIN
```

Login with:

**Username:** `admin`

**Password:** (your password)

<img src={require("./../img/docker-compose/login.png").default} alt="Admin general" width="1920"/>

## Troubleshooting
If you encounter any issues, check the [Common Issues & Help](./../../resources/common-issues.md)

---

## Enable Keycloak Integration (optional)
<br/>

#### To enable Keycloak for identity and access management, **uncomment** the following lines in your `.env` file:

```env
LDAP=:ldap.yml
LDAP_MANAGER_DOMAIN=ldap.your.domain
LDAP_ADMIN_PASSWORD="your.save.password"
KEYCLOAK=:keycloak.yml
KEYCLOAK_DOMAIN=keycloak.your.domain
KEYCLOAK_ADMIN_USER="your.username"
KEYCLOAK_ADMIN_PASSWORD="your.save.password"
```

This will include the LDAP and Keycloak service definitions in the Docker Compose setup.

#### After starting OpenCloud, Keycloak will be available at:

```bash
https://keycloak.your.domain
```


## 👤 Initial User Setup in Keycloak
### Once Keycloak is running:

**1. Open your browser and go to**
```bash
https://keycloak.your.domain
```
<img src={require("./../img/docker-compose/keycloak-dashboard.png").default} alt="Keyclosk dashboard" width="1920"/>
<br/><br/>

**2. Log in with the admin credentials (default is admin / admin).**
<img src={require("./../img/docker-compose/keycloak-login.png").default} alt="Keycloak login" width="1920"/>
<br/><br/>

**3. In the top-left dropdown (labeled Keycloak), switch to the OpenCloud realm.**
<img src={require("./../img/docker-compose/top-left-dropdown.png").default} alt="Top left dropdown menue" width="400"/>
<br/><br/>

**4. Navigate to the "Users" section and click "Add user":**
<img src={require("./../img/docker-compose/users-section.png").default} alt="User section" width="1920"/>
<br/>
- Fill in a username
- Optionally add email, first/last name
- Click "Create"
<img src={require("./../img/docker-compose/fill-in-userdata.png").default} alt="Fill in userdata" width="1920"/>
<br/><br/>

**5. Go to the "Credentials" tab:**
- Click "Set password"
<img src={require("./../img/docker-compose/credentials.png").default} alt="Credentials" width="1920"/>
<br/>
- Set a temporary password
- Enable "Temporary" to force password change on first login (optional)
- Click "Save"
<img src={require("./../img/docker-compose/set-password.png").default} alt="Set password" width="400"/>
<br/><br/>

**6. Go to the "Role Mapping" tab:**
<img src={require("./../img/docker-compose/role-mapping.png").default} alt="Role mapping" width="1920"/>
<br/>
- Click "Assign role"
<img src={require("./../img/docker-compose/assign-role.png").default} alt="Assign role" width="1920"/>
<br/>
- In the dialog, click "Filter by realm roles"
<img src={require("./../img/docker-compose/filter-by-realm-roles.png").default} alt="Filter by realm roles" width="1920"/>
<br/>
- Choose the appropriate role (e.g., user, admin, etc.)
- Click "Assign"
<img src={require("./../img/docker-compose/realm-roles.png").default} alt="Realm roles" width="1920"/>
<br/>

**The user can now log in via OpenCloud using the Keycloak credentials.**