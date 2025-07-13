---
sidebar_position: 1
id: storage-posix
title: "PosixFS"
---

# PosixFS Storage Driver

PosixFS is a storage driver that saves OpenClouds files and folders in a folder structure how the user sees that in the web interface or other clients. That is a difference to the previously used driver DecomposedFS, which stores files in a technical folder structure that has limited meaning for admins.

PosixFS Driver supports two different modes:

1. The _non collaborative mode_ where the filesystem tree in use is exclusively granted to OpenCloud
2. The _collaborative mode_ where modifications of the underlying file tree are permitted by other processes than OpenCloud

# General Notes

The following general notes apply to both modes of the driver.

## Metadata

To enable OpenCloud to operate without a database, additional metadata is stored using the extended file attributes of each file. If the total size of this metadata exceeds the limitations imposed by the underlying file system, it is automatically moved to a separate metadata file. In such cases, only a reference to this metadata file remains in the extended attributes. This entire process is handled transparently by OpenCloud.

## Access Model

To ensure reliable operation in _non-collaborative mode_, the underlying file system used by the PosixFS driver **must not** be modified while OpenCloud is running. The assigned file system tree must be exclusively reserved for access by OpenCloud.
All files and directories must be owned by the same user and group under which the OpenCloud process is running. File and directory permissions must allow OpenCloud to read, write, and traverse the entire tree.

These conditions are automatically fulfilled as long as the root directory of the assigned tree is writable.

### Assimilation

When OpenCloud starts up, it scans the assigned file system tree for newly added or modified files and directories. During this process, metadata is updated and internal caches are built accordingly. This is referred to as the _assimilation_ of new resources.

It is important to note that assimilation does **not** trigger post-upload checks, such as virus scanning. Since the files are already in their final location within the file system, such checks would be ineffective at this stage and are therefore skipped.

However, indexing for the search service **does** take place for assimilated resources.

## Startup

When OpenCloud with PosixFS starts up, it is running over the entire file system to warm up the caches. This might take some time.

## Backup

With PosixFS backup and restore is easy. The entire OpenCloud filesystem tree can be snapshotted regularly and restored as needed. It depends on the filesystem type how that has to be done in detail.

## Migration

PosixFS in this so called _non collaborative mode_ is the default for new installations of OpenCloud. There is currently no way to migrate OpenCloud installations with DecomposedFS backend to PosixFS.

If that is needed, data needs to be copied into a new installation of OpenCloud.

# PosixFS Non Collaborative Mode

This describes special aspects of the non collaborative mode.

## External Access

When OpenCloud is shut down, limited manipulation of the underlying file system tree is possible for certain administration tasks such as

- adding files and folders
- removing files and folders
- renaming files and folders

:::warning

Whenever files are manipulated externally to OpenCloud, it is important to remember to

- shut down OpenCloud before starting
- do not lose the extended file attributes of individual files
- set the file- and folder permissions correctly

:::

## Configuration

The PosixFS storage driver is part of the default OpenCloud bundle.

Involved configuration settings (environment variables) to enable PosixFS are:

- `STORAGE_USERS_DRIVER` defaults to `posix` from version `2.0.0`, in older versions it needs to be explicitly set
- `STORAGE_USERS_ID_CACHE_STORE` needs to be set to `nats-js-kv`
- `STORAGE_USERS_POSIX_ROOT` can be omitted for default, or set the storage root directory

# PosixFS Collaborative Mode

This section describes the collaborative mode of the PosixFS driver, which allows the file system to be modified while OpenCloud is running. Changes made in this mode are reflected in real time in OpenCloud clients.

## Usage

Collaborative mode should always be used with caution. It is intended only for well-defined use cases that are carefully planned, configured, and tested. Operation must take place in a controlled environment.

Compared to non-collaborative mode, collaborative mode requires significantly more system resources to monitor the file system. Server hardware must be appropriately sized to handle this increased load.

## External Access

External access to files is permitted under specific conditions. File changes are detected and assimilated in real time.

The following guidelines are critical for smooth and reliable operation:

- Creating new files and folders is the preferred method of external modification.
- Do **not use** symbolic links.
- Moving files across OpenCloud spaces is not supported and will not be detected as such.
- Editing or deleting large numbers of files may cause errors in tree size calculation.
- Continuously monitor server system resources to identify potential bottlenecks.
- Carefully configure components such as Apache Tika to optimize indexing performance.

It is essential to maintain correct file ownership and permissions when modifying the file system externally. Files must be created with the correct user and permissions from the outset. Retroactive changes are discouraged, as assimilation may already be in progress.

## Configuration

In addition to the configuration required for non-collaborative mode, the following setting must be enabled for local file systems such as XFS, ext4, and others:

```
STORAGE_USERS_POSIX_WATCH_FS=true
```
