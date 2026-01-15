---
sidebar_position: 1
id: installation
title: Installation
description: Install OpenCloud Desktop Client on Linux
draft: false
---

# Installation on Linux (AppImage with AppImageLauncher)

The OpenCloud Desktop Client is available as an AppImage for Linux.  
Using AppImageLauncher is recommended to ensure proper system integration, menu entries, and simplified updates.

## Install AppImageLauncher

AppImageLauncher integrates AppImages into your system and manages them like regular applications.

Follow the installation instructions here:

[AppImageLauncher Installation Guide](https://github.com/TheAssassin/AppImageLauncher/releases/tag/v3.0.0-beta-3)

## Download the OpenCloud AppImage

Download the latest or desired `.AppImage` version from the official release page:

- [OpenCloud Desktop Releases on GitHub](https://github.com/opencloud-eu/desktop/releases)

Save the file to your preferred download directory.

## Integrate the AppImage

Once AppImageLauncher is installed:

1. Right-click the downloaded `OpenCloud.AppImage`.
2. Select “Open with AppImageLauncher”.
3. Confirm integration when prompted.

AppImageLauncher will automatically:

- store the AppImage in the correct location
- register a menu entry
- ensure the app behaves like a native application

## Launching OpenCloud Desktop

After integration, you can start the client as usual through your application menu:

- open your Application Launcher
- search for OpenCloud Desktop
- start the application

The client will guide you through the initial setup.

## Updating the AppImage

When a new version is available, download the updated AppImage from GitHub.  
AppImageLauncher will detect it and offer to replace the existing version automatically.

## Uninstallation

To remove the OpenCloud Desktop Client:

1. Open your application menu.
2. Search for OpenCloud Desktop
3. Select the option to remove or uninstall the AppImage (menu wording may vary depending on distribution and launcher).

AppImageLauncher will cleanly remove the integrated AppImage.
