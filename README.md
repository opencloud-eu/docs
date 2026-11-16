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

Deployment is done by the Woodpecker CI (`.woodpecker/build.yaml`), there is no manual deploy step:

- Every push to `main` builds the site and deploys it to staging.
- Every tag deploys the site to production. Tags are created by the release PR that [ready-release-go](https://github.com/woodpecker-ci/plugin-ready-release-go) opens (`🎉 Release x.y.z`): merging that PR creates the tag.


## Screenshot Guidelines

| Component        | Width  |
|:----------------|:------:|
| Full screen      | 1920px |
| Menu             | 400px  |
| Pop-up / Modal   | 500px  |

The widths are display sizes for the `width` attribute. Save the image file at most twice as large as it is displayed (e.g. at most 1000px wide for a 500px pop-up, or at most 800px tall for a phone screenshot shown with `height="400"`). That's sharp enough for high-DPI screens, and larger files only make readers download more. The content column is never wider than 1300px, so full-screen screenshots don't need more than 2600px.

### Example

To include a screenshot in your documentation, use the following format:

```jsx
<img src={require("./../../img/PATH/EXAMPLE.png").default} alt="EXAMPLE" width="1920" height="1080" loading="lazy" decoding="async" />
```

- Use `require(...)` for image paths so they are bundled correctly by Docusaurus
- Always include a meaningful `alt` text to improve accessibility and SEO

### Image Directory Structure

- Store images in the `img` directory of the corresponding documentation area.
- Mirror the documentation structure below `img` as closely as possible.
- Do not create an additional `index` directory for images used by an `index.md` page.
- Place area-specific or topic-specific images in the corresponding subdirectory.
- Place shared images in a clearly named common directory.
- Use lowercase, descriptive, kebab-case filenames without spaces.
- Add `loading="lazy"` and `decoding="async"` to every `<img>` tag, so browsers only download an image when it gets close to the visible area. Docusaurus adds these attributes automatically for Markdown image syntax (`![alt](./img.png)`), but not for JSX `<img>` tags.
- Set both `width` and `height` on every `<img>` tag, with the same aspect ratio as the image file (e.g. a 2880×1620 screenshot shown with `width="1920"` gets `height="1080"`). The browser then reserves the image's space before it is loaded, so the page doesn't jump while lazy images load.

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
