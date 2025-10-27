---
sidebar_position: 2
id: lifecycle
title: Release Lifecycle
description: Release Lifecycle
draft: false
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Release Types

OpenCloud offers three release types to suit different needs: Rolling, Production, and LTS. For most users, Rolling is ideal, providing the latest features every few weeks. Production focuses on stability. LTS (Long-Term Support Release) is designed specifically for businesses that need longevity and extended backports.

<img src={require("./img/lifecycle/Release Cycle OpenCloud.png").default} alt="Release types" width="1920"/>

### Advantage of the LTS Releases

With LTS, businesses can continue using an older production release without needing to upgrade to the latest version, while still receiving critical security patches and critical stability fixes. This makes LTS the perfect choice for organizations seeking a stable long-term solution. LTS is available exclusively to customers with a service and support entitlement through a business license.

| Rolling                                                                                                                                                                                       | Production                                                                                                                                                              | LTS                                                                                                                                                                      |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li>For enthusiasts</li><li>Contains latest features</li><li>Every 3 weeks</li><li>Automated quality assurance</li><li>Community supported</li><li>Documentation on best effort</li></ul> | <ul><li>For production</li><li>Focus on stability</li><li>About every 6 months</li><li>Full quality assurance</li><li>Professional support</li><li>Documented</li></ul> | <ul><li>For production</li><li>Focus on longevity</li><li>Backports for 2 years</li><li>Full quality assurance</li><li>Professional support</li><li>Documented</li></ul> |

## Release Dates

<Tabs>
  <TabItem value="rolling" label="Rolling" default>
    | Version | Release Date | Release Notes & Download|
    |:--------|:-------------|:--------------|
    | - | 2026 Januar 5 | - |
    | - | 2025 December 15 | - |
    | - | 2025 November 24 | - |
    | - | 2025 November 3 | - |
    | v3.6.0 | 2025 October 27 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v3.5.0) |
    | v3.5.0 | 2025 September 22 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v3.5.0) |
    | v3.4.0 | 2025 September 2 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v3.4.0) |
    | v3.3.0 | 2025 August 11 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v3.3.0) |
    | v3.2.0 | 2025 July 21 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v3.2.0) |
    | v3.1.0 | 2025 June 30 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v3.1.0) |
    | v3.0.0 | 2025 June 10 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v3.0.0) |
    | v2.3.0 | 2025 May 19 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v2.3.0) |
    | v2.2.0 | 2025 April 28 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v2.2.0) |
    | v2.1.0 | 2025 April 07 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v2.1.0) |
    | v2.0.0 | 2025 March 26 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v2.0.0) |
    | v1.1.0 | 2025 March 18 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v1.1.0) |
    | v1.0.0 | 2025 February 24 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v1.0.0) |

  </TabItem>
  <TabItem value="production " label="Production">
    | Version | Release Date | Release Notes & Download |
    |:--------|:-------------|:--------------|
    | - | 2025 November 24 | - |
    | v2.0.4 | 2025 July 16 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v2.0.4) |
    | v2.0.3 | 2025 June 10 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v2.0.3) |
    | v2.0.2 | 2025 May 2 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v2.0.2) |
    | v2.0.1 | 2025 April 28 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v2.0.1) |
    | v2.0.0 | 2025 March 26 | [Details · Download](https://github.com/opencloud-eu/opencloud/releases/tag/v2.0.0) |
    </TabItem>
  <TabItem value="lts" label="LTS">
    LTS Releases will be availabile as the second Production Releases will be published. Until then a LTS release makes no sense.
  </TabItem>
</Tabs>

## Versioning Scheme: Semantic Versioning

OpenCloud follows [Semantic Versioning](https://semver.org/), also known as SemVer. Version numbers are structured as MAJOR.MINOR.PATCH. Breaking changes increase the MAJOR version, new backward-compatible features increase the MINOR version, and backward-compatible bug fixes increment the PATCH version.

<img src={require("./img/lifecycle/semver.png").default} alt="Semantic Versioning" width="1920"/>
