---
sidebar_position: 10
id: settings
title: Settings
description: Settings
draft: false
---

# Admin area overview

The admin area of OpenCloud provides the main tools for managing your organization. It is available only to users with the administrator role. Other users do not see Admin Settings in the app switcher.

To open the admin area, select the app switcher in the upper-right corner and then select “Admin Settings”. The most important areas are shown below.

<img src={require("./img/settings/admin_settings.png").default} alt="Admin settings" width="1920"/>

## General

- Version overview:  
  In the General section, you can view your current OpenCloud version and check whether a newer version is available.
- Announcement banner:
  Administrators can display an organization-wide message to all users. For configuration instructions, see [Announcement Banner](../../admin/configuration/announcement-banner.md).
  <img src={require("./img/settings/admin_general.png").default} alt="General administration settings" width="1920"/>

:::note
If a security-critical upgrade is available, administrators may also see a warning in the lower-left corner of the web interface.
An administrator may disable the version check. If this option is turned off, information about newer versions will not be displayed.
:::

## Users

- User overview:  
  Here you can see all users in your OpenCloud instance.
- User management:  
  Depending on your user management settings, you can:
  - create or delete users
  - edit users, for example change rights or settings
  - change user quotas
  - add or remove users from groups
  - allow or block logins for individual users
    <img src={require("./img/settings/admin_users.png").default} alt="Admin users" width="1920"/>

:::note
If OpenCloud is connected to an external IdP, you can still see the users here, but user management must be done in the IdP.
:::

## Groups

- Group overview:  
  Here you can see the existing groups in your OpenCloud instance.
- Group management:  
  You can create, edit, or delete local groups and add or remove members.
- Imported groups:  
  External groups that were imported through an external user management system cannot be edited here. These groups are marked with a lock symbol to show that they are locked.
  <img src={require("./img/settings/admin_groups.png").default} alt="Admin groups" width="1920"/>

## Spaces

- Space overview:  
  Here you can see all existing Spaces in your OpenCloud instance.
- Space management:  
  As an administrator, you can:
  - rename Spaces
  - customize descriptions, subtitles, images, and icons
  - change Space quotas
  - deactivate or activate Spaces
  - delete disabled Spaces
    <img src={require("./img/settings/admin_spaces.png").default} alt="Admin spaces" width="1920"/>

## Apps

- App overview:
  Here you can see installed apps, their versions, compatible OpenCloud versions, and their current status.
  <img src={require("./img/settings/admin_apps.png").default} alt="Admin apps" width="1920"/>
