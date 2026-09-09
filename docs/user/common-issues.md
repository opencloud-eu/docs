---
sidebar_position: 110
id: common-issues
title: Common Issues & Help
description: Common issues & help
draft: false
toc_max_heading_level: 2
---

# Common Issues & Help

## Desktop Client cannot establish a connection

### Problem

After entering the OpenCloud server address, the browser does not open. The Desktop Client window may flicker and its memory usage may increase.

### Cause

This can happen when the OpenCloud instance is accessed through an external reverse proxy that interferes with the connection or server discovery request.

### Solution

Contact your OpenCloud administrator and ask them to verify the reverse proxy configuration. Administrators can find troubleshooting steps under [Desktop Client cannot connect through an external reverse proxy](../admin/resources/common-issues.md#desktop-client-cannot-connect-through-an-external-reverse-proxy).

## Symlinks are not synchronized with the Desktop Client

### Problem

Symbolic links (symlinks) are not synchronized by the OpenCloud Desktop Client. Users often wonder why linked folders or files are missing or not accessible.

### Cause

Symlinks are deliberately excluded from synchronization for several important reasons:

- Not portable: Symlinks often point to paths that only exist on the original machine. On another device, the target path likely doesn't exist.
- Not usable in the web interface: The web interface cannot interpret or display symlinks.
- Problematic on Windows: Symlink support on Windows is limited and inconsistent.
- Risk of circular references: Symlinks could point to each other in loops, causing infinite synchronization cycles.
- Loss of identity: If the client were to follow the link and synchronize the target, it would become a regular copy of the data. The original nature of the symlink would be lost.

### Solution

#### Sync folders outside the sync root using symlinks

If you want to synchronize a folder that is located outside your sync root, you can still achieve this by moving the folder into your sync root and replacing the original location with a symlink.

#### Example

You want to synchronize the folder `/foo/A`, but your sync root is `/home/bar/OpenCloud/Personal`.

1. Move the folder into (a sub-folder of) your sync root:

   ```bash
   mkdir -p /home/bar/OpenCloud/Personal/foo/
   mv /foo/A /home/bar/OpenCloud/Personal/foo/A
   ```

2. Create a symlink in the original place:

   ```bash
   ln -s /home/bar/OpenCloud/Personal/foo/A /foo/A
   ```

## Files with "~$" in the name will not be synchronized

### Problem

The OpenCloud Desktop Client does not synchronize files starting with `~$`, such as `~$document.docx`.

<img src={require("./img/common-issues/desktop-excluded.png").default} alt="Show the ~$ file is excluded from synchronizing" width="500"/>

### Cause

These files are temporary lock files created by Microsoft Office applications while a document is open. They are internal markers that prevent multiple users from editing the same document simultaneously, rather than content files.

### Solution

Close the document in Microsoft Office. Office automatically removes the corresponding `~$` file.

For more details, see the [Microsoft support article on temporary Office lock files created by Word/Excel/PowerPoint](https://support.microsoft.com/en-gb/topic/-the-document-is-locked-for-editing-by-another-user-error-message-when-you-try-to-open-a-document-in-word-10b92aeb-2e23-25e0-9110-370af6edb638?).
