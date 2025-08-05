---
sidebar_position: 4
id: keycloak-user
title: adding user with keycloak
description: Adding user with Keycloak
draft: false
---

# Creating New Users in Keycloak for OpenCloud

This guide explains how to create new users in Keycloak for OpenCloud, including guest users without personal spaces. While OpenCloud currently does not have a built-in "invite external user" feature, this functionality can be replicated using Keycloak.

## Background

One of the most frequently requested features by administrators has been support for guest or external users. Previously, this was discussed as adding external users during the sharing process. These users were provisioned on the fly and received an invite link.

Although OpenCloud does not natively support this method, similar functionality can be achieved using Keycloak for user management.

## Step 1: Assign Admin Permissions in Keycloak

To manage users and groups for OpenCloud, you need a user with administrative privileges in the Keycloak realm.

1. Log in to Keycloak as an admin.
2. Navigate to the OpenCloud realm:  
   [https://keycloak.keycloak-daily.opencloud.rocks/admin/openCloud/console/#/openCloud](https://keycloak.keycloak-daily.opencloud.rocks/admin/openCloud/console/#/openCloud)
3. Assign appropriate roles (such as `realm-admin`) to the user you want to promote.

> Example: A user named `dennis` is assigned as a Realm Admin.

Once assigned, the user can log in as a Realm Administrator and access user and group management.

## Step 2: Add New Users or Groups

With admin permissions, you can now create users and groups:

- Navigate to the Users section in the Keycloak Admin Console.
- Click Add User.
- Fill in the required user details (e.g., username, email).
- Optionally assign the user to one or more groups.
- Assign roles to define their access level.

### Recommended Role: `OpenCloudGuest`

Assigning the `OpenCloudGuest` role ensures that the user does not receive a personal space in OpenCloud. This setup is ideal for guest or lightweight accounts.

## Step 3: Configure User Settings

Once the user is created, you can define mandatory actions:

- Set an initial password.
- Require the user to update their profile on first login.
- Require email verification.

These actions can be set under the User Settings > Required Actions section.

## First Login Experience for Guest Users

When a guest user logs in for the first time, they will:

1. Be prompted to change their password.
2. Update their profile (name, email, etc.).
3. Verify their email address.

After successful login, they will not receive a personal space — fulfilling the guest user requirement.

## Optional: Enable Self Registration

You can allow users to register themselves without manual creation.

To enable self-registration:

1. Go to the Login settings in the OpenCloud realm.
2. Enable the User Registration option.

### Self Registration Flow

- Users see a Register option on the login screen.
- They complete the registration form.
- After submission, they receive a verification email.
- Once verified, they can log in with their credentials.

## Summary

By leveraging Keycloak:

- You can create and manage guest users for OpenCloud.
- Guest users can log in without receiving a personal space.
- You can streamline the process with self-registration.

This setup provides a flexible and scalable way to manage external and lightweight users in OpenCloud through Keycloak.
