---
sidebar_position: 2
id: desktop-client-symlinks
title: Symlinks are not synchronized
description: Understand how the Desktop Client handles symbolic links
draft: false
hide_table_of_contents: true
---

# Symlinks are not synchronized with the Desktop Client

## Problem

Symbolic links (symlinks) are not synchronized by the OpenCloud Desktop Client. Linked folders or files may be missing or inaccessible.

## Cause

Symlinks are deliberately excluded from synchronization for several reasons:

- Not portable: Symlinks often point to paths that only exist on the original machine. On another device, the target path likely doesn't exist.
- Not usable in the web interface: The web interface cannot interpret or display symlinks.
- Problematic on Windows: Symlink support on Windows is limited and inconsistent.
- Risk of circular references: Symlinks could point to each other in loops, causing infinite synchronization cycles.
- Loss of identity: If the client followed the link and synchronized the target, it would become a regular copy of the data and lose its original nature as a symlink.

## Solution

### Sync folders outside the sync root using symlinks

To synchronize a folder outside your sync root, move the folder into the sync root and replace its original location with a symlink.

#### Example

You want to synchronize the folder `/foo/A`, but your sync root is `/home/bar/OpenCloud/Personal`.

1. Move the folder into a subfolder of your sync root:

   ```bash
   mkdir -p /home/bar/OpenCloud/Personal/foo/
   mv /foo/A /home/bar/OpenCloud/Personal/foo/A
   ```

2. Create a symlink in the original location:

   ```bash
   ln -s /home/bar/OpenCloud/Personal/foo/A /foo/A
   ```
