import React, {type ReactNode} from 'react';
import DocsVersionDropdownNavbarItem from '@theme-original/NavbarItem/DocsVersionDropdownNavbarItem';
import type DocsVersionDropdownNavbarItemType from '@theme/NavbarItem/DocsVersionDropdownNavbarItem';
import type {WrapperProps} from '@docusaurus/types';
import {useLocation} from '@docusaurus/router';

type Props = WrapperProps<typeof DocsVersionDropdownNavbarItemType>;

export default function DocsVersionDropdownNavbarItemWrapper(props: Props): ReactNode {
  const location = useLocation();
  const isDocsPage = location.pathname.split('/').includes('docs');

  // Don't render version dropdown on landing pages
  if (!isDocsPage) {
    return null;
  }

  return <DocsVersionDropdownNavbarItem {...props} />;
}
