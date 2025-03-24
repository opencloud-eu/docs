---
sidebar_position: 3
id: datasheet
title: Datasheet
---


## Deployment Options

| Category                    | Details                                                                                                                                                                                                                                                                                                                               |
|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Types**                   | <ul><li>On-Premises</li><li>Managed Service: Available through partners</li><li>SaaS: Available through partners</li></ul>                                                                                                                                                                                                            |
| **Container (recommended)** | <ul><li>Docker Compose</li><li>Kubernetes Helm Charts or Podman (Q2 / 2025)</li></ul>                                                                                                                                                                                                                                                           |
| **Bare-Metal (not officially supported)**              | <ul><li>OpenCloud can run as a single binary. However, integrating additional services like Collabora, Apache Tika for search, or antivirus is not documented. Bare-metal deployments are not officially supported by OpenCloud. They are great for quick evaluation but are undocumented and have a minimalist feature set.</li></ul> |

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
| **KQL**     | <ul><li>Keyword Query Language (KQL) is a search language to perform advanced searches by filtering and querying structured data, metadata, and documents efficiently.</li></ul>                                                            |
| **ICAP**     | <ul><li>Network protocol for offloading content scanning (e.g., antivirus).</li></ul>                                                                             |
