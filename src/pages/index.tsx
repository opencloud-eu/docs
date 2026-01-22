import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import {useDocsPreferredVersion} from '@docusaurus/theme-common';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import Translate from '@docusaurus/Translate';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();

  const {preferredVersion} = useDocsPreferredVersion();

  // Construct base path with version path and section
  const getDocsPath = (section: string) => {
     if (!preferredVersion) {
         return `/docs/${section}/`;
     }

      return `${preferredVersion.path}/${section}/`;
  };

  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)} >
        <div className="container">
            <Heading as="h1" className="hero__title">
                {siteConfig.title}
            </Heading>
            <p className="hero__subtitle">{siteConfig.tagline}</p>
            <div className={styles.buttons}><br/><br/><br/>
                <Link
                    className="button button--secondary button--lg"
                    to={getDocsPath('user')}>
                    <Translate
                        id="homepage.link.item.label.User Documentation"
                        description="The label for the link to user documentation">
                        User Documentation
                    </Translate>
                </Link>
            </div>
            <br/>
            <div className={styles.buttons}>
                <Link
                    className="button button--secondary button--lg"
                    to={getDocsPath('admin')}>
                    <Translate
                        id="homepage.link.item.label.Admin Documentation"
                        description="The label for the link to admin documentation">
                        Admin Documentation
                    </Translate>
                </Link>
            </div>
            <br/>
            <div className={styles.buttons}>
                <Link
                    className="button button--secondary button--lg"
                    to={getDocsPath('dev')}>
                    <Translate
                        id="homepage.link.item.label.Developer Documentation"
                        description="The label for the link to developer documentation">
                        Developer Documentation
                    </Translate>
                </Link>
            </div>
        </div>
    </header>
  );
}

export default function Home(): ReactNode {
    return (
        <Layout
            description="Excellent file sharing">
            <HomepageHeader/>
            <main>
            </main>
        </Layout>
    );
}
