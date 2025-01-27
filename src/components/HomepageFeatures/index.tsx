import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import { useColorMode } from '@docusaurus/theme-common';

type FeatureItem = {
  title: string;
  lightSvg: React.ComponentType<React.ComponentProps<'svg'>>;
  darkSvg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [

  {
    title: 'Dokumentation',
    lightSvg: require('@site/static/img/oc-logo-petrol.svg').default,
    darkSvg: require('@site/static/img/oc-logo-lilac.svg').default,
    description: (
      <>
        Dokumentation zur Nutzung von OpenCloud
      </>
    ),
  },
  
];

function Feature({title, lightSvg, darkSvg, description}: FeatureItem) {
  const { colorMode } = useColorMode();
  const Svg = colorMode === 'dark' ? darkSvg : lightSvg

  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
