---
title: 'Configuration'
sidebar_position: 1
---

This page describes how to add configuration options to your app. Administrators can then change the behaviour of your
app.

## Manifest and defaults

Put static metadata of your app into `src/manifest.json`. It ends up in the `manifest.json` of your build, together with
the `name`, `version`, `description`, `license` and `author` fields of your `package.json`, and the entry point of your
app.

Default values for the app config belong under the `config` key:

```json title="src/manifest.json"
{
  "config": {
    "maxFileSize": 10485760,
    "showPreview": true
  }
}
```

## Overriding values

There are two ways to override the defaults:

- During development, put your values into `src/config.json`. The file is merged on top of the `config` key of
  `src/manifest.json`. Don't commit values that only apply to your machine.
- In a real deployment, administrators override them via the `apps.yaml` file, see the
  [web applications admin docs](../../../../admin/configuration/web-applications).

```json title="src/config.json"
{
  "showPreview": false
}
```

## Reading values in your app

The merged config is passed to the `setup` function of your app definition as `applicationConfig`:

```typescript title="src/index.ts"
import { defineWebApplication } from '@opencloud-eu/web-pkg';

export default defineWebApplication({
  setup({ applicationConfig }) {
    const showPreview = applicationConfig?.showPreview ?? true;

    // ...
  }
});
```

Always provide a fallback value. The config can be empty, and an administrator can set any value.
