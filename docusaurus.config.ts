import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// Webpack plugin für raw-loader (?raw an YAML-Dateien)
function rawLoaderPlugin() {
  return {
    name: 'custom-webpack-raw-loader',
    configureWebpack() {
      return {
        module: {
          rules: [
            {
              test: /\.ya?ml$/i,
              resourceQuery: /raw/,
              use: 'raw-loader',
            },
          ],
        },
      };
    },
  };
}

const config: Config = {
  title: 'OpenCloud Docs',
  tagline: 'Excellent file sharing',
  favicon: 'img/oc-favicon.svg',

  url: 'https://docs.opencloud.eu',
  baseUrl: '/',

  organizationName: 'opencloud-eu',
  projectName: 'docs',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'de'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/opencloud-eu/docs/tree/main',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/oc-docs-social-card.jpg',
    colorMode: {
      defaultMode: 'light',
    },
    navbar: {
      logo: {
        alt: 'OpenCloud Logo',
        src: 'img/oc-logo-petrol.svg',
        srcDark: 'img/oc-logo-lilac.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'user',
          position: 'left',
          label: 'User',
        },
        {
          type: 'docSidebar',
          sidebarId: 'admin',
          position: 'left',
          label: 'Admin',
        },
        {
          type: 'docSidebar',
          sidebarId: 'dev',
          position: 'left',
          label: 'Dev',
        },
        {
          type: 'localeDropdown',
          position: 'right',
        },
      ],
    },
    footer: {
      links: [
        {
          title: 'Docs',
          items: [
            {label: 'User', to: '/docs/user/intro'},
            {label: 'Admin', to: '/docs/admin/intro'},
            {label: 'Dev', to: '/docs/dev/intro'},
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'OpenCloud Community',
              href: 'https://opencloud.eu/opencloud-community',
            },
            {label: 'GitHub', href: 'https://github.com/opencloud-eu'},
          ],
        },
        {
          title: 'More',
          items: [
            {label: 'OpenCloud', href: 'https://opencloud.eu/'},
            {label: 'Blog & News', href: 'https://opencloud.eu/blog-news'},
            {
              label: 'Linkedin',
              href: 'https://www.linkedin.com/company/opencloud-eu',
            },
            {label: 'Mastodon', href: 'https://social.opencloud.eu/@OpenCloud'},
            {label: 'Bluesky', href: 'https://bsky.app/profile/opencloud.eu'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} OpenCloud, powered by Heinlein Gruppe`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash'],
    },
  } satisfies Preset.ThemeConfig,

  plugins: [
    rawLoaderPlugin,
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        language: ['en', 'de'],
      },
    ],
    '@docusaurus/theme-mermaid',
  ],

  markdown: {
    mermaid: true,
  },
};

export default config;
