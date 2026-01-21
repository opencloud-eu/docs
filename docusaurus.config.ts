import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import { redirects } from './redirects';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'OpenCloud Docs',
  tagline: 'Excellent file sharing',
  favicon: 'img/oc-favicon.svg',

  // Set the production url of your site here
  url: 'https://docs.opencloud.eu',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'opencloud-eu', // Usually your GitHub org/user name.
  projectName: 'docs', // Usually your repo name.

  onBrokenLinks: 'throw',

  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn'
    }
  },

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'de'],
    localeConfigs: {
      en: {
        label: 'English',
        htmlLang: 'en-GB', // or 'en-US'
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
      defaultMode: 'light'
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
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'User',
              to: '/docs/user',
            },
            {
              label: 'Admin',
              to: '/docs/admin',
            },
            {
              label: 'Dev',
              to: '/docs/dev',
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
      copyright: `Copyright © ${new Date().getFullYear()} OpenCloud, powered by Heinlein Gruppe`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash'],
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
  },
};

export default config;
