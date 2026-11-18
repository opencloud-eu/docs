---
sidebar_position: 0
id: roles-overview
title: Roles
---

# Roles

OpenCloud uses different role models for different areas of the system. User roles, Space roles, and Share roles are separate from each other and control different permissions.

## Access Methods

People can access content in different ways:

- Public links provide access to anyone who has the link, subject to the link's permissions and optional protection.
- [Guest Access](../sharing/guest-access.md) gives an invited external recipient access through their email address without creating a regular OpenCloud account.
- Regular OpenCloud accounts authenticate as users and have a system-wide User role.

These access methods are not User roles. For help choosing an access method, see [Sharing Methods](../sharing/index.md#sharing-methods).

User roles define what a regular account can do across OpenCloud. They control system-wide capabilities, such as administering users or Spaces and creating shares.

Space roles define what a member can do inside a specific Space. They control access to Space content and Space management options.

Share roles define what a recipient can do with a shared file or folder. Public links use their own link permissions, which are separate from Share roles. Share roles do not change the user's role in OpenCloud or their role inside a Space.

These permission concepts complement each other. A Space role or Share role does not remove restrictions imposed by a system-wide User role.

## In this section

- [User roles](./user-roles.md)  
  Learn about system-wide user roles in OpenCloud, including Admin, Space Admin, User, and User Light.

- [Space roles](./space-roles.md)  
  Understand the permissions available for members inside a Space, including Can View, Can Edit, and Can Manage.

- [Share roles](./share-roles.md)  
  Review the access levels available for shared files and folders.
