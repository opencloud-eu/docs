---
title: 'Authentication and Identity Management'
---

# Authentication and Identity Management

OpenCloud offers two ways to handle user authentication:

1. **Built-in IDP (Identity Provider)**:
   - Based on LibreGraph Connect (Lico)
   - Targeted at smaller installations (up to 500 users)
   - Designed for standalone or small deployments

2. **External IDP**:
   - Keycloak as the recommended OIDC provider for larger installations
   - Support for Azure AD, EntraID, ADFS through Keycloak
   - Enterprise-focused solution

## Your Use Cases

### Choose Lico if you need:
- A simple, lightweight and minimal OpenID Connect Provider
- Small to medium deployments
- Minimal resource footprint
- Quick setup with basic features
- Ideal for development environment
- No Multifactor Authentication (MFA) and migration path to other IDPs

### Choose Keycloak if you need:
- Enterprise-grade IAM solution
- Complex authorization requirements
- Multifactor Authentication
- Advanced user federation
- Fine-grained permissions
- Multiple authentication methods
- Large-scale deployments
- Commercial support options

### Bottom Line

Keycloak is a comprehensive, enterprise-ready IAM platform with extensive features including SSO, user federation, and support for multiple protocols like OpenID Connect, OAuth 2.0, and SAML, while Lico is a lightweight OpenID Connect provider with integrated web login and consent forms, designed as a simpler alternative for smaller installations. Keycloak offers more features but requires more resources and expertise, while Lico provides a minimalist approach suitable for basic authentication needs.

## Authentication with Keycloak

For production environments, we recommend using Keycloak with LDAP integration. This setup provides a robust authentication system that can scale to enterprise needs.

OpenCloud now supports two authentication modes when using Keycloak with LDAP:

### Shared User Directory Mode

In this mode, LDAP serves as a central user directory for both Keycloak and OpenCloud.
This setup is suitable for scenarios where the LDAP server is not under the control of the OpenCloud admin and can be connected to KeyCloak and OpenCloud using standard attributes and a read-only bind user.

For detailed configuration and setup instructions, see the [Keycloak Shared User Directory](./keycloak#shared-user-directory-mode) guide.

### Autoprovisioning Mode

In this mode, Keycloak is holding all users and OpenCloud autoprovisions new users during first login.
This mode is suitable in scenarios where the OpenIDConnect provider is external and not under control of the OpenCloud admin. To mitigate that lack of control, OpenCloud will use an LDAP server which is fully under the control of the OpenCloud admin to store the users and groups and additional attributes.
OpenCloud can disable users for login to actively prevent unwanted access to the system when the workflow with the external Identity Provider is slow or indirect. In this case, the LDAP server needs an OpenCloud Schema and write access for the LDAP bind user.

For detailed configuration and setup instructions, see the [Keycloak with Autoprovisioning](./keycloak#autoprovisioning-mode) guide.
