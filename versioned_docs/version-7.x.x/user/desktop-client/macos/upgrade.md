---
sidebar_position: 4
id: upgrade-macos
title: Upgrade Desktop Client on macOS
description: Upgrade Desktop Client on macOS
draft: false
---

# Upgrade Desktop Client on macOS

The OpenCloud Desktop Client for macOS can be upgraded using the official signed `.pkg` installer.

The upgrade replaces the existing application while preserving your account settings, synchronization configuration, preferences, cached data, and credentials.

## Download the Latest Installer

Download the latest `.pkg` installer from the official release page:

- [OpenCloud Desktop Releases on GitHub](https://github.com/opencloud-eu/desktop/releases)

Choose the installer that matches your Mac architecture:

- Apple Silicon Macs (M1, M2, M3): `arm64`
- Intel Macs: `x86_64`

Save the installer to your Downloads folder or another location where you can easily find it.

## Close OpenCloud Desktop

Before starting the upgrade, close the running Desktop Client:

1. Click the OpenCloud Desktop icon in the macOS menu bar.
2. Open the menu.
3. Select Quit OpenCloud Desktop.

This ensures that all synchronization processes are stopped cleanly before the upgrade.

## Run the Installer

To upgrade OpenCloud Desktop:

1. Double-click the downloaded `.pkg` file.
2. Follow the instructions in the macOS installer.
3. When prompted, confirm that the existing installation should be replaced.

The installer updates the application in the Applications folder.

Existing accounts, synchronization folders, preferences, cached data, and credentials are preserved automatically.

## Launch the Updated Application

After the installation has completed, launch OpenCloud Desktop from one of the following locations:

- Applications folder
- Launchpad
- Spotlight

The client should start normally and use your existing configuration.

## Verify the Installed Version

To confirm that the upgrade was successful:

1. Open OpenCloud Desktop.
2. Open the settings.
3. Select About and check the version.

The currently installed version number is displayed in the about dialog.

:::note
Upgrading does not remove synchronized files.

Existing user accounts and sync connections remain configured.

A system restart is usually not required after upgrading.
:::
