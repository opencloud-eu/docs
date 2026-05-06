---
sidebar_position: 80
id: locked-files
title: Locked files
description: When files in OpenCloud can be locked and what this means for users.
---

# Locked files

OpenCloud can temporarily mark files as locked or unavailable. For users, this usually means the file cannot be opened, edited, saved, or synchronized as usual while the lock is active.

A file can be locked for different reasons. Common causes are an active Office editing session or background processing after upload.

## When can a file be locked?

A file can be locked when:

- it is open or being edited in an integrated Office app
- several users are working on the same Office file at the same time
- an Office editing session has not ended cleanly yet
- an upload is still being processed
- a virus scan is still running
- a post-upload processing step has not finished yet

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

A file can also be locked after upload while OpenCloud processes it.

This may include:

- virus scanning
- metadata processing
- preview generation
- search index updates

While this work is still running, the file may be locked or only partially available.

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

1. wait a few minutes
2. reload the file list
3. check whether the file is still open in another browser tab
4. check whether the file is open on another device
5. check whether a sync client is currently uploading or synchronizing the file
6. close the Office file and open it again

If the file stays locked for a longer time, an administrator should check the cause.

## When should an admin check?

An administrator should check when:

- the file stays locked for a long time
- several files are affected
- files are not released after upload
- Office files stay locked after closing
- users cannot save even though they have editing rights
- the file is blocked for all users

## Summary

A file can be locked in OpenCloud while it is being edited or while OpenCloud is still processing it after upload.

The lock protects against conflicting changes or prevents access until required processing steps are finished. In many cases the file is released automatically. If the lock persists, the cause should be checked by an administrator.
