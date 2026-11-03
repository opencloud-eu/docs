---
sidebar_position: 1
id: thumbnailer
title: 'Thumbnailer'
description: Use imagor as thumbnail generator to enable previews for HEIC, HEIF, and AVIF images
draft: false
---

# Use imagor as Thumbnail Generator

OpenCloud creates previews (thumbnails) of images and documents, which are displayed in the file list and in the preview app. By default, the built-in `thumbnails` service generates these previews.

As of OpenCloud 9.0.0, you can replace the built-in thumbnail generator with [imagor](https://github.com/cshum/imagor). imagor is a fast image processing server based on libvips and can read image formats that the built-in generator does not support.

This guide explains how to enable imagor in a deployment based on the [`opencloud-compose`](https://github.com/opencloud-eu/opencloud-compose) deployment example.

## Benefits

| Feature                                                | Built-in generator | imagor                                                       |
| ------------------------------------------------------ | ------------------ | ------------------------------------------------------------ |
| Previews for common formats such as JPEG, PNG, and GIF | Yes                | Yes                                                          |
| Previews for HEIC and HEIF, for example iPhone photos  | No                 | Yes                                                          |
| Previews for AVIF                                      | No                 | Yes                                                          |
| Open HEIC, HEIF, and AVIF images in the preview app    | No                 | Yes                                                          |
| Additional formats such as PSD, XCF, and BMP           | No                 | With the [ImageMagick variant](#use-the-imagemagick-variant) |
| Additional container                                   | No                 | Yes                                                          |

The OpenCloud container image intentionally does not include a HEIC decoder. Without imagor, OpenCloud does not create previews for HEIC, HEIF, and AVIF files, and users can only download them.

## How It Works

As of OpenCloud 9.0.0, the `webdav` service handles all thumbnail requests and manages the thumbnail cache. To create a preview, it sends the source image to a thumbnail generator. The built-in `thumbnails` service and imagor use the same interface, so imagor can replace the built-in generator without further changes.

The `opencloud-compose` deployment example provides a module that:

- Starts imagor as an additional container.
- Connects imagor to the OpenCloud container through an internal network without access to the internet.
- Configures OpenCloud to send preview requests to imagor.
- Enables previews for HEIC, HEIF, and AVIF files, including image sequences.

## Prerequisites

- A running OpenCloud deployment based on `opencloud-compose`.
- OpenCloud version 9.0.0 or later.
- A current version of the `opencloud-compose` repository that contains the file `thumbnails/imagor.yml`.

If you are running an older OpenCloud version, follow the [Standard Upgrade Guide](../../maintenance/upgrade/upgrade.md) and the [Upgrade 9.x.x](../../maintenance/upgrade/upgrade-9.x.x.md) guide first.

All commands in this guide are run in the root directory of the `opencloud-compose` deployment.

## Enable imagor

### Update the `opencloud-compose` Repository

Update your local copy of the `opencloud-compose` repository:

```bash
git pull
```

Check that the imagor module is available:

```bash
ls thumbnails/imagor.yml
```

### Add the Module to `COMPOSE_FILE`

Add `thumbnails/imagor.yml` to the end of the existing `COMPOSE_FILE` variable in your `.env` file, for example:

```env
COMPOSE_FILE=docker-compose.yml:traefik/opencloud.yml:thumbnails/imagor.yml
```

Keep all files that are already part of your deployment.

:::note
Make sure that the `.env` file contains only one active `COMPOSE_FILE` line. If there are several lines, only the last one is used.
:::

Alternatively, add the module directly to the startup command:

```bash
docker compose -f docker-compose.yml -f traefik/opencloud.yml -f thumbnails/imagor.yml up -d
```

### Restart OpenCloud

Apply the changes:

```bash
docker compose up -d
```

Docker Compose starts the `imagor` container and restarts OpenCloud. OpenCloud waits until imagor is ready.

## Verify the Configuration

Check that the `imagor` container is running and healthy:

```bash
docker compose ps imagor
```

The status must be `Up` and `(healthy)`.

Check that OpenCloud uses imagor as thumbnail generator:

```bash
docker compose exec opencloud printenv WEBDAV_THUMBNAILS_GENERATOR_URL
```

The output must be `http://imagor:8000`.

Finally, test the previews in the Web Client:

1. Upload a HEIC image, for example a photo taken with an iPhone.
2. Check that a preview is displayed in the file list.
3. Open the image. It is displayed in the preview app.

Previews are created when they are requested for the first time. This also applies to HEIC, HEIF, and AVIF files that were uploaded before you enabled imagor.

## Optional Settings

You can adjust the imagor module with the following variables in your `.env` file:

| Variable                             | Default                                                                    | Description                                                                   |
| ------------------------------------ | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `IMAGOR_DOCKER_IMAGE`                | `shumc/imagor`                                                             | Container image of imagor.                                                    |
| `IMAGOR_DOCKER_TAG`                  | `1.9.14`                                                                   | Version of the imagor container image.                                        |
| `IMAGOR_MAX_SOURCE_SIZE`             | `50000000`                                                                 | Maximum size of a source image in bytes.                                      |
| `THUMBNAILS_ADDITIONAL_SOURCE_TYPES` | `image/heic,image/heif,image/avif,image/heic-sequence,image/heif-sequence` | Comma-separated list of additional MIME types for which previews are created. |

:::important
If you set `THUMBNAILS_ADDITIONAL_SOURCE_TYPES`, the value replaces the default list. To keep previews for HEIC, HEIF, and AVIF files, include their MIME types in your list.
:::

If imagor cannot read a file of an additional type, no preview is created for this file.

### Use the ImageMagick Variant

The ImageMagick variant of imagor supports additional formats such as PSD, XCF, and BMP. To use it, set the container image in your `.env` file and add the MIME types of the additional formats to `THUMBNAILS_ADDITIONAL_SOURCE_TYPES`:

```env
IMAGOR_DOCKER_IMAGE=ghcr.io/cshum/imagor-magick
THUMBNAILS_ADDITIONAL_SOURCE_TYPES=image/heic,image/heif,image/avif,image/heic-sequence,image/heif-sequence,<additional-mime-types>
```

Restart OpenCloud to apply the changes:

```bash
docker compose up -d
```

:::caution
The ImageMagick variant is slower, uses more memory, and has a larger attack surface than the standard image. Use the standard image unless you need the additional formats.
:::

## Security

The imagor module is configured with restrictive security settings:

- imagor runs in an internal network and cannot connect to the internet.
- imagor only processes images that OpenCloud sends to it. Loading images from URLs is disabled.
- The container runs with a read-only file system, without Linux capabilities, and with `no-new-privileges`.

Do not publish the imagor port. imagor does not authenticate requests.

## Limitations

- Source images larger than 7680 × 7680 pixels are not processed.
- Animated images with more than 100 frames are not processed.
- Files in [end-to-end encrypted folders](../../../user/files-and-folders/e2ee-folders.md) have no server-side previews, because the server only stores encrypted data.

## Disable imagor

To return to the built-in thumbnail generator:

1. Remove `thumbnails/imagor.yml` from `COMPOSE_FILE` in your `.env` file.
2. Apply the changes and remove the `imagor` container:

   ```bash
   docker compose up -d --remove-orphans
   ```

Previews for HEIC, HEIF, and AVIF files are no longer created.

## Troubleshooting

### No Previews Are Displayed for HEIC Files

- Check that you are running OpenCloud version 9.0.0 or later.
- Check that `thumbnails/imagor.yml` is part of `COMPOSE_FILE`.
- Check that OpenCloud uses imagor as described in [Verify the Configuration](#verify-the-configuration).
- If you set `THUMBNAILS_ADDITIONAL_SOURCE_TYPES`, check that the list contains `image/heic`.

### The OpenCloud Container Does Not Start

OpenCloud waits until imagor is healthy. Check the status and the logs of the `imagor` container:

```bash
docker compose ps imagor
docker compose logs --tail=40 imagor
```

<!-- Screenshot suggestion:
Show a folder in the Web Client with HEIC previews in the file list.
Store screenshots in ./img and do not show personal data.
-->
