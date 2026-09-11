---
sidebar_position: 130
id: e2ee-folders
title: End-to-End Encrypted Folders
description: Viewing the e2ee encryption for folders in OpenCloud
draft: false
---

# End-to-End Encrypted Folders

End-to-end encrypted folders provide an additional layer of protection for sensitive files in OpenCloud.

When creating an end-to-end encrypted folder, you set a separate password for the folder. This password is required to unlock and access the folder contents.

:::danger

You must remember the password for an end-to-end encrypted folder.

OpenCloud cannot reset, change, recover, or assign a new password for this folder. If the password is lost, access to the folder is permanently lost. This also means that the data inside this folder cannot be recovered.

No password means no access. If the password is lost, data loss for this folder is final.

:::

## Create an end-to-end encrypted folder

To create an end-to-end encrypted folder:

1. Go to the location where you want to create the encrypted folder.
2. Click **New**.
3. Select **Folder**.

<img src={require("./img/e2ee-folders/create-folder-menu.png").default} alt="Create a new folder from the New menu" width="1920"/>

## Enable end-to-end encryption

In the **Create a new folder** dialog:

1. Enter a folder name.
2. Enable **End-to-end encrypt this folder**.

<img src={require("./img/e2ee-folders/create-folder-name.png").default} alt="Create a new folder dialog" width="400"/>

When end-to-end encryption is enabled, OpenCloud automatically adds the `.vault` suffix to the folder name.

<img src={require("./img/e2ee-folders/encryption-enabled.png").default} alt="End-to-end encryption enabled for the new folder" width="400"/>

Click **Continue** to proceed.

## Set the folder password

After enabling end-to-end encryption, you must set a password for the folder.

This password unlocks the encrypted folder and is required to access the files inside it.

<img src={require("./img/e2ee-folders/set-password.png").default} alt="Set a password for the encrypted folder" width="400"/>

You can use the following controls while entering the password:

- **Show password** – Displays the entered password.
  <img src={require("./img/e2ee-folders/show-password.png").default} alt="Show password button" width="400"/>

- **Copy password** – Copies the entered password to the clipboard.
  <img src={require("./img/e2ee-folders/copy-password.png").default} alt="Copy password button" width="400"/>

:::important

Store the password in a safe place, for example in a password manager.

OpenCloud cannot restore access if the password is forgotten. The password cannot be reset, changed, or newly assigned later.

:::

Click **Create** to create the encrypted folder.

## Encrypted folder in the file list

After the folder has been created, it appears in the file list with a lock icon.

<img src={require("./img/e2ee-folders/encrypted-folder-created.png").default} alt="Encrypted folder created in OpenCloud" width="1920"/>

The lock icon indicates that the folder is end-to-end encrypted.

## Unlock an encrypted folder

When opening an encrypted folder, you are asked to enter the folder password.

<img src={require("./img/e2ee-folders/unlock-folder.png").default} alt="Unlock an end-to-end encrypted folder" width="400"/>

Enter the password and click **Unlock**.

After unlocking the folder, you can access its contents on this device.

<img src={require("./img/e2ee-folders/unlocked-folder.png").default} alt="Unlocked encrypted folder" width="1920"/>

:::note

The password is required to decrypt the files in the encrypted folder on the device where you access it.

Without the password, the folder contents cannot be accessed.

:::

## Upload files to an encrypted folder

After unlocking the encrypted folder, you can upload files into it.

1. Open the encrypted folder.
2. Click **New**.
3. Select **Files Upload**.
4. Choose the file from your device.

<img src={require("./img/e2ee-folders/upload-file.png").default} alt="Upload a file to an encrypted folder" width="1920"/>

The uploaded file is stored inside the encrypted folder.

## Preview and download behavior

Some files inside end-to-end encrypted folders may not be available for preview directly in the browser.

In this case, OpenCloud shows a message that no preview is available and offers the file for download instead.

<img src={require("./img/e2ee-folders/no-preview-available.png").default} alt="No preview available for a file in an encrypted folder" width="1920"/>

## Limitations

End-to-end encrypted folders are designed for storing sensitive data.

Because the contents are encrypted, some OpenCloud features may be limited, including collaboration features and in-browser previews.

:::danger

Keep the password safe.

OpenCloud cannot reset, change, recover, or assign a new password for an end-to-end encrypted folder. If the password is lost, the folder can no longer be unlocked and the data inside the folder is permanently lost.

:::
