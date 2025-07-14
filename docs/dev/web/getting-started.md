---
title: 'Getting Started'
sidebar_position: 1
---

## Source Code

The source code is hosted at [https://github.com/opencloud-eu/web](https://github.com/opencloud-eu/web).

## Installation

To install and setup the Web client on your local machine, please refer to the [development setup docs](./development/tooling.md#development-setup).

## Configuration

Web can be configured using a configuration file in `json` format. Sample configuration files are available in the [config folder](https://github.com/opencloud-eu/web/tree/main/config) of the OpenCloud Web Git repository. Below is a detailed overview of all available configuration options.

### `server`

Specifies the server URL, e.g. `https://host.docker.internal:9200`.

### `theme`

Specifies the URL for the theme to be loaded, e.g. `https://host.docker.internal:9200/themes/opencloud/theme.json`.

### `options`

General options that control the behavior of the Web client. Expects an object with the following possible options:

- `options.accountEditLink` This accepts an object with the following optional fields to have a link on the account page:
  - `options.accountEditLink.href` Set a different target URL for the edit link. Make sure to prepend it with `http(s)://`.
- `options.sharingRecipientsPerPage` Sets the amount of users shown as recipients in the dropdown when sharing resources. Default amount is 200.
- `options.runningOnEos` Set this option to `true` if running on an [EOS storage backend](https://eos-web.web.cern.ch/eos-web/) to enable its specific features. Defaults to `false`.
- `options.cernFeatures` Enabling this will activate CERN-specific features. Defaults to `false`.
- `options.editor.autosaveEnabled` Specifies if the autosave for the editor apps is enabled.
- `options.editor.autosaveInterval` Specifies the time interval for the autosave of editor apps in seconds.
- `options.editor.openAsPreview` Specifies if non-personal files i.e. files in shares, spaces or public links are being opened in read only mode so the user needs to manually switch to edit mode. Can be set to `true`, `false` or an array of web app/editor names.
- `options.contextHelpersReadMore` Specifies whether the "Read more" link should be displayed or not.
- `options.tokenStorageLocal` Specifies whether the access token will be stored in the local storage when set to `true` or in the session storage when set to `false`. If stored in the local storage, login state will be persisted across multiple browser tabs, means no additional logins are required. Defaults to `true`.
- `options.loginUrl` Specifies the target URL to the login page. This is helpful when an external IdP is used. This option is disabled by default. Example URL like: '[https://www.myidp.com/login](https://www.myidp.com/login)'.
- `options.logoutUrl` Adds a link to the user's profile page to point him to an external page, where he can manage his session and devices. This is helpful when an external IdP is used. This option is disabled by default.
- `options.userListRequiresFilter` Defines whether one or more filters must be set in order to list users in the Web admin settings. Set this option to 'true' if running in an environment with a lot of users and listing all users could slow down performance. Defaults to `false`.
- `options.concurrentRequests` This accepts an object with the following optional fields to customize the maximum number of concurrent requests in code paths where we limit concurrent requests
  - `resourceBatchActions` Concurrent number of file/folder/space batch actions like e.g. accepting shares. Defaults to 4.
  - `sse` Concurrent number of SSE event handlers. Defaults to 4.
  - `shares` Accepts an object regarding the following sharing related options:
    - `create` Concurrent number of share invites. Defaults to 4.
    - `list` Concurrent number of individually loaded shares. Defaults to 2.

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

Options for the connection to the oIDC provider. Expects an object with the following possible options:

- `openIdConnect.authority` URL of the OIDC/OAuth2 provider.
- `openIdConnect.metadata_url` URL of the OIDC configuration.
- `openIdConnect.client_id` The client id registered with the OIDC/OAuth2 provider.
- `openIdConnect.client_secret`
- `openIdConnect.dynamic`
- `openIdConnect.post_logout_redirect_uri`
- `openIdConnect.response_type`
- `openIdConnect.scope`

See the [oidc-client-ts documentation](https://authts.github.io/oidc-client-ts/interfaces/OidcClientSettings.html) for more information.

### `customTranslations`

Specify custom translations to overwrite existing ones. Expects an array of objects that specify a `url` attribute, like `[{url: "https://host.docker.internal:9200/customTranslations.json"}]`.

### `styles`

Additional CSS files to further customize the user experience and adapt it to your specific needs. Expects an array of objects that specify a `href` attribute, pointing to the path/URL of your stylesheet, like `[{ "href": "css/custom.css" }]`.

### `scripts`

Additional JavaScript files to further customize the user experience and adapt it to your specific needs. Expects an array of objects that specify a `src` attribute, pointing to the path/URL of your script, and an optional `async` attribute (defaults to false), like `[{ "src": "js/custom.js", "async": true }]`.

:::note
Check out the [extension system docs](./extension-system) for a more convenient way to add functionality to the Web client.
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
