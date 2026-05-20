---
sidebar_position: 5
id: upgrade-linux
title: Upgrade Desktop Client on Linux
description: Upgrade Desktop Client on Linux
draft: false
---

# Upgrade on Linux

The OpenCloud Desktop Client on Linux can be upgraded using the package format or package manager originally used for installation.
Existing synchronization settings, accounts, and preferences are preserved during the upgrade process.

## Upgrade on Debian / Ubuntu (.deb package)

Download the latest .deb package from the official release page:

- [OpenCloud Desktop Releases on GitHub](https://github.com/opencloud-eu/desktop/releases)
- Choose the package matching your system architecture.
- Save the file to your Downloads folder.
- Close OpenCloud Desktop

## Before upgrading

- Open the OpenCloud Desktop menu.
- Stop active synchronization if necessary.
- Quit the application completely.
- Install the Updated Package

## Install the Upgrade

- Open a terminal and navigate to your Downloads directory:

```bash
cd ~/Downloads
```

- Install the updated package:

```bash
sudo dpkg -i opencloud-desktop_version.deb
```

- If dependency issues occur, repair them using:

```bash
sudo apt -f install
```

The existing installation will be updated automatically.

- Launch the Updated Application

- After installation, start OpenCloud Desktop from:
  - the application menu
    GNOME/KDE launcher
  - or from a terminal:
    opencloud

Your existing configuration and synchronization settings remain available.

## Verify the Installed Version

- To check the installed version:

```bash
opencloud --version
```

- You can also verify the version from within the graphical application:
  - Help → About OpenCloud Desktop

## If OpenCloud Desktop was installed from a configured repository, upgrade it using the package manager

- Update Package Information

```bash
sudo apt update
```

- Upgrade OpenCloud Desktop

```bash
sudo apt upgrade
```

- Or upgrade only the desktop client:

```bash
sudo apt install --only-upgrade opencloud-desktop
```

## Upgrade on Fedora / RHEL (.rpm package)

- Download the newest .rpm package from:

[OpenCloud Desktop Releases on GitHub](https://github.com/opencloud-eu/desktop/releases)

- Save the package locally.

- Install the Updated Package

```bash
sudo dnf install opencloud-desktop_version.rpm
```

The package manager upgrades the existing installation automatically.

## Verify the Installation

```bash
opencloud --version
```

:::note
User accounts and synchronization settings are preserved during upgrades.
Existing synchronized files are not modified or removed.
Restarting the system is typically not required after upgrading.
:::
