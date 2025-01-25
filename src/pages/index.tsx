import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)} style={{backgroundImage: `url('/img/OpenCloud_Filemanagement_Filesharing_144dpi.jpg')`}}>
      <div className="container">
      <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}><br/><br/><br/>
          <Link
            className="button button--secondary button--lg"
            to="/docs/user/intro">
            User Doku
          </Link>
        </div><br/> 
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/admin/intro">
            Admin Doku
          </Link>
        </div><br/> 
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/dev/intro">
            Developer Doku
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
