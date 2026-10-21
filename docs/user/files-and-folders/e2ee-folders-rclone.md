---
sidebar_position: 131
id: e2ee-folders-rclone
title: Access End-to-End Encrypted Folders with rclone
description: Access an OpenCloud end-to-end encrypted folder locally with rclone crypt.
draft: false
---

# Access End-to-End Encrypted Folders with rclone

Use `rclone crypt` to access an end-to-end encrypted folder locally while keeping file contents and names encrypted on the OpenCloud server.

This setup has been tested on macOS with rclone v1.75.1.

## Before You Begin

First, [create the end-to-end encrypted folder in the OpenCloud Web Client](./e2ee-folders).

You need:

- The password of the end-to-end encrypted folder
- An OpenCloud App Token
- The WebDAV URL of the encrypted folder
- [rclone](https://rclone.org/install/) installed locally

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

## Create an App Token

Create a dedicated App Token for rclone in your OpenCloud account settings. Copy it when it is displayed because it cannot be shown again.

For detailed instructions, see [App Tokens](../admin/app-tokens).

The App Token is used as the password for the WebDAV remote. It is not the password for the encrypted folder.

<!-- Screenshot suggestion:
Show App Token creation in the OpenCloud account settings.
Do not show a real token or other credentials.
-->

## Get the WebDAV URL

Enable the WebDAV information in your OpenCloud account settings, open the details panel of the encrypted folder, and copy its WebDAV URL. For general instructions, see [Connect to a Space via WebDAV](../admin/web-dav).

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

When rclone writes passwords to its configuration, it stores them in obscured form. If you edit the configuration manually, use [`rclone obscure`](https://rclone.org/commands/rclone_obscure/) to create the value for `pass`.

The resulting configuration should look similar to:

```ini
[opencloud-e2ee]
type = webdav
url = https://cloud.example.com/dav/spaces/<space-id>/Encrypted.vault
vendor = infinitescale
user = <username>
pass = <encrypted-app-token>
```

For more information about the backend options, see the [rclone WebDAV documentation](https://rclone.org/webdav/).

Test the WebDAV connection before continuing:

```bash
rclone ls opencloud-e2ee:
```

Replace `opencloud-e2ee` with the name of your WebDAV remote if you chose a different name.

If the connection works, rclone may display encrypted file names. This is expected for the WebDAV remote.

## Configure the Encrypted Remote

Before creating the `crypt` remote, make sure that the WebDAV remote has been created with the App Token and can connect to OpenCloud. The `crypt` remote does not connect to OpenCloud directly. It adds encryption and decryption on top of the existing WebDAV remote.

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
password = <encrypted-folder-password>
```

The `remote` value must reference the WebDAV remote by name. If the WebDAV remote is named `opencloud-e2ee`, use:

```ini
remote = opencloud-e2ee:
```

The value always consists of the exact WebDAV remote name followed by `:`. Do not enter the WebDAV URL in this field.

If you edit the configuration manually, use [`rclone obscure`](https://rclone.org/commands/rclone_obscure/) to create the value for `password`. For more information about the backend options, see the [rclone crypt documentation](https://rclone.org/crypt/).

## Test the Encrypted Remote

List the data stored directly on the server:

```bash
rclone ls opencloud-e2ee:
```

Replace `opencloud-e2ee` with the name of your WebDAV remote if you chose a different name.

Encrypted file names may be displayed. This is expected because the WebDAV remote accesses the encrypted data stored on the server without decrypting it.

For normal file operations, use the decrypted remote instead:

```bash
rclone ls opencloud-decrypted:
```

Replace `opencloud-decrypted` with the name of your `crypt` remote if you chose a different name.

rclone should display the original decrypted file names. This has been tested with a file created in the OpenCloud Web Client.

## Copy Files to the Encrypted Folder

Use the decrypted remote when copying files to the encrypted folder:

```bash
rclone copy ~/Documents/example.txt opencloud-decrypted:
```

Replace `opencloud-decrypted` with the name of your `crypt` remote if you chose a different name.

Files copied this way are encrypted locally before upload. The following operations have been tested successfully:

- Files created in the OpenCloud Web Client can be read through rclone.
- Files uploaded through rclone can be opened in the OpenCloud Web Client.
- Subdirectories created through rclone work correctly.

For additional copy options, see the [`rclone copy` documentation](https://rclone.org/commands/rclone_copy/).

## Synchronize a Local Directory

To make the encrypted folder match a local directory, use `rclone sync` with the decrypted remote:

```bash
rclone sync ~/Documents/opencloud opencloud-decrypted:
```

Replace `opencloud-decrypted` with the name of your `crypt` remote if you chose a different name.

:::warning

`rclone sync` makes the destination match the source. Files that exist only in the destination are deleted. The direction of the command therefore determines where deletions are applied.

:::

Check the planned changes before synchronizing:

```bash
rclone sync ~/Documents/opencloud opencloud-decrypted: --dry-run
```

Replace `opencloud-decrypted` with the name of your `crypt` remote if you chose a different name.

Use `rclone copy` instead when files should only be added or updated without deleting files from OpenCloud. For more information, see the [`rclone sync` documentation](https://rclone.org/commands/rclone_sync/).

## Platform Support

The OpenCloud-specific rclone configuration is platform-independent. The same WebDAV and `crypt` configuration can be used on macOS, Windows, and Linux.

The complete workflow described in this guide has currently been tested on macOS. Verification on Windows and Linux is still pending.

Installation methods, local path syntax, mounting, and automation depend on the operating system and are documented by rclone. For installation and platform-specific information, see the [rclone documentation](https://rclone.org/docs/).

To determine the configuration file used on your system, run:

```bash
rclone config file
```

## Troubleshooting

### Encrypted File Names Are Displayed

Encrypted file names are expected when you use the WebDAV remote directly:

```bash
rclone ls opencloud-e2ee:
```

Replace `opencloud-e2ee` with the name of your WebDAV remote if you chose a different name.

Use the decrypted remote for normal file operations:

```bash
rclone ls opencloud-decrypted:
```

Replace `opencloud-decrypted` with the name of your `crypt` remote if you chose a different name.

### rclone Does Not Find the Configuration Section

The following error indicates that the `crypt` remote contains the WebDAV URL instead of the WebDAV remote name:

```text
didn't find section in config file ("https")
```

The WebDAV connection must first be configured as a separate remote. It uses the App Token to authenticate with OpenCloud. The `crypt` remote then uses that existing connection for encrypted and decrypted file operations. This guide uses `opencloud-e2ee` for the WebDAV remote and `opencloud-decrypted` for the `crypt` remote, but both names are examples.

The `remote` option in the `crypt` configuration must therefore contain the name of the WebDAV remote followed by a colon:

Correct:

```ini
remote = opencloud-e2ee:
```

If your WebDAV remote has a different name, replace `opencloud-e2ee` with that exact name.

Incorrect:

```ini
remote = https://cloud.example.com/dav/...
```

Create and test the WebDAV remote before configuring the `crypt` remote. Then update the `remote` value and run the test again.
