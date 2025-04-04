---
sidebar_position: 11
id: traefik-dashboard
title: "Traefik-Dashboard"
---

# Traefik-Dashboard

## Here we explain how you can activate the Traefik dashboard in the .env file so that you can access it via the browser.

---

### ✅ Enable the Traefik-Dashboard and set the Traefik-Domain

The Traefik-Dashboard must be activated in the .env file.

Open the .env with an editor e.g. nano

```bash
nano .env
```
<br/>

In the .env file the following lines must be enabled, set to true and set the domain:

```Shell
TRAEFIK_DASHBOARD=true
TRAEFIK_DOMAIN=traefik.your_domain
```
The traefik-domain starts with "traefik." and ends after the dot with your domain.

---

### ✅ Create a bcrypt passwort-hash for Traefik-Dashboard

To log in to the Traefik dashboard, a bcrypt hash must be created for the password to be assigned.

```bash
echo $(htpasswd -nB user) | sed -e s/\\$/\\$\\$/g
```
For "user", the username to be used for the login must be entered.
<br/>

In the next step, a password must be selected and entered a second time for confirmation (in our example wie use as "username" "admin").<br/>
Subsequently, a line is output with username and the hashed password. This line must be copied complete.<br/>

<img src={require("./img/traefik-dashboard/bcrypt-password-hash.png").default} alt="Certificate Details" width="500"/>
<br/><br/>

In our example, the row to be copied looks like this:

```Shell
admin:$$2y$$05$$ilHtPf3ieC.ihMPTeXQmy.klOLLw/HqNAKT6JPFJsVdcArXUrgxbW
```
<br/>

The copied "username-password-line" must now be entered in the .env-file.

```bash
nano .env
```

```Shell
TRAEFIK_BASIC_AUTH_USERS=
```

In our example, the entry looks this:

```Shell
TRAEFIK_BASIC_AUTH_USERS=admin:$$2y$$05$$ilHtPf3ieC.ihMPTeXQmy.klOLLw/HqNAKT6JPFJsVdcArXUrgxbW
```

After saving the new entries in the .env-file you must be restart docker.

---

### ✅ Traefik-Dashboard in Browser

- Open a browser and enter your traffic domain.<br/>
- Then enter your username and password (the password must be entered in plain text for registration).
- After this the Traefik-Dashboard opens.

<img src={require("./img/traefik-dashboard/traefik-dashboard.png").default} alt="Certificate Details" width="1920"/>