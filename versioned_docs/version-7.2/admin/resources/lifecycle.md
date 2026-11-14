---
sidebar_position: 2
id: lifecycle
title: Release Lifecycle
description: Release Lifecycle
draft: false
---

import ReleaseDates from '@site/static/templates/release-dates.md';

## Release Types

OpenCloud offers three release types to suit different needs: Rolling, Production, and LTS. For most users, Rolling is ideal, providing the latest features every few weeks. Production focuses on stability. LTS (Long-Term Support Release) is designed specifically for businesses that need longevity and extended backports.

<img src={require("./img/lifecycle/Release Cycle OpenCloud.png").default} alt="Release types" width="1920"/>

### Advantage of the LTS Releases

With LTS, businesses can continue using an older production release without needing to upgrade to the latest version, while still receiving critical security patches and critical stability fixes. This makes LTS the perfect choice for organizations seeking a stable long-term solution. LTS is available exclusively to customers with a service and support entitlement through a professional or premium subscription.

| Rolling                                                                                                                                                                                       | Production                                                                                                                                                              | LTS                                                                                                                                                                      |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li>For enthusiasts</li><li>Contains latest features</li><li>Every 3 weeks</li><li>Automated quality assurance</li><li>Community supported</li><li>Documentation on best effort</li></ul> | <ul><li>For production</li><li>Focus on stability</li><li>About every 6 months</li><li>Full quality assurance</li><li>Professional support</li><li>Documented</li></ul> | <ul><li>For production</li><li>Focus on longevity</li><li>Backports for 2 years</li><li>Full quality assurance</li><li>Professional support</li><li>Documented</li></ul> |

## Release Dates

<ReleaseDates />

## Versioning Scheme: Semantic Versioning

OpenCloud follows [Semantic Versioning](https://semver.org/), also known as SemVer. Version numbers are structured as MAJOR.MINOR.PATCH. Breaking changes increase the MAJOR version, new backward-compatible features increase the MINOR version, and backward-compatible bug fixes increment the PATCH version.

<img src={require("./img/lifecycle/semver.png").default} alt="Semantic Versioning" width="1920"/>
