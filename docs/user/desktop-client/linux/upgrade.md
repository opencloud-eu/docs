---
sidebar_position: 5
id: upgrade-linux
title: Upgrade Desktop Client on Linux
description: Upgrade Desktop Client on Linux
draft: false
---

# Upgrade Desktop Client on Linux

The OpenCloud Desktop Client for Linux is provided as an AppImage.

If you installed OpenCloud Desktop with AppImageLauncher, the client can be upgraded by downloading the updated AppImage and replacing the existing integrated version.

Existing accounts, synchronization settings, preferences, cached data, and credentials are preserved during the upgrade.

## Download the Latest AppImage

Download the latest `.AppImage` file from the official release page:

- [OpenCloud Desktop Releases on GitHub](https://github.com/opencloud-eu/desktop/releases)

Choose the AppImage that matches your system architecture and save it to your Downloads folder or another location where you can easily find it.

## Close OpenCloud Desktop

Before starting the upgrade, close the running Desktop Client:

1. Open the OpenCloud Desktop menu.
2. Stop active synchronization if necessary.
3. Select Quit OpenCloud Desktop.

This ensures that all synchronization processes are stopped cleanly before the upgrade.

## Replace the Existing AppImage

To upgrade OpenCloud Desktop with AppImageLauncher:

1. Right-click the downloaded `.AppImage` file.
2. Select Open with AppImageLauncher.
3. Confirm that the existing integrated version should be replaced when prompted.

AppImageLauncher replaces the existing AppImage and keeps the application menu entry available.

## Launch the Updated Application

After the upgrade has completed, start OpenCloud Desktop from your application menu:

1. Open your application launcher.
2. Search for OpenCloud Desktop.
3. Start the application.

The client should start normally and use your existing configuration.

## Verify the Installed Version

To confirm that the upgrade was successful:

1. Open OpenCloud Desktop.
2. Open the settings.
3. Select About.
4. Check the displayed version number.

The currently installed version number is displayed in the about dialog.

:::note
Upgrading does not remove synchronized files.

Existing user accounts and sync connections remain configured.

A system restart is usually not required after upgrading.
:::
