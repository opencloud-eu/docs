---
sidebar_position: 130
id: e2ee-folders
title: End-to-End Encrypted Folders
description: Create, unlock, and use end-to-end encrypted folders in OpenCloud.
draft: false
---

# End-to-End Encrypted Folders

End-to-end encrypted folders provide an additional layer of protection for sensitive content in OpenCloud.

When you create an end-to-end encrypted folder, you set a separate password for it. You need this password whenever you unlock the folder and access its contents on a device.

:::danger

Keep the password for an end-to-end encrypted folder in a safe place. OpenCloud cannot reset or recover it. If you lose the password, you permanently lose access to the folder and its contents.

:::

## Create an end-to-end encrypted folder

To create an end-to-end encrypted folder:

1. Go to the location where you want to create the encrypted folder.
2. Open the “+ New” menu.
3. Select “Folder”.

<img src={require("./img/e2ee-folders/create-folder-menu.png").default} alt="Create a new folder from the New menu" width="1920"/>

## Enable end-to-end encryption

In the “Create a new folder” dialog:

1. Enter a folder name.
2. Enable “End-to-end encrypt this folder”.

<img src={require("./img/e2ee-folders/create-folder-name.png").default} alt="Create a new folder dialog" width="400"/>

When end-to-end encryption is enabled, OpenCloud automatically adds the `.vault` suffix to the folder name.

<img src={require("./img/e2ee-folders/encryption-enabled.png").default} alt="End-to-end encryption enabled for the new folder" width="400"/>

Click “Continue”.

## Set the folder password

After enabling end-to-end encryption, you must set a password for the folder.

This password unlocks the encrypted folder and is required to access the files inside it.

<img src={require("./img/e2ee-folders/set-password.png").default} alt="Set a password for the encrypted folder" width="400"/>

The dialog provides the following controls:

- “Show password” displays the password you entered.
  <img src={require("./img/e2ee-folders/show-password.png").default} alt="Show password button" width="400"/>

- “Copy password” copies the password to the clipboard.
  <img src={require("./img/e2ee-folders/copy-password.png").default} alt="Copy password button" width="400"/>

:::important

Store the password in a safe place, such as a password manager.

:::

Click “Create”.

## Identify an encrypted folder

The encrypted folder appears in the file list with a lock icon.

<img src={require("./img/e2ee-folders/encrypted-folder-created.png").default} alt="Encrypted folder created in OpenCloud" width="1920"/>

The lock icon indicates that the folder is end-to-end encrypted.

## Unlock an encrypted folder

When opening an encrypted folder, you are asked to enter the folder password.

<img src={require("./img/e2ee-folders/unlock-folder.png").default} alt="Unlock an end-to-end encrypted folder" width="400"/>

Enter the password and click “Unlock”.

After unlocking the folder, you can access its contents on this device.

<img src={require("./img/e2ee-folders/unlocked-folder.png").default} alt="Unlocked encrypted folder" width="1920"/>

:::note

You must enter the password on each device where you want to access the encrypted folder.

:::

## Add files to an encrypted folder

After unlocking an encrypted folder, you can add files by uploading existing files or by creating supported file types directly in the folder.

### Upload files

You can upload existing files or folders to an encrypted folder in the same way as to any other folder.

For details, see [Upload files or folders](./upload-download-unzip.md#upload-files-or-folders).

### Create files

Only the following file types can be created directly inside an encrypted folder:

- Markdown files
- OC Notes

Other file types, such as documents, spreadsheets, and presentations, are not available for direct creation in encrypted folders.

<img
src={require("./img/e2ee-folders/create-file-menu.png").default}
alt="New menu in an encrypted folder with document, spreadsheet, and presentation options disabled"
width="1920"
/>

For details about creating files, see [Create files and folders](./create-rename-move.md#create-files-and-folders).

## Preview and download behavior

Some files in end-to-end encrypted folders cannot be previewed directly in the browser.

In this case, OpenCloud indicates that no preview is available and offers the file for download instead.

<img src={require("./img/e2ee-folders/no-preview-available.png").default} alt="No preview available for a file in an encrypted folder" width="1920"/>

## Limitations

End-to-end encrypted folders are designed for storing sensitive data. Because their contents are encrypted, some OpenCloud features are not available.

The following limitations apply:

- Files and folders cannot be moved from another location in OpenCloud into an encrypted folder.
- Collaborative editing is not available for files stored in encrypted folders.
- Office documents cannot be opened or edited in the browser with Collabora.
- In-browser previews are not available for encrypted files.

You can still upload existing files directly to an encrypted folder.
