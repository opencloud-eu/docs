---
sidebar_position: 1
id: intro
title: Welcome
---

# Documentation for OpenCloud Administrators

# Technical Datasheet

## System Requirements

| Category                    | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:-----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Server Operating System** | <ul><li>Linux</li><li>MacOS or Windows WSL (for testing and development)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Database**                | <ul><li>None 🤠 (OpenCloud stores files exclusively on the storage to minimize complexity and ensure maximum reliability)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Storage**                 | <ul><li>Local storage: Classic file storage on a local file system with POSIX compatibility (e.g., ext4, XFS, ZFS)</li><li>S3</li><li>NFS</li><li>CephFS (Q3 / 2025)</li><li>GPFS (Q3 / 2025)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Hardware requirements**   | Minimum (Small Deployment - Up to 10 Users) <ul><li>eg. Raspberry Pi 3</li><li>1 GHz (Single-core)</li><li>512 MB Ram</li><li>Storage: depends on data usage</li></ul> Medium (Deployment - Up to 1,000 Users) <ul><li>2 GHz (Dual-core)</li><li>8 GB Ram</li><li>Storage: depends on data usage</li></ul> General: <ul><li>Disk Performance (IOPS): Input/output operations per second (IOPS) should be unrestricted for maintaining optimal performance.</li><li>The server requirements vary based on load factors such as requests per second, number of client devices per user, file volume, post-processing tasks, and additional apps like Collabora. Proper sizing depends on these variables and should be adjusted accordingly.</li></ul> |


## Deployment Options

| Category                    | Details                                                                                                                                                                                                                                                                                                                               |
|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Types**                   | <ul><li>On-Premises</li><li>Managed Service: Available through partners</li><li>SaaS: Available through partners</li></ul>                                                                                                                                                                                                            |
| **Container (recommended)** | <ul><li>Docker Compose</li><li>Kubernetes Helm Charts (Q2 / 2025)</li></ul>                                                                                                                                                                                                                                                           |
| **Bare-Metal**              | <ul><li>OpenCloud can run as a single binary. However, integrating additional services like Collabora, Apache Tika for search, or antivirus is not documented. This deployment is recommended only for experienced users who require minimal file management features. Support is available exclusively from the community.</li></ul> |

## Backup

| Category            | Details                                                                                                                                          |
|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Backup strategy** | <ul><li>**Snapshots:** Backups can be easily done solely through storage snapshots, eliminating the need for complex database backups.</li></ul> |


## Security

| Category                 | Details                                                                                                                                                              |
|:-------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Encryption**           | <ul><li>Transport Encryption: TLS</li><li>Server-Side Encryption: S3 SSE</li><li>E2EE Client-Side Encryption: Handled exclusively via OS-native encryption</li></ul> |
| **Access management**    | <ul><li>RBAC (Role-Based Access Control)</li><li>2FA / MFA</li><li>SSO (LDAP, SAML, OAuth)</li></ul>                                                                 |
| **Auditing & Logging**   | <ul><li>Detailed logs, audit trails, monitoring APIs</li></ul>                                                                                                       |
| **File Firewall**        | <ul><li>Prevent upload of restricted filetypes based on a allow- or denylist.</li></ul>                                                                                                |
| **Antivirus**            | <ul><li>ClamAV (default)</li><li>ICAP: Integrate 3rd party anti-virus scanner via Internet Content Adaptation Protocol (ICAP)</li></ul>                              |
| **Data Loss Prevention** | <ul><li>Collabora Secure View</li></ul>                                                                                                                              |

## Identity Management

| Category       | Details                                                                                                                                          |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Integrated** | <ul><li>Integrated user and group management (LibreIDM) for up to 500 users. Designed for standalone or small-sized deployments that do not rely on third-party identity services, usually for friends and family.</li></ul>                                                            |
| **External**   | <ul><li>OpenID Connect (OIDC): Integration of external identity providers via Keycloak.</li><li>Integration of Azure AD, EntraID, ADFS</li></ul> |

## Compliance

| Regulation                                | Details                                                                                                                                                                                                 |
|:------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EU-GDPR**                               | <ul><li>Compliant</li></ul>                                                                                                                                                                             |
| **WCAG 2.1 / BITV 2.0 Web Accessibility** | <ul><li>Compliant. To prevent accessibility regressions, we treat any accessibility violation as a bug and continuously fix these issues as part of our daily software development lifecycle.</li></ul> |

## High Availability

| Category                  | Details                                                                                                                                                                                                          |
|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Redundancy & Failover** | <ul><li>Supported in clustered environments to ensure high availability and system reliability.</li><li>Automatic failover mechanisms help minimize downtime in case of hardware or software failures.</li></ul> |

## Integrations

| Category | Details |
|:---------|:--------|
| **Plugins & Extensibility** | <ul><li>Web: Extension system for adding custom functionality.</li><li>Server: Microservices architecture for modular and scalable server-side extensions</li></ul> |

## APIs

| API          | Description                                                                                                                                                       |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WebDAV**   | <ul><li>Standard file API for remote file management over HTTP/HTTPS.</li></ul>                                                                                   |
| **GraphAPI** | <ul><li>Microsoft Graph API for managing cloud storage and collaboration spaces.</li></ul>                                                                        |
| **gRPC**     | <ul><li>High-performance RPC framework for microservice communication.</li></ul>                                                                                  |
| **OCS**      | <ul><li>API for programmatic file/folder sharing and management.</li></ul>                                                                                        |
| **OCM**      | <ul><li>Open Cloud Mesh API for federated file and folder sharing between different file cloud platforms like Cernbox, ownCloud, Nextcloud or Seafile .</li></ul> |
| **SSE**      | <ul><li>Server-sent event stream for real-time client notifications.</li></ul>                                                                                    |
| **WOPI**     | <ul><li>Microsoft API for integrating Office apps with third-party storage, e.g., Collabora.</li></ul>                                                            |
| **ICAP**     | <ul><li>Network protocol for offloading content scanning (e.g., antivirus).</li></ul>                                                                             |