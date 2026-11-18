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

`docker compose exec` runs the command with the environment variables of the container, so it gets the same settings as OpenCloud. Without containers, this isn't automatic. In particular, variables that you set with `Environment=` in a systemd unit only reach the OpenCloud service. A command that you run from a shell or from cron doesn't get them: it finds no strategy and stops with an error, and it doesn't see the settings of the file metadata cache either (see [Share the file metadata cache](#share-the-file-metadata-cache) below).

On such a server, keep the settings in an environment file, for example `/etc/opencloud/opencloud.env`, and load it in the systemd unit with `EnvironmentFile=`:

```ini
[Service]
EnvironmentFile=/etc/opencloud/opencloud.env
```

Then load the same file for the command, as the user OpenCloud runs as:

```bash
sudo -u opencloud sh -c 'set -a; . /etc/opencloud/opencloud.env; exec opencloud storage-users revisions cleanup --all --dry-run'
```

`set -a` exports every variable the file sets, so that the command sees them. This works as long as the file only contains lines of the form `NAME=value`, with values that contain spaces in quotes, as in `OC_REVISIONS_CLEANUP_STRATEGY="7d, auto, 90d"`.

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
  kept      2026-09-30T09:00:00+02:00   2.2 MiB  kept by "auto" (last 30 days): the oldest in its slot of 1 day starting 2026-09-30T00:00:00Z
  deleted   2026-04-02T08:00:00+02:00   2.1 MiB  deleted by "90d": older than 2026-07-23T15:00:00+02:00
3 files in 1 space: would delete 1 revision (2.1 MiB) of 1 file, 0 skipped, 0 failed
```

Each version is either `deleted`, `kept` (by the strategy) or `protected` (always kept, for example because it is among the newest ones). The reason names the part of the strategy that decided, and the time it compared the version with. The time shown for each version is when it was created, which can differ from the date the version list in the web interface shows, see [How Old Is a Version?](../configuration/storage/revisions-cleanup.md#how-old-is-a-version).

When the result looks right, run the same command without `--dry-run`. On a default installation, the command then stops with an error about the file metadata cache, see the next section.

#### Share the file metadata cache

OpenCloud keeps the metadata of files and their versions in a cache, the file metadata cache. By default, each process keeps a cache of its own, in its memory. The command runs in a process of its own, next to OpenCloud, so with the default cache, OpenCloud doesn't learn which versions the command deleted.

OpenCloud lists the versions of a file from the storage, so a list of versions that is opened after the cleanup is right. But a list that was already open while the command ran, for example the Versions panel of a file in the web interface, still shows the deleted versions. Downloading or restoring one of them fails, as they are gone. Opening the list again shows the remaining versions.

That's why the command refuses to delete versions when each process keeps a cache of its own, which is the case with the default, `memory`, and with `ocmem`. It stops right away, before it deletes anything, with this error:

```plaintext
the file metadata cache of the storage-users service is kept in the memory of each process (store "memory"): the server doesn't learn about the revisions this command deletes, so a list of versions that is already open keeps showing them, and downloading or restoring one of them fails. Share the cache by setting STORAGE_USERS_FILEMETADATA_CACHE_STORE to 'nats-js-kv' (OC_CACHE_STORE would set the cache store of all services), or run the command anyway with --allow-local-cache
```

To share the cache, set `STORAGE_USERS_FILEMETADATA_CACHE_STORE` to `nats-js-kv`. OpenCloud then keeps the cache in NATS, and the command uses the same cache. With OpenCloud Compose, add the setting to the `opencloud` service, for example in the same file as the strategy, as described in [Turning the Cleanup On](../configuration/storage/revisions-cleanup.md#with-opencloud-compose):

```yaml
services:
  opencloud:
    environment:
      OC_REVISIONS_CLEANUP_STRATEGY: '7d, auto, 90d'
      STORAGE_USERS_FILEMETADATA_CACHE_STORE: 'nats-js-kv'
```

Then restart OpenCloud:

```bash
docker compose down
docker compose up -d
```

With other installations, set the variable for the OpenCloud process, in the same way as the strategy, and restart OpenCloud. The command must get the same setting, see above for a server that runs OpenCloud with systemd.

`OC_CACHE_STORE` would also work, but it sets the cache of all services, not only the one of the storage.

If you can accept that open lists of versions show deleted versions until they are opened again, for example because the command runs at night, when nobody is working, you can run it anyway with `--allow-local-cache`:

```bash
opencloud storage-users revisions cleanup --all --allow-local-cache
```

A dry run needs neither: it deletes nothing, so there is nothing OpenCloud would have to learn about. It always keeps a cache of its own in its memory, whatever is configured, so that it doesn't fill the shared cache with the metadata of every file it looks at.

#### Choose the files

Exactly one of these options selects the files to clean up:

- `--all` (`-a`): all files of all spaces.
- `--space <space-id>`: all files of a space. The option can be given several times, for several spaces.
- `--space <space-id> --path <path>`: only a file, or a folder with everything in it, within one space.
- `--fs-path <path>` (`-p`): a file, or a folder with everything in it, by its path on disk. This only works with the PosixFS storage driver.

Space IDs often contain a `$`, so put them in single quotes. The ID of a file or a folder, which looks like `<storage-id>$<space-id>!<node-id>`, isn't accepted as a space ID, so that a mix-up doesn't clean up the whole space. Give its space with `--space` and its path with `--path` instead:

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

Replace `/opt/opencloud-compose` with the directory of your OpenCloud Compose installation. `-T` is needed because cron doesn't provide a terminal. The entry needs the shared file metadata cache, see [Share the file metadata cache](#share-the-file-metadata-cache). Otherwise, every run ends with an error and exit code `1`, and deletes nothing.

Without containers, load the environment file of OpenCloud in the crontab entry, as described at the beginning of this section, for example in the crontab of the user `opencloud`:

```crontab
0 3 * * * sh -c 'set -a; . /etc/opencloud/opencloud.env; exec opencloud storage-users revisions cleanup --all --timeout 1h --shuffle' >> /var/log/opencloud/revisions-cleanup.log 2>&1
```

The command ends with one of these exit codes, which you can use in scripts:

- `0`: the cleanup is done.
- `1`: the cleanup, or the cleanup of at least one file, failed. The output says which and why. The command also ends with `1` when you interrupt it with Ctrl-C, or when it gets a `SIGTERM`.
- `2`: `--timeout` stopped the cleanup before all files were cleaned up, and nothing failed.

#### While OpenCloud is running

The command can run while OpenCloud is running. It works on the storage directly, in a process of its own, next to OpenCloud. Three things are good to know:

- **Run it as the user OpenCloud runs as.** While the command cleans up a file, it locks it, and the first time a file is locked, a lock file is created. That lock file belongs to the user that runs the command, and only that user can open it. If the command runs as another user, for example as `root`, OpenCloud may no longer be able to lock these files, and changing, moving or deleting them fails. A dry run (`--dry-run`) changes nothing on disk and creates no lock files, so it does no harm, but the real cleanup must run as the right user. With Docker Compose, `docker compose exec` already runs the command as the user of the container. On a server where OpenCloud runs as the user `opencloud`, run the command with `sudo -u`, and load the environment file of OpenCloud, as described at the beginning of this section:

  ```bash
  sudo -u opencloud sh -c 'set -a; . /etc/opencloud/opencloud.env; exec opencloud storage-users revisions cleanup --all --dry-run'
  ```

  When the storage belongs to another user than the one that runs the command, the command prints a warning before it starts, except in a dry run, which changes nothing on disk. For example:

  ```plaintext
  2026-11-17T10:00:00+01:00 WRN the storage /var/lib/opencloud/storage/users belongs to the user opencloud, but the command runs as root: the lock files it creates belong to root, and OpenCloud may not be able to lock these files anymore; run the command as opencloud, e.g. with 'sudo -u opencloud'
  ```

  If you see it, stop the command with Ctrl-C and run it again as the right user.

- **The file metadata cache must be shared**, so that OpenCloud learns which versions the command deleted. See [Share the file metadata cache](#share-the-file-metadata-cache).
- **PosixFS needs NATS.** With the PosixFS driver, the command connects to NATS, like OpenCloud itself. When NATS runs within OpenCloud, which is the default where a single `opencloud server` process runs all services, the command only works while OpenCloud is running. When OpenCloud is stopped, the command gives up after 10 seconds, after a few log lines about the failed attempts to connect:

  ```plaintext
  could not create the event stream for the posix driver: could not connect to NATS at 127.0.0.1:9233 within 10s: the command needs NATS, i.e. a running OpenCloud server or a separate NATS
  ```

  If NATS runs as a separate service in your installation, the command also works while OpenCloud is stopped, as long as NATS is running.

#### Other options

- `--async`, `--workers` and `--queue-size` override the settings of the background workers for this run, see [Background Workers](../configuration/storage/revisions-cleanup.md#background-workers).
- `--queue-full` and `--queue-full-timeout` say what happens when the queue of the background workers is full. Unlike the other settings, they don't default to the configured ones: the command finds files much faster than the workers can clean them up, so the queue is full most of the time, and skipping the files that don't fit would skip most of them. That's why the command waits for room in the queue by default (`--queue-full block`), as long as it takes (`--queue-full-timeout 0`). You rarely need to change them. With `--queue-full drop`, or with a timeout, for example `--queue-full-timeout 10s`, the skipped files are listed in the output, and are cleaned up with their next version or the next run.
- Ctrl-C stops the cleanup gracefully, like `--timeout`, but the command then ends with the exit code `1`, not `2`. Press Ctrl-C a second time to end the command right away, for example when it waits for a file that another process has locked, or for NATS. Use this only when the first Ctrl-C doesn't help: a version is deleted in two steps, first its entry, then its content. If the command ends between them, the content stays on disk without anything pointing to it, and takes up storage.
- A dry run changes nothing on disk. It doesn't keep the files locked while it decides, so its result is a snapshot: for a file that changes while the command runs, for example because a user uploads a new version of it, the real run may decide differently.

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
