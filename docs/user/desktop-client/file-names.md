---
sidebar_position: 11
id: file-names
title: File Naming Rules
description: File Naming Rules for OpenCloud Desktop
draft: true
---

# Filename restrictions on OpenCloud Desktop

When using the OpenCloud Desktop Client, file and folder names must meet certain operating system (OS) requirements to ensure seamless sync across different platforms. These restrictions are not enforced by OpenCloud but originate from system limitations.

## Key Guidelines

1. Avoid using prohibited characters or reserved words in filenames on any OS.
2. If syncing from Linux/macOS to a Windows-based share, ensure filenames follow Windows naming rules.
3. To change casing (e.g., `File.txt` → `file.txt`) on Linux/macOS when syncing to Windows, rename the file to a completely new name, let it sync, then rename it to the desired casing.

## Common Limitations

### a. Maximum Path Length

- Some environments allow long filenames but Windows has a default limit of 260 characters when using APIs (e.g., VFS). Exceeding this limit may result in sync errors, often with notifications in-app
- Windows 10 and later versions can lift this limit if explicitly enabled (see Microsoft’s documentation).

### b. Forbidden Characters

| OS              | Forbidden Characters            |
| --------------- | ------------------------------- | ------------ |
| **Linux/macOS** | `/`                             |
| **Windows**     | `<`, `>`, `:`, `"`, `/`, `\`, ` | `, `?`, `\*` |

### c. Non-Printable ASCII Characters

- Linux/macOS: NUL (character code 0)
- Windows: ASCII 0 – 31  
  While valid on some systems, such characters often cause issues during syncing.

### d. Reserved Filenames (Windows)

Avoid using any of the following as filenames:  
`CON`, `PRN`, `AUX`, `NUL`, `COM1`–`COM9`, `LPT1`–`LPT9`

### e. Special Rules

- On Linux/macOS syncing to SMB, filenames that differ only by case may cause conflicts—rename files clearly to avoid sync failures.
- Windows: Filenames must not end in a space or period (`.`).

## Example

Creating a file named `example.` or `example.LPT1` on macOS may sync to OpenCloud successfully. However, when accessed via a Windows client, these files may be rejected due to reserved naming or format rules, leading to inconsistent sync behavior across devices.

## Summary

| Restriction Type     | Action Item                                      |
| -------------------- | ------------------------------------------------ |
| Path Length          | Keep paths under ~260 characters unless extended |
| Forbidden Characters | Remove disallowed characters from names          |
| Control Characters   | Avoid non-printable ASCII characters             |
| Reserved Filenames   | Do not use Windows reserved names                |
| Case-Only Changes    | Rename to a temporary name before syncing        |
| Trailing Characters  | Avoid filenames ending in space or period        |
