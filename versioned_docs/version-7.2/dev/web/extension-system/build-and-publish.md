---
title: 'Build and publish'
sidebar_position: 2
---

This page describes how to build your app for production and how to publish it in the OpenCloud app store.

## Building an app

Run a production build:

```bash
pnpm build
```

The build writes your app into the `dist` folder. Static assets from a `public` folder are copied over as is. The result
contains:

- `js/<name>-<hash>.mjs` - the entry point of your app, plus its chunks.
- `manifest.json` - the metadata that OpenCloud uses to discover and load your app.
- any static assets of your app.

The generated `manifest.json` is your `src/manifest.json` plus the `entrypoint` key, which the build sets. Only
`entrypoint` is required by the server. Add any other metadata of your app to `src/manifest.json` yourself.

```json title="dist/manifest.json"
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "My OpenCloud app",
  "entrypoint": "js/my-app-a1b2c3d4.mjs"
}
```

## Publishing in the app store

Apps in the OpenCloud app store are listed in the
[awesome-apps repository](https://github.com/opencloud-eu/awesome-apps). Publishing means adding your app to its
`webApps/apps.json` file via a pull request.

### Requirements

- Your app must be downloadable as a `.zip` file from a stable URL, for example a GitHub release asset.
- The zip must contain a `manifest.json` in its root, next to your built files. A production build produces this
  already, so zip the content of your `dist` folder, not the folder itself.

### apps.json entry

Add one entry under the `apps` key. The schema is defined in the
[app store types](https://github.com/opencloud-eu/web/blob/stable-7.1/packages/web-app-app-store/src/types.ts).

```json title="webApps/apps.json"
{
  "id": "com.github.my-org.my-repo.my-app",
  "name": "My App",
  "subtitle": "One short line about what the app does.",
  "description": "A longer description.",
  "license": "Apache-2.0",
  "versions": [
    {
      "version": "1.0.0",
      "minOpenCloud": "7.2.0",
      "url": "https://github.com/my-org/my-repo/releases/download/v1.0.0/my-app-1.0.0.zip"
    }
  ],
  "authors": [{ "name": "My Organization", "url": "https://example.org" }],
  "tags": ["editor", "viewer"],
  "coverImage": {
    "url": "https://raw.githubusercontent.com/opencloud-eu/awesome-apps/main/webApps/my-org/my-repo/cover.png"
  },
  "screenshots": [
    {
      "url": "https://raw.githubusercontent.com/opencloud-eu/awesome-apps/main/webApps/my-org/my-repo/screenshots/1.png",
      "caption": "What this screenshot shows"
    }
  ],
  "resources": [
    { "url": "https://github.com/my-org/my-repo", "label": "Source code", "icon": "github" }
  ]
}
```

Notes on the fields:

- `versions` must be sorted from newest to oldest. `minOpenCloud` is the lowest OpenCloud version your app supports.
- `badge` is optional and accepts a `label` and a `color` of `primary`, `success` or `danger`.
- `screenshots` and `resources` are optional.

### Assets

Cover image and screenshots are stored in the awesome-apps repository. Use a 3:2 aspect ratio and prefer PNG or JPEG.

Follow this folder structure:

- `webApps/<org-name>/<repo-name>/cover.png`
- `webApps/<org-name>/<repo-name>/screenshots/1.png`

If your repository hosts several apps, add the app name to the path, for example
`webApps/<org-name>/<repo-name>/<app-name>/cover.png`.

Make sure the license of your assets allows us to keep them in the repository and to show them in the app store. If you
are not sure about the license of an asset, do not add it.
