---
sidebar_position: 5
id: dataexport
title: 'Data Export'
description: 'Information about data export.'
---

# Data Export

## Files

OpenCloud stores files by default in the file system under the path `/var/lib/opencloud/`. Any other path that is local
to the server instance running the OpenCloud backend can be configured as alternative path using the environment
variable `OC_BASE_DATA_PATH`.

Files and folders are stored in a folder structure underneath that base path in folder `data/storage/users/`.

Files are by default stored in the original format and not encrypted.

## Metadata

File metadata is stored in the file system with every file. It is either in the extended file attributes (user
namespace) or in a separate metadata file. That file is in the [MessagePack](https://msgpack.org) format and can be read
with the CLI tools for that file type.

## Configuration

Configuration files are written as yaml files by default under `$HOME/.config/OpenCloud`.

## Other

Other, non-file-related metadata such as links is also stored under the general data base path, in JSON format.
