---
sidebar_position: 1
id: user-roles
title: User roles in OpenCloud
---

## User Roles in OpenCloud

| Role          | Personal Space | create Spaces | can be Space Manager | manage Users and Groups |
| :------------ | :------------: | :-----------: | :------------------: | :---------------------: |
| Administrator |       x        |       x       |          x           |            x            |
| Space Admin   |       x        |       x       |          x           |            -            |
| User          |       x        |       -       |          x           |            -            |
| User Light    |       -        |       -       |          x           |            -            |

### Administrator

The Administrator role in OpenCloud has the same abilities as a Space Admin but in addition it has special permissions
to manage users, groups, and system settings. However, administrators do not have direct access to Space data or the
ability to add users to Spaces where they don't have the "can manage" role. Below are the key actions an administrator
can perform:

- #### Create and Delete local Users & Groups

  Administrators can add new local users and remove existing local users from the system. They can also create and
  delete local groups to organize users efficiently.

- #### Edit Users & Groups

  User details such as names, emails, and roles can be modified. Groups can be updated by adding or removing members as
  needed.

- #### Prevent Login

  If necessary, administrators can disable user accounts, preventing them from logging in. This is useful for security
  reasons or when an account is no longer needed.

- #### Manage Spaces (without Access to Space Data)

  Administrators can manage Spaces like enable, disable or delete them and rename it or adjust the quota, even if they
  don't have the "can manage" role. However, they cannot access the files inside a Space or add members to it.

- #### Change the Logo

  The system logo can be updated to reflect the company branding. This can be done in the Admin Settings under the
  "General" section.

### Space Admin

A Space Admin has the highest level of control over Spaces. They can:

- Create and manage Spaces
- Be assigned the "Can Edit" role in Spaces they didn’t create
- Have a personal Space where they can create files, folders, and upload data

### User

A regular User has access to their own Space and can be part of other Spaces. They can:

- Create files and folders in their personal Space
- Upload and manage their own data
- Be added as a member to a Space
- Can have the "Can Edit" role in a Space

### User Light

A User Light has limited access and does not have their own personal Space. They can:

- Be added as a member to a Space
- Can have the "Can Edit" role in a Space
- They do not have a personal Space
