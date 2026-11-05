---
sidebar_position: 30
id: share-roles
title: Share roles in OpenCloud
description: Share roles in OpenCloud
draft: false
---

# Share Roles in OpenCloud

:::note

Share roles also apply to [Guest Access](../sharing/guest-access.md). An invited guest can receive `Can view (secure)`, `Can view`, `Can upload`, or `Can edit`, depending on the resource type and the OpenCloud configuration. Guest Access is an access method, not a separate User role.

:::

| Role              | view | upload | edit | add | delete | only view doc, img, pdf with watermark |
| :---------------- | :--: | :----: | :--: | :-: | :----: | :------------------------------------: |
| can view (secure) |  -   |   -    |  -   |  -  |   -    |                   x                    |
| can view          |  x   |   -    |  -   |  -  |   -    |                   -                    |
| can upload        |  x   |   x    |  -   |  -  |   -    |                   -                    |
| can edit          |  x   |   x    |  x   |  x  |   x    |                   -                    |

## Can View Secure

The `can view (secure)` role allows recipients to view supported files in a restricted viewer.

Recipients with this role can:

- View documents, images, and PDF files
- View files with a watermark

Recipients with this role cannot upload, edit, add, or delete files and folders.

## Can View

The `can view` role allows recipients to view shared files and folders.

Compared with `can view (secure)`, recipients with this role can view shared content without the restricted viewer and watermark.

Recipients with this role cannot upload, edit, add, or delete files and folders.

## Can Upload

The `can upload` role is available for shared folders. It allows recipients to view and download existing content and upload new files.

Recipients with this role cannot edit or delete existing content.

## Can Edit

The `can edit` role includes the permissions of `can view` and allows recipients to modify shared content.

Recipients with this role can:

- Upload files
- Create files and folders
- Edit files and folders
- Delete files and folders
