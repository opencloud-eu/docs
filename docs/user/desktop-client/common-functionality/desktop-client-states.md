---
sidebar_position: 5
id: desktop-client-states
title: Desktop Client State
description: Desktop Client State Icons
draft: false
---

## Understanding Desktop Client State Icons

The OpenCloud Desktop Client uses tray icons to show the current synchronization and connection state. This helps you quickly see whether everything is working normally or if something needs attention.

## Quick Overview

| Icon                                                                                                                              | State         | Meaning                                                              | Typical action                                         |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------------------------------------------------------------------- | ------------------------------------------------------ |
| <img src={require(".././img/desktop-client-states/ocl-ui_logo-petrol.png").default} alt="Ready state" width="28"/>                | Ready         | The client is connected and all files are up to date.                | No action required.                                    |
| <img src={require(".././img/desktop-client-states/ocl-ui_sync-petrol-colour.png").default} alt="Synchronizing state" width="28"/> | Synchronizing | Files are currently being uploaded or downloaded.                    | Wait until synchronization is complete.                |
| <img src={require(".././img/desktop-client-states/ocl-ui_pause-petrol-colour.png").default} alt="Paused state" width="28"/>       | Paused        | Synchronization has been temporarily stopped.                        | Resume synchronization when you are ready.             |
| <img src={require(".././img/desktop-client-states/ocl-ui_offline-petrol-colour.png").default} alt="Offline state" width="28"/>    | Offline       | The client cannot connect to the OpenCloud server.                   | Check your network connection and server availability. |
| <img src={require(".././img/desktop-client-states/ocl-ui_info-petrol-colour.png").default} alt="Information state" width="28"/>   | Information   | The client shows a non-critical informational message.               | Review the message for details if needed.              |
| <img src={require(".././img/desktop-client-states/ocl-ui_error-petrol-colour.png").default} alt="Error state" width="28"/>        | Error         | The client encountered a problem that blocks normal synchronization. | Open the client and resolve the reported issue.        |

## Ready

The Ready icon appears when the Desktop Client is connected to OpenCloud and no synchronization activity is currently taking place.

- Connected to OpenCloud
- No active file transfers
- All files are up to date

<img src={require(".././img/desktop-client-states/ocl-ui_logo-petrol.png").default} alt="Ready state" width="100"/>

No action is required. Your files are fully synchronized.

## Synchronizing

The Synchronizing icon indicates that files are currently being uploaded or downloaded.

- Files are being synchronized
- Changes are actively being processed
- The client is communicating with the server

<img src={require(".././img/desktop-client-states/ocl-ui_sync-petrol-colour.png").default} alt="Synchronizing state" width="100"/>

Wait until synchronization is complete before shutting down your device.

## Paused

The Paused icon appears when synchronization has been temporarily paused.

- Synchronization is stopped
- No files are transferred
- Local and remote changes are not synchronized

<img src={require(".././img/desktop-client-states/ocl-ui_pause-petrol-colour.png").default} alt="Paused state" width="100"/>

Resume synchronization from the Desktop Client menu when you are ready to continue syncing files.

## Offline

The Offline icon indicates that the Desktop Client cannot currently connect to the OpenCloud server.

- No connection to the server
- Synchronization is unavailable
- Local files remain accessible

<img src={require(".././img/desktop-client-states/ocl-ui_offline-petrol-colour.png").default} alt="Offline state" width="100"/>

Common causes include:

- No internet connection
- Server unavailable
- DNS or network issues
- Firewall restrictions

Verify your network connection and confirm that the OpenCloud server is reachable.

## Information

The Information icon is used for informational messages that do not require immediate user action.

- General notifications
- Non-critical events
- Informational client messages

<img src={require(".././img/desktop-client-states/ocl-ui_info-petrol-colour.png").default} alt="Information state" width="100"/>

Review the message for additional details if needed.

## Error

The Error icon indicates that the Desktop Client encountered an issue that prevents normal synchronization.

- Synchronization failed
- Authentication issues
- Configuration problems
- File access or permission errors

<img src={require(".././img/desktop-client-states/ocl-ui_error-petrol-colour.png").default} alt="Error state" width="100"/>

Open the Desktop Client and review the reported error. Synchronization may not continue until the issue has been resolved.

:::info
The visual appearance and coloring of the icons in the taskbar (Windows), dock (macOS), or system tray/panel (Linux) may vary depending on the operating system.
:::
