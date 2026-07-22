---
sidebar_position: 60
id: not-allowed-upload-files
title: Files Not Allowed for Upload
description: Learn what happens when the Desktop Client cannot upload certain files.
draft: false
---

# Files Not Allowed for Upload

Some files cannot be uploaded or synchronized to OpenCloud. This can happen, for example, when a file does not meet the naming rules, contains unsupported characters, or is blocked by server-side restrictions.

When the Desktop Client detects a file that is not allowed to be uploaded, the file is not uploaded to OpenCloud.

## What happens to these files?

Files that are not allowed to be uploaded are moved to the local trash or recycle bin of your operating system.

This means:

- The file is removed from the local sync folder.
- The file is not uploaded to OpenCloud.
- The file is not available in the web interface.
- The file may still be recoverable from the local trash or recycle bin.

## Why is the file moved to the trash?

Moving the file to the local trash prevents the Desktop Client from repeatedly trying to upload a file that OpenCloud does not accept.

This also helps avoid recurring synchronization errors caused by the same file.

## Where can I find the file?

Depending on your operating system, you may be able to restore the file from the local trash or recycle bin:

- **Windows**: Recycle Bin
- **macOS**: Trash
- **Linux**: Trash, or the trash location used by your desktop environment

## Recommended action

If a file was moved to the trash because it could not be uploaded:

1. Open the local trash or recycle bin of your operating system.
2. Restore the file if you still need it.
3. Check whether the file name, file path, or file type is allowed.
4. Rename or adjust the file if necessary.
5. Move the file back into the sync folder.

After the file has been adjusted, the Desktop Client can try to synchronize it again.

:::important

Before emptying your local trash or recycle bin, check whether it contains files that were moved there by the Desktop Client.

:::

:::note

Files that are not allowed to be uploaded are handled locally by the Desktop Client. They are not stored in OpenCloud unless they are successfully synchronized.

:::
