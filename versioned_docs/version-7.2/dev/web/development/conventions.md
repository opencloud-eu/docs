---
title: 'Conventions'
sidebar_position: 3
id: conventions
---

This is a collection of tips and conventions to follow when working on the [OpenCloud Web frontend](https://github.com/opencloud-eu/web).
Since it is a living document, please open a PR if you find something missing.

## Contributing to OpenCloud Web

Everyone is invited to contribute. Simply fork the [codebase](https://github.com/opencloud-eu/web/),
check the [issues](https://github.com/opencloud-eu/web/issues?q=is%3Aopen%20is%3Aissue%20label%3AType%3AGood-First-Issue)
for a suitable one and open a pull request!

### Formal checks

To make sure your pull request can be efficiently reviewed and won't need a lot of changes down the road, please run all formal checks (linter, formatter, type checks and unit tests) via `pnpm check:all` locally. Our [CI](https://ci.opencloud.eu/repos/6) will run on
pull requests and report back any problems after that. For a further introduction on how we handle testing, please head to
the [testing docs](../testing/running-tests).

## Code Conventions

### Early Returns

We're trying to stick with early returns in our code to make it more performant and simpler to reason about it.

### Translations

Use `$gettext` (or a variation of it) inside HTML tags (instead of a `<translate tag="h1">` or similar) in order to translate strings.

### TypeScript

We're using TypeScript which allows us to catch bugs at transpile time. Clean types make sure our IDEs can support us in reasoning about our ever-growing, complex codebase.

### Composition API and script setup

We prefer using Vue's Composition API in combination with [script setup](https://vuejs.org/api/sfc-script-setup) over the traditional options API. This integrates nicely with TypeScript and allows us to use composables and reactive APIs more effectively.

That being said, due to the fact that we are still in the process of migrating our codebase, you might find some files using the options API or even composition API without script setup. We are working on this and will eventually migrate all files.

### Composables

We make heavy use of composables to encapsulate reusable logic. This allows us to share code between components and keep our components clean and focused on their specific tasks.

### Split large components

If a component is getting too big, consider splitting it into smaller components. This will make it easier to read and maintain. A good rule of thumb is to keep components under 300 lines of code.

### Services

We try to avoid services when possible and rather use composables instead. If writing a service is necessary, it should be instantiated once via the `web-runtime` package and then made available via a `useYourService` composable.

### Dependencies

To keep the bundle size small and reduce the risk of introducing security problems for our users, we try to limit
the amount of dependencies in our code base and keep them as up-to-date as possible.
