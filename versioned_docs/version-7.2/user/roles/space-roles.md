---
sidebar_position: 20
id: space-roles
title: Space roles in OpenCloud
description: Space roles in OpenCloud
draft: false
---

# Space Roles in OpenCloud

In a Space, members can have different roles. Each role defines what a member can do within that Space.

| Role       | view | download | upload | edit | add | delete | manage members | disable / enable Space | edit quota | delete Space |
| :--------- | :--: | :------: | :----: | :--: | :-: | :----: | :------------: | :--------------------: | :--------: | :----------: |
| can view   |  x   |    x     |   -    |  -   |  -  |   -    |       -        |           -            |     -      |      -       |
| can edit   |  x   |    x     |   x    |  x   |  x  |   x    |       -        |           -            |     -      |      -       |
| can manage |  x   |    x     |   x    |  x   |  x  |   x    |       x        |           x            |     x      |      -       |

## Can View

The `can view` role allows members to view and download files in the Space.

Members with this role cannot upload, create, edit, or delete files and folders.

## Can Edit

The `can edit` role includes the permissions of `can view` and allows members to work with content in the Space.

Members with this role can:

- Upload files to the Space
- Create files and folders
- Edit files and folders
- Delete files and folders, including their history
- Restore deleted files

## Can Manage

The `can manage` role includes the permissions of `can edit` and allows members to manage the Space.

Members with this role can:

- Add members to the Space
- Remove members from the Space
- Change the roles of other Space members
- Enable and disable the Space
- Edit the Space quota

:::note
Members with the `can manage` role can manage a Space, but they cannot delete it.

Deleting a Space requires the OpenCloud user role `Admin` or `Space Admin`. For more information, see [User roles in OpenCloud](./user-roles.md).
:::
