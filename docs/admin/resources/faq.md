---
sidebar_position: 1
id: faq
title: FAQ
description: Frequently asked questions FAQ
draft: false
---

# FAQ

Welcome to the frequently asked questions (FAQ). Here you will find answers to the most common questions.

## General Questions

<details>
<summary>What problem does OpenCloud solve for me?</summary>

### Simplified Administration

OpenCloud is designed to be straightforward to set up and manage, allowing administrators to handle the system with minimal effort and without unnecessary complexity.

### Independent File-sharing

OpenCloud is designed to give you a privacy-focused alternative to mainstream platforms like Microsoft OneDrive or Google Drive, freeing you from reliance on big tech services and their data-collection practices.

</details>

<details>
<summary>How does OpenCloud differ from other open source file sharing applications?</summary>

OpenCloud is simpler and more reliable than existing PHP-based solutions. OpenCloud stands out by offering a radically simplified architecture compared to other open-source file-sharing solutions. While many alternatives require maintaining complex stacks involving multiple components like PHP, MySQL, Redis, and Apache — creating a web of dependencies and potential security risks—OpenCloud avoids this entirely. It writes data directly to disk instead of relying on a dedicated database, making it much easier to maintain and far more reliable. With OpenCloud, you can focus on your files without worrying about intricate setups or data loss risks.

</details>

<details>
<summary>Is OpenCloud 100% open source?</summary>

Yes. The source code of OpenCloud is licenced under the Apache 2 licence.

</details>

## Cost and Licensing

<details>
<summary>Is OpenCloud free to use?</summary>

Yes, please!

</details>

<details>
<summary>Can I use it for commercial purposes?</summary>

Absolutely!

</details>

<details>
<summary>If OpenCloud is free, how are the employees paid?</summary>

We're glad you asked.
We provide a paid support subscription, see [https://opencloud.eu/en/product/service-and-support](https://opencloud.eu/en/product/service-and-support). With a support subscription you’ll be the first to know about security vulnerabilities and receive detailed instructions on how to address them or how to integrate OpenCloud into your existing systems and storage. We also provide Long-Term-Support if you don't want to upgrade your system so frequently.

</details>

<details>
<summary>Are there educational or non-profit discounts or support plans?</summary>

Please contact sales for such inquiries and we'll find a good sulution.

</details>

## Privacy and Security

<details>
<summary>Does OpenCloud comply with privacy regulations such as GDPR or HIPAA?</summary>

Yes, of course!

</details>

## Features and Functionality

<details>
<summary>What types of files can I store and share with OpenCloud?</summary>

No restrictions. You can store and share any filetype. If necessary, you can restrict the upload of certain filetypes like .exe or documents with macros like xlsm.

</details>

<details>
<summary>Is there an upload file size limit in OpenCloud?</summary>

Nope.

</details>

<details>
<summary>Does OpenCloud support real-time collaboration and editing?</summary>

Yes. We use the WOPI standard for realtime collabration in the web office application Collabora.

</details>

<details>
<summary>Can I create and manage user accounts and permissions?</summary>

Yes, you can either use the built-in user management system or integrate OpenCloud with your existing identity management.

</details>

<details>
<summary>Are there mobile apps, and do they offer the same features as the desktop version?</summary>

We provide apps for Windows, MacOS, Linux, iOS and Android. Please refer to the roadmap to see when the apps will be available: [https://opencloud.eu/roadmap](https://opencloud.eu/roadmap)

</details>

<details>
<summary>Does OpenCloud support versioning?</summary>

Yes. In case you made a mistake, you can always jump back to older versions of a file. We got your back!

</details>

## Deployment and Installation

<details>
<summary>Can I self-host OpenCloud on my own server?</summary>

Yes and we encourage you to do so! (We do not provide a SaaS service that stores your files on our servers, like Google Drive or Microsoft OneDrive do.)

</details>

<details>
<summary>What are the system requirements for hosting OpenCloud?</summary>

The system requirements for hosting OpenCloud depend heavily on the number of concurrent users and the workload they generate, such as the frequency of their requests. OpenCloud is versatile—it can run on anything from a Raspberry Pi to a large data center setup.

For example, a Raspberry Pi 4 can support hundreds of registered users, but the key factor is the number of users actively using the system at the same time. Concurrent users, especially those using desktop or mobile clients (which frequently check for updates), require more resources. Additional features like the web office integration Collabora or antivirus scanning also impact performance.

For a minimal setup, OpenCloud can comfortably support 20 concurrent users browsing files via the web interface. As your user base or workload increases, scaling the hardware accordingly will ensure smooth performance. A factor to scale performance is just to add storage, as OpenCloud needs storage IOPS for performance.

Key Factors for Optimal Performance:

- Storage IOPS: The performance of OpenCloud highly relies on the amount of IOPS of your storage - the more, the better.
- Network throughput: Another factor for enhancing the performance of OpenCloud is network throughput in distributed storage.

</details>

<details>
<summary>How difficult is it to set up, and is technical expertise required?</summary>

One of our goals is to make the deployment of OpenCloud as simple as possible. Depending on your expereince, it's possible to set up a basic OpenCloud instance in less than 1 minute. See [the Quick Start](https://docs.opencloud.eu/docs/admin/intro)

</details>

<details>
<summary>Can it be deployed in a Docker or Kubernetes environment?</summary>

Yes.

- Docker Compose: The docker compose files are maintained and tested by us.
- Community HELM charts: Feel free to contribute!

</details>

## Customization and Extensibility

<details>
<summary>Can I add modifications like add-ons or extensions?</summary>

Yes, OpenCloud allows you customizations:

- Wordings: You can replace specific terms, such as changing the word “Spaces” to “Datarooms” to better fit your terminology.
- Extensions: The web UI also supports custom web extensions. Check out our developer documentation [here] to learn how to get started with creating and adding your own extensions and find existing extensions [here].

</details>

## Collaboration and Sharing

<details>
<summary>How does file sharing work within OpenCloud?</summary>

OpenCloud offers three main ways to share files, making it easy to collaborate and manage access:

### Personal Share

Share files with registered users within your organization. You can assign permissions such as view, edit, or download, providing flexible control over file access.

### Share via Link

Share files with anyone, even outside your organization, by generating a link. No account is required for accessing the file.

### Spaces

Spaces are user-independent datarooms that belong to the organization rather than an individual. This ensures files remain within the organization, even if users leave. Examples of Spaces include school classes, collaborative projects, or organizational units like Marketing, Sales, or Finance. Spaces are easier for admins to manage, as they can be self-managed by designated users.

### Special Feature: Secret File Drop

The Secret File Drop allows anonymous users to securely upload files (e.g., homework, photos or even whistleblower material) without needing an account.

</details>

<details>
<summary>Can I share files with external users?</summary>

Yes. You can share files with anyone, even outside your organization, by generating a link. No account is required for accessing the file. Link sharing can be disabled if needed.

</details>

<details>
<summary>Does it support federated sharing between different instances?</summary>

Yes, federated sharing is possible via Open Cloud Mesh (OCM). This feature allows you to securely share files and collaborate across different instances, even if they are hosted by different organizations.

For example, a company with multiple branches in different regions could use OCM to share files between instances, enabling collaboration across teams while maintaining control over local data.

</details>

<details>
<summary>Are there limits on the number of users or size of files shared?</summary>

No.

</details>

## Data Management

<details>
<summary>Where is my data stored, and can I choose the storage location?</summary>

OpenCloud is a fully self-hosted (on-premise) solution, meaning you have complete control over where your data is stored. You can choose the server and country where OpenCloud will be installed. Unlike SaaS services like Google Drive or Microsoft OneDrive, which store your files on their servers, OpenCloud gives you full control over your data, ensuring privacy and security on your terms.

</details>

<details>
<summary>Does it support integration with third-party storage solutions like S3 Storage?</summary>

Yes, the following storage can be used:

- Posix Storage
- S3ng
- Ceph

</details>

## Support and Community

<details>
<summary>How often is OpenCloud updated, and how are updates delivered?</summary>

Download updates on download.opencloud.eu or via docker hub.

OpenCloud is released in three different release types: Production, Rolling and Daily. Each of them is targeted to a specific use case and audience group.

</details>

## Migration

<details>
<summary>Can I migrate from ownCloud or Nextcloud?</summary>

Yes, there will be a migration available in 2025.

</details>

## Compliance and Legal

<details>
<summary>Is OpenCloud compliant with GDPR (DSGVO) or HIPAA?</summary>

Yes, of course!

</details>

<details>
<summary>Is the OpenCloud Web UI accessible according to EN 301 549 / WCAG / BITV 2.0?</summary>

Yes, the OpenCloud Web UI is accessible according to EN 301 549, WCAG, and BITV 2.0. We believe that accessibility is important for everyone, not just for individuals with disabilities, as it benefits all users at some point in their lives.

As we release new features every 3 weeks, we ensure that accessibility is integrated into the feature development lifecycle. While we strive to maintain high accessibility standards, we’re only human and occasional mistakes may happen. If a new feature unintentionally impacts accessibility, we treat it as a bug and address it in the next release.

If you encounter any accessibility violations, please let us know so we can promptly resolve the issue.

</details>

<details>
<summary>Can access controls and permissions be configured to meet regulatory requirements?</summary>

Yes, OpenCloud offers robust access control and permission settings that can be fully configured to meet various regulatory requirements. You can define user roles, assign specific permissions, and set up granular access controls to ensure compliance with industry standards and regulations such as GDPR, HIPAA, and others. With OpenCloud, you have the flexibility to control who accesses your data, what actions they can perform, and how data is shared, ensuring that your system remains secure and compliant with the required regulations.

</details>

<details>
<summary>How does it handle requests for data access or deletion under GDPR?</summary>

OpenCloud provides users with the ability to trigger a GDPR Export in a self-service manner. This export generates a detailed report of all personal data stored in the context of OpenCloud, excluding the user’s own files. The report includes relevant data related to the user’s account and activity within the system, ensuring transparency and compliance with GDPR requirements. For the deletion of personal files, users have full control to manage and remove their own data as needed.

</details>

## Miscellaneous

<details>
<summary>Does OpenCloud offer multi-language support?</summary>

Yes, OpenCloud fully maintains both English and German languages. Additionally, the web UI offers support for other languages, which are listed below. Please note that these languages are not 100% translated and are maintained by the community on a best-effort basis. We appreciate the contributions from our community to help improve the language support over time.

Community maintained languages:

- Albanian
- Afrikaans
- Arabic
- Bosnian
- Bulgarian
- Chinese
- Croatian
- Czech
- Estonian
- French
- Galician
- Georgian
- Greek
- Hebrew
- Indonesian
- Italian
- Japanese
- Korean
- Dutch
- Polish
- Portuguese
- Romanian
- Russian
- Serbian
- Sinhala
- Slovak
- Spanish
- Swedish
- Turkish
- Ukrainian

</details>
