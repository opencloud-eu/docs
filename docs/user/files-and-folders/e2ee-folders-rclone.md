---
sidebar_position: 131
id: e2ee-folders-rclone
title: Access End-to-End Encrypted Folders with rclone
description: Mount an OpenCloud end-to-end encrypted folder on your computer with rclone crypt.
draft: false
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Access End-to-End Encrypted Folders with rclone

The OpenCloud Web Client encrypts end-to-end encrypted folders in the `rclone crypt` format. You can therefore mount such a folder on your computer with [rclone](https://rclone.org/). The mounted folder appears like a local folder: you open, edit, and add files with your usual applications, while the file contents and names stay encrypted on the OpenCloud server.

Files are encrypted on your computer before rclone uploads them. Files created through the mount can be opened in the OpenCloud Web Client, and files created in the Web Client can be opened through the mount.

This guide is based on OpenCloud 9.0.0. It is intended for users who are familiar with the command line.

## Overview

The setup consists of the following steps:

1. [Create the encrypted folder](./e2ee-folders.md) in the OpenCloud Web Client.
2. [Install rclone](#install-rclone) on your computer.
3. [Create an App Token](#create-an-app-token) in OpenCloud.
4. [Get the WebDAV URL](#get-the-webdav-url) of the encrypted folder.
5. [Create a WebDAV remote](#configure-the-webdav-remote) in rclone.
6. [Create a crypt remote](#configure-the-encrypted-remote) for decryption.
7. [Mount the encrypted folder](#mount-the-encrypted-folder).

## Before You Begin

You need:

- An end-to-end encrypted folder in OpenCloud and its password
- An OpenCloud App Token
- The WebDAV URL of the encrypted folder

The setup uses two rclone remotes that build on each other:

| Remote type | Example name          | Purpose                                                |
| ----------- | --------------------- | ------------------------------------------------------ |
| WebDAV      | `opencloud-e2ee`      | Connects to the encrypted `.vault` folder in OpenCloud |
| `crypt`     | `opencloud-decrypted` | Provides decrypted access to the folder contents       |

`opencloud-e2ee` and `opencloud-decrypted` are example names. You can choose any names for the remotes. What matters is that you use the chosen names consistently throughout the configuration and commands.

:::danger

Store the encrypted folder password safely. OpenCloud cannot reset or recover it. If you lose the password, you permanently lose access to the encrypted folder and its contents.

:::

The App Token and encrypted folder password are separate credentials with different purposes:

| Credential                | Purpose                                                           |
| ------------------------- | ----------------------------------------------------------------- |
| OpenCloud App Token       | Authenticates the WebDAV connection                               |
| Encrypted folder password | Used by `rclone crypt` to encrypt and decrypt the folder contents |

Do not use the App Token as the `crypt` password or the encrypted folder password as the WebDAV password.

<!-- Screenshot suggestion:
Show the E2EE folder in the OpenCloud Web Client.
Do not show real credentials, URLs, or sensitive IDs.
-->

## Install rclone

Mounting requires rclone and a FUSE or NFS component, depending on your operating system.

<Tabs groupId="operating-system">
<TabItem value="linux" label="Linux" default>

Install rclone with the official install script:

```bash
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

Install FUSE 3, for example on Debian and Ubuntu:

```bash
sudo apt install fuse3
```

For other installation methods, see the [rclone installation guide](https://rclone.org/install/).

</TabItem>
<TabItem value="macos" label="macOS">

Install rclone with the official install script:

```bash
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

:::caution

Do not install rclone with Homebrew. The Homebrew version of rclone does not support mounting.

:::

No additional software is required. On macOS, this guide uses `rclone nfsmount`, which mounts the folder through a built-in NFS server.

For other installation methods, see the [rclone installation guide](https://rclone.org/install/).

</TabItem>
<TabItem value="windows" label="Windows">

Install rclone and [WinFsp](https://winfsp.dev/) in PowerShell:

```powershell
winget install Rclone.Rclone
winget install WinFsp.WinFsp
```

WinFsp is required to mount folders on Windows. Open a new PowerShell window after the installation so that the `rclone` command is available.

For other installation methods, see the [rclone installation guide](https://rclone.org/install/).

</TabItem>
</Tabs>

Check the installation:

```bash
rclone version
```

## Create an App Token

Create a dedicated App Token for rclone in your OpenCloud account settings. Copy it when it is displayed because it cannot be shown again.

For detailed instructions, see [App Tokens](../admin/app-tokens.md).

The App Token is used as the password for the WebDAV remote. It is not the password for the encrypted folder. Your OpenCloud account password does not work with rclone.

<!-- Screenshot suggestion:
Show App Token creation in the OpenCloud account settings.
Do not show a real token or other credentials.
-->

## Get the WebDAV URL

Enable “Show WebDAV info in details view” in your OpenCloud account settings, open the details panel of the encrypted folder, and copy its WebDAV URL. For general instructions, see [Connect to a Space via WebDAV](../admin/web-dav.md).

The URL must point to the encrypted `.vault` folder, for example:

```text
https://cloud.example.com/dav/spaces/<space-id>/Encrypted.vault
```

<!-- Screenshot suggestion:
Show where the WebDAV URL of the encrypted folder can be copied in the Web Client.
Do not show real credentials or sensitive IDs.
-->

## Configure the WebDAV Remote

Run `rclone config` and create a WebDAV remote. This guide uses `opencloud-e2ee` as the example name. Use:

- The encrypted folder's WebDAV URL as the URL
- `infinitescale` as the vendor
- Your OpenCloud username as the user
- Your OpenCloud App Token as the password

When rclone writes passwords to its configuration, it stores them in obscured form. If you edit the configuration manually, use [`rclone obscure`](https://rclone.org/commands/rclone_obscure/) to create the value for `pass`. To find the configuration file on your system, run `rclone config file`.

The resulting configuration should look similar to:

```ini
[opencloud-e2ee]
type = webdav
url = https://cloud.example.com/dav/spaces/<space-id>/Encrypted.vault
vendor = infinitescale
user = <username>
pass = <obscured-app-token>
```

For more information about the backend options, see the [rclone WebDAV documentation](https://rclone.org/webdav/).

Test the WebDAV connection before continuing:

```bash
rclone ls opencloud-e2ee:
```

Replace `opencloud-e2ee` with the name of your WebDAV remote if you chose a different name.

If the connection works, rclone may display encrypted file names. This is expected for the WebDAV remote.

## Configure the Encrypted Remote

The `crypt` remote does not connect to OpenCloud directly. It adds encryption and decryption on top of the existing WebDAV remote. Create and test the WebDAV remote first.

Create a second remote with the `crypt` backend. This guide uses `opencloud-decrypted` as the example name. Configure it as follows:

- Set `remote` to the exact name of your WebDAV remote followed by a colon.
- Set `filename_encryption` to `standard`.
- Enable `directory_name_encryption`.
- Use the encrypted folder password as `password`.
- Do not configure an additional `password2` value.

The resulting configuration should look similar to:

```ini
[opencloud-decrypted]
type = crypt
remote = opencloud-e2ee:
filename_encryption = standard
directory_name_encryption = true
password = <obscured-folder-password>
```

The `remote` value always consists of the exact WebDAV remote name followed by `:`. Do not enter the WebDAV URL in this field.

If you edit the configuration manually, use [`rclone obscure`](https://rclone.org/commands/rclone_obscure/) to create the value for `password`. For more information about the backend options, see the [rclone crypt documentation](https://rclone.org/crypt/).

:::caution

The passwords stored in the rclone configuration file are obscured, not securely encrypted. Protect the configuration file from unauthorized access.

:::

Test the encrypted remote:

```bash
rclone ls opencloud-decrypted:
```

Replace `opencloud-decrypted` with the name of your `crypt` remote if you chose a different name.

rclone should display the original file names. If encrypted file names are displayed, see [Encrypted File Names Are Displayed](#encrypted-file-names-are-displayed).

## Mount the Encrypted Folder

Mount the `crypt` remote, not the WebDAV remote. Only the `crypt` remote decrypts the folder contents.

<Tabs groupId="operating-system">
<TabItem value="linux" label="Linux" default>

Create an empty folder as mount point:

```bash
mkdir -p ~/OpenCloud-Encrypted
```

Mount the encrypted folder:

```bash
rclone mount opencloud-decrypted: ~/OpenCloud-Encrypted --vfs-cache-mode writes
```

The folder is mounted as long as the command runs. Keep the terminal open while you work with the files.

To run the mount in the background, add `--daemon`:

```bash
rclone mount opencloud-decrypted: ~/OpenCloud-Encrypted --vfs-cache-mode writes --daemon
```

</TabItem>
<TabItem value="macos" label="macOS">

Create an empty folder as mount point:

```bash
mkdir -p ~/OpenCloud-Encrypted
```

Mount the encrypted folder:

```bash
rclone nfsmount opencloud-decrypted: ~/OpenCloud-Encrypted --vfs-cache-mode writes
```

The folder is mounted as long as the command runs. Keep the terminal open while you work with the files. The mounted folder is also shown in Finder.

To run the mount in the background, add `--daemon`:

```bash
rclone nfsmount opencloud-decrypted: ~/OpenCloud-Encrypted --vfs-cache-mode writes --daemon
```

</TabItem>
<TabItem value="windows" label="Windows">

Mount the encrypted folder as drive `X:` in PowerShell:

```powershell
rclone mount opencloud-decrypted: X: --vfs-cache-mode writes
```

Use a drive letter that is not in use. To let rclone choose a free drive letter, use `*` instead of `X:`.

The drive is mounted as long as the command runs. Keep the PowerShell window open while you work with the files. The drive is shown in File Explorer.

</TabItem>
</Tabs>

Replace `opencloud-decrypted` with the name of your `crypt` remote if you chose a different name.

:::note

An rclone mount provides access to files through a virtual file system. It does not create a fully synchronized local copy. An active connection to OpenCloud is required to access files that are not already cached.

:::

`--vfs-cache-mode writes` buffers changed files on your computer before they are uploaded. Most applications need this to edit files in the mounted folder, and rclone retries failed uploads. For more information, see the [`rclone mount` documentation](https://rclone.org/commands/rclone_mount/).

You can now work with the files in the mounted folder. New and changed files are encrypted on your computer and uploaded to OpenCloud.

### Verify the Mount

1. Create a small test file in the mounted folder.
2. After the upload finishes, verify that the file appears correctly in the OpenCloud Web Client.
3. Create a small file in the encrypted folder in the Web Client.
4. Verify that the file becomes accessible through the mounted folder.

:::note

Changes made in the OpenCloud Web Client can take up to five minutes to appear in the mounted folder, because rclone caches the folder structure.

:::

## Unmount the Encrypted Folder

Before unmounting, close all open files and make sure that pending uploads have completed. With VFS caching enabled, changes may still be stored locally and waiting to be uploaded to OpenCloud. Verify that recently changed files appear correctly in the Web Client before stopping rclone.

<Tabs groupId="operating-system">
<TabItem value="linux" label="Linux" default>

If the mount runs in the terminal, press <kbd>Ctrl</kbd>+<kbd>C</kbd>.

If the mount runs in the background, run:

```bash
fusermount3 -u ~/OpenCloud-Encrypted
```

On systems with FUSE 2, use `fusermount -u` instead.

</TabItem>
<TabItem value="macos" label="macOS">

If the mount runs in the terminal, press <kbd>Ctrl</kbd>+<kbd>C</kbd>.

If the mount runs in the background, run:

```bash
pgrep -fl "rclone nfsmount opencloud-decrypted: $HOME/OpenCloud-Encrypted"
```

Confirm that the output shows only the rclone process for this mount. Note the process ID at the beginning of the line, then send SIGTERM to that process:

```bash
kill -TERM <pid>
```

If you chose a different remote name or mount point, adjust the `pgrep` pattern. Do not use `killall` or an unfiltered `pkill`, because they can stop unrelated rclone processes.

</TabItem>
<TabItem value="windows" label="Windows">

Press <kbd>Ctrl</kbd>+<kbd>C</kbd> in the PowerShell window in which the mount runs.

</TabItem>
</Tabs>

## Troubleshooting

### Encrypted File Names Are Displayed

Encrypted file names are expected when you use the WebDAV remote directly, for example with `rclone ls opencloud-e2ee:`.

Use the `crypt` remote for listing and mounting:

```bash
rclone ls opencloud-decrypted:
```

If `rclone ls opencloud-decrypted:` returns no output, first check whether the encrypted folder contains any files. The `rclone ls` command lists files but does not display empty directories, so an empty result does not necessarily indicate a configuration error.

If the folder contains files and the `crypt` remote displays encrypted file names or no files, check that the `crypt` password matches the encrypted folder password and that `filename_encryption` and `directory_name_encryption` are set as described in [Configure the Encrypted Remote](#configure-the-encrypted-remote).

### rclone Does Not Find the Configuration Section

The following error indicates that the `crypt` remote contains the WebDAV URL instead of the WebDAV remote name:

```text
didn't find section in config file ("https")
```

The `remote` option in the `crypt` configuration must contain the name of the WebDAV remote followed by a colon:

Correct:

```ini
remote = opencloud-e2ee:
```

Incorrect:

```ini
remote = https://cloud.example.com/dav/...
```

Update the `remote` value and run the test again.

### The Folder Cannot Be Mounted

<Tabs groupId="operating-system">
<TabItem value="linux" label="Linux" default>

- Check that FUSE 3 is installed.
- Check that the mount point exists and is empty.
- On recent Ubuntu versions, AppArmor can block FUSE mounts. For details, see the [`rclone mount` documentation](https://rclone.org/commands/rclone_mount/).

</TabItem>
<TabItem value="macos" label="macOS">

- Check that rclone was not installed with Homebrew. Run `which rclone` and reinstall rclone with the install script if required.
- Check that the mount point exists and is empty.
- If macOS blocks rclone with a "developer cannot be verified" message, see the [rclone installation guide](https://rclone.org/install/).

</TabItem>
<TabItem value="windows" label="Windows">

- Check that WinFsp is installed.
- Check that the drive letter is not already in use.

</TabItem>
</Tabs>
