---
sidebar_position: 3
id: file-drop
title: File Drop
description: File Drop (secret)
draft: false
---

# File Drop (secret) - How it works

File Drop lets people who receive a specific link, the so-called link recipients, upload files to a shared folder.
Link recipients cannot see the files that are already in the folder.

## Create a File Drop

- Right-click the file or folder, or click the three-dot menu next to its name, to open the context menu.
- Select “Share” from the context menu.
  <img src={require("./img/file-drop/share-drop-down-menu.png").default} alt="Drop down menu" width="1920" />
- A sidebar window will open on the right-hand side of the screen.
  <img src={require("./img/file-drop/sidebar-window.png").default} alt="Sidebar window" width="400"/>
- In the sidebar window, find the “Public links” section and click “Add link”.
  <img src={require("./img/file-drop/add-link-button.png").default} alt="Add link button" width="400"/>
- Click "Options" to open the link settings.
- Open the access rights dropdown menu and select "Secret File Drop".
  <img src={require("./img/file-drop/file-drop-button.png").default} alt="Select file drop" width="1920"/>

- Enter a password and click “Copy link” to confirm.
- You can also set an “Expiry date” if you want the link to expire.
  <img src={require("./img/file-drop/password-and-copy-link-button.png").default} alt="Enter password and copy link" width="1920"/>
- Share the link and password with the recipient.

## What the recipient does

- The recipient opens the received link in a browserand enters the password and clicks “Continue”.
  <img src={require("./img/file-drop/password-and-continue.png").default} alt="Enter password and continue" width="1920"/>
- Upload files:
  - The File Drop folder opens. The recipient can upload files without seeing the existing contents of the folder.
    <img src={require("./img/file-drop/file-drop-area.png").default} alt="File drop area" width="1920"/>
  - A pop-up window appears in the lower right corner to confirm that the upload was successful.
    <img src={require("./img/file-drop/upload-confirmation.png").default} alt="Upload confirmation" width="1920"/>

:::important
Recipients do not have access to existing files. They can only add new files.
:::

Now you know how to share a File Drop link.
