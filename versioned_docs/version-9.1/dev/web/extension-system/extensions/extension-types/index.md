---
title: 'Extension Types'
---

For building an extension you can choose from the types predefined by the OpenCloud Web extension system. The full list
is shown below. Please refer to the respective subpages to learn more about the individual extension types.

| Extension type                                                         | `type`                 | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`ActionExtension`](./action-extensions)                               | `action`               | Registers `Action` items that get shown in various places, for example context menus or batch actions. Most commonly used for file and folder actions like copy, rename or delete. |
| [`AppMenuItemExtension`](./app-menu-item-extensions)                   | `appMenuItem`          | Registers links to internal or external pages in the application switcher menu.                                                                                                    |
| [`CustomComponentExtension`](./custom-component-extensions)            | `customComponent`      | Registers a custom component for a render target.                                                                                                                                  |
| [`FolderViewExtension`](./folder-view-extensions)                      | `folderView`           | Registers additional ways of displaying the content of a folder, meaning resources like spaces, folders or files.                                                                  |
| [`SidebarNavExtension`](./left-sidebar-menu-item-extensions)           | `sidebarNav`           | Registers additional navigation items for the left sidebar. These can be scoped to specific apps, and enabled or disabled programmatically.                                        |
| [`SidebarPanelExtension`](./right-sidebar-panel-extensions)            | `sidebarPanel`         | Registers panels for the right sidebar.                                                                                                                                            |
| [`SearchExtension`](./search-extensions)                               | `search`               | Registers additional search providers.                                                                                                                                             |
| [`FloatingActionButtonExtension`](./floating-action-button-extensions) | `floatingActionButton` | Registers one or multiple primary actions. Displayed in the left sidebar on desktop resolutions and as a floating action button on mobile resolutions.                             |
| [`AccountExtension`](./account-extensions)                             | `accountExtension`     | Registers a panel on the preferences page.                                                                                                                                         |
| [`ResourceIndicatorExtension`](./resource-indicator-extensions)        | `resourceIndicator`    | Registers status icons or tags that get shown next to the name of a resource.                                                                                                      |
| [`VaultExtension`](./vault-extensions)                                 | `vault`                | Registers a client side encryption scheme for vault folders and vault spaces.                                                                                                      |

You're free to introduce your own extension types within your application code and use the extension registry to query
the available ones. However, if you have the impression that an important extension type is missing and would be
beneficial for the platform, please reach out to us by opening a
[GitHub issue](https://github.com/opencloud-eu/web/issues/new/choose).
