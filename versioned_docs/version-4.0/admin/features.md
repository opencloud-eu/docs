---
sidebar_position: 2
id: features
title: Features
description: Features
draft: false
---

## Key Features at a Glance

- Seamless File Synchronization: Access your files across all devices.
- Secure & Flexible File Sharing: Share files with granular roles, expiration dates, and password protection.
- Spaces - Collaborative Team Folders: Ensure continuity even if team members leave.
- Real-Time Collaboration: Work on documents simultaneously with Collabora Web Office.
- Advanced Search & Organization: Use full-text search, tags, and filters for quick access.
- Unlimited Storage & Uploads: No file size restrictions.
- Privacy-First Design: Zero-Knowledge principle ensures admins can't access user content.
- Cross-Client Availability: Works on Windows, Mac, Linux, Android, iOS, and Web.

## File Management

**Functions for storage, access and organization of files.**

Full control over storage and access. Seamless operation across all devices.

### Access from Anywhere

Files and folders can be opened, synchronized, and shared from any location and device—via browser, desktop client (Windows, macOS, Linux), or mobile apps (iOS, Android).

### Synchronization Across Devices

Changes are synchronized automatically across all connected devices, in real time via the respective OpenCloud client.

### Offline Access

Users can mark files or folders for offline use to open and edit them without an internet connection. Changes are automatically synced once connectivity is restored.

### Files On-Demand

Files can be viewed directly in the device’s File Explorer and are stored efficiently, as they are only downloaded when needed. Large folder structures are immediately accessible without full synchronization, reducing network load and sync overhead. Available on Windows desktop operating systems and mobile clients.

### Advanced Search

Files can be found quickly—by title or full text. The search provides live suggestions and supports filtering by file type, modification date, tag, or storage location.

### Versioning and Recovery

Every change is automatically saved as a version and can be restored at any time. Administrators can define how many versions to keep and the rules for deleting older versions.

### No Limit on File Size, Count, or Type

OpenCloud supports storing any number of files in any format and size.

### Folders and Tags

Files can be organized in hierarchical folder structures or with tags. Tags serve as a cross-project taxonomy, while folders typically represent team or project structures.

### Open Files with Native Applications

Files in OpenCloud can be opened directly with local programs, edited, and saved back—without manual exporting or importing. Files remain in their original OpenCloud location and keep their permissions, version history, etc.

### Resuming Interrupted Uploads

Uploads interrupted by connection issues are automatically resumed. Transfers use the TUS protocol (Resumable Uploads), ensuring even very large files can be uploaded without data loss.

### Automatic Upload

New or changed files are automatically uploaded as soon as a connection is available. Users and administrators can define which folders sync automatically, exclude certain file types, and configure parallel uploads. Transfers run in the background and adapt to connection quality and system resources.

### Integration as a Network Drive

OpenCloud can be integrated as a network drive in standard operating systems and behaves like a local drive. This uses WebDAV or the native desktop client.

### Document Scanning via Camera

Using the mobile app, documents can be captured with the camera, automatically cropped, and saved as PDFs in OpenCloud.

### Unlimited Storage Space

There are no system-side limits on the number or size of stored files. Available capacity depends on the deployed server or storage infrastructure.

### Integrated Preview

Documents, images, videos, and audio files can be viewed directly in the browser, desktop client, and mobile apps. Common formats are supported. On mobile devices, previews use native viewers or Collabora integration.

### Personal Storage

Each user has a private storage area visible only to them by default. Files can be organized, shared, or moved to Spaces from here—ensuring clear separation between personal and shared work areas.

### Customizable Storage Limits (Quotas)

Administrators can assign storage limits per user or Space to allocate storage efficiently.

## Usability & User Experience

**Simple and blazing fast to use for all user groups.**

Intuitive usage without training. Accessibility for all users. Consistent, brand-compliant user experience.

### Fast User Interface

The application remains responsive even in folders with many files and avoids unnecessary page reloads. Asynchronous updates keep lists and detail views usable without interruptions.

### Drag & Drop, Multi-Selection, Copy/Paste

Files can be moved via drag & drop, multiple files can be selected at once, and actions like copy/paste can be performed using keyboard shortcuts—just like in a desktop file manager. Everyday file operations thus become faster and feel familiar.

### Accessible User Interface

The OpenCloud web interface is optimized according to the European Accessibility Act (EAA) and WCAG 2.1/BITV 2.0 guidelines for users with visual, motor, or cognitive impairments. It provides clear keyboard navigation, understandable labels, sufficient color contrast, and full screen-reader and focus support—helping organizations meet legal and procurement requirements.

### Email Notifications

Users receive email notifications about events such as new shares or membership changes in a Space.

### Customizable View Modes

Files can be displayed in list, tile, or compact views. Columns, visible elements, and items per page can be configured to keep large directories tidy.

### Color Scheme Selection

Users can switch between light and dark modes to improve readability under different lighting conditions and reduce eye strain.

### Responsive Design

The interface adjusts automatically to screen sizes from smartphones to 8K monitors. Navigation and file views remain fully usable without separate desktop or mobile apps.

### Consistent Look & Feel

Web, desktop, and mobile apps follow a unified interaction concept. Consistent navigation patterns and icons reduce onboarding time and user errors.

### Individual Branding

Administrators can create or customize design themes, including color palettes, logos, backgrounds, and UI elements. A fully accessible theme can be automatically generated from a single corporate color or defined manually. This allows OpenCloud to seamlessly match an organization’s corporate design.

:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

## Collaboration & Productivity

**Collaborative work in real time and structured team organization:** Real-time collaboration without additional software. Structured workflows and a unified work environment.

### Workspaces for Teams and Projects (“Spaces”)

Spaces are independent work areas that go beyond simple folders. They bundle files, permissions, and responsibilities for projects or departments and can be managed separately—with dedicated owners, rules, and storage limits. This creates a clear separation between personal storage, team/project files, and organization-wide content.

### Delegated Space Administration

Project or team leads can manage individual Spaces without requiring global admin rights. Member and permission management can thus be decentralized.

### Internal Sharing

Files and folders can be shared with users or groups within the organization. Access rights such as read, edit, or upload can be precisely controlled to ensure secure collaboration.

### External Sharing

Content can be shared securely with customers, service providers, suppliers, or authorities via password-protected links or guest accounts (soon).

### Federation – Sharing Across Sites or Organizations

Enables secure collaboration between multiple OpenCloud instances, e.g., across branches or subsidiaries. Files are shared directly across servers without creating duplicates. Authentication and access rights are centrally managed.

### Web Office

Through Collabora Online integration, office documents can be opened and collaboratively edited directly within the web interface—without local installation. Users can comment, co-edit in real time, and rely on full compatibility with Microsoft Office and OpenDocument formats.

### Real-Time Editing

Multiple users can work on the same files simultaneously. Changes sync immediately, and automatic locking mechanisms prevent version conflicts—ensuring smooth co-editing.

### Calendar and Contacts

Integration with CalDAV and CardDAV enables teams to manage shared calendars and contact lists directly in OpenCloud. Appointments and deadlines can be linked to files, and shared contacts can be centrally maintained. Compatible with Apple Calendar, Outlook, Thunderbird, Evolution, and others. Note that this feature is not Supported in the enterprise licence.

## Compliance & Data Protection

**Protects data and fulfills all legal requirements.**

Maximum data security and transparent processing. Trusted for regulated industries.

### Zero-Knowledge Principle

Administrators can manage Spaces (e.g., cleanup, quota changes) but cannot access its content. This ensures full confidentiality: even admins cannot view user data.

### Compliance with Data Protection and Security Policies

OpenCloud meets key international standards such as GDPR, ISO 27001, CCPA, HIPAA, FERPA, SOC 2, and CRA through features like encryption, audit logs, and access controls. Actual certifiability depends on the operational model: self-hosted deployments fall under the operator’s responsibility, while the Enterprise Licence follows auditable, policy-compliant processes. OpenCloud integrates with existing compliance or GRC systems and provides exportable audit data.

:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### §20 GDPR Personal Data Export

Includes features that support GDPR compliance (e.g., personal data export according to §20 GDPR.).
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Server-Side Encryption

Files are encrypted automatically when stored on the server. The key resides securely on the server and protects against physical access or unauthorized access to drives or backups. Combined with TLS in transit, this provides consistent security—but does not prevent admin-level access inside the application (unlike end-to-end encryption).

### Metadata Encryption

Sensitive metadata such as file names or tags can also be stored encrypted, preventing third parties from inferring content based on file structure or names.

### Ransomware Protection

Files encrypted by an infected user can be restored to their pre-attack state, keeping data safe and available.

### Audit Logs and Change Tracking

All security-relevant actions—uploads, shares, deletions, login attempts—are logged. File and metadata changes can be traced down to user level for full transparency.

### Virus Protection

Incoming and synchronized files are scanned automatically for malware. OpenCloud uses ICAP interfaces (e.g., for ClamAV, Sophos, Kaspersky) and integrates with existing security gateways.

:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### File Firewall

Prevents unsafe file uploads by blocking defined file types (e.g., executables, macros). Admins centrally manage allow/deny lists and apply them to users and Spaces.

:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Protected Preview with Watermarks

Documents can be displayed with dynamic watermarks to deter screenshots or unauthorized sharing. Watermarks may include username, timestamp, or organization ID for traceability. Based on “Secure View” using Collabora or OnlyOffice.

:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

## Identity and Access Management (IAM)

**Central, secure management of users, roles, and permissions.**

Centralized user and group management. Secure access across organizational boundaries. Integration with existing identity systems.

### Password Policies and Generator

Enforces strong passwords with rules for complexity and expiration. A “Banned Password List” blocks weak patterns (e.g., “Password123”). An integrated generator creates compliant passwords.

:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Two-Factor Authentication (2FA/MFA)

Adds a second authentication factor beyond the password. Enforced via the connected identity provider (e.g., Keycloak). Supports TOTP, push notifications, and FIDO2/U2F tokens.

### Role-Based Access Control (RBAC)

User rights are assigned centrally via roles reflecting the organizational structure. RBAC simplifies management in complex environments and enables fine-grained control (e.g., link creation rules, password enforcement, preset expiration dates).

### Biometric Unlock (Touch & Face ID)

The mobile app can be unlocked using fingerprint or facial recognition, improving security.

### Multiple Accounts per Client

Users can use multiple accounts in parallel on desktop and mobile clients, making it easy to switch between work, tenant, and private contexts.

### LDAP

OpenCloud supports LDAP systems such as OpenLDAP, FreeIPA, or Univention Directory via secure bindings with filter support.

### Active Directory

The Enterprise Licence supports integration with Microsoft Active Directory and Azure Entra ID, including optional managed connectivity for paying customers.

:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Single Sign-On (SSO)

Users log in with their central company account. Supported protocols include OpenID Connect, LDAP, SAML 2.0, and OAuth 2.0.

### External Identity Providers (IdP)

OpenCloud integrates with leading IdPs such as Keycloak, Azure AD, EntraID, or ADFS—ideal for environments with existing directory infrastructures.

### Share Links

Content can be shared externally via link, optionally protected with a password and expiration date. Links are quick and simple but offer limited traceability compared to guest accounts.

### Guest Accounts (soon)

External users receive personal, password-protected accounts. Their access is fully attributable and auditable, with policies for expiration, 2FA/MFA, and individual revocation—ideal for compliance-sensitive use cases.

### Session Management

Administrators can monitor, terminate, or limit user sessions to prevent unauthorized access, especially on shared or remote devices.

## Operation & Deployment

**Reliable, scalable, and professional operation.**

High stability, minimal downtime, secure deployment, and scalable architecture.

### Snapshots and Backups

Automated snapshots enable restoring whole instances or individual user areas. Backups can be scheduled and stored locally or externally. Because metadata is stored directly with the files, elements such as versions and tags remain intact during restores or migrations—without dependency on database states.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Security Advisories

Enterprise Licence customers receive early security notifications about new vulnerabilities, including risk assessments and scheduled patch plans.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Kubernetes Deployment

OpenCloud can be deployed as containerized microservices in Kubernetes clusters using Helm charts for installation, scaling, and upgrades. Automated orchestration enables load balancing, self-healing, zero-downtime deployments, and dynamic scaling.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Scalable Enterprise Storage Systems

Integrates storage systems like CephFS, GPFS (IBM Spectrum Scale), or S3-compatible backends to support petabyte-scale volumes with high performance and redundancy.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Performance and Load Optimization

Optimized for scalability and speed through parallel transfers and distributed I/O. Monitoring with Prometheus and Grafana enables continuous analysis and scaling.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Multi-Tenancy

Multiple organizational units can be hosted on the same instance—ideal for corporations, public authorities, or service providers.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Metadata Stored in Files

All metadata, including tags and version information, is stored securely within the system and remains consistent across storage environments.

### High Availability and Failover

Redundant nodes can take over operations automatically in case of component failure, preventing downtime.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Long-Term Support (LTS)

Enterprise customers receive long-term supported versions with security updates and bug fixes—suitable for critical and compliance-sensitive environments.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Installation and Security Check

Before deployment or upgrades, OpenCloud runs configuration and security checks and provides an assessment with recommendations.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Mass Rollouts

Clients can be preconfigured with a server address for simplified mass deployment, reducing helpdesk requests.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Guaranteed Upgrade Support

Supports smooth upgrades across major and minor versions with migration paths for data and accounts. The Enterprise Licence provides validated scripts, compatibility checks, and rollback options.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Service Level Agreements (SLA)

The Enterprise Licence includes SLAs with defined response and resolution times, priority support, escalation management, and security notifications—ensuring professional operation.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### On-Demand Support

During planned changes or upgrades, an OpenCloud engineer is available live for immediate troubleshooting and guidance.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Air-Gapped Operation

OpenCloud can run in isolated networks without internet access. Installation, updates, and extensions occur via internal repositories or offline media. External integrations (e.g., Web Office) can also be hosted on-premises to keep all data within the isolated environment.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

## Integrations & Interfaces

**Open APIs and extensions for seamless integration and automation.**

Third-party extensibility and custom development. Open architecture for automation and data exchange.

### Plugin Architecture

OpenCloud’s functionality can be extended or customized. The documented developer interface offers hooks, events, and a modular framework for server-side extensions.

### Client SDKs

SDKs for Desktop, Mobile, and Web encapsulate OpenCloud’s server interfaces, allowing developers to build client-side applications or integrations without implementing API calls manually. Supported languages include Objective-C, TypeScript, PHP, Go, and C++.

### Headless and Microservices Architecture

OpenCloud uses a modern headless architecture that separates UI from backend services. Individual services can be operated, scaled, or developed independently.

### File and Collaboration APIs

OpenCloud supports WebDAV for file access and sync, WOPI for office integration, OCS for user and app communication, and OCM for federated sharing across compatible systems.

### Native REST API

Provides automation-friendly access to nearly all OpenCloud features—user and rights management, file operations, integration into external systems, and more.

### Federation API

Allows connecting multiple OpenCloud or compatible platforms (e.g., Nextcloud, ownCloud).

### GraphAPI

Used for communication between clients and the server, inspired by Microsoft Graph.

### Security, Compliance, and Monitoring APIs

The Enterprise Licence includes extended APIs for security checks, compliance monitoring, and real-time reporting. ICAP enables external antivirus/DLP integration, KQL supports compliance data analysis, and SSE provides live notifications and monitoring.
:::info supported within the [enterprise licence](https://opencloud.eu/en/product/service-and-support)
:::

### Custom File Types

Admins and developers can define custom file types and metadata structures to adapt OpenCloud to industry-specific needs (e.g., medical, legal, industrial). Managed via the plugin system and REST APIs.
