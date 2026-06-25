---
sidebar_position: 4
id: sync-settings-win
title: Synchronisation Settings in Windows
description: Synchronisation Settings in Windows
draft: false
---

# Windows: Synchronization Settings

The OpenCloud Desktop Client uses the Windows Virtual File System (VFS) to integrate your cloud data directly into the File Explorer.  
Files and folders appear in the system without needing to be fully downloaded, saving local disk space.

## File States

Files and folders can appear in different states, depending on whether they are stored locally or only available online.

### Always available on this device (full pinned)

- Stored locally and always accessible offline.
- Windows will not remove the file automatically.

<img src={require(".././img/vfs/full-pinned.png").default} alt="full pinned file icon" width="400"/>

### Available on this device (full)

- Downloaded and accessible offline.
- Can be removed by Windows if disk space is needed.
- Newly created or added files automatically receive this state.

<img src={require(".././img/vfs/full.png").default} alt="full file icon" width="400"/>

### Available when online (placeholder)

- Shown in File Explorer but stored only in the cloud.
- Downloaded automatically when opened; requires an internet connection.

<img src={require(".././img/vfs/placeholder.png").default} alt="placeholder file icon" width="400"/>

## Making Items Available Offline

To store a file, folder, or Space locally:

1. Right-click the item in File Explorer.
2. Select “Always keep on this device”.

<img src={require(".././img/vfs/always-keep-on-this-device.png").default} alt="select always keep on this device" width="400"/>

## Freeing Up Disk Space

To remove local copies while keeping them visible in File Explorer:

1. Right-click the item.
2. Select “Free up space”.

<img src={require(".././img/vfs/free-up-space.png").default} alt="select free up space" width="400"/>

## Accessing Files

- Online-only items are downloaded automatically when opened.
- Changes are synced back to OpenCloud.

:::note
An internet connection is required for online-only files.
:::
