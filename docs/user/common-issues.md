---
sidebar_position: 10
id: common-issues
title: Common Issues & Help
description: Common issues & help
draft: false
---

# Common Issues & Help

## Symlinks are not synchronized with the Desktop Client

### Problem

Symbolic links (symlinks) are not synchronized by the OpenCloud Desktop Client. Users often wonder why linked folders or files are missing or not accessible.

### Reasoning

Symlinks are deliberately excluded from synchronization for several important reasons:

- Not portable: Symlinks often point to paths that only exist on the original machine. On another device, the target path likely doesn't exist.
- Not usable in the web interface: The web interface cannot interpret or display symlinks.
- Problematic on Windows: Symlink support on Windows is limited and inconsistent.
- Risk of circular references: Symlinks could point to each other in loops, causing infinite synchronization cycles.
- Loss of identity: If the client were to follow the link and synchronize the target, it would become a regular copy of the data. The original nature of the symlink would be lost.

### Solution

Sync Folders Outside the Sync Root Using Symlinks

If you want to synchronize a folder that is located outside your sync root, you can still achieve this by moving the folder into your sync root and replacing the original location with a symlink.

#### Example

You want to synchronize the folder `/foo/A`, but your sync root is `/home/bar/OpenCloud/Personal`.

1. Move the folder into your sync root:

   ```bash
   mv /foo/A /home/bar/OpenCloud/Personal/foo/A
   ```

## Files with "~$" in the name will not be synchronized

The OpenCloud Desktop Client does not synchronize files starting with `~$`, such as `~$document.docx`.  
These files are temporary lock files created by Microsoft Office applications (Word, Excel, PowerPoint) while a document is open.

<img src={require("./img/common-issues/desktop-excluded.png").default} alt="Show the ~$ file is excluded from synchronizing" width="500"/>

They are not actual content files but serve as internal markers to prevent multiple users from editing the same document simultaneously.  
Once the file is closed, the `~$` file is automatically removed by Office.

For more details, see Microsoft’s explanation:  
[Description of how Word creates temporary files](https://support.microsoft.com/en-us/topic/description-of-how-word-creates-temporary-files-66b112fb-d2c0-8f40-a0be-70a367cc4c85)
