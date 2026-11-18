---
title: 'Getting Started'
sidebar_position: 1
---

## Source Code

The source code is hosted at [https://github.com/opencloud-eu/web](https://github.com/opencloud-eu/web).

## Installation

To install and setup the Web client on your local machine, please refer to the [development setup docs](./development/tooling#development-setup).

## Configuration

Web can be configured using a configuration file in `json` format. This is completely optional, as default settings are used when no configuration file is provided. You need to tell the server where to find a custom configuration file via the `WEB_UI_CONFIG_FILE` environment variable.

Below is a detailed overview of all available configuration options.

### `server`

Specifies the server URL, e.g. `https://host.docker.internal:9200`.

### `theme`

Specifies the URL for the theme to be loaded, e.g. `https://host.docker.internal:9200/themes/opencloud/theme.json`.

### `apps`

Controls the Web apps to be loaded. This is not for adding external apps, but for specifying which of the internal apps that are shipped with Web should be loaded. Expects a list of strings, e.g.:

```json
[
  "files",
  "text-editor",
  "pdf-viewer",
  "search",
  "external",
  "admin-settings",
  "epub-reader",
  "app-store",
  "preview"
]
```

### `openIdConnect`

The Web client forwards all configuration options under `openIdConnect` to the [oidc-client-ts library](https://authts.github.io/oidc-client-ts/). Setting the following 3 options however won't have any effect, as they get discovered automatically via the `/.well-known/webfinger` endpoint:

- `client_id`
- `scope`
- `authority`

See the [oidc-client-ts documentation](https://authts.github.io/oidc-client-ts/interfaces/OidcClientSettings.html) for information on the available configuration options for the library.

### `customTranslations`

Specify custom translations to overwrite existing ones. Expects an array of objects that specify a `url` attribute, like `[{url: "https://host.docker.internal:9200/customTranslations.json"}]`.

### `styles`

Additional CSS files to further customize the user experience and adapt it to your specific needs. Expects an array of objects that specify a `href` attribute, pointing to the path/URL of your stylesheet, like `[{ "href": "css/custom.css" }]`.

### `scripts`

Additional JavaScript files to further customize the user experience and adapt it to your specific needs. Expects an array of objects that specify a `src` attribute, pointing to the path/URL of your script, and an optional `async` attribute (defaults to false), like `[{ "src": "js/custom.js", "async": true }]`.

:::note
Check out the [extension system docs](./extension-system/) for a more convenient way to add functionality to the Web client.
:::

### `sentry`

Web supports [Sentry](https://sentry.io/welcome/) to provide monitoring and error tracking.
To enable sending data to a Sentry instance, you can use the following configuration keys:

- `sentry.dsn` Should contain the DSN for your sentry project.
- `sentry.environment`: Lets you specify the environment to use in Sentry. Defaults to `production`.

Any other key under `sentry` will be forwarded to the Sentry initialization. You can find out more
settings in the [Sentry docs](https://docs.sentry.io/platforms/javascript/configuration/).

:::note
If you are using an old version of Sentry (9 and before), you might want to add the setting `sentry.autoSessionTracking: false` to avoid errors related to breaking changes introduced in the
integration libraries.
:::
