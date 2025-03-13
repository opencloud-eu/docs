---
sidebar_position: 8
id: storage-posix
title: "Storage: Posix"
draft: true
---

# PosixFS Storage Driver

PosixFS is a storage driver that saves OpenClouds files and folders in a folder structure how the user sees that in the web interface or other clients. That is a difference compared to DecomposedFS, which stores files in a technical folder structure that has limited meaning for admins.

There are two modes to destinguish:

1. *non collaborative mode* where the filesystem tree in use is exclusively granted to OpenCloud
2. *collaborative mode* where modifications of the underlying file tree are permitted by other processes than OpenCloud

The *collaborative mode* is not yet available and follow later.

## Metadata

To allow OpenCloud to work database less, extra metadata is stored in the extended file attributes of each file. To mitigate size limitations for extended file attributes of file systems, metadata is moved to an extra metadata file if overall size exceeds a certain limit. In that case, only a reference to the meta data file is kept in the extended file attributes.

## Access Model

PosixFS in *non collaborative mode* must not be changed manually in the file system while OpenCloud is up and running. The assigned file system tree has to be exclusive granted for OpenClouds access.

File- and folder permissions must be set to the same user and group that OpenCloud is running under. That is happening autmatically as long as the root directory of the tree is writeable.

### External Access

When OpenCloud is shut down, limited manipulation of the underlying file system tree is possible for certain administration tasks such as

- adding files and folders
- removing files and folders
- renaming files and folders

:::warning

Whenever files are manipulated externally of OpenCloud, it is important to remember to

- shut down OpenCloud before starting
- do not loose the extended file attributes of individual files
- set the file- and folder permissions correctly

:::

## Backup

With PosixFS backup and restore is easy. The entire OpenCloud filesystem tree can be snapshotted regularly and restored as needed. It depends on the filesystem type how that has to be done in detail.

## Migration

PosixFS in this so called *non collaborative mode* is the default for new installations of OpenCloud. There is currently no way to migrate OpenCloud installations with DecomposedFS backend to PosixFS.

If that is needed, data needs to be copied into a new installation of OpenCloud with PosixFS.

# Configuration

T collaborative PosixFS storage driver is part of the default OpenCloud bundle.

Involved configuration settings (environment variables) to enable PosixFS are:

- `STORAGE_USERS_DRIVER` needs to be set to `posix`
- `STORAGE_USERS_ID_CACHE_STORE` needs to be set to `nats-js-kv`
- `STORAGE_USERS_POSIX_ROOT` can be omitted for default, or set the storage root directory

---


