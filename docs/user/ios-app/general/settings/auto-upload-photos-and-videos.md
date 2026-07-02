---
sidebar_position: 2
id: auto upload photos and videos
title: Auto Upload Photos and Videos
description: Auto upload photos and videos from your iPhone or iPad.
draft: false
---

# Auto Upload

Auto Upload automatically uploads newly created photos and videos from your iPhone or iPad to your OpenCloud account.

Once configured, new media is uploaded automatically whenever the OpenCloud app is opened and running in the foreground.

## Requirements

Before using Auto Upload, ensure that:

- You are signed in to your OpenCloud account.
- The OpenCloud app has permission to access your photo library.
- A destination folder has been configured for uploads.

## Configure Auto Upload

1. Open the **OpenCloud** app.
2. Tap **Settings**.

<img src={require("../../img/settings/auto-upload-photos-and-videos/settings-button.png").default} alt="OpenCloud Settings" height="650"/>

3. Scroll down to the **Media Files** section.
4. Tap **Media Upload**.

<img src={require("../../img/settings/auto-upload-photos-and-videos/media-upload-button.png").default} alt="Media Upload settings" height="650"/>

## Enable Auto Upload

Photos and videos can be enabled independently.

The following options are available:

- **Auto Upload Photos** – Automatically uploads newly created photos.
- **Auto Upload Videos** – Automatically uploads newly created videos.
- **Photo upload path** – Selects the destination folder for uploaded photos.
- **Convert HEIC to JPEG** – Converts HEIC images to JPEG before uploading.
- **Convert videos to MP4** – Converts videos to MP4 before uploading.
- **Preserve original media file names** – Keeps the original filename instead of generating a new one.

<img src={require("../../img/settings/auto-upload-photos-and-videos/auto-upload-photos.png").default} alt="Auto Upload settings" height="650"/>

## Select the Upload Destination

Before Auto Upload can begin, you must select the destination folder.

1. Tap **Photo upload path**.
2. Browse to the folder where photos should be uploaded.
3. Tap **Select Destination**.

<img src={require("../../img/settings/auto-upload-photos-and-videos/select-destination.png").default} alt="Selecting an upload destination" height="650"/>

## How Auto Upload Works

:::important Current iOS Behavior

At the moment, Auto Upload only detects and uploads newly created photos and videos while the OpenCloud app is running in the foreground.

If the app is closed or running in the background, new media is **not** uploaded until the app is opened again.

Simply opening the OpenCloud app starts the Auto Upload process. Any new media created since the last successful upload is detected automatically and uploaded.

:::

General behavior:

- Photo and video uploads can be enabled or disabled independently.
- Before Auto Upload can begin, an account and an upload destination must be configured.
- Changes to the iOS photo library are detected whenever the OpenCloud app returns to the foreground.
- If the configured upload folder is deleted, Auto Upload stops automatically until a new destination folder is selected.

### Preventing Duplicate Uploads

To prevent duplicate uploads, Auto Upload stores the timestamp of the last successfully uploaded item.

When Auto Upload is enabled for the first time, the activation timestamp is stored and compared with the creation date of each photo and video. After a file has been uploaded successfully, its creation timestamp becomes the new reference point.

This approach provides several advantages:

- Prevents photos and videos from being uploaded more than once.
- Eliminates the need to maintain a local database of uploaded files.
- Previously uploaded media is not uploaded again, even if it is edited later.

### Media Conversion

If media conversion is enabled, Auto Upload automatically applies the selected conversion settings before uploading photos and videos.
