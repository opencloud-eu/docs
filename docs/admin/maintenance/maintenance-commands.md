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

The `--basepath` (`-p`) option is required by storage, revision, and trash commands. It must point to the storage provider path as seen from inside the OpenCloud container.

For Docker Compose deployments, the default path is usually:

```bash
/var/lib/opencloud/storage/users
```

Example:

```bash
docker compose exec opencloud opencloud backup consistency -p /var/lib/opencloud/storage/users
```

If your deployment uses a custom storage path, replace `/var/lib/opencloud/storage/users` with the path configured for your storage backend.

## General

### Check the OpenCloud version

```bash
opencloud version
```

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

### Scanning resources on PosixFS

When using the [PosixFS Storage Driver](../configuration/storage/posixfs.md) in collaborative mode (with `STORAGE_USERS_POSIX_WATCH_FS` set to `true`), files and directories can be added or manipulated in the storage directly. When files are added, OpenCloud transparently adds metadata to track the files for future changes, as if they were uploaded through OpenCloud.

Administrators can trigger the storage scanning manually. This might be useful during migrations, or when [collaborative mode](../configuration/storage/posixfs.md#posixfs-collaborative-mode) is disabled.

It is recommended practice in such situations, since files that have not been scanned:

- may have a negative performance impact when accessed, since OpenCloud transparently performs a storage scan to ingest previously untracked files when listing a directory through its UIs and APIs (but not recursively)
- prevents those files from being accounted for in directory tree sizes and quotas

For such cases, use the following command:

```bash
opencloud posixfs scan [path path ...]
```

Optionally, one might want to specify resources to scan, using optional arguments that specify paths.

When that path is a directory, it will recurse and perform a storage scan for all the files contained within that directory and all its subdirectories.

Scanning can also be performed on an individual space, simply by specifying its storage path as a parameter.

And when that path is a regular file instead, it will solely perform a storage scan on that one file.

Note that in either case, the resource must be underneath the PosixFS storage root, or be the PosixFS storage root itself, as set using `STORAGE_USERS_POSIX_ROOT`; if not, an error will occur.

When no arguments are specified, the default behavior is to start the storage scanning recursively at the root of the PosixFS storage (as defined by `STORAGE_USERS_POSIX_ROOT`).

The optional command-line option `--halt-on-error` (or `-E`) will make the command stop as soon as an error is encountered, whereas the default behaviour is to keep going by skipping paths that yield unrecoverable errors and proceeding to processing the subsequent ones.

### Clean up old file versions

OpenCloud can delete old file versions automatically, according to a cleanup strategy, whenever a file gets a new version. That cleanup and its strategies are explained in [Cleaning Up Old Versions](../configuration/storage/revisions-cleanup.md).

The automatic cleanup only looks at files that get a new version. Files that are never changed again keep all their versions. The `revisions cleanup` command cleans up the versions of whole spaces, of folders or of single files on demand. Use it:

- once after turning the cleanup on, to clean up the versions that existed before,
- after changing the strategy, to apply the new one to all files,
- regularly, for example every night, so that files that are no longer changed are cleaned up too,
- to free storage, with a stricter strategy than the configured one.

```bash
opencloud storage-users revisions cleanup [flags]
```

The command uses the configuration of the storage-users service, including the configured strategy, and can run while OpenCloud is running. Unlike the commands above, it doesn't need `--basepath`. With Docker Compose, run it inside the OpenCloud container:

```bash
docker compose exec opencloud opencloud storage-users revisions cleanup --all --dry-run
```

:::caution

Deleted versions can't be restored. Always run the command with `--dry-run` first, and check what it would delete.

:::

#### Try it out first

`--dry-run` (`-n`) deletes nothing. It prints what would be deleted. Together with `--verbose` (`-v`), it lists every version, with what would happen to it and why:

```bash
opencloud storage-users revisions cleanup --all --strategy "7d, auto, 90d" --dry-run --verbose
```

```plaintext
25b69780-5f39-43be-a7ac-a9b9e9fe4230 /Documents/report.odt (node 8a1c0e2f-6b4d-4f7a-9c3e-2d5b7f1a0c94): would delete 1 of 3 revisions (2.1 MiB)
  protected 2026-10-21T14:50:00+02:00   2.3 MiB  protected by "7d": newer than 2026-10-14T15:00:00+02:00
  kept      2026-09-30T09:00:00+02:00   2.2 MiB  kept by "auto" (last 30 days): the newest in its slot of 1 day starting 2026-09-30T00:00:00Z
  deleted   2026-04-02T08:00:00+02:00   2.1 MiB  deleted by "90d": older than 2026-07-23T15:00:00+02:00
3 files in 1 space: would delete 1 revision (2.1 MiB) of 1 file, 0 skipped, 0 failed
```

Each version is either `deleted`, `kept` (by the strategy) or `protected` (always kept, for example because it is among the newest ones). The reason names the part of the strategy that decided, and the time it compared the version with.

When the result looks right, run the same command without `--dry-run`.

#### Choose the files

Exactly one of these options selects the files to clean up:

- `--all` (`-a`): all files of all spaces.
- `--space <space-id>`: all files of a space. The option can be given several times, for several spaces.
- `--space <space-id> --path <path>`: only a file, or a folder with everything in it, within one space.
- `--fs-path <path>` (`-p`): a file, or a folder with everything in it, by its path on disk. This only works with the PosixFS storage driver.

Space IDs often contain a `$`, so put them in single quotes:

```bash
# all files of two spaces
opencloud storage-users revisions cleanup --space '<space-id-1>' --space '<space-id-2>'

# only the Documents folder of a space
opencloud storage-users revisions cleanup --space '<space-id>' --path /Documents

# a folder of a project space, by its path on disk (PosixFS only)
opencloud storage-users revisions cleanup --fs-path /var/lib/opencloud/storage/users/projects/<space-id>/Documents
```

#### Choose the strategy

Without `--strategy` (`-s`), the command uses the configured strategy, `OC_REVISIONS_CLEANUP_STRATEGY`. If none is configured, it stops with an error and doesn't delete anything. With `--strategy`, it uses the given one for this run only:

```bash
# keep only the 10 newest versions of every file in a space
opencloud storage-users revisions cleanup --space '<space-id>' --strategy 10

# delete all versions older than a year, but keep the 3 newest of every file
opencloud storage-users revisions cleanup --all --strategy "3, 52w"
```

The strategies are explained in [Choosing a Strategy](../configuration/storage/revisions-cleanup.md#choosing-a-strategy).

#### Read the output

By default, the command prints a line for every file whose versions it deleted, that failed, or that it skipped, followed by a summary:

```plaintext
25b69780-5f39-43be-a7ac-a9b9e9fe4230 /Documents/report.odt: deleted 3 of 12 revisions (4.2 MiB)
25b69780-5f39-43be-a7ac-a9b9e9fe4230 /Photos/holiday.jpg: skipped: an upload to the file is still being processed
1520 files in 3 spaces: deleted 3 revisions (4.2 MiB) of 1 file, 1 skipped, 0 failed
```

Each line starts with the ID of the space and the path of the file within the space. A file is skipped while an upload to it is still being processed, for example by the antivirus scanner. A later run cleans it up.

For scripts and monitoring, `--json` (`-j`) prints the same as JSON objects, one per line. The last line is the summary. Sizes are in bytes:

```json
{"type":"file","space_id":"25b69780-5f39-43be-a7ac-a9b9e9fe4230","node_id":"8a1c0e2f-6b4d-4f7a-9c3e-2d5b7f1a0c94","path":"/Documents/report.odt","dry_run":false,"revisions":12,"deleted":3,"deleted_bytes":4404019,"failed":0}
{"type":"summary","dry_run":false,"spaces":3,"files":1520,"cleaned":1,"deleted":3,"deleted_bytes":4404019,"skipped":1,"failed":0}
```

#### Run it regularly

To clean up files that are no longer changed, run the command regularly, for example every night with cron. On large installations, a single run can take a long time, so limit it with `--timeout` (`-t`), and add `--shuffle`:

```bash
opencloud storage-users revisions cleanup --all --timeout 1h --shuffle
```

`--timeout` stops the cleanup gracefully: files that are being cleaned up are finished, and the rest is left for the next run. As every run starts from the beginning again, `--shuffle` makes it go through the spaces and folders in a random order. That way, each run starts in a different place, and over several nights, all files are reached.

An example crontab entry for OpenCloud Compose, which runs the cleanup every night at 3:00 for at most one hour, and appends the output to a log file:

```crontab
0 3 * * * cd /opt/opencloud-compose && docker compose exec -T opencloud opencloud storage-users revisions cleanup --all --timeout 1h --shuffle >> /var/log/opencloud-revisions-cleanup.log 2>&1
```

Replace `/opt/opencloud-compose` with the directory of your OpenCloud Compose installation. `-T` is needed because cron doesn't provide a terminal.

The command ends with one of these exit codes, which you can use in scripts:

- `0`: the cleanup is done.
- `1`: the cleanup, or the cleanup of at least one file, failed. The output says which and why.
- `2`: `--timeout` stopped the cleanup before all files were cleaned up, and nothing failed.

#### While OpenCloud is running

The command can run while OpenCloud is running. It works on the storage directly, in a process of its own, next to OpenCloud. Two things are good to know:

- **Versions in an open Versions panel.** OpenCloud keeps the metadata of files and versions in a cache. With the default cache (`STORAGE_USERS_FILEMETADATA_CACHE_STORE=memory`), each process has a cache of its own, so OpenCloud doesn't learn which versions the command deleted. That does no harm: OpenCloud lists the versions from the storage, and refuses to download or restore a version that no longer exists. But a user who had the Versions panel of a file open while the command ran still sees the deleted versions there, and gets an error when trying to download or restore one of them. Opening the panel again shows the remaining versions.
- **PosixFS needs NATS.** With the PosixFS driver, the command connects to NATS, like OpenCloud itself. When NATS runs within OpenCloud, which is the default where a single `opencloud server` process runs all services, the command only works while OpenCloud is running. When OpenCloud is stopped, the command gives up after 10 seconds, after a few log lines about the failed attempts to connect:

  ```plaintext
  could not create the event stream for the posix driver: could not connect to NATS at 127.0.0.1:9233 within 10s: the command needs NATS, i.e. a running OpenCloud server or a separate NATS
  ```

  If NATS runs as a separate service in your installation, the command also works while OpenCloud is stopped, as long as NATS is running.

#### Other options

- `--async`, `--workers` and `--queue-size` override the settings of the background workers for this run, see [Background Workers](../configuration/storage/revisions-cleanup.md#background-workers).
- `--queue-full` and `--queue-full-timeout` say what happens when the queue of the background workers is full. Unlike the other settings, they don't default to the configured ones: the command finds files much faster than the workers can clean them up, so the queue is full most of the time, and skipping the files that don't fit would skip most of them. That's why the command waits for room in the queue by default (`--queue-full block`), as long as it takes (`--queue-full-timeout 0`). You rarely need to change them. With `--queue-full drop`, or with a timeout, for example `--queue-full-timeout 10s`, the skipped files are listed in the output, and are cleaned up with their next version or the next run.
- Ctrl-C stops the cleanup gracefully, like `--timeout`.
- A dry run doesn't change any file, but it takes the same locks on the files as a real run, which can create lock files.

Not to be confused with `opencloud revisions purge`, an older command that deletes all versions of a DecomposedFS storage, or of a single file or space, directly on disk and without a strategy.

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

## Search

### Rebuild the search index

Re-index a specific space:

```bash
opencloud search index --space <space-id>
```

Re-index all spaces:

```bash
opencloud search index --all-spaces
```

A reindex only picks up new or changed files; content that has already been indexed is not scanned again, even if the configuration or extractor changed. To force a full rescan, add `--force-rescan`:

```bash
opencloud search index --all-spaces --force-rescan
```

Run this after an upgrade, a restore, or when search results are missing or outdated.

## Authentication

### Reset the admin password

Resetting the password requires stopping the OpenCloud container first, since `idm resetpassword` needs exclusive access to the user store. Run it in a temporary container instead of `docker compose exec`:

```bash
docker compose stop opencloud
```

```bash
sudo docker run -it --rm -v <opencloud-data-path>:/var/lib/opencloud -v <opencloud-config-path>:/etc/opencloud opencloudeu/opencloud:<opencloud-version> idm resetpassword
```

See [Admin password cannot be changed in `.env`](../resources/common-issues/admin-password-reset.md) for the full walkthrough, including how to find the volume names.

### Create an app token

Creates an app-specific authentication token for a user, for example for clients that do not support the primary login method.

```bash
opencloud auth-app create --user-name=<user-name> --expiration=<token-expiration>
```
