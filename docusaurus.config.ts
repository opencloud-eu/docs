import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'OpenCloud Docs',
  tagline: 'Excellent file sharing',
  favicon: 'img/oc-favicon.ico',

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
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
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
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/opencloud-eu/docs/tree/main',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      defaultMode: 'dark',
      disableSwitch: true,
      respectPrefersColorScheme: false,
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
          label: 'Developer',
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
              to: '/docs/user/intro',
            },
            {
              label: 'Admin',
              to: '/docs/admin/intro',
            },
            {
              label: 'Developer',
              to: '/docs/dev/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'OpenCloud Community',
              href: 'https://opencloud.eu/en/opencloud-community',
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
              href: 'https://opencloud.eu/de',
            },
            {
              label: 'Blog & News',
              href: 'https://opencloud.eu/en/blog-news',
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
    },
  } satisfies Preset.ThemeConfig,

  themes: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
      ({
        hashed: true,
        language: ["en", "de"],
      }),
    ],
  ],
};

export default config;
