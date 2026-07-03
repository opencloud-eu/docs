---
sidebar_position: 3
title: Logging
description: Enable application logging and browse generated log files for troubleshooting.
draft: false
---

# Logging

The **Logging** settings allow you to enable diagnostic logging, browse generated log files, and share them when troubleshooting issues.

## Open Logging Settings

1. Open the **OpenCloud** app.
2. Tap **Settings**.
3. Under **User Interface**, tap **Logging**.

The **Logging** page lets you enable or disable logging and manage the generated log files.

<img src={require("../../img/settings/logging/logging-button.png").default} alt="Logging Button" height="650"/>

## Enable Logging

Diagnostic logging can help identify and troubleshoot issues with the OpenCloud app.

- Enable **Enable logging** to start collecting diagnostic information.
- Tap **Browse** to view the stored log files.

<img src={require("../../img/settings/logging/logging-menu.png").default} alt="Logging options" height="650"/>

:::warning

Logging may slightly impact application performance and can include sensitive information such as server URLs or user-related data.

Only enable logging when troubleshooting an issue.

:::

## Browse and Share Log Files

Selecting **Browse** opens the list of available log files stored on your device.

From this screen you can:

- View available log files.
- Share a log file using the **Share** button.
- Delete all stored log files using **Delete all**.

<img src={require("../../img/settings/logging/log-files-list.png").default} alt="Log files" height="650"/>

## How Logging Works

The OpenCloud iOS app stores log files locally on your device.

:::tip

Enable logging only while reproducing an issue. After collecting the required information, disable logging again to minimize performance impact and storage usage.

:::

:::note

- Log files remain on your device until you delete them.
- They are **not automatically uploaded** to OpenCloud servers.
- Up to the **10 most recent archived log files** are retained.
- Each log file can contain up to **24 hours** of application activity.

:::
