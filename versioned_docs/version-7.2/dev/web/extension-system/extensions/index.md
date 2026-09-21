---
title: 'Extensions'
---

Extensions are small, scoped pieces of functionality that can be added to the OpenCloud Web interface. They typically
hook into specific [extension points](./extension-points) and always need to be shipped by an app.

Every extension has a [type](./extension-types/), which defines what the extension does and which data it provides.
The extension point it registers on defines where it appears in OpenCloud Web.

## Extension registry

The OpenCloud Web runtime provides a globally available extension registry. It is used to both register and query
extensions. All extensions that are made available via an app get registered in the extension registry automatically.

## Base configuration

Any extension is required to define at least an `id` and a `type` in order to fulfill the generic `Extension` interface.

The `id` is supposed to be unique throughout the OpenCloud Web ecosystem. In order to keep `id`s readable for humans we
didn't want to enforce uniqueness through e.g. uuids. Instead, we chose to use dot-formatted namespaces like e.g.
`com.github.opencloud-eu.web.files.search`. We'd like to encourage you to follow the same format for your own extensions.

For the `type` you can choose from the [predefined extension types](./extension-types/) or define a custom one.

In addition, you can pass optional `extensionPointIds` to determine where the extension will appear. You can find all
predefined ids in the [extension points docs](./extension-points).

## Registering extensions

### Via the app definition

The `extensions` key of an app definition takes a `Ref<Extension[]>`, so use a `computed`. The runtime registers its
content when your app is loaded:

```typescript title="src/index.ts"
import { defineWebApplication, Extension } from '@opencloud-eu/web-pkg';
import { computed } from 'vue';

export default defineWebApplication({
  setup() {
    const extensions = computed<Extension[]>(() => [
      {
        id: 'com.github.my-org.my-app.my-action',
        type: 'action',
        extensionPointIds: ['global.files.context-actions'],
        action: {
          // See the action extension docs
        }
      }
    ]);

    return {
      appInfo: {
        name: 'My app',
        id: 'my-app'
      },
      extensions
    };
  }
});
```

Because the value is a ref, the list is reactive. You can hide or show an extension based on the app config, the
capabilities of the server, or the permissions of the user:

```typescript
const extensions = computed<Extension[]>(() => {
  if (!unref(isFeatureAvailable)) {
    return [];
  }
  return [myExtension];
});
```

### At runtime

You can also register extensions from any place that has access to the injection context, for example a component or a
composable:

```typescript
import { useExtensionRegistry } from '@opencloud-eu/web-pkg';

const extensionRegistry = useExtensionRegistry();

extensionRegistry.registerExtensions(computed(() => [myExtension]));
```

Remove them again via `unregisterExtensions`, which takes the ids:

```typescript
extensionRegistry.unregisterExtensions([myExtension.id]);
```

Prefer the app definition. Use the runtime API only when the extensions are not known at that point, for example because
they depend on data that you load first.

:::note
Administrators can switch off single extensions via the `options.disabledExtensions` key of the OpenCloud Web config. A
disabled extension stays registered, but the registry does not return it.
:::

## Querying extensions

Use `requestExtensions` to get all extensions of an extension point. The registry returns only the extensions whose
`type` matches the `extensionType` of the extension point, and whose `extensionPointIds` allow this extension point:

```typescript
import { ActionExtension, useExtensionRegistry } from '@opencloud-eu/web-pkg';
import { computed } from 'vue';

const extensionRegistry = useExtensionRegistry();

const actions = computed(() =>
  extensionRegistry.requestExtensions<ActionExtension>(myExtensionPoint).map(({ action }) => action)
);
```

To learn how to define `myExtensionPoint`, please refer to the
[extension points docs](./extension-points#defining-your-own-extension-points).

## User preferences

Extension points can let users choose between the registered extensions. The extension point then gets a dropdown on
the preferences page, reachable via the top right user menu. Your extension provides the label for that dropdown via
`userPreference.optionLabel`. For the extension point side, please refer to the
[extension points docs](./extension-points#letting-users-choose).

## Creating an extension

Please check out the [web-app-skeleton repository](https://github.com/opencloud-eu/web-app-skeleton) for a boilerplate
app that also includes an extension. In addition to that, the [extension types docs](./extension-types/) provide
instructions and examples on how to implement the different extension types.
