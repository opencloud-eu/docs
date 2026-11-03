---
sidebar_position: 0
id: sharing-overview
title: Share files and folders
---

# Share files and folders

This section explains how sharing works in OpenCloud. It covers internal sharing with members and groups, public links for external access, File Drop links for receiving uploads, and sharing with users on other OpenCloud instances through ScienceMesh.

## Sharing Methods

Choose a sharing method based on who needs access and how long the collaboration will continue.

| Feature           | Public Link                            | Guest Access                                               | Regular Account                  |
| :---------------- | :------------------------------------- | :--------------------------------------------------------- | :------------------------------- |
| Typical use       | One-time file exchange                 | Ongoing collaboration with an external partner             | Regular team collaboration       |
| Access            | Shared link                            | Personal, single-use invitation sent by email              | Account authentication           |
| Identification    | No individual recipient identification | Guest's email address                                      | User directory                   |
| Expiration        | Optional link expiration               | Fixed link lifetime; configurable session and share expiry | Account lifecycle                |
| Supported clients | Web                                    | Web                                                        | Web, desktop, and mobile clients |
| Personal data     | None required                          | Email address                                              | Directory profile                |

Guest Access must be enabled by an administrator and does not create a regular OpenCloud account. An invitation link is valid for 30 minutes, and the default guest-session lifetime is 24 hours. Administrators can configure the session lifetime, and guests can renew an expired session by email.

Public link permissions, Guest Access Share roles, and permissions assigned to regular accounts are separate concepts. For an overview, see [Roles](../roles/index.md).

## In this section

- [Internal sharing](./internal.md)  
  Share files and folders with members or groups within your organization.

- [External sharing](./external.md)  
  Create public links and manage options such as permissions, passwords, and expiry dates.

- [Guest Access](./guest-access.md)
  Invite external guests by email address and assign access to shared content.

- [File Drop](./file-drop.md)  
  Allow external users to upload files without giving them access to existing content.

- [ScienceMesh](./opencloud-mesh.md) - Connect with users on another OpenCloud instance and share files or folders with them.
