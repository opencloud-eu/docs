---
sidebar_position: 90
id: best-practice
title: Best Practices for Organizing Spaces
description: Learn how to organize files and folders in Spaces so that content remains easy to find, understand, and maintain.
draft: false
---

# Best Practices for Organizing Spaces

Spaces are collaborative areas designed for content that is shared and maintained by multiple users.

A good structure helps users find content quickly and keeps a Space manageable as the amount of content grows.

When organizing a Space, follow two main principles:

1. Keep folder structures flat.
2. Use descriptive, self-contained filenames.

The general rule is:

> Folder structure should provide additional context, but files should not depend on that context to be understood.

## Keep Folder Structures Flat

Avoid creating deeply nested folder structures.

As a general guideline, use no more than three folder levels. Keep the structure even flatter where possible.

Deep structures can make content harder to navigate and require users to know exactly where a file was stored.

Avoid structures such as:

```text
Customers/
└── Acme/
    └── Contracts/
        └── 2026/
            └── Final/
                └── contract.pdf
```

Instead, reduce the number of levels and move important information into the filename:

```text
Customers/
└── Acme/
    └── Contracts/
        └── Acme - Service Agreement - 2026.pdf
```

This keeps the folder structure easy to navigate while preserving the information required to identify the file.

Do not create additional folder levels only to represent attributes such as:

- year
- document status
- document type
- version
- responsible person

Consider whether this information can be included in the filename instead.

## Use Descriptive Filenames

A filename should describe its content without requiring users to know where the file was originally stored.

Files can appear outside their folder structure when they are:

- returned in search results
- shown in a recent-files list
- downloaded
- attached to an email
- shared with other users
- moved to another folder or Space

For example, a filename such as:

```text
contract.pdf
```

provides very little information outside its original folder.

A more descriptive filename is:

```text
Acme - Service Agreement - 2026.pdf
```

The file can now be identified independently of its location.

### Include Relevant Context

Depending on the type of content, useful filename components can include:

- customer, team, or project name
- document type
- date or year
- reporting period
- topic
- status, if relevant

For example:

```text
Acme - Service Agreement - 2026.pdf
Marketing - Campaign Report - 2026-Q2.pdf
Project Atlas - Meeting Notes - 2026-08-11.odt
Class 3B - Parent Information - Summer Trip.pdf
```

Only include information that helps users identify the file. Avoid filenames that become unnecessarily long or difficult to scan.

## Use Consistent Naming Conventions

Choose a naming convention for a Space and apply it consistently.

For example:

```text
[Project] - [Document Type] - [Date]
```

could result in:

```text
Project Atlas - Budget - 2026.xlsx
Project Atlas - Meeting Notes - 2026-08-11.odt
Project Atlas - Status Report - 2026-Q3.pdf
```

Consistency makes files easier to recognize and helps users understand how new files should be named.

When dates are part of a filename, use a consistent format. A format such as `YYYY-MM-DD` also keeps files sorted chronologically:

```text
2026-08-11 - Meeting Notes.odt
2026-08-18 - Meeting Notes.odt
2026-08-25 - Meeting Notes.odt
```

## Organize Content by Purpose

Folders should represent meaningful areas of work rather than every possible property of a file.

For example, a team Space could use:

```text
Marketing/
├── Campaigns/
├── Reports/
├── Templates/
└── Archive/
```

Files inside these folders should still use descriptive filenames:

```text
Marketing/
├── Campaigns/
│   ├── Product Launch - Campaign Plan - 2026.odt
│   └── Summer Campaign - Results - 2026.pdf
├── Reports/
│   ├── Marketing - Monthly Report - 2026-07.pdf
│   └── Marketing - Monthly Report - 2026-08.pdf
├── Templates/
│   └── Marketing - Campaign Brief - Template.odt
└── Archive/
```

This allows the folder structure and filenames to complement each other.

## Examples

The appropriate structure depends on how a Space is used. The following examples provide starting points that can be adapted to your organization.

### Company or Team

```text
Marketing/
├── Campaigns/
│   ├── Product Launch - Campaign Plan - 2026.odt
│   └── Summer Campaign - Results - 2026.pdf
├── Reports/
│   └── Marketing - Quarterly Report - 2026-Q2.pdf
├── Templates/
│   └── Marketing - Campaign Brief - Template.odt
└── Archive/
```

### Project

```text
Project Atlas/
├── Planning/
│   ├── Project Atlas - Project Plan.odt
│   └── Project Atlas - Budget - 2026.xlsx
├── Meetings/
│   ├── Project Atlas - Meeting Notes - 2026-08-04.odt
│   └── Project Atlas - Meeting Notes - 2026-08-11.odt
└── Deliverables/
    └── Project Atlas - Final Report.pdf
```

### School or Kindergarten

```text
Class 3B/
├── Teaching Materials/
│   └── Class 3B - Mathematics - Fractions.pdf
├── Parent Information/
│   └── Class 3B - Parent Information - Summer Trip.pdf
└── Events/
    └── Class 3B - Summer Festival - 2026.pdf
```

### Family

```text
Family/
├── Household/
│   ├── Insurance - Home - 2026.pdf
│   └── Electricity - Contract - Example Energy.pdf
├── Photos/
│   └── Summer Holiday - 2026/
└── Archive/
```

The same principles apply in each case: keep the hierarchy understandable and include enough information in filenames for files to remain identifiable outside their folders.

## Manage Access Separately From Structure

Do not use deeply nested folders only to represent organizational responsibilities or access models.

Where possible:

- assign appropriate Space roles
- use groups for recurring sets of users
- grant only the permissions users require
- use a separate Space for sensitive content when a different set of members requires access

A folder should primarily help users organize and find content.

## Archive Content Regularly

Spaces become harder to use when obsolete and current content is mixed together.

Consider creating an `Archive` folder for content that is no longer actively used but should be retained:

```text
Project Atlas/
├── Planning/
├── Meetings/
├── Deliverables/
└── Archive/
```

Review Spaces regularly and move outdated content to the archive when appropriate.

Avoid creating archive structures with unnecessary levels. Descriptive filenames should make archived files identifiable even when several years of content are stored together.

## Common Pitfalls

| Avoid                                               | Instead                                                 |
| --------------------------------------------------- | ------------------------------------------------------- |
| Deep folder hierarchies                             | Keep structures to approximately three levels           |
| Generic filenames such as `document.pdf`            | Include enough context in the filename                  |
| Encoding all information in the folder path         | Put important identifying information in filenames      |
| Creating folders for every year, status, or version | Add these attributes to filenames when appropriate      |
| Different naming styles within the same Space       | Define and follow one convention                        |
| Mixing obsolete and active content                  | Move inactive content to an archive                     |
| Using folders as the primary access-control model   | Manage access through appropriate roles and permissions |

## Quick Start

When creating a new Space:

1. Identify the main areas of work.
2. Create only the folders needed for those areas.
3. Keep the hierarchy as flat as possible.
4. Define a filename convention.
5. Make filenames understandable without their folder path.
6. Define who is responsible for maintaining the Space.
7. Review and archive content regularly.

A simple starting point could be:

```text
[Space Name]/
├── Documents/
├── Planning/
├── Resources/
└── Archive/
```

Adapt the folder names to the purpose of the Space instead of adding additional hierarchy.

The goal is not to create the most detailed folder structure possible. The goal is to make content easy to find, understand, share, and maintain.
