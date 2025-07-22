---
sidebar_position: 4
id: keycloak
title: Keycloak
description: 'OpenCloud with Keycloak.'
draft: true
---

# Keycloak Integration

## Enable Keycloak

To enable Keycloak for identity and access management, uncomment the following lines in your `.env` file

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

## Starting OpenCloud

After starting OpenCloud, Keycloak will be available at

```bash
https://keycloak.your.domain
```

## Initial User Setup in Keycloak

Once Keycloak is running

### Open your browser and go to

```bash
https://keycloak.your.domain
```

<img src={require("./../../img/docker-compose/keycloak-dashboard.png").default} alt="Keyclosk dashboard" width="1920"/>

### Log in with the admin credentials (default is admin / admin)

<img src={require("./../../img/docker-compose/keycloak-login.png").default} alt="Keycloak login" width="1920"/>

### In the top-left dropdown (labeled Keycloak), switch to the OpenCloud realm

<img src={require("./../../img/docker-compose/top-left-dropdown.png").default} alt="Top left dropdown menue" width="400"/>

### Navigate to the "Users" section and click "Add user"

<img src={require("./../../img/docker-compose/users-section.png").default} alt="User section" width="1920"/>

- Fill in a username
- Optionally add email, first/last name
- Click "Create"
  <img src={require("./../../img/docker-compose/fill-in-userdata.png").default} alt="Fill in userdata" width="1920"/>

### Go to the "Credentials" tab

- Click "Set password"
  <img src={require("./../../img/docker-compose/credentials.png").default} alt="Credentials" width="1920"/>
  <br/>
- Set a temporary password
- Enable "Temporary" to force password change on first login (optional)
- Click "Save"
  <img src={require("./../../img/docker-compose/set-password.png").default} alt="Set password" width="400"/>

### Go to the "Role Mapping" tab

<img src={require("./../../img/docker-compose/role-mapping.png").default} alt="Role mapping" width="1920"/>

- Click "Assign role"
  <img src={require("./../../img/docker-compose/assign-role.png").default} alt="Assign role" width="1920"/>

- In the dialog, click "Filter by realm roles"
  <img src={require("./../../img/docker-compose/filter-by-realm-roles.png").default} alt="Filter by realm roles" width="1920"/>

- Choose the appropriate role (e.g., user, admin, etc.)
- Click "Assign"
  <img src={require("./../../img/docker-compose/realm-roles.png").default} alt="Realm roles" width="1920"/>

The user can now log in via OpenCloud using the Keycloak credentials.
