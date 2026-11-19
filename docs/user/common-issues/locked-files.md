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
- If the step still fails after the maximum number of attempts, processing is aborted. In this case, the file stays unavailable until an administrator resumes the processing.
- If the virus scan detects malware, the file is deleted or stays blocked, depending on the server configuration.

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

Office files are unlocked automatically after 30 minutes at the latest, even if an editing session was not closed cleanly.

If the file stays locked for a longer time, an administrator should check the cause.

## When should an admin check?

An administrator should check when:

- an Office file is still locked more than 30 minutes after all users have closed it
- an uploaded file stays in the processing state
- several files are affected
- users cannot save even though they have editing rights
- the file is blocked for all users

If the processing of uploads has failed, an administrator can list the upload sessions and resume failed uploads with the following commands:

```bash
opencloud storage-users uploads sessions
opencloud storage-users uploads sessions --resume
```
