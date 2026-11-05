---
sidebar_position: 10
id: user-roles
title: User roles in OpenCloud
description: User roles in OpenCloud
draft: false
---

# User Roles in OpenCloud

| Role        | can be Space Manager | Personal Space | create/delete Spaces | manage Users and Groups |
| :---------- | :------------------: | :------------: | :------------------: | :---------------------: |
| User Light  |          x           |       -        |          -           |            -            |
| User        |          x           |       x        |          -           |            -            |
| Space Admin |          x           |       x        |          x           |            -            |
| Admin       |          x           |       x        |          x           |            x            |

## User Light

A User Light has limited access and does not have a personal Space by default.

A User Light can:

- Be added as a member to a Space
- Be assigned a role in a Space

:::note
If a user previously had the role User or higher and is later changed back to User Light, they keep their existing personal Space.
:::

## User

A User has the same Space membership options as User Light and also has a personal Space for their own files and folders.

A User can:

- Create files and folders in their personal Space
- Upload and manage their own data

## Space Admin

A Space Admin has the same permissions as a User and can also manage Spaces on an administrative level.

A Space Admin can:

- Create, delete, enable, and disable Spaces
- Rename Spaces
- Adjust Space quotas
- Manage Spaces without accessing their content

Space Admins can manage the Space itself, even if they are not members of the Space. This includes administrative actions such as enabling, disabling, deleting, renaming, or changing the quota of a Space.

Space Admins cannot access the files inside a Space unless they have been added to the Space with the required Space role. They also cannot add or remove Space members unless they have the "Can manage" role in that Space.

## Admin

An Admin has the highest administrative role in OpenCloud. Admins have Space Admin permissions and can also manage users, groups, and system settings.

An Admin can:

- Create and delete local users
- Create and delete local groups
- Edit user details, such as names, email addresses, and roles
- Add users to groups or remove users from groups
- Disable user accounts to prevent login
