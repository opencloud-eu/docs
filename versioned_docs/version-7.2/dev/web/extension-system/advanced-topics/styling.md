---
title: 'Styling'
sidebar_position: 2
---

This page describes how to style your app so that it fits into OpenCloud Web.

## Design system components

The `@opencloud-eu/design-system` package contains the components that OpenCloud Web is built with, for example buttons,
inputs and modals. Use them where possible. Your app then follows the platform look and inherits accessibility and
theming for free. See the [design system documentation](../../design-system) for the list of components.

## Color roles

OpenCloud Web exposes its colors as CSS variables with the `--oc-role-` prefix, for example `--oc-role-surface` or
`--oc-role-on-surface`. Always use these variables instead of fixed color values. They change with the active theme and
with the color scheme, so your app stays readable in light and dark mode.

```css
.my-panel {
  background-color: var(--oc-role-surface-container);
  color: var(--oc-role-on-surface);
}
```

See [the defaults](https://github.com/opencloud-eu/web/blob/stable-7.1/packages/design-system/src/styles/defaults.css) for a
complete list of color roles.

## Tailwind CSS

The `@opencloud-eu/extension-sdk` package ships a preconfigured [Tailwind CSS](https://tailwindcss.com/) setup. Import
its stylesheet in your entrypoint (typically `src/index.ts`) to use it:

```typescript title="src/index.ts"
import '@opencloud-eu/extension-sdk/tailwind.css';
```

Tailwind classes need the `ext:` prefix in apps. The prefix avoids style conflicts with the OpenCloud Web runtime.

```html
<main class="ext:p-4 ext:flex ext:gap-2">...</main>
```

The setup maps the color roles to Tailwind color utilities, so `--oc-role-surface` is available as `bg-role-surface`,
`text-role-on-surface` and so on:

```html
<div class="ext:bg-role-surface-container ext:text-role-on-surface">...</div>
```

It also sets the OpenCloud font family, a spacing unit of `4px`, and the breakpoints `xs`, `sm`, `md`, `lg` and `xl`.
