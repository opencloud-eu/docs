import React, {type ReactNode} from 'react';
import {interpolate} from '@docusaurus/Interpolate';
import Copyright from '@theme-original/Footer/Copyright';
import type CopyrightType from '@theme/Footer/Copyright';
import type {WrapperProps} from '@docusaurus/types';

type Props = WrapperProps<typeof CopyrightType>;

export default function CopyrightWrapper(props: Props): ReactNode {
  const copyright = props.copyright
    ? interpolate(props.copyright, {year: new Date().getFullYear()})
    : undefined;

  return <Copyright {...props} copyright={copyright} />;
}
