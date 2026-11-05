---
sidebar_position: 30
id: share-roles
title: Share roles in OpenCloud
description: Share roles in OpenCloud
draft: false
---

# Share Roles in OpenCloud

| Role              | view | upload | edit | add | delete | only view doc, img, pdf with watermark |
| :---------------- | :--: | :----: | :--: | :-: | :----: | :------------------------------------: |
| can view (secure) |  -   |   -    |  -   |  -  |   -    |                   x                    |
| can view          |  x   |   -    |  -   |  -  |   -    |                   -                    |
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

## Can Edit

The `can edit` role includes the permissions of `can view` and allows recipients to modify shared content.

Recipients with this role can:

- Upload files
- Create files and folders
- Edit files and folders
- Delete files and folders
