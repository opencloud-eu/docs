import React, {type ReactNode} from 'react';
import Copyright from '@theme-original/Footer/Copyright';
import type CopyrightType from '@theme/Footer/Copyright';
import type {WrapperProps} from '@docusaurus/types';

type Props = WrapperProps<typeof CopyrightType>;

export default function CopyrightWrapper(props: Props): ReactNode {
    return (
        <>
            Copyright © {new Date().getFullYear()} OpenCloud, powered by Heinlein Gruppe
        </>
    );
}
