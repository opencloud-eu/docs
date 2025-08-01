---
sidebar_position: 4
id: keycloak-user
title: adding user with keycloak
description: Adding user with Keycloak
draft: true
---

# Creating New Users in Keycloak for OpenCloud

This guide explains how to create new users in Keycloak for OpenCloud, including "User Light" without personal spaces. While OpenCloud currently does not have a built-in "invite external user" feature, this functionality can be replicated using Keycloak.

## Background

One of the most frequently requested features by administrators has been support for guest or external users. Previously, this was discussed as adding external users during the sharing process. These users were provisioned on the fly and received an invite link.

Although OpenCloud does not natively support this method, similar functionality can be achieved using Keycloak for user management.

## Assign Admin Permissions in Keycloak

To manage users and groups for OpenCloud, you need a user with administrative privileges in the Keycloak realm.

- Log in to Keycloak as an admin.
- Navigate to the OpenCloud realm
- Assign appropriate roles (such as `manage-user` and `view-users`) to the user you want to promote.

Example: A user named `dennis` is assigned as a Realm Admin.

<img src={require(".././img/keycloak/add-user/set-admin-roles.png").default} alt="Add admin roles to user" width="1920"/>

Once assigned, the user can log in as a Realm Administrator and access user and group management.

## Add New User with standard rights (no Space)

With admin permissions, you can now create users and groups:

- Login in Keycloak with the user who has admin rights

- Navigate to the "Users" section in the Keycloak Admin Console

- Click Add User
  <img src={require(".././img/keycloak/add-user/add-user.png").default} alt="Add user" width="1920"/>

- Fill in the required user details (e.g., username, email)
  <img src={require(".././img/keycloak/add-user/fill-out-userinfo.png").default} alt="Fill out user information" width="1920"/>

- Optionally assign the user to one or more groups.

- Click on "Create"

- Set an inital password

<img src={require(".././img/keycloak/add-user/set-password.png").default} alt="Set initial user password" width="1920"/>

## First Login Experience for the "User Light"

When a "User Light" logs in for the first time, they will:

- Be prompted to change their password
- Update their profile (name, email, etc.)
- Verify their email address

if this was set before.

After successful login, they will not receive a personal space — fulfilling the guest user requirement.

<img src={require(".././img/keycloak/add-user/guest-login.png").default} alt="Guest login" width="1920"/>

## Optional: Enable Self Registration

You can allow users to register themselves without manual creation.

To enable self-registration:

- Log in to Keycloak as an admin.
- Go to the Login settings in the OpenCloud realm.
- Enable the User Registration option.

<img src={require(".././img/keycloak/add-user/enable-self-registration.png").default} alt="Enable self registration" width="1920"/>

### Self Registration Flow

- Users see a Register option on the login screen.

<img src={require(".././img/keycloak/add-user/register-button.png").default} alt="Register Button" width="1920"/>

- They complete the registration form.

<img src={require(".././img/keycloak/add-user/fill-out-registration-form.png").default} alt="Fill out the registration form" width="1920"/>

After loggin in, the user has now the "User Light" Role with no personal Space.

## Summary

By leveraging Keycloak:

- You can create and manage guest users for OpenCloud.
- Guest users can log in without receiving a personal space.
- You can streamline the process with self-registration.

This setup provides a flexible and scalable way to manage external and lightweight users in OpenCloud through Keycloak.
