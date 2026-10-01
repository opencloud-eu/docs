---
title: 'Viewer and editor apps'
---

OpenCloud Web allows developers to implement apps for viewing and editing specific file types. For instance, the built-in preview app serves as the default application for opening media files like images, videos, or audio.

This section will guide you through the process of implementing such an app within OpenCloud Web.

## App setup

The `src/index.ts` file for a viewer or editor app may look like this:

```typescript title="src/index.ts"
import { AppWrapperRoute, defineWebApplication, AppMenuItemExtension } from '@opencloud-eu/web-pkg';
import { urlJoin } from '@opencloud-eu/web-client';
import translations from '../l10n/translations.json';
import { useGettext } from 'vue3-gettext';
import { computed } from 'vue';

// This is the base component of your app.
import App from './App.vue';

export default defineWebApplication({
  setup() {
    // The ID of your app.
    const appId = 'advanced-pdf-viewer';

    const { $gettext } = useGettext();

    // This creates a route under which your app can be opened.
    // Later, this route will be bound to one or more file extensions.
    const routes = [
      {
        name: 'advanced-pdf-viewer',
        path: '/:driveAliasAndItem(.*)?',
        component: AppWrapperRoute(App, {
          applicationId: appId
        }),
        meta: {
          authContext: 'hybrid',
          title: $gettext('Advanced PDF Viewer'),
          patchCleanPath: true
        }
      }
    ];

    // if you want your app to be present in the app menu on the top left.
    const menuItems = computed<AppMenuItemExtension[]>(() => [
      {
        id: `app.${appId}.menuItem`,
        label: () => $gettext('Advanced PDF Viewer'),
        type: 'appMenuItem',
        color: '#ffffff',
        icon: 'file-pdf',
        priority: 30,
        path: urlJoin(appId)
      }
    ]);

    return {
      appInfo: {
        name: 'Advanced PDF Viewer',
        id: appId,
        defaultExtension: 'pdf',
        extensions: [
          // This makes sure all files with the "pdf" extension will be routed to your app when being opened.
          // See the `ApplicationFileExtension` interface down below for a list of all possible properties.
          {
            extension: 'pdf',
            routeName: 'advanced-pdf-viewer',

            // Add this if you want your app to be present in the "New" file menu.
            newFileMenu: {
              menuTitle() {
                return $gettext('PDF document');
              }
            }
          }
        ]
      },
      routes,
      translations,
      extensions: menuItems
    };
  }
});
```

Here is the interface defining the `extensions` property of the `appInfo` object.

```typescript
interface ApplicationFileExtension {
  app?: string;
  extension?: string;
  createFileHandler?: (arg: {
    fileName: string;
    space: SpaceResource;
    currentFolder: Resource;
  }) => Promise<Resource>;
  hasPriority?: boolean;
  label?: string;
  name?: string;
  icon?: string;
  mimeType?: string;
  newFileMenu?: { menuTitle: () => string };
  routeName?: string;
}
```
