import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import Translate from '@docusaurus/Translate';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
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
                    to="/docs/user/">
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
                    to="/docs/admin/">
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
                    to="/docs/dev/">
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
