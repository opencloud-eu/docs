---
sidebar_position: 4
id: win-vfs
title: Windows VFS
description: Windows Virtual File System
draft: false
---

# Windows Virtual File System (VFS)

The OpenCloud Desktop Client uses the Windows Virtual File System (VFS) to integrate your cloud data directly into the Windows File Explorer.  
VFS displays all files and folders without requiring them to be stored locally.

VFS is **always enabled** on Windows and cannot be turned off, as it is required for the native Windows integration.

## File States

Files and folders can appear in different states, depending on whether they are stored locally or only available online.

### Always available on this device (full pinned)

The item is stored locally and always accessible, even without an internet connection.  
Windows will not automatically remove it.

<img src={require("./img/vfs/full-pinned.png").default} alt="full pinned file icon" width="400"/>

### Available on this device (full)

The item is downloaded and available offline.  
If disk space is needed, Windows may remove the local copy. The file remains listed and can be downloaded again at any time.

Files that are newly created or added on the device will receive this state automatically.

<img src={require("./img/vfs/full.png").default} alt="full file icon" width="400"/>

### Available when online (placeholder)

The item is shown in the File Explorer but stored only in the cloud.  
It will be downloaded automatically when opened and requires an active internet connection.

<img src={require("./img/vfs/placeholder.png").default} alt="placeholder file icon" width="400"/>

## Making Items Available Offline

To ensure a file, folder, or Space is stored locally:

1. Open the Windows File Explorer.
2. Right-click the item.
3. Select “Always keep on this device”.

<img src={require("./img/vfs/always-keep-on-this-device.png").default} alt="select always keep on this device" width="400"/>

Windows downloads the selected content and keeps it available offline.

## Freeing Up Disk Space

If you need to remove local copies:

1. Open the Windows File Explorer.
2. Right-click the file or folder.
3. Select “Free up space”.

<img src={require("./img/vfs/free-up-space.png").default} alt="select free up space" width="400"/>

The local version is removed, but the item remains visible and can be downloaded again when needed.

## Accessing Files

Online-only items can be opened normally. The Desktop Client downloads them automatically and syncs any changes back to OpenCloud.

:::note
An internet connection is required when opening items that are not stored locally.
:::

## Storage Behavior

Windows manages disk space automatically:

- Items set to online-only free up local storage.
- Depending on system settings, unused content may be switched back to online-only automatically.
