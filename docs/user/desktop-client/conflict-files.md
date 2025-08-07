---
sidebar_position: 10
id: file-conflicts
title: Handle file conflicts
description: How to handle file conflicts
draft: true
---

# Handle file conflicts in the OpenCloud Desktop Client

When files are modified both locally and remotely before synchronization, the Desktop Client creates "conflicted copy" files—examples include:

- `conflict.txt` (remote version)
- `conflict (conflicted copy YYYY-MM-DD HHMMSS).txt` (local version)

  <img src={require("./img/conflict-files/conflict-file.png").default} alt="Choose what to sync" width="400"/>

This usually happens when:

- Your local copy and the server copy diverge simultaneously,
- and the app cannot automatically merge changes.

## How You’ll Be Notified


## Resolve File Conflicts Manually

To resolve a conflict:

1. Open both files (the original and the conflicted copy).
2. Manually compare and merge the differences.
3. Edit the base file (`conflict.txt`) to include both sets of changes if needed.
4. After merging, delete the conflicted copy file.
5. Leave the updated base file—sync will now continue as normal.

## Optional: Upload Conflict Copies Automatically (Experimental)

By default, conflicted copy files are kept locally and not uploaded to the server. The reasoning is to avoid confusion—since only the file author knows which version is correct.

To enable automatic upload of these conflict copies (so both versions are visible on the server), set the following environment variable:

## ✅ Good Practices to Prevent Conflicts

- Avoid editing the same file simultaneously on multiple devices.
- Always wait for sync completion before making local changes.
- Keep system clocks synchronized (use NTP) to avoid timestamp mismatches that can trigger conflicts :contentReference[oaicite:1]{index=1}.

## Why Conflict Files Appear

Under the hood, the Desktop Client determines a conflict when:

- Local and remote versions of a file both change since the last sync.
- Content is compared using file IDs and checksums—not only timestamps :contentReference[oaicite:2]{index=2}.
- The client preserves both versions by renaming the local file with `"(conflicted copy ...)"`.

Conflict files are **created locally**; they do not appear on the server unless explicitly uploaded.

## 🧩 Summary Table

| Situation                     | What happens                                       |
|------------------------------|----------------------------------------------------|
| Local and remote change same file | Conflict copy created and sync paused        |
| Conflict resolution performed | Sync resumes with final merged file              |
| Automatic upload enabled     | Conflict copy also uploaded to server            |
| Conflict unresolved          | Conflict badge appears until local resolution     |

--- 

If you're experiencing frequent conflicts—especially on simple edits—it’s likely due to permission issues, read-only files, or syncing the same files via other tools. Check logs and file attributes accordingly.
::contentReference[oaicite:3]{index=3}










Sources

Ask ChatGPT
