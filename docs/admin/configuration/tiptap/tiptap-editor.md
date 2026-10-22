---
sidebar_position: 2
id: tiptap-editor
title: Tiptap Editor
description: Create and edit Markdown files directly in OpenCloud using the Tiptap editor.
draft: false
---

# Using the Tiptap Editor in OpenCloud

OpenCloud provides a built-in text editor based on Tiptap that allows you to create and edit Markdown files directly in your web browser.

The editor offers a user-friendly interface for formatting text, creating lists, inserting tables, and adding other elements without requiring knowledge of Markdown syntax.

## Open a Markdown File

To open a Markdown file in the Tiptap editor:

- Navigate to the folder or Space containing your Markdown file.
- Click on a file with the `.md` extension, such as `README.md`.
- OpenCloud opens the file in the integrated Markdown editor.
- If you have the necessary permissions, you can start editing the content.

<img src={require("./img/editor-overview.png").default} alt="Tiptap editor overview" width="1000"/>

:::note
You need write permissions for the file to modify its content. Without write permissions, you can only view the file.
:::

## Edit and Format Text

The Tiptap editor allows you to format text using the formatting toolbar or the slash menu.

### Use the Formatting Toolbar

The formatting toolbar provides access to frequently used formatting options.

- Open a Markdown file.
- Select the text you want to format.
- Choose the desired formatting option from the toolbar.

Available formatting options include:

- **Bold** – Highlight important text.
- **Italic** – Emphasize individual words or sentences.
- **Headings** – Organize your document into sections.
- **Bullet lists** – Create unordered lists.
- **Numbered lists** – Create ordered lists.
- **Links** – Add hyperlinks to websites or other resources.
- **Quotes** – Highlight quotations.
- **Code** – Format inline code or code blocks.

<img src={require("./img/formatting-toolbar.png").default} alt="Formatting toolbar" width="900"/>

### Create Headings

Headings help structure your document and make it easier to read.

- Place the cursor in the line you want to turn into a heading.
- Open the heading selection in the formatting toolbar.
- Select the desired heading level.

For example:

```markdown
# Main Heading

## Section Heading

### Subsection Heading
```

The editor displays the headings with the corresponding formatting.

### Create Lists

You can create bullet lists and numbered lists.

- Place the cursor where you want to create a list.
- Select the bullet list or numbered list option from the toolbar.
- Enter the first list item.
- Press `Enter` to add another item.

Example of a bullet list:

```markdown
- First item
- Second item
- Third item
```

Example of a numbered list:

```markdown
1. First step
2. Second step
3. Third step
```

## Use the Slash Menu

The slash menu provides quick access to formatting and content elements directly from the keyboard.

To open the slash menu:

- Place the cursor on a new line in the editor.
- Type `/`.
- A menu with available formatting and content options appears.
- Select the desired option.

<img src={require("./img/slash-menu.png").default} alt="Tiptap slash menu" width="700"/>

The slash menu can be used to insert elements such as:

- Headings
- Bullet lists
- Numbered lists
- Quotes
- Code blocks
- Tables
- Images

This allows you to format documents without repeatedly switching between the keyboard and the formatting toolbar.

## Insert Links

You can add hyperlinks to your Markdown document.

- Select the text you want to turn into a link.
- Choose the link option from the formatting toolbar.
- Enter the destination URL.
- Confirm the link.

The selected text becomes a clickable hyperlink.

Example:

```markdown
[OpenCloud Website](https://opencloud.eu)
```

<img src={require("./img/insert-link.png").default} alt="Insert hyperlink" width="700"/>

## Insert Tables

Tables help organize information into rows and columns.

To insert a table:

- Place the cursor where you want to insert the table.
- Open the slash menu by typing `/`, or use the table option in the toolbar.
- Select the table option.
- Enter your content into the table cells.

<img src={require("./img/insert-table.png").default} alt="Insert table" width="900"/>

For example, you can use a table to document project responsibilities:

| Name    | Role          | Department    |
| ------- | ------------- | ------------- |
| Alice   | Administrator | IT            |
| Bob     | Editor        | Documentation |
| Charlie | Viewer        | Support       |

## Insert Images

The editor supports inserting images into Markdown documents.

- Place the cursor at the desired position.
- Open the slash menu or use the image option in the formatting toolbar.
- Select the available image insertion option.
- Follow the displayed instructions to insert the image.

<img src={require("./img/insert-image.png").default} alt="Insert image" width="900"/>

:::note
The available image insertion options may depend on the OpenCloud version and editor configuration.
:::

## Insert Code Blocks

Code blocks are useful for technical documentation, configuration examples, and command-line instructions.

To insert a code block:

- Place the cursor on a new line.
- Open the slash menu or use the code formatting option.
- Select the code block option.
- Enter or paste your code.

Example:

```bash
docker compose up -d
```

<img src={require("./img/code-block.png").default} alt="Code block in the editor" width="900"/>

## Save Your Changes

After editing a Markdown file, make sure your changes are saved.

- Finish editing your document.
- Use the available save function or press `Ctrl + S` (`Cmd + S` on macOS).
- Wait until the save operation has completed before closing the editor.

The content is saved in the original Markdown file.

:::tip
Markdown files remain compatible with other Markdown editors and applications. You can download and edit them outside OpenCloud if necessary.
:::

## Use Markdown Files as Folder Descriptions

OpenCloud can display the content of a `README.md` file directly above the file list in a folder.

This is useful for documenting the purpose of a folder or providing instructions for other users.

To create a folder description:

- Navigate to the desired folder.
- Create or upload a file named `README.md`.
- Open the file in the Tiptap editor.
- Add your description and format the content.
- Save the file.

When the folder is opened or refreshed, OpenCloud displays the rendered Markdown content above the file list.

<img src={require("./img/readme-folder-description.png").default} alt="README file displayed as folder description" width="1000"/>

## Good to Know

- The editor is integrated into the OpenCloud web interface.
- Markdown files can be edited directly in the browser.
- The formatting toolbar and slash menu simplify document creation.
- The editor supports headings, lists, links, tables, images, and code blocks.
- Changes are stored in the original Markdown file.
- Editing requires the appropriate file permissions.
- Markdown files can also be opened with external Markdown editors.
