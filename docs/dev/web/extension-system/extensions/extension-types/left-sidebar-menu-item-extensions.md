---
title: 'Left sidebar menu item extensions'
sidebar_position: 5
id: left-sidebar-menu-item-extensions
---

## Left sidebar menu item extension type

One possible extension type is left sidebar menu items. Registered left sidebar menu items get rendered in the left sidebar, as long as there is more than one available.

### Configuration

To define a left sidebar menu item, you implement the `SidebarNavExtension` interface. It looks like this:

```typescript
interface SidebarNavExtension {
  id: string;
  type: 'sidebarNav';
  extensionPointIds?: string[];
  navItem: AppNavigationItem; // Please check the AppNavigationItem section below
}
```

For `id`, `type`, and `extensionPointIds`, please see [base configuration section](../index.md#base-configuration) in the extensions docs.

Each app has its own nav items extension point with the id `app.${appId}.navItems`. Use it in `extensionPointIds` to
place your nav item in the left sidebar of that app.

#### AppNavigationItem

The most important configuration options are:

- `icon` - The icon to be displayed, can be picked from [Remix Icon](https://remixicon.com/)
- `name` - The text to be displayed
- `route` - The string/route to navigate to, if the nav item should be a `<router-link>` (Mutually exclusive with `handler`)
- `handler` - The action to perform upon click, if the nav item should be a `<button>` (Mutually exclusive with `route`)

Please check the [`AppNavigationItem` type](https://github.com/opencloud-eu/web/blob/main/packages/web-pkg/src/apps/types.ts) for a full list of configuration options.

### Example

The following example is taken from the [office settings app](https://github.com/opencloud-eu/web/blob/main/packages/web-app-office-settings/src/index.ts). It adds a nav item to the left sidebar of the admin settings app, linking to a view of the office settings app.

```typescript title="src/index.ts"
import { defineWebApplication, SidebarNavExtension } from '@opencloud-eu/web-pkg';
import { useGettext } from 'vue3-gettext';
import { computed } from 'vue';
import App from './App.vue';

export default defineWebApplication({
  setup() {
    const { $gettext } = useGettext();
    const appId = 'admin-settings/office';

    const extensions = computed<SidebarNavExtension[]>(() => [
      {
        id: 'com.github.opencloud-eu.web.admin-settings.left-nav.office',
        type: 'sidebarNav',
        extensionPointIds: ['app.admin-settings.navItems'],
        navItem: {
          isVisible: () => true,
          name: $gettext('Office'),
          icon: 'attachment',
          route: {
            path: `/${appId}`
          }
        }
      }
    ]);

    const routes = [
      {
        path: '/',
        name: 'office',
        component: App,
        meta: {
          title: $gettext('Office Settings'),
          authContext: 'user'
        }
      }
    ];

    return {
      appInfo: {
        name: $gettext('Office Settings'),
        id: appId
      },
      routes,
      extensions
    };
  }
});
```
