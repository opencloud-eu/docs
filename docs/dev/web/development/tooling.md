---
title: "Tooling"
sidebar_position: 1
id: tooling
---

## Packaging

Web is using [pnpm](https://pnpm.io/) as package manager and [vite](https://vitejs.dev/) as build tool. The latter is built on top of [rollup](https://rollupjs.org/) and brings some additional features such as instant hot-reloading.

## Development Setup

### Prerequisites

Please make sure you have the following tools installed on your system:

- docker
- docker-compose (if not already included in your docker installation)
- node
- pnpm (we recommend the installation via `corepack` which is included in newer node versions)

:::note
If you’re not using Docker Desktop, you might have to modify your `/etc/hosts` and add `127.0.0.1 host.docker.internal` to make `host.docker.internal` links work.
:::

:::note
This setup currently doesn't work on Windows out of the box.

<details>
  <summary>Workaround</summary>
  
  One of our contributors has opened a PR to a dependency that prevents us from successfully bundling the frontend.
  Feel free to check out [their changes](https://github.com/egoist/rollup-plugin-postcss/pull/384) and build them locally if you absolutely want to work on Windows.
</details>
:::

### Installing Dependencies

After cloning the source code, install the dependencies via `pnpm install`.

### Starting the Server

You can start the OpenCloud server by running `docker-compose up opencloud -d`. If you want to run the full stack, you can run `docker-compose up -d` instead. This will also start the wopi service and an instance of Collabora.

### Building and Accessing Web

After starting the docker containers, you can build Web by running `pnpm build:w`. This command compiles the project and includes support for hot-reloading, allowing you to see changes as you make them. However, note that the rebuild process may take some time.

For a faster development experience, consider enabling instant hot-reloading. Details on how to set this up are provided below.

Now you can access Web via https://host.docker.internal:9200.

### Using Instant Hot-Reload via Vite

To work with instant hot-reloading, you can also build Web by running `pnpm vite`. The port to access Web is slightly different then: https://host.docker.internal:9201. Also note that the initial page load may take a bit longer than usual. This is normal and to be expected.

:::note
Make sure that you ran `pnpm build` once before starting the server with `pnpm vite`. Also, you need to accept the self-signed certificate in your browser for https://host.docker.internal:9200 _and_ https://host.docker.internal:9201.
:::
