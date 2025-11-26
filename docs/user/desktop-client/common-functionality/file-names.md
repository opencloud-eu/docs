---
sidebar_position: 5
id: file-names
title: File Naming Rules
description: File Naming Rules for OpenCloud Desktop
draft: false
---

# Filename restrictions on OpenCloud Desktop

When using the OpenCloud Desktop Client, file and folder names must meet certain operating system (OS) requirements to ensure seamless sync across different platforms. These restrictions are not enforced by OpenCloud but originate from system limitations.

## Key Guidelines

- Avoid using prohibited characters or reserved words in filenames on any OS.
- If syncing from Linux/macOS to a Windows-based share, make sure filenames are compatible with Windows naming restrictions.
- To change casing (e.g., `File.txt` → `file.txt`) on Linux/macOS when syncing to Windows, rename the file to a completely new name, let it sync, then rename it to the desired casing.

## Common Limitations

### a. Maximum Path Length

Windows limits file paths to 260 characters by default.  
If your sync root exceeds this, the Desktop Client will warn:  
"The path 'YOUR.LONG.PATH' is too long. Please enable long paths in the Windows settings or choose a different folder."

On Windows 10 and later, you can remove this limit by enabling Long Paths. See [Microsoft’s documentation](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later).

### b. Forbidden Characters

| OS      | Forbidden Characters            |
| ------- | ------------------------------- | ------------ |
| Windows | `<`, `>`, `:`, `"`, `/`, `\`, ` | `, `?`, `\*` |

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
