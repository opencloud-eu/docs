---
sidebar_position: 80
id: locked-files
title: Locked files
description: When files in OpenCloud can be locked, when they are unlocked again, and what this means for users.
---

# Locked files

OpenCloud can temporarily mark files as locked or unavailable. For users, this usually means the file cannot be opened, edited, saved, or synchronized as usual while the lock is active.

A file can be locked for different reasons. Common causes are an active Office editing session or processing after upload.

## When can a file be locked?

A file can be locked when:

- it is open or being edited in an integrated Office app
- several users are working on the same Office file at the same time
- an Office editing session has not ended cleanly yet
- an upload is still being processed, for example by a virus scan
- a WebDAV client has locked it, for example a desktop Office application that opens files via WebDAV or the macOS Finder

## Office editing

Office files can be locked while they are being edited.

This typically applies to files such as:

- `.odt`
- `.ods`
- `.odp`
- `.docx`
- `.xlsx`
- `.pptx`

While the file is being edited, the lock protects it from conflicting writes. This helps prevent changes from being overwritten by other write operations.

When several users edit the same Office file together, the file can still be technically locked. In that case, the lock does not block collaboration inside the Office app. It only prevents external write access while the session is active.

## WebDAV clients

Applications that access OpenCloud via WebDAV can lock files as well. Examples are desktop Office applications that open files via WebDAV or the macOS Finder. While such a lock is active, other users and applications cannot change the file.

## Processing after upload

Depending on the server configuration, OpenCloud processes a file after upload before it becomes available. While this processing is running, the file cannot be opened or downloaded.

Processing steps can include:

- a virus scan
- checks against policies defined by the administrator

## When is a file unlocked?

When a lock is released depends on its cause.

### Office editing

- The lock is released when the last user closes the document or the browser tab.
- While the document is open, the Office app renews the lock regularly. The lock therefore stays active as long as someone is working on the document.
- If the editing session does not end cleanly, for example because the browser crashed or the network connection was lost, the lock expires automatically after 30 minutes at the latest.

### Processing after upload

- The file is unlocked as soon as all processing steps have finished. This usually takes only a few seconds.
- There is no fixed time limit. If a processing step fails, OpenCloud repeats it automatically after an increasing waiting time.
- If the step still fails after the maximum number of attempts, processing is aborted and the upload is reverted. A new file disappears from the folder again. If an existing file was overwritten, it returns to its previous version. Users therefore do not see a locked file, but the upload is missing or their changes are not saved.
- If the virus scan detects malware, the result depends on the server configuration:
  - The file is deleted. This is the default.
  - The file is kept for inspection by an administrator, but it is not added to the folder.
  - The file is marked as infected but is available as usual.

### WebDAV clients

The lock is released when the WebDAV client closes the file and removes the lock, or when the lock time set by the client expires.

## What does a lock look like?

Depending on the situation, a locked file may:

- show a lock icon or processing status
- be unavailable for editing
- fail to save changes
- open read-only
- be temporarily unavailable
- show an error when opening or saving

## What can users do?

In many cases the lock is temporary. Users can:

1. wait until the processing of an upload has finished
2. reload the file list
3. check whether the file is still open in another browser tab
4. check whether the file is open on another device
5. check whether a sync client is currently uploading or synchronizing the file
6. close the Office file and open it again
7. upload the file again if an upload is missing or changes were not saved after the upload

Office files are unlocked automatically after 30 minutes at the latest, even if an editing session was not closed cleanly.

If the file stays locked for a longer time, an administrator should check the cause.

## When should an admin check?

An administrator should check when:

- an Office file is still locked more than 30 minutes after all users have closed it
- an uploaded file stays in the processing state
- uploads disappear again or changes are reverted after the upload
- several files are affected
- users cannot save even though they have editing rights
- the file is blocked for all users

If the processing of an upload has failed, an administrator can list the upload sessions and restart a failed upload. First list the upload sessions and identify the ID of the failed upload:

```bash
opencloud storage-users uploads sessions
```

Then restart this upload:

```bash
opencloud storage-users uploads sessions --id <upload-id> --restart
```

Replace `<upload-id>` with the ID of the failed upload.

:::caution
Do not run the command with `--restart` without a filter such as `--id`. Otherwise, the command affects all upload sessions, including uploads that are still being processed.

The `--resume` option does not help with failed uploads. After the maximum number of attempts, an upload is marked as finished, and `--resume` skips finished uploads.
:::
