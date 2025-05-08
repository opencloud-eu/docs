---
sidebar_position: 4
id: search
title: Search
---

# Search
<br/><br/>

## Using the search in OpenCloud
You can use the search bar in the top bar to find files and content quickly.
<br/><br/>

### This is how the search works

- Find search bar
    - The **search bar** is located at the top of the **top bar** in the **web interface**.
<img src={require("./img/search/searchbar.png").default} alt="search bar" width="1920"/>
<br/><br/>

- Select search area
    - Click on the **drop-down menu** next to the **search bar**.
    - Select whether you want to search in all files or only in the current folder.
<img src={require("./img/search/drop-down-menu-searchbar.png").default} alt="select where to search" width="500"/>
<br/><br/>
- Search function
    - This **searches** through file names as well as the content of the files to **display relevant results**.
<img src={require("./img/search/search-example.png").default} alt="example search" width="500"/>
<br/><br/>

### Advanced search syntax

OpenCloud supports advanced search operators to help you find exactly what you're looking for:

- **Boolean operators**: Combine terms using `AND`, `OR`, and `NOT` (case-sensitive)
  - Example: `customer AND 2025` will find documents containing both "customer" and "2025"
  - Example: `project OR task` will find documents containing either "project" or "task"
  - Example: `document NOT draft` will find documents containing "document" but not "draft"

- **Field-specific search**: Search in specific metadata fields using `field:value`
  - Example: `name:"quarterly report"` searches only in file names
  - Example: `tag:important` searches for files with the "important" tag

- **Date filtering**: Search by modification time using `mtime`
  - The accepted date formats for `mtime` are:
    - `YYYY` (e.g., `mtime:2023` for any modification in 2023)
    - `YYYY-MM` (e.g., `mtime:2023-05` for modifications in May 2023)
    - `YYYY-MM-DD` (e.g., `mtime:2023-05-15` for modifications on May 15, 2023)
  - Example: `report AND mtime:2023` finds reports modified in 2023

- **Grouping**: Use parentheses to group expressions
  - Example: `(invoice OR receipt) AND 2025` finds invoices or receipts from 2025

These advanced search operators can be combined to create powerful search queries for finding exactly what you need.

Use these steps to find your files or folders quickly and efficiently!