---
sidebar_position: 10
id: maintenance-commands
title: Maintenance Commands
description: Common maintenance commands for OpenCloud administrators.
draft: false
---

# Maintenance Commands

:::caution

Some maintenance commands can delete or modify data. Create a backup before running cleanup or purge commands. Use dry-run options where available and check the output before running destructive commands.

:::

## Run commands in Docker Compose

If OpenCloud runs with Docker Compose, run maintenance commands inside the OpenCloud container:

```bash
docker compose exec opencloud opencloud <command>
```

For one-off commands, you can also use:

```bash
docker compose run --rm opencloud opencloud <command>
```

## Storage path

The `--basePath` (`-p`) option is required by storage, revision, and trash commands. It must point to the storage provider path as seen from inside the OpenCloud container.

For Docker Compose deployments, the default path is usually:

```bash
/var/lib/opencloud/storage/users
```

Example:

```bash
docker compose exec opencloud opencloud backup consistency -p /var/lib/opencloud/storage/users
```

If your deployment uses a custom storage path, replace `/var/lib/opencloud/storage/users` with the path configured for your storage backend.

## Storage

### Check storage consistency

Checks the storage for inconsistencies such as orphaned blobs, missing blobs, missing nodes, missing links, missing files, missing or malformed metadata, and invalid parent-child relationships.

```bash
opencloud backup consistency -p /var/lib/opencloud/storage/users
```

To return a non-zero exit code when inconsistencies are found:

```bash
opencloud backup consistency -p /var/lib/opencloud/storage/users --fail
```

Run this command after storage-related incidents, manual file-system changes, migrations, restores, or when users report missing or misplaced files.

### Purge expired trash-bin items

```bash
opencloud storage-users trash-bin purge-expired
```

The purge behavior can be configured with these environment variables:

```bash
STORAGE_USERS_PURGE_TRASH_BIN_USER_ID
STORAGE_USERS_PURGE_TRASH_BIN_PERSONAL_DELETE_BEFORE
STORAGE_USERS_PURGE_TRASH_BIN_PROJECT_DELETE_BEFORE
```

By default, the delete-before values are `720h`, which equals 30 days.

### List trash-bin items of a space

```bash
opencloud storage-users trash-bin list <space-id>
```

### Restore trash-bin items

Restore all trash-bin items for a space:

```bash
opencloud storage-users trash-bin restore-all <space-id>
```

Restoring is only possible to the original location. The behavior when the target name already exists can be configured with the available restore options: skipping, replacing, or keeping both items.

## Uploads

The `opencloud storage-users uploads sessions` command lists and manages upload sessions. Flags can be combined to filter sessions by state.

### List upload sessions

List all sessions:

```bash
opencloud storage-users uploads sessions
```

List sessions that are not expired and not currently processing:

```bash
opencloud storage-users uploads sessions --expired=false --processing=false
```

To print output as JSON:

```bash
opencloud storage-users uploads sessions --expired=false --processing=false --json
```

### Clean expired uploads

Expired uploads are not removed automatically and accumulate storage over time.

First, review which sessions would be removed:

```bash
opencloud storage-users uploads sessions --expired=true
```

Then remove them:

```bash
opencloud storage-users uploads sessions --expired=true --clean
```

### Resume failed upload processing

Resume uploads that are not currently processing and are not marked as virus infected:

```bash
opencloud storage-users uploads sessions --processing=false --has-virus=false --resume
```

Use `--restart` instead of `--resume` if processing should restart from the beginning rather than continue from the last completed step:

```bash
opencloud storage-users uploads sessions --processing=false --has-virus=false --restart
```

## Roles

### List unified roles

Lists unified roles and their IDs. Useful when a configuration or documentation step requires a role ID.

```bash
opencloud graph list-unified-roles
```
