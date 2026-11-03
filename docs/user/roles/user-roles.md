---
sidebar_position: 1
id: user-roles
title: User roles in OpenCloud
description: User roles in OpenCloud
draft: false
---

# User Roles in OpenCloud

| Role        | can receive Can manage | Personal Space | create/delete Spaces | manage Users and Groups |
| :---------- | :--------------------: | :------------: | :------------------: | :---------------------: |
| User Light  |           x            |       -        |          -           |            -            |
| User        |           x            |       x        |          -           |            -            |
| Space Admin |           x            |       x        |          x           |            -            |
| Admin       |           x            |       x        |          x           |            x            |

## User Light

A User Light is a regular OpenCloud account with restricted system-wide permissions and does not have a personal Space by default.

A User Light can:

- Be added as a member to a Space
- Be assigned a role in a Space
- Work with content according to the assigned Space or Share Role, subject to the restrictions below

The following restrictions currently apply:

- A User Light cannot create internal shares with users or groups, even when assigned `Can manage` in the Space.
- A User Light can create public links when public links are available and the permissions for the resource allow it.
- A User Light cannot assign `Can manage` to another Space member, even when assigned `Can manage` themselves.

:::caution

If only User Light accounts retain `Can manage`, it may not be possible for them to restore `Can manage` to another member. Keep at least one Space member with the User, Space Admin, or Admin User Role and the `Can manage` Space Role.

:::

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
