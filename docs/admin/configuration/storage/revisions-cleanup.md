---
sidebar_position: 4
id: storage-revisions-cleanup
title: 'Cleaning Up Old Versions'
description: How OpenCloud deletes old file versions according to a cleanup strategy
draft: false
---

# Cleaning Up Old Versions

Every time a file is changed in OpenCloud, the previous content is kept as a version. Users can see these versions in the web interface and restore an earlier one, for example after saving a document by mistake.

This is the case as long as versioning is enabled, which it is by default. Versioning can be turned off by setting `OC_DISABLE_VERSIONING` to `true`, see the [global environment variables](../../../dev/server/configuration/global-envvars.mdx). A changed file then simply replaces its previous content, and no new versions are created.

Without a cleanup, OpenCloud keeps every version forever. On a server where files change often, the versions can take up much more space than the files themselves: a document that is saved twenty times a day has thousands of versions after a year, and every one of them is a full copy of the file at that time.

The version cleanup deletes old versions according to a **cleanup strategy** that you choose, for example "keep the 10 newest versions", "delete versions older than 90 days", or "keep everything from the last week, and fewer versions the older they get". It works with all storage drivers: PosixFS, DecomposedFS and DecomposedS3.

The cleanup is **disabled by default**. No file versions are deleted until you configure a strategy.

:::note

The configuration and the commands call versions _revisions_, for example `OC_REVISIONS_CLEANUP_STRATEGY`. Both words mean the same thing.

:::

## How the Cleanup Works

### When the Cleanup Runs

Once a strategy is configured, OpenCloud applies it to a file whenever the file gets a new version:

- when a user uploads new content for an existing file, as soon as the upload is complete. If the upload is checked first, for example by the antivirus scanner, the cleanup runs once the check has passed.
- when a user restores an earlier version. The version that holds the content from just before the restore is always kept, so that the restore can be undone.
- with PosixFS in [collaborative mode](./posixfs.md#posixfs-collaborative-mode), when a file is changed directly in the file system and OpenCloud picks up the change. This only creates a version if `STORAGE_USERS_POSIX_ENABLE_FS_REVISIONS` is set to `true`, which is not the default.

The cleanup only looks at the file that got the new version. Files that are never changed again keep all their versions, even if the strategy would delete some of them. To clean those up too, or to apply a different strategy once, use the [command to clean up versions on demand](../../maintenance/maintenance-commands.md#clean-up-old-file-versions).

The cleanup skips a file while an upload to it is still being checked. It cleans up that file with its next version.

### The Cleanup Runs in the Background

With the default settings, the cleanup doesn't slow down uploads. When a file gets a new version, OpenCloud puts the file into a queue, and background workers clean up the files in the queue one after the other. Usually, the cleanup is done a moment after the upload.

Two settings change this, and can make uploads slower: with `OC_REVISIONS_CLEANUP_ASYNC` set to `false`, an upload waits until the cleanup of the file is done, and with `OC_REVISIONS_CLEANUP_ASYNC_QUEUE_FULL` set to `block`, an upload waits for room in the queue when the queue is full. See [Background Workers](#background-workers) below.

If a file gets several new versions while it waits in the queue, it is cleaned up only once.

## Turning the Cleanup On

The cleanup is configured with environment variables of the OpenCloud service. The most important one is `OC_REVISIONS_CLEANUP_STRATEGY`, which sets the strategy. All variables are listed in the [environment variables of the storage-users service](../../../dev/server/services/storage-users/env-vars.mdx).

### With OpenCloud Compose

If you run OpenCloud with [OpenCloud Compose](https://github.com/opencloud-eu/opencloud-compose), create a file of your own for the setting, for example `revisions-cleanup.yml` in your `opencloud-compose` directory. That way, your setting is kept when you update OpenCloud Compose.

```bash
nano opencloud-compose/revisions-cleanup.yml
```

Set the strategy for the `opencloud` service. In this example, OpenCloud keeps all versions from the last 7 days, keeps fewer versions the older they get, and deletes versions older than 90 days (the strategies are explained below):

```yaml
services:
  opencloud:
    environment:
      OC_REVISIONS_CLEANUP_STRATEGY: '7d, auto, 90d'
```

Then add the file to the `COMPOSE_FILE` variable in your `.env` file, at the end of the list. For example, if your `.env` file has

```env
COMPOSE_FILE=docker-compose.yml:traefik/opencloud.yml
```

change it to

```env
COMPOSE_FILE=docker-compose.yml:traefik/opencloud.yml:revisions-cleanup.yml
```

Restart OpenCloud to apply the change:

```bash
docker compose down
docker compose up -d
```

### With Other Installations

Set the environment variable for the OpenCloud process. How you do that depends on how you run OpenCloud. As the strategy contains spaces, mind the quotes.

In a systemd unit, for example in a drop-in file that you create with `systemctl edit` and the name of your OpenCloud unit, put the whole assignment in double quotes:

```ini
[Service]
Environment="OC_REVISIONS_CLEANUP_STRATEGY=7d, auto, 90d"
```

In an environment file, for example one that your systemd unit reads with `EnvironmentFile=`, or one that you pass to `docker run` with `--env-file`, no quotes are needed:

```env
OC_REVISIONS_CLEANUP_STRATEGY=7d, auto, 90d
```

When you start the container with `docker run` directly, quote the value for the shell:

```bash
docker run -e 'OC_REVISIONS_CLEANUP_STRATEGY=7d, auto, 90d' ...
```

Then restart OpenCloud. After changing a systemd unit, run `systemctl daemon-reload` first.

### Checking the Configuration

OpenCloud checks the strategy when it starts. If the strategy is invalid, for example because of a typo, the storage-users service doesn't start, and its log says what is wrong with the strategy. This is deliberate: a strategy that is silently ignored, or that deletes more than intended, would be worse.

To see what a strategy would delete before you configure it, run the cleanup command with `--dry-run`, see [Trying Out a Strategy](#trying-out-a-strategy) below.

## Choosing a Strategy

### Numbers and Durations

A strategy is made of up to three parts, separated by commas. Each part is one of these:

- **A number**, for example `10`, means a number of versions, counted from the newest one. `10` means "the 10 newest versions".
- **A duration**, for example `30d`, means the versions from that period of time, counted back from now. The units are `w` (weeks), `d` (days), `h` (hours), `m` (minutes) and `s` (seconds). `30d` means "the versions of the last 30 days".
- **`auto`** thins out the versions: the older the versions are, the fewer of them are kept. It is explained in more detail below.

The spaces after the commas are optional: `5, 30d` and `5,30d` are the same.

### The Example File

The examples below all use the same file, a report that was worked on over several months. Today is October 21 at 15:00, and the report has these 8 versions, besides its current content:

| Version | Saved on                                  |
| ------- | ----------------------------------------- |
| 1       | October 21, 14:50 (10 minutes ago)        |
| 2       | October 21, 14:20                         |
| 3       | October 21, 11:05                         |
| 4       | October 20, 16:30 (yesterday)             |
| 5       | October 14, 10:00 (one week ago)          |
| 6       | September 30, 09:00 (three weeks ago)     |
| 7       | August 12, 13:00 (ten weeks ago)          |
| 8       | April 2, 08:00 (more than six months ago) |

The current content of a file is never deleted by the cleanup, whatever the strategy. Only versions are.

### Keeping a Number of Versions: `10`

A single number keeps that many versions and deletes all older ones.

With `5`, OpenCloud keeps versions 1 to 5 and deletes versions 6, 7 and 8. With `10`, all 8 versions are kept, as the report has fewer than 10.

`0` deletes **all versions of every file that gets a new version**. Unlike turning versioning off with `OC_DISABLE_VERSIONING`, this also deletes the versions that already exist.

### Keeping Versions for a Period of Time: `30d`

A single duration keeps the versions of that period and deletes the older ones.

With `30d`, the period starts on September 21 at 15:00. Versions 1 to 6 are kept, versions 7 and 8 are deleted. With `14d`, the period starts on October 7, so versions 1 to 5 are kept and versions 6 to 8 are deleted.

Read [How Old Is a Version?](#how-old-is-a-version) before you choose a strategy with only a duration: a file that wasn't changed for a long time can lose all its versions at once.

### Counting From Midnight: `1D`

A duration in days or weeks counts back from the current time by default: `1d` means the last 24 hours. With an uppercase unit, `D` or `W`, it counts from midnight instead (in the time zone of the server): `1D` means "since yesterday at 00:00", `0D` means "since today at 00:00", and `1W` "since 00:00 seven days ago".

For the report, `1d` keeps the versions since yesterday at 15:00, which are versions 1 to 4. `1D` keeps the versions since yesterday at 00:00, which are also versions 1 to 4. The difference shows for a version saved yesterday at 09:00: `1d` deletes it, as it is older than 24 hours, while `1D` keeps it, because it is from yesterday.

### Thinning Out Versions: `auto`

`auto` keeps fewer versions the older they get. It divides time into slots, and keeps the newest version of each slot:

| Age of the version | `auto` keeps                 |
| ------------------ | ---------------------------- |
| less than a minute | one version every 10 seconds |
| less than an hour  | one version per minute       |
| less than a day    | one version per hour         |
| less than 30 days  | one version per day          |
| older              | one version per week         |

`auto` never deletes the only version of a slot. It deletes versions that were saved shortly after each other, of which it only needs one.

For the report, `auto` keeps all 8 versions: each one is the only version in its slot. Version 2 and version 1 are only 30 minutes apart, but they are less than an hour old, so each of them has a slot of one minute.

Here is an example where `auto` makes a difference. A user edits a presentation yesterday afternoon and saves it six times between 14:00 and 14:05. Today, these six versions are more than a day old, so they share one slot, the one for yesterday. `auto` keeps the newest of them, the one from 14:05, and deletes the other five. If the user had saved the presentation six times within the last few minutes, `auto` would still keep all six for now, and thin them out later as they get older.

`auto` alone never deletes a version that is the only one of its week. Over the years, a file that changes every week keeps one version per week.

### Combining a Number and a Duration: `5, 30d`

With two parts, the first part sets what is always kept, and the second part sets what is deleted:

- `5, 30d` deletes versions older than 30 days, but always keeps the 5 newest versions, however old they are.
- `7d, 10` keeps the 10 newest versions, and also every version from the last 7 days, even if there are more than 10 of them.

Let's look at the report again. Today is October 21 at 15:00:

| Version | Saved on                                  |
| ------- | ----------------------------------------- |
| 1       | October 21, 14:50 (10 minutes ago)        |
| 2       | October 21, 14:20                         |
| 3       | October 21, 11:05                         |
| 4       | October 20, 16:30 (yesterday)             |
| 5       | October 14, 10:00 (one week ago)          |
| 6       | September 30, 09:00 (three weeks ago)     |
| 7       | August 12, 13:00 (ten weeks ago)          |
| 8       | April 2, 08:00 (more than six months ago) |

For the report, `5, 30d` keeps versions 1 to 6: versions 1 to 5 are the 5 newest, and version 6 is from the last 30 days. Versions 7 and 8 are deleted.

`5, 30d` is a good choice for files that are rarely changed. Take a contract that was edited a few times in spring and then put aside. When someone changes it again in October, all its versions are months old. `30d` alone would delete all of them right away. `5, 30d` keeps the 5 newest, so the content from before the October change can still be restored.

One part must be a number and the other a duration. Two numbers or two durations, like `5, 10`, are rejected, as one of them would have no effect: `5, 10` is the same as `10`. The error message tells you which value to use instead.

The versions of the first part are always kept, whatever the second part says. The number counts all versions, including the ones the first part keeps anyway. For the report, which has 4 versions from the last 7 days:

- `7d, 5` keeps versions 1 to 5: versions 1 to 4 are from the last 7 days, and version 5 makes 5 versions in total. It doesn't keep 5 versions in addition to the 4 from the last 7 days.
- `7d, 2` keeps versions 1 to 4. They are from the last 7 days, so they are kept, although that's more than 2.

### Combining `auto` With a Number or a Duration

`auto` can be combined with a number or a duration before or after it:

- **`14d, auto`** keeps all versions of the last 14 days, and thins out the older ones with `auto`.
- **`auto, 90d`** deletes versions older than 90 days, and thins out the rest with `auto`.
- **`auto, 50`** keeps at most 50 versions, and thins them out with `auto`.
- **`7d, auto, 90d`** keeps all versions of the last 7 days, deletes versions older than 90 days, and thins out the versions in between.

For the report, `7d, auto, 90d` keeps versions 1 to 4, as they are from the last 7 days. Versions 5, 6 and 7 are between 7 and 90 days old, and `auto` keeps all three, as each is the only version of its slot. Version 8 is older than 90 days and is deleted.

With a number after `auto`, as in `auto, 50`, the number is applied first, and `auto` thins out the rest: `auto, 50` keeps at most 50 versions, and often fewer. It doesn't mean "thin out first, then keep 50 of what is left".

In `7d, auto, 90d` or `2, auto, 50`, the first value must be smaller than the last one, otherwise `auto` would never apply.

### Overview

| Strategy       | Meaning                                                                                 | Examples                         |
| -------------- | --------------------------------------------------------------------------------------- | -------------------------------- |
| `disabled`     | Keep all versions (the default)                                                         | `disabled`                       |
| `X`            | Delete everything beyond `X`                                                            | `10`, `30d`, `0`                 |
| `auto`         | Thin out versions the older they get                                                    | `auto`                           |
| `X, auto`      | Keep everything within `X`, thin out the older versions                                 | `14d, auto`                      |
| `auto, X`      | Delete everything beyond `X`, thin out the rest                                         | `auto, 90d`, `auto, 50`          |
| `X1, X2`       | Keep everything within `X1`, delete everything beyond `X2`; one number and one duration | `5, 30d`, `7d, 10`               |
| `X1, auto, X2` | Keep everything within `X1`, delete everything beyond `X2`, thin out in between         | `7d, auto, 90d`, `1D, auto, 30d` |

### Suggestions

Which strategy is right depends on how your users work and how much storage you have. Some starting points:

- **Keep everything recent, and a history for a few months:** `7d, auto, 90d`. Users can go back to any version of the last week, and to about one version per day or week for three months.
- **Save storage, but never lose the last few versions of a file:** `5, 30d`.
- **A fixed upper limit per file:** `auto, 50` or simply `20`.
- **Keep a long history, but not every save:** `auto`. The number of versions grows slowly, by about one per week for files that keep changing.

## How Old Is a Version?

The age of a version is the time its content was saved, which is also the date that the version list in the web interface shows for it. It is _not_ the time when the file was changed again and the content became a version.

For files that are changed often, the two are close together. For files that are left alone for a long time, they are far apart. An example:

1. On August 14, a user saves a document.
2. Nobody touches the document for two months.
3. On October 14, the user changes it. The content from August 14 becomes a version, and it is dated August 14.
4. The cleanup runs right after the change. For the cleanup, the version is 61 days old.

With a strategy that deletes by duration, like `30d`, `auto, 30d` or `7d, 30d`, this version is deleted right away. The content the document had until that morning is gone, although the user only changed it a minute ago.

To avoid this, combine the duration with a number, for example `5, 30d`, which always keeps the 5 newest versions. `auto` also helps: it always keeps one version per week, also for old content.

## Trying Out a Strategy

Before you configure a strategy, or before you change it, you can see what it would delete. The cleanup command has a dry run, which deletes nothing and lists every version with what would happen to it and why:

```bash
docker compose exec opencloud opencloud storage-users revisions cleanup --all --strategy "7d, auto, 90d" --dry-run --verbose
```

For the report from above, the output would look like this (shortened, the lines for versions 3 to 7 are left out):

```plaintext
25b69780-5f39-43be-a7ac-a9b9e9fe4230 /Documents/report.odt (node 8a1c0e2f-6b4d-4f7a-9c3e-2d5b7f1a0c94): would delete 1 of 8 revisions (2.1 MiB)
  protected 2026-10-21T14:50:00+02:00   2.3 MiB  protected by "7d": newer than 2026-10-14T15:00:00+02:00
  protected 2026-10-21T14:20:00+02:00   2.3 MiB  protected by "7d": newer than 2026-10-14T15:00:00+02:00
  ...
  deleted   2026-04-02T08:00:00+02:00   2.1 MiB  deleted by "90d": older than 2026-07-23T15:00:00+02:00
```

See [Clean up old file versions](../../maintenance/maintenance-commands.md#clean-up-old-file-versions) for all options of the command.

## Background Workers

The settings of the background workers rarely need to be changed. The defaults work for most installations.

| Variable                                        | Default         | Meaning                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `OC_REVISIONS_CLEANUP_ASYNC`                    | `true`          | Clean up in background workers. With `false`, the cleanup runs right away, and the operation that created the new version, for example the upload, waits until the cleanup is done.                                                                                                                                          |
| `OC_REVISIONS_CLEANUP_ASYNC_WORKERS`            | `0` (automatic) | The number of background workers. Automatically, half the number of CPUs, and at least 2.                                                                                                                                                                                                                                    |
| `OC_REVISIONS_CLEANUP_ASYNC_QUEUE_SIZE`         | `0` (automatic) | The number of files that can wait for a worker. Automatically, 64 per worker.                                                                                                                                                                                                                                                |
| `OC_REVISIONS_CLEANUP_ASYNC_QUEUE_FULL`         | `drop`          | What happens when the queue is full. With `drop`, the cleanup of that file is skipped, and happens with its next version instead. With `block`, the operation that created the new version, for example the upload, waits until there is room in the queue, but at most for `OC_REVISIONS_CLEANUP_ASYNC_QUEUE_FULL_TIMEOUT`. |
| `OC_REVISIONS_CLEANUP_ASYNC_QUEUE_FULL_TIMEOUT` | `5s`            | How long `block` waits for room in the queue at most, for example `5s` or `1m`. After that, the cleanup of the file is skipped, as with `drop`. With `0`, `block` waits as long as it takes: no cleanup is ever skipped, but under heavy load, uploads can get slower and slower for as long as the load lasts.              |

The queue only fills up under heavy load, when files get new versions faster than the workers can clean them up. By default, OpenCloud then skips the cleanup of the files that don't fit into the queue, so that uploads never wait for the cleanup.

A skipped cleanup isn't lost: the file is cleaned up with its next version, or by the [cleanup command](../../maintenance/maintenance-commands.md#clean-up-old-file-versions). Every skipped cleanup is logged as a warning, with the location of the file on disk:

```text
revision cleanup: queue is full, skipping the cleanup of this node until its next revision
```

If you see this warning often, add workers with `OC_REVISIONS_CLEANUP_ASYNC_WORKERS`, or make the queue larger with `OC_REVISIONS_CLEANUP_ASYNC_QUEUE_SIZE`.

If you prefer to wait for room in the queue rather than to skip cleanups, use `block`. Uploads can then get slower under heavy load, but at most by the timeout. In this example, an upload waits up to 30 seconds:

```yaml
services:
  opencloud:
    environment:
      OC_REVISIONS_CLEANUP_STRATEGY: '7d, auto, 90d'
      OC_REVISIONS_CLEANUP_ASYNC_QUEUE_FULL: 'block'
      OC_REVISIONS_CLEANUP_ASYNC_QUEUE_FULL_TIMEOUT: '30s'
```

When the timeout is over, the cleanup of the file is skipped, as with `drop`, and logged as a warning as well:

```text
revision cleanup: queue is still full after the timeout, skipping the cleanup of this node until its next revision
```

With a timeout of `0`, uploads wait as long as it takes, and no cleanup is ever skipped. Only use it if you can accept that uploads get slower and slower for as long as heavy load lasts.

When OpenCloud stops, cleanups that are already running are finished, and the cleanups still waiting in the queue are abandoned. The queue isn't stored anywhere, so these cleanups are **not resumed** when OpenCloud starts again. Each of these files is cleaned up with its next version, or by the [cleanup command](../../maintenance/maintenance-commands.md#clean-up-old-file-versions).

## Logs

For every file it deleted versions of, the cleanup writes a line at log level `info`: `revision cleanup: purged old revisions`, with the number and the size of the deleted versions. Nothing is logged for files where nothing was deleted.

At log level `debug`, every deleted version is logged as well, with the reason, for example `deleted by "30d": older than 2026-09-21T15:00:00Z`. See [Logging](../logging.md) for how to set the log level.

## Things to Keep in Mind

- **Versions count towards the quota of a space.** Deleting old versions frees storage and quota.
- **The cleanup can't be undone.** Deleted versions are gone. Try a new strategy with a dry run first.
- **Versions that are not deleted stay as they are.** The cleanup never changes a version, it only deletes versions.
- **Turning versioning off is different.** Turning versioning off with `OC_DISABLE_VERSIONING` only stops creating new versions, while the existing ones are kept. The cleanup deletes existing versions, gradually, as files get new versions, or all at once with the [cleanup command](../../maintenance/maintenance-commands.md#clean-up-old-file-versions).
