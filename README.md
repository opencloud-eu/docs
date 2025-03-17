# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

### Installation

```Shell
pnpm install
```

### Local Development

clone this repository

```Shell
pnpm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Start docs in German

To see the docs in German you need to start it with the following command

```Shell
pnpm run start --locale de
```

It is not possible to switch between the languages via the language switcher

### Build

```Shell
pnpm build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```Shell
USE_SSH=true pnpm deploy
```

Not using SSH:

```Shell
GIT_USER=<Your GitHub username> pnpm deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

-----

### Standard for screenshots

#### Defined size for screenshots

| Component        | Size             |
|:-----------------| :-:              |
| complete screen  | width: "1920px"  |
| menu             | width: "400px"   | 
| pop up           | width: "500px"   |

The screenshot should show the important aspects and you can put red frames around the specific buttons or areas.
