---
title: 'Extension Points'
sidebar_position: 1
---

Extension points are standardized places where extensions are used. If you build an extension that has the
[type](./extension-types/) of an extension point, and lists the id of that extension point in its `extensionPointIds`,
your extension gets used there without any further wiring.

The lists below show the extension points that the OpenCloud Web runtime and the built-in apps provide. The `Multiple`
column tells you if the extension point renders all matching extensions or only a single one. Your app can also
[define its own extension points](#defining-your-own-extension-points), so that other apps can extend it.

## Dynamic extension points

Dynamic extension points are specific to each app. `${appId}` is the `id` you define in the `appInfo` of your app,
for example `files` or `admin-settings`. Use these ids to add something to the user interface of a specific app,
including apps you do not own (e.g. add a nav item to the sidebar of the files app).

| Extension point id                    | Extension type         | Multiple | Description                                                                                               |
| ------------------------------------- | ---------------------- | -------- | --------------------------------------------------------------------------------------------------------- |
| `app.${appId}.navItems`               | `sidebarNav`           | yes      | Navigation items in the left sidebar.                                                                     |
| `app.${appId}.sidebar-nav.main`       | `customComponent`      | yes      | Main area of the left sidebar, below the nav items.                                                       |
| `app.${appId}.sidebar-nav.bottom`     | `customComponent`      | yes      | Bottom area of the left sidebar, above the version info.                                                  |
| `app.${appId}.floating-action-button` | `floatingActionButton` | no       | Primary action button. Rendered in the left sidebar on desktop and as a floating action button on mobile. |

## Runtime

| Extension point id                | Extension type     | Multiple | Description                                                                                                            |
| --------------------------------- | ------------------ | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| `app.runtime.header.left`         | `customComponent`  | yes      | Left area of the global top bar.                                                                                       |
| `app.runtime.header.center`       | `customComponent`  | yes      | Center area of the global top bar.                                                                                     |
| `app.runtime.header.right`        | `customComponent`  | yes      | Right area of the global top bar.                                                                                      |
| `app.runtime.header.app-menu`     | `appMenuItem`      | yes      | Application switcher menu in the top left.                                                                             |
| `app.runtime.global-progress-bar` | `customComponent`  | no       | Progress bar for the global loading state. The user can pick one of the registered extensions on the preferences page. |
| `app.runtime.snackbars`           | `customComponent`  | yes      | Snackbar (toast message) area.                                                                                         |
| `app.runtime.preferences.panels`  | `accountExtension` | yes      | Panels on the preferences page, reachable via the top right user menu.                                                 |

## Files app

### Actions

| Extension point id                     | Extension type | Multiple | Description                                                                                    |
| -------------------------------------- | -------------- | -------- | ---------------------------------------------------------------------------------------------- |
| `global.files.context-actions`         | `action`       | yes      | Right click context menu of a resource.                                                        |
| `global.files.batch-actions`           | `action`       | yes      | Batch actions in the app bar above file lists.                                                 |
| `global.files.resource-table-actions`  | `action`       | yes      | Inline actions in a row of the resource table.                                                 |
| `global.files.default-action-fallback` | `action`       | no       | Fallback for the default action (left click) on a resource, used when no other app handles it. |
| `app.files.sidebar.actions`            | `action`       | yes      | Actions panel of the right sidebar.                                                            |
| `app.files.upload-menu`                | `action`       | yes      | Upload menu.                                                                                   |
| `app.files.quick-actions`              | `action`       | yes      | Quick actions in a row of the resource table.                                                  |
| `app.files.trash-quick-actions`        | `action`       | yes      | Quick actions in a row of the trash overview.                                                  |

### Right sidebar

| Extension point id                                  | Extension type    | Multiple | Description                                                                                                           |
| --------------------------------------------------- | ----------------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| `global.files.sidebar`                              | `sidebarPanel`    | yes      | Panels of the right sidebar. Used in any file context, meaning the files app as well as viewer and editor apps.       |
| `app.files.sidebar.file-details.table`              | `customComponent` | no       | Details table of a file. `space` and `resource` can be retrieved via injection context.                               |
| `app.files.sidebar.space-details.table`             | `customComponent` | no       | Details table of a space. `space` and `resource` can be retrieved via injection context.                              |
| `app.files.sidebar.shares-panel.shared-with.top`    | `customComponent` | no       | Top section of the people list in the shares panel. `space` and `resource` can be retrieved via injection context.    |
| `app.files.sidebar.shares-panel.shared-with.bottom` | `customComponent` | no       | Bottom section of the people list in the shares panel. `space` and `resource` can be retrieved via injection context. |

### Folder views

Folder views define how the content of a page is presented, for example as a table or as a tile grid. Each page has its
own extension point.

| Extension point id                          | Extension type | Multiple | Description              |
| ------------------------------------------- | -------------- | -------- | ------------------------ |
| `app.files.folder-views.folder`             | `folderView`   | no       | Regular folders.         |
| `app.files.folder-views.project-spaces`     | `folderView`   | no       | Project spaces overview. |
| `app.files.folder-views.favorites`          | `folderView`   | no       | Favorites page.          |
| `app.files.folder-views.trash`              | `folderView`   | no       | Trash of a single space. |
| `app.files.folder-views.trash-overview`     | `folderView`   | no       | Trash overview.          |
| `app.files.folder-views.shared-with-me`     | `folderView`   | no       | Shared with me page.     |
| `app.files.folder-views.shared-with-others` | `folderView`   | no       | Shared with others page. |
| `app.files.folder-views.shared-via-link`    | `folderView`   | no       | Shared via link page.    |
| `app.files.folder-views.search`             | `folderView`   | no       | Search results page.     |

### Other

| Extension point id                 | Extension type         | Multiple | Description                                                                                      |
| ---------------------------------- | ---------------------- | -------- | ------------------------------------------------------------------------------------------------ |
| `app.files.floating-action-button` | `floatingActionButton` | no       | Primary action button of the files app. Instance of the dynamic extension point described above. |
| `global.files.resource-indicator`  | `resourceIndicator`    | yes      | Status icons and tags shown next to the name of a resource.                                      |

## Other apps

| Extension point id            | Extension type | Multiple | Description                                                |
| ----------------------------- | -------------- | -------- | ---------------------------------------------------------- |
| `app.search.provider`         | `search`       | yes      | Search engines for the search input in the global top bar. |
| `app.preview.toolbar-actions` | `action`       | yes      | Toolbar of the preview app.                                |

## Defining your own extension points

Define an extension point wherever your app has a place that other apps may fill. A good example is a toolbar or a
panel that is useful beyond your own use case.

### Declaring an extension point

An extension point is a plain object of the `ExtensionPoint` type. Keep it in its own file, for example
`src/extensionPoints.ts`, so that you can use it in several places:

```typescript title="src/extensionPoints.ts"
import { ActionExtension, ExtensionPoint } from '@opencloud-eu/web-pkg';

export const toolbarExtensionPoint: ExtensionPoint<ActionExtension> = {
  id: 'app.my-app.toolbar',
  extensionType: 'action',
  multiple: true
};
```

`ExtensionPoint` accepts the following keys:

- `id` - the id of the extension point. Extensions list it in their `extensionPointIds`. Use the same dot-formatted
  namespace as for extension ids, and put your app id in it.
- `extensionType` - the [type](./extension-types/) of the extensions that this extension point accepts.
- `multiple` - whether all matching extensions are used, or only a single one. Defaults to `false`.
- `defaultExtensionId` - the extension that is used when `multiple` is `false` and the user did not pick one.
- `userPreference` - makes the extension point configurable by users, see below.

### Registering an extension point

Return your extension points from the app definition. The key takes a `Ref<ExtensionPoint[]>`, so use a `computed`:

```typescript title="src/index.ts"
import { defineWebApplication } from '@opencloud-eu/web-pkg';
import { computed } from 'vue';
import { toolbarExtensionPoint } from './extensionPoints';

export default defineWebApplication({
  setup() {
    return {
      appInfo: {
        name: 'My app',
        id: 'my-app'
      },
      extensionPoints: computed(() => [toolbarExtensionPoint])
    };
  }
});
```

Registration is not needed to query extensions. It makes your extension point known to the runtime, which is required
for the preferences page, and it documents the extension point for other developers.

### Rendering the extensions

For the type `customComponent`, mount a `CustomComponentTarget` at the place where the extensions belong. It queries
the registry and respects the user preference:

```html title="src/App.vue"
<template>
  <custom-component-target :extension-point="componentExtensionPoint" />
</template>

<script setup lang="ts">
  import { CustomComponentTarget } from '@opencloud-eu/web-pkg';
  import { componentExtensionPoint } from './extensionPoints';
</script>
```

For all other types, query the registry yourself and render the result the way your extension point needs it:

```typescript
import { ActionExtension, useExtensionRegistry } from '@opencloud-eu/web-pkg';
import { computed } from 'vue';
import { toolbarExtensionPoint } from './extensionPoints';

const extensionRegistry = useExtensionRegistry();

const actions = computed(() =>
  extensionRegistry
    .requestExtensions<ActionExtension>(toolbarExtensionPoint)
    .map(({ action }) => action)
);
```

### Letting users choose

Add a `userPreference` to your extension point to let users pick one of the registered extensions. This only makes
sense when `multiple` is `false`:

```typescript title="src/extensionPoints.ts"
import { ExtensionPoint, CustomComponentExtension } from '@opencloud-eu/web-pkg';
import { useGettext } from 'vue3-gettext';

const { $gettext } = useGettext();

export const progressBarExtensionPoint: ExtensionPoint<CustomComponentExtension> = {
  id: 'app.my-app.progress-bar',
  extensionType: 'customComponent',
  userPreference: {
    label: $gettext('Progress bar'),
    description: $gettext('Choose how the loading state is shown.')
  }
};
```

The extension point then gets a dropdown on the preferences page, reachable via the top right user menu. The dropdown
only appears when at least one extension is registered for the extension point. Each extension can provide its own
`userPreference.optionLabel` as the label in that dropdown.
