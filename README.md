# 🌐 Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.


## Installation

```bash
pnpm install
```


## Local Development

Clone this repository and start the local dev server:

```bash
pnpm start
```

This command will launch a local development server and open the site in your browser. Changes are hot-reloaded automatically.

> ⚠️ `docs` tree contains redirects, because some documentation files may have been removed or moved, and old bookmarks should still work. To have those working in the local dev server, the documentation needs to be built first:

```bash
pnpm build
pnpm run serve
```

### Start docs in German

To launch the documentation in German, run:

```bash
pnpm run start --locale de
```

> ⚠️ Switching languages via the language switcher is currently not supported.




## Build

```bash
pnpm build
```

This command generates static content in the `build` folder. You can serve it using any static file hosting service.


## Deployment

### Using SSH:

```bash
USE_SSH=true pnpm deploy
```

### Without SSH:

```bash
GIT_USER=<Your GitHub username> pnpm deploy
```

If you're using GitHub Pages, this will push the production build to the `gh-pages` branch.


## Screenshot Guidelines

| Component        | Width  |
|:----------------|:------:|
| Full screen      | 1920px |
| Menu             | 400px  |
| Pop-up / Modal   | 500px  |

> Highlight key elements in the screenshot with red borders or boxes if needed.

### Example

To include a screenshot in your documentation, use the following format:

```jsx
<img src={require("./../../img/PATH/EXAMPLE.png").default} alt="EXAMPLE" width="1920" />
```

- Use `require(...)` for image paths so they are bundled correctly by Docusaurus
- Always include a meaningful `alt` text to improve accessibility and SEO


## Markdown Guidelines

To maintain a consistent structure across all docs, follow these formatting conventions:

### Frontmatter Example

All `.md` files must begin with a valid frontmatter block:

```yaml
---
id: getting-started
title: Getting Started
sidebar_position: 1
description: A quick intro to OpenCloud
---
```

- `id` must be unique and match the filename (without `.md`)
- `sidebar_position` defines the ordering in the sidebar
- `description` is required to ensure consistent SEO metadata and link previews. Always include a meaningful and concise description.

### Heading Hierarchy

Use the correct heading levels:

```markdown
# Page Title

## Section Heading

### Subsection Heading

#### Optional Sub-subsection
```

> Do not skip heading levels (e.g., don’t go from `##` directly to `####`).


### Info Blocks

Use Docusaurus-style info blocks to highlight important content:

```markdown
:::tip
Helpful tip content goes here.
:::

:::info
General information goes here.
:::

:::warning
Warnings go here.
:::

:::danger
Critical notices go here.
:::
```

### Lists and Steps

Use regular markdown for ordered lists. Do **not** nest deeply.

```markdown
1. First step
2. Second step
3. Third step
```

## Format Before Pushing

Before committing changes, ensure proper formatting using:

```bash
pnpm format:write
pnpm lint:md:fix
```

These commands will:

- Format all project files
- Lint and auto-fix markdown formatting
- Ensure consistent style across documentation

Thanks for helping us keep the docs clean, professional, and easy to read!