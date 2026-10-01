---
title: 'Translations'
sidebar_position: 3
---

OpenCloud Web uses [gettext](https://www.gnu.org/software/gettext/) for translations, via the
[vue3-gettext](https://jshmrtn.github.io/vue3-gettext/) library. Your app brings its own translations and hands them to
the Web runtime. The language that the user picked in OpenCloud is then also used for your app.

Translations are optional. An app without them simply shows its original strings.

## Marking strings

In a script or a composable, get `$gettext` from `useGettext`:

```typescript
import { useGettext } from 'vue3-gettext';

const { $gettext } = useGettext();

const title = $gettext('Your application name');
```

In a template, `$gettext` is globally available:

```html
<template>
  <p>{{ $gettext('No files here') }}</p>
</template>
```

Pass variables as an object. Use the `%{name}` syntax in the string, never string concatenation, because the word order
changes between languages:

```typescript
$gettext('Open «%{resource}»', { resource: resource.name });
```

For plurals, use `$ngettext` with the singular form, the plural form, the count, and the variables:

```typescript
const { $ngettext } = useGettext();

$ngettext(
  'Delete the selected resource?',
  'Delete %{amount} selected resources?',
  resources.length,
  { amount: resources.length.toString() }
);
```

:::warning
The extraction tool reads your source code, not your runtime values. Always pass a plain string literal to `$gettext`.
A variable or a template literal cannot be extracted.
:::

## Setting up the workflow

Add [vue3-gettext](https://jshmrtn.github.io/vue3-gettext/) as a dev-dependency. It ships the `vue-gettext-extract` and
`vue-gettext-compile` commands.

Create a `gettext.config.cjs` in the root of your app. It defines which files are scanned and which languages you
support:

```javascript title="gettext.config.cjs"
module.exports = {
  input: {
    path: './src',
    include: ['**/*.js', '**/*.ts', '**/*.vue']
  },
  output: {
    locales: ['de', 'es', 'fr', 'it'],
    path: './l10n/locale',
    potPath: '../template.pot',
    jsonPath: '../translations.json',
    flat: false,
    linguas: false
  }
};
```

Add two scripts to your `package.json`:

```json title="package.json"
{
  "scripts": {
    "l10n:extract": "vue-gettext-extract",
    "l10n:compile": "vue-gettext-compile"
  }
}
```

`l10n:extract` collects all marked strings into `l10n/template.pot` and creates one `.po` file per language under
`l10n/locale`. Run it whenever you add or change a string.

`l10n:compile` turns the `.po` files into a single `l10n/translations.json`. Run it after the translated `.po` files
come back. Commit `translations.json`, because the build imports it.

How the `.po` files get translated is up to you. The OpenCloud repositories use
[Transifex](https://www.transifex.com/), but any gettext based service or a manual workflow works as well.

## Registering translations

Import `translations.json` and return it from your app definition. The Web runtime merges it into the global
translations when your app is loaded.

```typescript title="src/index.ts"
import { defineWebApplication } from '@opencloud-eu/web-pkg';
import { useGettext } from 'vue3-gettext';
import translations from '../l10n/translations.json';

export default defineWebApplication({
  setup() {
    const { $gettext } = useGettext();

    return {
      appInfo: {
        name: $gettext('Your application name'),
        id: 'your-app'
      },
      translations
    };
  }
});
```

The file is a map of language key to message map:

```json title="l10n/translations.json"
{
  "de": {
    "No files here": "Keine Dateien hier"
  },
  "fr": {
    "No files here": "Aucun fichier ici"
  }
}
```
