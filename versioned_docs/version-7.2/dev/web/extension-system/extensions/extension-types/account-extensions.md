---
title: 'Account extensions'
sidebar_position: 9
id: account-extensions
---

## Extension Type AccountExtension

Account extensions add a panel to the preferences page, which is reachable via the user menu in the top right. Each
registered extension gets its own entry in the navigation of that page.

### Configuration

To define an account extension, you implement the `AccountExtension` interface. Here's what it looks like:

```typescript
interface AccountExtension {
  id: string;
  type: 'accountExtension';
  extensionPointIds?: string[];
  content: Slot | Component;
  label: () => string;
  icon: string;
}
```

For `id`, `type`, and `extensionPointIds`, please see [base configuration section](../index.md#base-configuration) in the extensions docs.

- `content` - The component to render inside the panel.
- `label` - Returns the title of the panel. Wrap it in `$gettext` to make it translatable.
- `icon` - The icon of the navigation entry, can be picked from [Remix Icon](https://remixicon.com/).

### Example

The following example is taken from the Web runtime. It adds the app tokens panel to the preferences page.

```typescript title="src/extensions.ts"
const extension: AccountExtension = {
  id: 'com.github.opencloud-eu.web.runtime.preferences-panels.app-tokens',
  type: 'accountExtension',
  extensionPointIds: ['app.runtime.preferences.panels'],
  label: () => $gettext('App Tokens'),
  icon: 'key-2',
  content: AppTokens
};
```
