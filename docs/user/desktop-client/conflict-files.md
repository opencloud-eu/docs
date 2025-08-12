---
sidebar_position: 10
id: file-conflicts
title: Handle file conflicts
description: How to handle file conflicts
draft: false
---

# Handle file conflicts in the OpenCloud Desktop Client

When files are modified both locally and remotely before synchronization, the Desktop Client creates "conflicted copy" files—examples include:

- `conflict.txt` (remote version)
- `conflict (conflicted copy YYYY-MM-DD HHMMSS).txt` (local version)

  <img src={require("./img/conflict-files/conflict-file.png").default} alt="Conflict files in explorer" width="1920"/>

This usually happens when:

- Your local copy and the server copy diverge simultaneously,
- and the app cannot automatically merge changes.

## How You’ll Be Notified

In the Desktop Client overview, a notification will appear when conflicting files are detected.  
This means that multiple versions of the same file exist—often because changes were made on different devices before synchronization.  
The notification serves as a prompt for you to review the conflicts and decide how to merge or keep the versions.

<img src={require("./img/conflict-files/conflict-info.png").default} alt="Notification about file conflicts in the Desktop Client" width="500"/>

## Resolve File Conflicts Manually

To resolve a conflict:

- Open both files (the original and the conflicted copy).
- Manually compare and merge the differences.
- Edit the base file (`conflict.txt`) to include both sets of changes if needed.
- After merging, delete the conflicted copy file.
- Leave the updated base file—sync will now continue as normal.

## Good Practices to Prevent Conflicts

- Avoid editing the same file simultaneously on multiple devices.
- Always wait for sync completion before making local changes.

## Why Conflict Files Appear

The Desktop Client determines a conflict when:

- Local and remote versions of a file both change since the last sync.
- Content is compared using file IDs and checksums—not only timestamps.
- The client preserves both versions by renaming the local file with `"(conflicted copy ...)"`.

Conflict files are created locally; they do not appear on the server unless explicitly uploaded.

If you're experiencing frequent conflicts—especially on simple edits—it’s likely due to permission issues, read-only files, or syncing the same files via other tools. Check logs and file attributes accordingly.
