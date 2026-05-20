---
sidebar_position: 4
id: upgrade-macos
title: Upgrade Desktop Client on macOS
description: Upgrade Desktop Client on macOS
draft: false
---

# Upgrade on macOS (.pkg file)

The OpenCloud Desktop Client for macOS can be upgraded using the official signed .pkg installer.
This process safely replaces the existing application while preserving your account settings and synchronization configuration.

## Download the Latest Installer

Download the newest .pkg installer from the official release page:

- [OpenCloud Desktop Releases on GitHub](https://github.com/opencloud-eu/desktop/releases)

Choose the correct version for your Mac:

- Apple Silicon Macs (M1, M2, M3): arm64
- Intel Macs: x86_64

## Save the installer to your Downloads folder

## Close OpenCloud Desktop

## Before starting the upgrade

- Click the OpenCloud Desktop icon in the macOS menu bar.
- Open the menu.
- Select Quit OpenCloud Desktop.

This ensures that all synchronization processes are stopped cleanly before the update.

## Run the Installer

- Double-click the downloaded .pkg file.
- The macOS installer will launch automatically.
- Follow the on-screen instructions.
- When prompted, confirm that the existing installation should be replaced.

The installer updates the application inside the system’s Applications directory.

Existing accounts, synchronization folders, preferences,cached and credentials are preserved automatically.

## Launch the Updated Application

After the installation completes, launch OpenCloud Desktop from:

- the Applications folder
- Launchpad
- or Spotlight (Cmd + Space)

The client should start normally using your existing configuration.

## Verify the Installed Version

To confirm the upgrade:

- Open OpenCloud Desktop.
- In the menu bar, select:
- OpenCloud Desktop → About OpenCloud Desktop

The currently installed version number will be displayed.

:::note
Upgrading does not remove synchronized files.
Existing user accounts and sync connections remain configured.
A system restart is usually not required after upgrading.:::
