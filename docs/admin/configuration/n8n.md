---
sidebar_position: 120
id: n8n
title: n8n
description: Automate OpenCloud workflows with n8n
draft: false
---

# Integrate OpenCloud with n8n

[n8n](https://n8n.io/) is a workflow automation platform that connects applications and services through reusable nodes. The [OpenCloud node for n8n](https://github.com/opencloud-eu/n8n-nodes-opencloud/tree/55edfedd020346e161c77dd3f9d1fa00edab5ef7) lets workflows interact with files and folders stored in OpenCloud.

By combining the OpenCloud node with triggers, filters, and nodes for other services, you can use OpenCloud as part of automated processes. For example, a workflow can:

- Process files in an OpenCloud folder on a schedule
- Select files based on their metadata
- Pass OpenCloud file information to other applications
- Apply retention or cleanup rules

This guide uses the automatic deletion of old files as a practical example. The same setup and workflow concepts can be adapted to other OpenCloud automations.

For general information about workflows, nodes, and operating n8n, see the [n8n documentation](https://docs.n8n.io/).

## Example: Automatically delete old files

The example workflow deletes files from an OpenCloud folder when they have not been modified for a defined period. It demonstrates how to:

- Authenticate the OpenCloud node with an app token
- List the contents of an OpenCloud folder
- Filter items using OpenCloud metadata
- Pass the result from one node to another
- Run a workflow manually or on a schedule

The workflow uses the `lastModifiedDateTime` value returned by OpenCloud. Opening or downloading a file does not update this value. Editing and saving the file updates the value after the changes have been written back to OpenCloud.

The example initially uses a retention period of five minutes for testing. After the workflow has been verified, the retention period can be changed to three months or another period appropriate for your use case.

:::warning

Test the workflow in a dedicated test Space before using it with production data.

Deleted files may no longer be available to users. Verify the filtered results before adding the delete operation and before activating the workflow.

:::

## Prerequisites

Before creating the workflow, ensure that the following requirements are met:

- A running [n8n](https://n8n.io/) instance
- The [OpenCloud node for n8n](https://github.com/opencloud-eu/n8n-nodes-opencloud/tree/55edfedd020346e161c77dd3f9d1fa00edab5ef7)
- An OpenCloud user account with access to the target Space
- An [OpenCloud app token](../../user/admin/app-tokens.md)
- A dedicated OpenCloud Space or folder containing test files
- At least one file older than the configured test period

The regular OpenCloud account password cannot be used for the n8n credentials. [Create an app token in OpenCloud](../../user/admin/app-tokens.md) and enter it in the password field of the n8n credential. Use a dedicated token for n8n and choose an appropriate expiration period.

The example workflow initially processes files in one folder. Processing nested folders and deleting empty folders requires additional workflow steps.

## Example workflow overview

The workflow has the following structure:

```text
Manual Trigger
    ↓
OpenCloud: List a folder
    ↓
Filter:
- item is a file
- file is older than five minutes
    ↓
OpenCloud: Delete a file
```

During testing, the workflow is started manually. After the workflow has been verified, the `Manual Trigger` can be replaced with a `Schedule Trigger`.

## Prepare the example

Create a dedicated test Space or test folder in OpenCloud.

For example:

```text
/
└── n8n
    ├── old-file.md
    └── new-file.md
```

Wait at least five minutes after creating `old-file.md`.

Create or modify `new-file.md` shortly before running the workflow. This allows you to verify that only the older file is selected.

## Connect n8n to OpenCloud

Add an OpenCloud node to a new n8n workflow and create a new credential.

Enter the following values:

```text
Server URL: https://cloud.example.com
Username: your OpenCloud username
Password: your OpenCloud app token
```

Use the base URL of the OpenCloud instance.

Do not use a public share or File Drop URL.

For example:

```text
Correct:
https://cloud.example.com

Incorrect:
https://cloud.example.com/s/AbCdEf123
```

Save the credential.

## Build the example workflow

### Add a manual trigger

Create a new n8n workflow and add a `Manual Trigger` node.

Use the manual trigger while configuring and testing the workflow.

### List the folder contents

Add an OpenCloud node after the manual trigger.

Select the `List a folder` action and configure the node:

```text
Space Name or ID: Select the test Space
Path: /n8n
```

The path is relative to the selected Space.

If the files are stored directly in the root of the Space, use:

```text
/
```

Execute the node.

The output contains files and folders. A file entry contains a `file` object and a modification timestamp:

```json
{
  "file": {
    "mimeType": "text/markdown"
  },
  "lastModifiedDateTime": "2026-07-23T12:30:00Z",
  "name": "old-file.md",
  "parentReference": {
    "path": "/n8n"
  }
}
```

A folder entry contains a `folder` object instead:

```json
{
  "folder": {},
  "name": "archive"
}
```

### Add the filter

Add an n8n `Filter` node after `List a folder`.

The Filter node is a standard n8n node. It is not part of the OpenCloud community node.

Configure the filter to match all conditions using `AND`.

#### Filter files

Add the first condition.

Use the following expression:

```javascript
{
  {
    $json.file !== undefined;
  }
}
```

Select:

```text
Boolean
is true
```

This condition excludes folders from the result.

#### Filter files older than five minutes

Add a second condition.

Use the following expression as the first value:

```javascript
{
  {
    $now.minus({ minutes: 5 });
  }
}
```

Select:

```text
Date & Time
is after
```

Use the following expression as the second value:

```javascript
{
  {
    DateTime.fromISO($json.lastModifiedDateTime);
  }
}
```

The complete comparison is:

```text
Current time minus five minutes
is after
lastModifiedDateTime
```

This condition matches files whose last modification time is more than five minutes in the past.

Enable `Convert types where required` if n8n does not automatically recognize the timestamp as a date.

Execute the Filter node.

Only files older than five minutes should appear in the output.

A file modified less than five minutes ago must not appear.

:::note

When testing file modifications, execute `List a folder` again before executing the Filter node.

Executing only the Filter node may reuse data from an earlier workflow execution.

:::

### Delete the filtered files

After verifying the Filter output, add another OpenCloud node.

Select the `Delete a file` action.

Configure the node:

```text
Space Name or ID: Select the same test Space
```

Set `Path` to an expression:

```javascript
{
  {
    $json.parentReference.path + '/' + $json.name;
  }
}
```

For the example file, this expression produces:

```text
/n8n/old-file.md
```

The expression uses the path returned by `List a folder`. This avoids hard-coding the source folder in the delete node.

Execute the node.

Verify in OpenCloud that only the expected files were deleted.

### Change the retention period to three months

After the workflow has been tested successfully, replace the five-minute expression:

```javascript
{
  {
    $now.minus({ minutes: 5 });
  }
}
```

with:

```javascript
{
  {
    $now.minus({ months: 3 });
  }
}
```

The filter then matches files whose `lastModifiedDateTime` is more than three months in the past.

The resulting condition is:

```text
Current time minus three months
is after
lastModifiedDateTime
```

### Run the workflow automatically

After the workflow has been verified, replace the `Manual Trigger` with a `Schedule Trigger`.

For example, run the workflow once per day:

```text
Trigger interval: Days
Every: 1
```

Connect the Schedule Trigger to the `List a folder` node.

The final workflow is:

```text
Schedule Trigger
    ↓
OpenCloud: List a folder
    ↓
Filter:
- file exists
- lastModifiedDateTime is older than three months
    ↓
OpenCloud: Delete a file
```

Save and activate the workflow.

n8n must remain running for scheduled executions. If n8n runs locally, the computer and the n8n process or container must remain available.

## Adapt the workflow

The deletion workflow is only one example of how OpenCloud can be used with n8n. You can replace the filter and delete steps, combine the OpenCloud node with nodes for other services, or use a different trigger. When adapting the workflow, inspect the output of each OpenCloud operation to identify the fields that can be mapped into subsequent nodes.

Start new workflows with a `Manual Trigger` and test them in a dedicated Space. Add a `Schedule Trigger` or another automatic trigger only after the workflow produces the expected results.

## Limitations of the example

The workflow uses `lastModifiedDateTime`.

This value indicates when the file was last changed. It does not indicate when the file was last opened, viewed, or downloaded.

The example workflow lists only one folder level. It does not automatically process nested folders.

Deleting files from nested folders and deleting empty folders requires recursive folder processing. Empty folders must be deleted after their files and subfolders have been removed.
