---
title: 'Testing'
sidebar_position: 4
---

This page describes how to test your app.

## Unit tests

The [web-app-skeleton repository](https://github.com/opencloud-eu/web-app-skeleton) comes with a
[vitest](https://vitest.dev/) setup. Run the unit tests with:

```bash
pnpm test:unit
```

## Test helpers

The `@opencloud-eu/web-test-helpers` package provides utilities for mounting components with a mocked OpenCloud Web
context. Without them, every component that uses a composable of `web-pkg` fails to mount.

```typescript title="tests/unit/App.spec.ts"
import { defaultPlugins, mount } from '@opencloud-eu/web-test-helpers';
import App from '../../src/App.vue';

describe('App', () => {
  it('renders the title', () => {
    const wrapper = mount(App, { global: { plugins: [...defaultPlugins()] } });
    expect(wrapper.text()).toContain('My app');
  });
});
```

For details, please refer to the package's
[README.md](https://github.com/opencloud-eu/web/blob/main/packages/web-test-helpers/README.md).

## End to end tests

For end to end tests with [Playwright](https://playwright.dev/), the
[web](https://github.com/opencloud-eu/web) and [web-extensions](https://github.com/opencloud-eu/web-extensions)
repositories contain working examples.
