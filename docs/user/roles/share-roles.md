---
sidebar_position: 3
id: share-roles
title: Share roles in OpenCloud
description: Share roles in OpenCloud
draft: false
---

# Share Roles in OpenCloud

Share Roles define what recipients can do with individual shared files and folders.

| Share Role        | Access                                                        |
| :---------------- | :------------------------------------------------------------ |
| Can view (secure) | Restricted browser viewer with watermarks; no download        |
| Can view          | View and download                                             |
| Can upload        | View, download, and upload; available for shared folders only |
| Can edit          | View, download, upload, edit, add, and delete                 |

The available Share Roles can depend on the resource type and the OpenCloud configuration.

:::note

Public links use separate link permissions, such as `Can view`, `Can edit`, and `File Drop (secret)`. They are not Share Roles. For more information, see [Public links](../sharing/external.md).

:::

## Can View (Secure)

The `Can view (secure)` role allows recipients to view supported files in a restricted viewer.

Recipients with this role can:

- View documents, images, and PDF files
- View files with a watermark

Recipients with this role cannot upload, edit, add, or delete files and folders.

## Can View

The `Can view` role allows recipients to view shared files and folders.

Compared with `Can view (secure)`, recipients with this role can view shared content without the restricted viewer and watermark.

Recipients with this role cannot upload, edit, add, or delete files and folders.

## Can Upload

The `Can upload` role is available for shared folders. It allows recipients to view and download existing content and upload new files.

Recipients with this role cannot edit or delete existing content.

## Can Edit

The `Can edit` role includes the permissions of `Can view` and allows recipients to modify shared content.

Recipients with this role can:

- Upload files
- Create files and folders
- Edit files and folders
- Delete files and folders
