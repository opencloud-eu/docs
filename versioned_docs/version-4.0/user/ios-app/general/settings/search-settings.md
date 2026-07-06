---
sidebar_position: 2
title: Search Settings
description: Configure the default search scope used by the OpenCloud iOS app.
draft: false
---

# Search Settings

The **Search Settings** allow you to define the default search scope that is used whenever you search for files and folders in the OpenCloud iOS app.

## Open Search Settings

1. Open the **OpenCloud** app.
2. Tap **Settings**.
3. Under **User Interface**, tap **Search Settings**.

The **Search Settings** page allows you to choose the default scope for all searches.

<img src={require("../../img/settings/search-settings/search settings button.png").default} alt="Search Settings Button" height="650"/>

## Available Search Scopes

You can choose one of the following default search scopes:

- **Folder** – Searches only the currently opened folder.
- **Tree** – Searches the current folder and all of its subfolders.
- **Space** – Searches only within the currently opened space.
- **Account** – Searches the complete personal account across all spaces.
- **Server** – Performs a server-wide search.

<img src={require("../../img/settings/search-settings/search settings menu.png").default} alt="Search Settings Menu" height="650"/>

## How Search Settings Work

The selected search scope becomes the default whenever you start a new search.

You can still change the search scope manually while performing a search without modifying your default preference.

:::tip

Choose the search scope that best matches your workflow:

- **Folder** for fast searches in the current directory.
- **Tree** when you also want to include subfolders.
- **Space** to search everything inside the current space.
- **Account** to search all files you have access to.
- **Server** when you want the broadest possible search across the server.

:::

:::note

Changing the default search scope only affects **future searches**. Existing search results are not modified.

:::
