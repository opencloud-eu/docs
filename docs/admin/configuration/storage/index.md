---
sidebar_position: 0
id: storage
title: 'Storage'
description: 'Configure storage backends, default user quotas, and file version cleanup in OpenCloud'
draft: false
---

# Storage

Decide where and how OpenCloud stores files.  
This section describes the available storage drivers, how to set default quotas for new users, and how to automatically clean up old file versions.

## In this section

- [PosixFS storage driver](./posixfs.md)  
  Store files in a regular filesystem with the same folder structure users see in OpenCloud, optionally in collaborative mode.

- [DecomposedS3 storage driver](./decomposeds3.md)  
  Store files in S3-compatible object storage such as MinIO.

- [Set default quota per user role](./set-default-quota.md)  
  Assign a default storage quota to new users based on their role.

- [Cleaning Up Old Versions](./revisions-cleanup.md)\
  Automatically delete old file versions according to a cleanup strategy.
