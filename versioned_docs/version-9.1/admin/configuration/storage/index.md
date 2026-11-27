---
sidebar_position: 0
id: storage
title: 'Storage'
description: 'Configure the storage backend and default user quotas in OpenCloud'
draft: false
---

# Storage

Decide where and how OpenCloud stores files.  
This section describes the available storage drivers and how to set default quotas so that new users automatically receive a defined amount of storage.

## In this section

- [PosixFS storage driver](./posixfs.md)  
  Store files in a regular filesystem with the same folder structure users see in OpenCloud, optionally in collaborative mode.

- [DecomposedS3 storage driver](./decomposeds3.md)  
  Store files in S3-compatible object storage such as MinIO.

- [Set default quota per user role](./set-default-quota.md)  
  Assign a default storage quota to new users based on their role.
