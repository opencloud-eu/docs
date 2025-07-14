---
id: opencloud-security
title: Security in OpenCloud
sidebar_position: 3
description: "Overview of OpenCloud's security architecture, encryption, access control, and compliance."
---

# 🔐 OpenCloud Security Overview

OpenCloud was designed with a strong focus on **security**, **data protection**, and **modern IT architecture**. This page outlines the key security mechanisms that make OpenCloud a secure and reliable solution for organizations of all sizes.

---

## 1. Encryption

OpenCloud protects your data both in transit and at rest using industry-standard encryption technologies:

- **Transport Layer Security (TLS)**  
  All data transmitted between clients and servers is encrypted using **TLS**, ensuring secure communication and protection from man-in-the-middle attacks.

- **Server-Side Encryption (S3 SSE)**  
  When using S3-compatible storage, OpenCloud supports **S3 Server-Side Encryption** to secure data directly at the storage layer.

- **Client-Side (End-to-End) Encryption**  
  OpenCloud leverages the **OS-native encryption capabilities** on user devices, providing local encryption before data is uploaded.

---

## 2. Access Control & Authentication

OpenCloud includes robust mechanisms for authentication and access management:

- **Role-Based Access Control (RBAC)**  
  Fine-grained permissions based on **roles** ensure users have access only to what they need.

- **Multi-Factor Authentication (MFA)**  
  Enhance account security with optional **two-factor authentication**.

- **Single Sign-On (SSO) Integration**  
  OpenCloud supports seamless SSO via:
  - **LDAP**
  - **SAML**
  - **OAuth 2.0**

---

## 3. Auditing & Logging

- **Audit Trails**  
  Every security-relevant action is logged for compliance and traceability.

- **Monitoring APIs**  
  Expose detailed logs to integrate with existing monitoring and SIEM systems.

---

## 4. File Protection & Antivirus

OpenCloud provides integrated protection against threats and data leaks:

- **File Firewall**  
  Prevent uploads of unwanted file types using **allow/deny rules**.

- **Antivirus Integration**
  - **ClamAV (default)**: Detects malware in uploaded files.
  - **ICAP support**: Enables external antivirus scanners via **ICAP** protocol.

- **Data Loss Prevention (DLP)**
  - **Collabora Secure View** ensures files cannot be downloaded or copied — only opened securely in the browser.

---

## 5. Secure File Sharing

Sharing is powerful — and secure:

- **Enforced Passwords for Public Links**  
  Public links are always protected with passwords. Admins can define strict sharing policies.

- **FileDrop Uploads**  
  External users can upload files **without accessing internal data**.

- **Expiration for Shared Links**  
  Automatically remove access after a defined expiration date.

- **Granular Sharing Permissions**  
  Control actions on shared files: read-only, editing, upload permissions, and more.

---

## 6. Secure Architecture

Built with modern, security-first technologies:

- **No PHP**  
  Unlike traditional solutions, OpenCloud is written in **Go (Golang)** — fast, secure, and efficient.

- **Vue.js Frontend**  
  The web interface is built with **Vue.js**, a modern and secure JavaScript framework.

- **REST API**  
  A comprehensive **REST API** allows secure automation and integrations.

---

## 7. Data Protection & GDPR Compliance

OpenCloud fully supports **data protection regulations**, including:

- **GDPR-Compliant Data Export**  
  Every user can request a personal data export that meets GDPR standards.

---

## 8. Security Processes

OpenCloud has a clearly defined security policy:

- **Responsible Disclosure Process**  
  Security issues are handled via a responsible disclosure program.

- **Regular Penetration Testing**  
  Vulnerabilities are actively tested and remediated.

- **Fast Security Updates**  
  Thanks to container-based deployment, patches and updates are rolled out quickly.

- **[Security Policy](https://github.com/opencloud-eu/.github/blob/main/profile/SECURITY.md)**  
  Transparent and documented handling of vulnerabilities.

---

## Conclusion

OpenCloud combines **modern security architecture**, **advanced encryption**, and **enterprise-grade access control** with:

- Secure, microservices-based backend
- Vue.js-based frontend with modern web security
- Antivirus, DLP, and secure sharing controls
- GDPR-compliant data access and export
- Fast and secure containerized deployments

> OpenCloud is the right choice for teams and organizations that prioritize **data protection**, **compliance**, and **security by design**.
