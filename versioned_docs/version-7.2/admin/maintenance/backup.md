---
sidebar_position: 2
id: backup
title: Backup
description: Backup
draft: false
---

# Backup

Regular backups are essential to ensure that your OpenCloud instance can be restored in case of issues

## General considerations

### Storage Options

OpenCloud supports two different storage setups:

- Pure POSIX Setup: All data (configuration, blobs, and metadata) is stored on a POSIX-compliant filesystem.

- Distributed Setup: Blobs are stored on an S3-compliant storage, while configuration and metadata remain on a POSIX-compliant filesystem

To determine which filesystems are supported, see: Filesystems and Shared Storage

## Backup strategies

### Consistent Backup Requirement

To create a consistent backup, the OpenCloud instance must be stopped before starting the backup process. After the backup is complete, the instance can be restarted

There are two recommended approaches:

- Snapshot-based backup (recommended)
  - If your storage system supports snapshots, creating a backup only takes a few seconds

  - Snapshots should be copied to secondary storage or used by backup software for additional security

- Backup software approach

- If snapshots are not available, you can use any backup software of your choice
- For more details on data locations, refer to the Default Paths documentation

## Required backup components

- Configuration data

- System data (shares the root path with metadata if not defined separately)

- Metadata (varies depending on the storage setup)

- Blobs (stored with metadata on POSIX or separately on S3)

- ⚠️ If the search index is not backed up, it must be recreated after restoration.

- Additionally, consider backing up:

- The OpenCloud binary or container used

- The configuration files

- This ensures compatibility when restoring and prevents issues caused by software version mismatches

## Pure POSIX setup

If all data (configuration, blobs, and metadata) is stored on a POSIX-compliant filesystem

- Stop the OpenCloud instance

- Create a backup of all data sets

- If everything is on one filesystem, this is straightforward

- If separate filesystems are used for configuration and blobs/metadata, back up each one individually

- Restart the OpenCloud instance after the backup is complete

## Distributed setup

If blobs are stored on S3, while configuration and metadata remain on a POSIX-compliant filesystem

- Stop the OpenCloud instance

- Back up the configuration and metadata

- Back up the S3 bucket according to the guidelines of your S3 provider

- Restart the OpenCloud instance after the backup is complete

:::note
With these backup strategies, you can ensure that your OpenCloud instance remains secure and restorable in case of issues
:::
