---
sidebar_position: 20
id: collabora-ms-office-formats
title: Enable MS-Office formats
description: How to enable MS-Office formats
draft: false
---

## Enable Microsoft file formats in the New menu

:::note
Starting with version 5.2.0, OpenCloud no longer enables Microsoft file formats as default creation options in the New menu. To make them available again, you must define them explicitly in `app-registry.yaml`.
:::

### Create the configuration file

Create an `app-registry.yaml` file in your `config/opencloud` directory.

If your deployment uses a bind mount for the OpenCloud configuration, place the file in the corresponding directory on the host system. In that case, use the path from your own Docker Compose setup rather than `config/opencloud`.

```bash
config/opencloud/app-registry.yaml
```

Insert following content:

```yaml
app_registry:
  mimetypes:
    - mime_type: application/pdf
      extension: pdf
      name: PDF
      description: PDF document
      icon: ''
      default_app: ''
      allow_creation: false
    - mime_type: application/vnd.oasis.opendocument.text
      extension: odt
      name: Document
      description: OpenDocument text document
      icon: ''
      default_app: Collabora
      allow_creation: true
    - mime_type: application/vnd.oasis.opendocument.spreadsheet
      extension: ods
      name: Spreadsheet
      description: OpenDocument spreadsheet document
      icon: ''
      default_app: Collabora
      allow_creation: true
    - mime_type: application/vnd.oasis.opendocument.presentation
      extension: odp
      name: Presentation
      description: OpenDocument presentation document
      icon: ''
      default_app: Collabora
      allow_creation: true
    - mime_type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
      extension: docx
      name: Microsoft Word
      description: Microsoft Word document
      icon: ''
      default_app: Collabora
      allow_creation: true
    - mime_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
      extension: xlsx
      name: Microsoft Excel
      description: Microsoft Excel document
      icon: ''
      default_app: Collabora
      allow_creation: true
    - mime_type: application/vnd.openxmlformats-officedocument.presentationml.presentation
      extension: pptx
      name: Microsoft PowerPoint
      description: Microsoft PowerPoint document
      icon: ''
      default_app: Collabora
      allow_creation: true
    - mime_type: application/vnd.jupyter
      extension: ipynb
      name: Jupyter Notebook
      description: Jupyter Notebook
      icon: ''
      default_app: ''
      allow_creation: true
```

### Verify ownership and permissions

:::important UID/GID and volume permissions
Make sure that `app-registry.yaml` can be read by the user running the OpenCloud container. Incorrect ownership or permissions on mounted files can prevent OpenCloud from using the configuration.
:::

By default, OpenCloud uses:

```bash
UID=1000
GID=1000
```

Adjust the file ownership and permissions if your container runs with different values.

### Restart OpenCloud

Restart your deployment after creating the file:

```bash
docker compose down
docker compose up -d
```

After the restart, Microsoft formats such as Word, Excel, and PowerPoint are available again in the New menu.
