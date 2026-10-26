---
id: markdown-editor
sidebar_position: 40
title: Editing Text and Notes
description: Create, format, collaborate on, and save text documents and notes in OpenCloud.
---

# Editing Text and Notes

OpenCloud 8.0 and later includes a Tiptap-based editor for working with supported text files directly in your browser. You can create and format Markdown documents and OpenCloud Notes without installing additional software. With collaborative editing enabled, several people can also work on the same document in real time.

## Create or Open a Document

To create a document:

1. Open the folder or Space where you want to store the document.
2. Select `New`.
3. Select `Note` to create an `.ocnote` file or `Markdown file` to create an `.md` file.
4. Enter a file name and confirm the creation.

The new document opens in the text editor.

To open an existing document, select the file in the file list. If the text editor is not the default application for that file, open its context menu and select `Open with...` and then `Text Editor`.

<img src={require("./img/markdown-editor/editor-overview.png").default} alt="OpenCloud text editor showing a formatted Markdown document" width="1920"/>

:::note
You need permission to edit the file. If you only have view permission, you can follow changes made by others but cannot change the document.
:::

## Choose a File Format

Choose the format based on how you want to use the document.

| Format                     | Use it for                                                                | Formatting                                                                                                                        |
| :------------------------- | :------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------- |
| Markdown (`.md`)           | Portable documents that you also want to use with external Markdown tools | Headings, emphasis, lists, quotes, links, images, tables, and code                                                                |
| OpenCloud Note (`.ocnote`) | Rich notes that you primarily edit in OpenCloud                           | Markdown-style features plus font size, text and background colors, line height, alignment, underline, subscript, and superscript |
| Plain text (`.txt`)        | Unformatted text, logs, or simple notes                                   | Plain text without rich formatting; search, replace, and printing remain available                                                |

An `.ocnote` file is an OpenCloud rich-text format stored as text-based JSON. It is not a standard Markdown format.

<!-- Screenshot TODO: note-formatting.png - Show an .ocnote document with additional formatting options, such as text colors or alignment. -->

## Format Your Content

Use the formatting toolbar to undo or redo changes, format text, create lists, and insert content. In narrow windows, actions that do not fit move into `More actions`.

<img src={require("./img/markdown-editor/formatting-toolbar.png").default} alt="Formatting toolbar in the OpenCloud text editor" width="1505"/>

To format existing text:

1. Select the text or place the cursor in the block you want to change.
2. Use `Turn into` to choose a paragraph, heading, quote, or code block.
3. Use the toolbar actions for bold, italic, strikethrough, or a list as needed.

### Use the Slash Menu

Type `/` at the beginning of a line to open the slash menu. Start typing the name of an action to filter the menu, then select an item such as a heading, list, quote, code block, link, image, or table.

<img src={require("./img/markdown-editor/slash-menu.png").default} alt="Slash menu with formatting and insertion actions" width="900"/>

When you hover next to a content block, use `Add content` to insert a block after it. On a desktop device, use `Drag to move` to rearrange blocks.

### Insert a Link

1. Select the text that should become a link, or place the cursor where you want to add one.
2. Select `Link` in the toolbar or slash menu.
3. Enter the destination URL and link text.

<img src={require("./img/markdown-editor/insert-link.png").default} alt="Link editor with fields for the URL and link text" width="900"/>

### Insert Code

Use `Inline code` for code within a sentence. For multiple lines, select `Code block` from `Turn into` or the slash menu. The editor highlights supported languages, detects the language when possible, and also lets you choose a language.

<img src={require("./img/markdown-editor/code-block.png").default} alt="Code block with syntax highlighting and a language selector" width="900"/>

## Insert Images and Tables

### Insert an Image

1. Place the cursor where you want the image.
2. Open `Insert image` in the toolbar, or type `/image`.
3. Choose one of the available options:
   - `Image from file` uploads an image from your device.
   - `Image from URL` inserts an image from an `http://` or `https://` address.
   - `Insert from cloud` selects an image already stored in OpenCloud. This option is not available from a public link.
4. After insertion, select the image and use its resize handles to adjust its size.

<img src={require("./img/markdown-editor/insert-image.png").default} alt="Slash menu showing the supported image insertion options" width="900"/>

### Insert a Table

1. Place the cursor where you want the table.
2. Select `Create a table` in the toolbar or slash menu.
3. Choose the required number of rows and columns.
4. Select a cell to open the table controls.

The table controls let you add or remove rows and columns, toggle the header row, or delete the table.

<img src={require("./img/markdown-editor/insert-table.png").default} alt="Table inserted into a document" width="900"/>

## Find and Navigate Content

### Find and Replace Text

Open `Search and replace` from the toolbar, or press `Ctrl + F` (`Cmd + F` on macOS). Enter the text to find and, if needed, replacement text. You can match the letter case or whole words only.

<!-- Screenshot TODO: find-replace.png - Show the find and replace interface. -->

### Navigate with the Table of Contents

Markdown and `.ocnote` documents provide a table of contents generated from their headings. Open the `Outlines` panel to see the document structure. Select a heading to jump to it; the active entry follows your position as you scroll and the list updates when headings change.

<!-- Screenshot TODO: table-of-contents.png - Show a longer document with several headings and the table of contents visible. -->

## Collaborate on Documents

Real-time collaboration is available for Markdown and `.ocnote` files. When several users open the same document, changes appear in their editors immediately. The toolbar shows active participants, and colored cursors indicate where they are working.

Users with edit permission can change the document. Users with view permission can follow the session without seeing editing controls.

<!-- Screenshot TODO: collaboration.png - Show a document being edited by multiple users, including participant avatars and an active cursor. -->

### Mention Another User

In a Markdown or `.ocnote` document, type `@` and select a user from the suggestion list. Only users who can access the document are offered. The mention notification is sent after the document is saved and follows the configured notification settings.

Mentions are not available through public links.

<!-- Screenshot TODO: mentions.png - Show the @mention suggestion menu with users available for selection. -->

:::note
Real-time collaboration requires the Yjs service. Administrators can find deployment details in [Collaborative Editing with the Yjs Server](../../admin/configuration/collaborative-editing.md).
:::

Collaboration has the following limitations:

- Public links do not join a collaborative session. A user with write access can still edit and save, but changes do not appear in other open editors in real time.
- Collaborative editing is disabled for files in end-to-end encrypted vaults.
- Source mode is read-only while collaboration is active because source changes cannot be merged into the shared document.

## Save Your Changes

Changes in the editor and changes saved to the file are separate:

- During a collaborative session, your edits synchronize with the other participants immediately.
- The file is updated when a participant selects `Save`, presses `Ctrl + S` (`Cmd + S` on macOS), or periodic autosave runs.
- The autosave interval is configured by the administrator and is shown in the editor when autosave is enabled.

If another application, such as a desktop sync client, changes the file while it is open, OpenCloud notifies the editor immediately. If you have no unsaved changes, the editor loads the newer file. If you have unsaved work, keep it by selecting `Save as`, or reload the page to discard it and open the external version.

Each successful save updates the regular OpenCloud file. Previous states are therefore available according to the normal [file versioning](./versions.md) rules.

## Good to Know

- Markdown files remain compatible with external Markdown editors, although rendering details can differ between applications.
- `.ocnote` preserves rich formatting that Markdown cannot represent and is intended for use with OpenCloud's editor.
- Code blocks provide syntax highlighting for common programming and configuration languages.
- Select `Print` to open the system print dialog. Depending on your operating system, the dialog may also offer `Save as PDF`; this creates a local file and does not save a PDF in OpenCloud.
- To display a `README.md` above a folder's file list, see [README Files in Folders](./readme-files.md).
