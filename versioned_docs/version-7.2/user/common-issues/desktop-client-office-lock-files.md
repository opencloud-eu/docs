---
sidebar_position: 3
id: desktop-client-office-lock-files
title: Microsoft Office lock files are not synchronized
description: Understand why the Desktop Client excludes Microsoft Office lock files
draft: false
hide_table_of_contents: true
---

# Microsoft Office lock files are not synchronized

## Problem

The OpenCloud Desktop Client does not synchronize files starting with `~$`, such as `~$document.docx`.

<img src={require("../common-issues/img/desktop-excluded.png").default} alt="Show the ~$ file is excluded from synchronizing" width="500"/>

## Cause

These files are temporary lock files created by Microsoft Office applications while a document is open. They are internal markers that prevent multiple users from editing the same document simultaneously, rather than content files.

## Solution

Close the document in Microsoft Office. Office automatically removes the corresponding `~$` file.

For more details, see the [Microsoft support article on temporary Office lock files created by Word, Excel, and PowerPoint](https://support.microsoft.com/en-gb/topic/-the-document-is-locked-for-editing-by-another-user-error-message-when-you-try-to-open-a-document-in-word-10b92aeb-2e23-25e0-9110-370af6edb638?).
