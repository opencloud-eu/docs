---
title: 'Authentication and Identity Management'
---

# Authentication and Identity Management

OpenCloud employs a dual-track authentication strategy:

1. **Built-in IDP (Identity Provider)**: 
   - Based on LibreGraph Connect (lico)
   - Targeted at smaller installations (up to 500 users)
   - Designed for standalone or small deployments

2. **External Identity Providers**:
   - Keycloak as the recommended OIDC provider for larger installations
   - Support for Azure AD, EntraID, ADFS through Keycloak
   - Enterprise-focused solution

## Authentication with Keycloak

For production environments, we recommend using Keycloak with LDAP integration. This setup provides a robust authentication system that can scale to enterprise needs.

OpenCloud now supports two authentication modes when using Keycloak with LDAP:

### Shared User Directory Mode

In this mode, LDAP serves as a central user directory for both Keycloak and OpenCloud.
This setup is suitable for scenarios where the LDAP server is not under the control of the OpenCloud admin and can be connected to KeyCloak and OpenCloud using standard attributes and a read-only bind user.

For detailed configuration and setup instructions, see the [Keycloak Shared User Directory](./keycloak-existing-users#shared-user-directory-mode) guide.

### Autoprovisioning Mode

In this mode, Keycloak is holding all users and OpenCloud autoprovisions new users during first login.
This mode is suitable in scenarios where the OpenIDConnect provider is external and not under control of the OpenCloud admin. To mitigate that lack of control, OpenCloud will use an LDAP server which is fully under the control of the OpenCloud admin to store the users and groups and additional attributes.
OpenCloud can disable users for login to actively prevent unwanted access to the system when the workflow with the external Identity Provider is slow or indirect. In this case, the LDAP server needs an OpenCloud Schema and write access for the LDAP bind user.

For detailed configuration and setup instructions, see the [Keycloak with Autoprovisioning](./keycloak-existing-users#autoprovisioning-mode) guide.
