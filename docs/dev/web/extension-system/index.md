---
title: 'Extension System'
---

OpenCloud Web can be extended with **apps**. An app is an artifact that gets installed in an OpenCloud instance.
It is the main building block of the extension system: everything you add to OpenCloud Web is delivered as an app.

An app can do two things, and both of them are optional:

1. It can take over the full app viewport, meaning everything below the top bar. There you can render any custom
   application code, define views with routes, add navigation items to the left sidebar, and more.
2. It can register [extensions](./extensions/). Extensions are small, focused pieces of functionality that get mounted
   into predefined places of the OpenCloud Web user interface, for example a file action or a panel in the right sidebar.

This means an app can be a file editor without any extensions, a pure extension host without any custom views, or a
combination of both.

## Creating an app

The [getting started guide](./getting-started) takes you from an empty folder to a running app. It is the entrypoint
for app development.

## Examples

You can find open source examples for apps and extensions in our
[curated list of OpenCloud apps and extensions](https://github.com/opencloud-eu/awesome-apps).
Feel free to contribute or just be inspired for your own apps and extensions.

## Installing an app

To learn how to integrate an app into OpenCloud Web, please refer to the
[Web application admin docs](../../../admin/configuration/web-applications). To learn how to ship your app to users,
please refer to the [build and publish docs](./build-and-publish).
