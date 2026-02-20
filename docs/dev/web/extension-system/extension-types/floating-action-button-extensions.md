---
title: 'Floating Action Button extensions'
sidebar_position: 8
id: floating-action-button-extensions
---

## Extension Type FloatingActionButton

This extension type allows apps to register a global action that is either displayed within the left sidebar (for desktop resolutions) or as a floating action button (for mobile resolutions). The extension point for this extension type is `global.floating-action-button`.

:::warning
You need to take care of the visibility of your floating action button extension via the `isActive` property, otherwise you might end up overwriting other extensions' action buttons. In most cases, it makes sense to only display the button when your app is currently active.
:::

### Configuration

To define a floating action button extension, you implement the `FloatingActionButtonExtension` interface. Here's what it looks like:

```typescript
interface FloatingActionButtonExtension {
  id: string;
  type: 'floatingActionButton';
  extensionPointIds?: string[];
  label: () => string;
  isActive: () => boolean;
  isDisabled?: () => boolean;
  color?: string;
  icon?: string;
  handler?: () => Promise<void> | void;
  dropComponent?: Component;
}
```

For `id`, `type`, and `extensionPointIds`, please see [extension base section](../#extension-base-configuration) in the top level docs.

The `handler` property specifies a function to be executed when the floating action button is clicked. If you want to use a dropdown component instead of a click handler, you can specify a `dropComponent` that will be rendered on click.

`isDisabled` controls the disabled state of the button whereas `isActive` determines if the button is showing at all.

`icon` is an icon name string that can be picked from [Remix Icon](https://remixicon.com/).

### Example

The following example shows how the files app is registering a floating action button extension for creating new files or folders. Note that the example assumes you're in a Vue injection context (e.g. within the `setup` method of your app's `defineWebApplication` call).

```typescript
import { useGettext } from 'vue3-gettext';
import CreateOrUploadMenu from './components/CreateOrUploadMenu.vue';
import { useIsFilesAppActive, useResourcesStore } from '@opencloud-eu/web-pkg';

const { $gettext } = useGettext();
const isFilesAppActive = useIsFilesAppActive();
const resourcesStore = useResourcesStore();

const extension = {
  id: 'com.github.opencloud-eu.web.files.floating-action-button',
  extensionPointIds: ['global.floating-action-button'],
  type: 'floatingActionButton',
  icon: 'add',
  label: () => $gettext('New'),
  isActive: () => {
    return unref(isFilesAppActive);
  },
  isDisabled: () => {
    return !resourcesStore.currentFolder?.canUpload();
  },
  dropComponent: CreateOrUploadMenu
};
```
