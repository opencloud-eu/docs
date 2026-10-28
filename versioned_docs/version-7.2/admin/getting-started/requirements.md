---
sidebar_position: 1
id: requirements
title: Requirements
description: Runs on anything from a Raspberry Pi to a data center.
draft: false
---

## Server Requirements

| Category                | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Server Operating System | <ul><li>Production: Linux</li><li>Testing and development: MacOS or Windows WSL</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Database                | <ul><li>None (OpenCloud stores files exclusively on the storage to minimize complexity and ensure maximum reliability)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Storage                 | <ul><li>The `posix` and `decomposed` storage drivers require:<ul><li>a fully POSIX compliant filesystem <ul><li> local e.g. ext4, XFS, ZFS</li><li>network e.g. CephFS, GPFS, NFS v4.2 or later</li></ul></li><li>atomic read after write consistency for directory metadata (NFS mount option `noac`)</li></ul></li><li>`decomposeds3` additionally requires an S3 bucket</li><li>`posix` requires extended attributes (offloading metadata >1KB into dedicated files)</li></ul>                                                                                                                                                                                                                                                                                 |
| Hardware requirements   | Minimum (Minimal bare-metal Deployment - Up to 10 Users) <ul><li>eg. Raspberry Pi 3</li><li>1 GHz (Single-core)</li><li>512 MB Ram</li><li>Storage: depends on data usage</li></ul> Medium (Deployment - Up to 1,000 Users) <ul><li>2 GHz (Dual-core)</li><li>8 GB Ram</li><li>Storage: depends on data usage</li></ul> General: <ul><li>Disk Performance (IOPS): Input/output operations per second (IOPS) should be unrestricted for maintaining optimal performance.</li><li>The server requirements vary based on load factors such as requests per second, number of client devices per user, file volume, post-processing tasks, and additional apps like Collabora. Proper sizing depends on these variables and should be adjusted accordingly.</li></ul> |

## Client Requirements

### Web Client

The OpenCloud Web Client requires a supported web browser. Supported versions follow the OpenCloud Web browser policy and exclude versions classified as end-of-life.

| Browser         | Supported versions                          |
| :-------------- | :------------------------------------------ |
| Google Chrome   | Releases from the last year                 |
| Mozilla Firefox | Firefox ESR and releases from the last year |
| Microsoft Edge  | Releases from the last year                 |
| Apple Safari    | Releases from the last year                 |

### Desktop Client

The OpenCloud Desktop Client is designed for file synchronization on local desktop computers and is not intended for use in Virtual Desktop Infrastructure (VDI) environments.

The following requirements are based on the ownCloud Desktop documentation and are provisional until confirmed by the OpenCloud Desktop developers.

| Operating system                | Supported versions                                                                                             |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------- |
| Windows (x64)                   | Windows 10 (version 1809 or later), Windows 11                                                                 |
| macOS (Intel and Apple Silicon) | macOS 13 or later                                                                                              |
| Linux (x86-64)                  | Latest two versions of supported distributions and the previous Ubuntu LTS release, where technically feasible |

For installation and setup information, see the [Desktop Client documentation](../../user/desktop-client/).

### Mobile Apps

OpenCloud provides mobile apps for Android and iOS/iPadOS.

| Platform     | Minimum supported OS version |
| :----------- | :--------------------------- |
| Android      | Android 8.0 or later         |
| iOS / iPadOS | iOS 15.4 or later            |

For installation and setup information, see the [Android App documentation](../../user/android-app/) and [iOS App documentation](../../user/ios-app/).
