---
sidebar_position: 3.5
title: README Files in Folders
description: Learn how README.md files are rendered in folders in OpenCloud.
---

# README Files in Folders

If a folder contains a file named `README.md`, OpenCloud renders its Markdown content above the file list.

<img src={require("./img/readme-files/readme-list-view.png").default} alt="README rendered in list view with the file still visible" width="1920"/>

## Create a README File

1. Open the folder where you want to add the README.
2. Create or upload a file named `README.md`.
3. Add your Markdown content and save the file.

OpenCloud renders the content when the folder is opened or refreshed.

## Supported File Name

The file name must be exactly:

```text
README.md
```

## Example

A `README.md` file can contain Markdown like this:

```markdown
# Photos

This folder contains visual samples for preview and documentation screenshots.

The images are used to show list view, thumbnail view, and image preview behavior in OpenCloud.

## Files

- moon-surface-public-domain.jpg
- rotated-chessboard-photo.jpg
- vintage-computer-terminal.jpg
- Space-Nebula.jpg
```

## Remove the README Section

Delete or rename `README.md` to remove the rendered section.

<img src={require("./img/readme-files/readme-removed.png").default} alt="Folder without the rendered README section" width="1920"/>
