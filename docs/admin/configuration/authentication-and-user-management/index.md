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
