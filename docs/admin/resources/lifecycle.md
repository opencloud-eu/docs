---
sidebar_position: 2
id: lifecycle
title: "Release Lifecycle"
draft: true
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Release Types

OpenCloud offers three release types to suit different needs: **Rolling**, **Production**, and **LTS**. For most users, Rolling is ideal, providing the **latest features** every few weeks. Production focuses on **stability**. LTS (Long-Term Support Release) is designed specifically for businesses that need longevity and extended **backports**. 

<img src={require("./img/lifecycle/Release Cycle OpenCloud.png").default} alt="Release types" width="1920"/>


### Advantage of the LTS Releases

With LTS, businesses can continue using an older production release without needing to upgrade to the latest version, while still **receiving critical security patches** and **critical stability fixes**. This makes LTS the perfect choice for organizations seeking a **stable long-term** solution. LTS is available exclusively to customers with a service and support entitlement through a business license.

| Rolling | Production | LTS |
|:--------|:-----------|:----|
| <ul><li>For enthusiasts</li><li>Contains latest features</li><li>Every 3 weeks</li><li>Automated quality assurance</li><li>Community supported</li></ul> | <ul><li>For production</li><li>Focus on stability</li><li>About every 6 months</li><li>Full quality assurance</li><li>Professional support</li></ul> | <ul><li>For production</li><li>Focus on longevity</li><li>Backports for 2 years</li><li>Full quality assurance</li><li>Professional support</li></ul> |

# Release Dates

<Tabs>
  <TabItem value="rolling" label="Rolling" default>
    | Version | Release Date | Release Notes |
    |:--------|:-------------|:--------------|
    | v2.1.0 | 2025 April 07 | [View Notes](https://github.com/opencloud-eu/opencloud/releases/tag/v2.1.0) |
    | v2.0.0 | 2025 March 26 | [View Notes](https://github.com/opencloud-eu/opencloud/releases/tag/v2.0.0) |
    | v1.1.0 | 2025 March 18 | [View Notes](https://github.com/opencloud-eu/opencloud/releases/tag/v1.1.0) |
    | v1.0.0 | 2025 February 24 | [View Notes](https://github.com/opencloud-eu/opencloud/releases/tag/v1.0.0) |

  </TabItem>
  <TabItem value="production " label="Production">
    | Version | Release Date | Release Notes |
    |:--------|:-------------|:--------------|
    | v2.0.0 | 2025 March 26 | [View Notes](https://github.com/opencloud-eu/opencloud/releases/tag/v2.0.0) |
    </TabItem>
  <TabItem value="lts" label="LTS">
    LTS Releases will be availabile as the second Production Releases will be published. Until then a LTS release makes no sense.
  </TabItem>
</Tabs>