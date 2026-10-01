---
title: 'Getting started'
sidebar_position: 1
---

This guide shows how to set up and run an OpenCloud Web app.

## Prerequisites

- git
- docker and docker compose
- node
- [pnpm](https://pnpm.io/installation), ideally installed via `corepack`

If you don't use Docker Desktop, add `127.0.0.1 host.docker.internal` to your `/etc/hosts` file. Otherwise
`host.docker.internal` cannot be resolved.

## Project setup

The fastest way to start is the [web-app-skeleton repository](https://github.com/opencloud-eu/web-app-skeleton). It
contains a working app, a docker compose setup with an OpenCloud server, and a unit test setup.

```bash
git clone https://github.com/opencloud-eu/web-app-skeleton.git my-app
cd my-app
pnpm install
```

Rename the app afterwards. The name `skeleton` appears in `package.json`, `vite.config.ts`, `src/index.ts`,
and `tests/unit/App.spec.ts`.

:::note
The skeleton follows the latest OpenCloud release. For OpenCloud 7.2, pin the `@opencloud-eu/*` dependencies in
`package.json` to `^7.0.0` and set `OC_IMAGE` in `docker-compose.yml` to a 7.x server image.
:::

## Running your app

There are two ways to run your app against a local OpenCloud instance.

### Watch build

This mode fully builds your app and writes it into the `dist` folder, which is then served by the OpenCloud server.

1. Start a watch build. It writes your app into the `dist` folder on every change.

   ```bash
   pnpm build:w
   ```

2. Start the OpenCloud server. In the skeleton repository, the `dist` folder is already mounted into the container, and
   `WEB_ASSET_APPS_PATH` points to the mount target.

   ```bash
   docker compose up
   ```

3. Open [https://host.docker.internal:9200](https://host.docker.internal:9200) and log in as `admin` with the password
   `admin`. Your app is loaded automatically.

Changes are picked up by the watch build, but you need to reload the page to see them.

### Module federation with hot reload

In this mode your app is served by its own Vite dev server and loaded into a running OpenCloud Web dev server as a
federated module. You get instant hot reload, but you need a local checkout of the
[web repository](https://github.com/opencloud-eu/web).

1. Start the OpenCloud Web dev server via `pnpm vite` in your `web` checkout, as described in the
   [tooling docs](../development/tooling#using-instant-hot-reload-via-vite). It listens on
   [https://host.docker.internal:9201](https://host.docker.internal:9201).

2. Start the dev server of your app:

   ```bash
   pnpm vite
   ```

   It listens on port `9210` by default. Change it via the `server.port` option in your Vite config.

3. Open [https://host.docker.internal:9210](https://host.docker.internal:9210) and accept the self-signed certificate
   (adjust the port if you changed it in your Vite config).

4. Open [https://host.docker.internal:9201](https://host.docker.internal:9201).

The extension-sdk registers your app with the OpenCloud Web dev server every few seconds, so the registration survives a
restart of either server.

## The app definition

The `src/index.ts` file acts as the entrypoint of the app. This file has to export an app definition created via
`defineWebApplication`:

```typescript title="src/index.ts"
import { defineWebApplication } from '@opencloud-eu/web-pkg'
import { computed } from 'vue';
import { useGettext } from 'vue3-gettext';

// Needs to be unique within all installed applications in any OpenCloud
// web instance. Should be short, unique and expressive as it is used as
// prefix on all routes within your application.
const appId = 'your-app'

export default defineWebApplication({
  setup({ applicationConfig }) {
    // Here, you have access to the full injection context.
    const { $gettext } = useGettext();

    return {
      appInfo: {
        name: $gettext('Your application name'),
        id: appId,
        icon: 'aliens' // See https://remixicon.com
      },
      navItems: [ ... ],
      routes: [ ... ],
      extensions: computed( () => [ ... ]),
      extensionPoints: computed( () => [ ... ]),
      translations: { ... }
    }
  }
})
```

`defineWebApplication` accepts the following keys:

- `appInfo` - the application metadata. It makes the application available via the app switcher and the app registry.
- `navItems` - the statically defined navigation items for the left sidebar. They only get rendered when more than 1
  navigation item exists at runtime. Additional dynamic navigation items can be registered via the extension registry.
- `routes` - the routes to the different views of your application. They may be referenced within the `navItems`.
  Authentication requirements can be defined per item.
- `extensions` - the extensions to be registered in the extension registry. For details, please refer to the
  [extensions docs](./extensions/).
- `extensionPoints` - the extension points to be registered in the extension registry. For details, please refer to the
  [extension points docs](./extensions/extension-points).
- `translations` - the translations of your application. For details, please refer to the
  [translations docs](./advanced-topics/translations).

## Vite configuration

Apps are built with [Vite](https://vite.dev/). The `@opencloud-eu/extension-sdk` package provides a ready to use Vite
config, so your `vite.config.ts` stays short:

```typescript title="vite.config.ts"
import { defineConfig } from '@opencloud-eu/extension-sdk';

export default defineConfig({
  name: 'my-app'
});
```

`defineConfig` accepts any [Vite option](https://vite.dev/config/), plus the following:

- `name` - The name of your app. Defaults to the `name` field of your `package.json`.
- `opencloudWebHostUrl` - The URL of the OpenCloud Web dev server. Defaults to `https://host.docker.internal:9201`.

The config sets up Vue, [Tailwind CSS](./advanced-topics/styling#tailwind-css), module federation and the generation of
`manifest.json`. It also declares the modules that the OpenCloud Web runtime shares with your app, such as `vue`, `pinia`,
`@opencloud-eu/web-pkg` and `@opencloud-eu/web-client`. These modules must not be bundled into your app.

The following environment variables are supported:

| Variable                       | Description                                                          |
| ------------------------------ | -------------------------------------------------------------------- |
| `OPENCLOUD_WEB_HOST_URL`       | URL of the OpenCloud Web dev server. Same as `opencloudWebHostUrl`.  |
| `OPENCLOUD_EXTENSION_DIST_DIR` | Output directory of the build. Defaults to `dist`.                   |
| `OPENCLOUD_CERTS_DIR`          | Directory with a `server.key` and a `server.crt` for the dev server. |

## What's next?

- [Build and publish](./build-and-publish) your app, so that users can install it.
- Register [extensions](./extensions/) to add functionality to existing places of the OpenCloud Web user interface.
- Make your app [configurable](./advanced-topics/configuration) for administrators.
- Follow the platform look with the [styling docs](./advanced-topics/styling).
- Add [translations](./advanced-topics/translations) to your app.
- Write [tests](./advanced-topics/testing) for your app.
- Build a [viewer or editor app](./viewer-editor-apps) for specific file types.
- Reuse our [helpful packages](./packages) instead of writing your own utilities.
