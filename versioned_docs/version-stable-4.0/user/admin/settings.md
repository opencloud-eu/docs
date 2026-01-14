---
sidebar_position: 1
id: settings
title: Settings
description: Settings
draft: false
---

# Admin area overview

In the admin area of OpenCloud you have extensive administration options for your organisation. Here are the most important areas:

<img src={require("./img/settings/admin_settings.png").default} alt="Admin settings" width="400"/>

## General

- Overview of the version:  
  In the General section, you can view information about your current OpenCloud version and see whether a newer version is available.  
  <img src={require("./img/settings/admin_general.png").default} alt="Admin general" width="1920"/>

:::note
The version check may have been disabled by an administrator.  
If this option is turned off, information about newer versions will not be displayed.
:::

## Users

- Overview of users:  
  Here you have an overview of all users of your OpenCloud.
- Manage users:  
  Depending on your user management settings, you can:
  - Create or delete users
  - Edit users (e.g. change rights or settings)
  - Change quota (storage space) of users
  - Add or remove users in groups
  - Allow or prohibit logins (for individual users)
    <img src={require("./img/settings/admin_users.png").default} alt="Admin users" width="1920"/>

## Groups

- Overview of the groups:  
  Here you can view the existing groups of your OpenCloud.
- Manage groups:  
  You can create, edit or delete local groups and add or remove members.
- Imported groups:  
  External groups that have been imported via an external user management system can not be edited here. These groups are labeled with a lock symbol to indicate that they are locked.
  <img src={require("./img/settings/admin_groups.png").default} alt="Admin groups" width="1920"/>

## Spaces

- Overview of the Spaces:  
  Here you can see all existing Spaces in your OpenCloud.
- Space management:  
  As an administrator, you have full rights to:
  - Edit
  - Deactivate or activate
  - Delete
    <img src={require("./img/settings/admin_spaces.png").default} alt="Admin spaces" width="1920"/>
