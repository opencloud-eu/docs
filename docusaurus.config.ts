import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import { redirects } from './redirects';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'OpenCloud Docs',
  tagline: 'Excellent file sharing',
  favicon: 'img/oc-favicon.svg',

  url: 'https://docs.opencloud.eu',
  baseUrl: '/',

  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',

  // Docusaurus Faster (Rspack, SWC, Lightning CSS), see
  // https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: {
      // required by faster.ssgWorkerThreads
      removeLegacyPostBuildHeadAttribute: true,
    },
    faster: true,
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'de'],
    localeConfigs: {
      en: {
        label: 'English',
        htmlLang: 'en-GB',
      },
      de: {
        label: 'Deutsch',
        htmlLang: 'de-DE',
      },
    },
  },

presets: [
  [
    'classic',
    {
      docs: {
        sidebarPath: require.resolve('./sidebars.ts'),
        editUrl: 'https://github.com/opencloud-eu/docs/tree/main',
        // 4.0, 7.2, and 9.1 are production releases that still get updates,
        // so they must not show the "no longer actively maintained" banner
        versions: {
          '4.0': {banner: 'none'},
          '7.2': {banner: 'none'},
          '9.1': {banner: 'none'},
        },
      },
      blog: false,
      theme: {
        customCss: require.resolve('./src/css/custom.css'),
      },
    } satisfies Preset.Options,
  ],
],


  themeConfig: {
    image: 'img/oc-docs-social-card.jpg',
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true
    },
    navbar: {
      logo: {
        alt: 'OpenCloud Logo',
        src: 'img/oc-logo-petrol.svg',
        srcDark: 'img/oc-logo-lilac.svg'
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
          type: 'docsVersionDropdown',
          position: 'right',
        },
        {
          type: 'localeDropdown',
          position: 'right'
        }
      ],
  },
  footer: {
      copyright: 'Copyright © {year} OpenCloud, powered by Heinlein Gruppe',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'User',
              to: '/docs/user/',
            },
            {
              label: 'Admin',
              to: '/docs/admin/',
            },
            {
              label: 'Dev',
              to: '/docs/dev/',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'OpenCloud Community',
              href: 'https://opencloud.eu/opencloud-community',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/opencloud-eu',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'OpenCloud',
              href: 'https://opencloud.eu/',
            },
            {
              label: 'Blog & News',
              href: 'https://opencloud.eu/blog-news',
            },
            {
              label: 'Linkedin',
              href: 'https://www.linkedin.com/company/opencloud-eu',
            },
            {
              label: 'Mastodon',
              href: 'https://social.opencloud.eu/@OpenCloud',
            },
            {
              label: 'Bluesky',
              href: 'https://bsky.app/profile/opencloud.eu',
            },
          ],
        },
      ],
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'diff', 'gherkin', 'http', 'ini', 'nginx', 'powershell', 'rego'],
    },
  } satisfies Preset.ThemeConfig,

  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
          redirects,
      },
    ],
  ],

  themes: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
      ({
        hashed: true,
        language: ["en", "de"],
        indexBlog: false,
      }),
    ],
    '@docusaurus/theme-mermaid',
  ],

  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'throw'
    }
  },
};

export default config;
