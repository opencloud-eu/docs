---
sidebar_position: 8
id: best-practice
title: Best practice
description: Best practice how to use Spaces
draft: true
---

# Best Practices for Organizing Spaces in OpenCloud

Spaces are collaborative areas meant to be used by multiple users. Unlike personal storage, they must be structured in a way that supports clarity, collaboration, and scalability. This guide helps you set up and maintain well-organized, long-term usable Spaces.

## General Principles

- Plan first – Don't treat Spaces like ad-hoc storage. Think ahead.
- Think in roles and teams – Structure based on how people work together.
- Keep it scalable – Choose a structure that works now _and_ with more users later.
- Apply consistency – Naming, access, and structure should follow shared rules.

## Folder Structure: Recommended Patterns

### Example: Family

```plaintext
📁 Family Space
 ├── 📂 Documents
 │    ├── 🧾 Insurance
 │    └── 📑 Contracts
 ├── 📂 Photos
 │    ├── 📸 2024
 │    └── 📸 2023
 └── 📂 Shared Notes
```

### School / Kindergarten

```plaintext

📁 2024
 ├── 📂 Class 3B
 │    ├── 📂 Teaching Materials
 │    ├── 📂 Parent Communication
 │    ├── 📂 Homework Submissions
 │    └── 📂 Events & Photos
 ├── 📂 Class 4C
 │    ├── 📂 Teaching Materials
 │    ├── 📂 Parent Communication
 │    ├── 📂 Homework Submissions
 │    └── 📂 Events & Photos

```

### Company / Team

```plaintext
📁 Marketing Team
 ├── 📂 Campaigns
 │    ├── 📂 Q1-2025
 │    └── 📂 Q2-2025
 ├── 📂 Templates
 ├── 📂 Reports
 └── 📂 Meeting Notes
```

## Naming Conventions

- Use clear, descriptive names – avoid "new folder" or cryptic titles
- Prefer lowercase-with-dashes or Title Case
- Add dates when relevant: `report-2025-Q2.pdf` or `Budget 2024.xlsx`
- Avoid special characters: `& % $ § !` may break integrations

## Ownership & Access Guidelines

- Assign Space Owners: Responsible for structure and permissions
- Use Groups where possible for access control (e.g. `staff`, `students`, `parents`)
- Keep sensitive content in separate folders with restricted access
- Define editing vs. viewing rights clearly

## Archiving & Clean-Up

- Set up an archive folder for old or unused files
- Annually review the Space and remove outdated content
- Use versioning or export before deletion if unsure

## Common Pitfalls to Avoid

| ❌ Don’t                        | ✅ Instead                       |
| ------------------------------- | -------------------------------- |
| Dump all files in root folder   | Use clear subfolders             |
| Mix personal and shared content | Keep personal data in "Personal" |
| Give all users full access      | Apply least-privilege principle  |
| Use inconsistent naming         | Define and follow conventions    |

## Shareable Quick Start Template

You can use this as a template for new Spaces:

```plaintext
📁 [Team/Project Name]
 ├── 📂 Documents
 ├── 📂 Planning
 ├── 📂 Resources
 ├── 📂 Archive
 └── README.md (Space purpose, structure, rules)
```

## Summary

| Goal                         | How                                |
| ---------------------------- | ---------------------------------- |
| Make Spaces easy to navigate | Use clear folder names & hierarchy |
| Avoid permission chaos       | Define ownership and roles         |
| Keep things clean            | Review regularly and archive       |
| Support collaboration        | Use group access & standard naming |
