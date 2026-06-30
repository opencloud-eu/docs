---
sidebar_position: 1
id: external-idp
title: External OpenID Connect Identity Provider
description: Integrating external OpenID Connect Identity Providers
draft: false
---

# Integrating external OpenID Connect Identity Providers

## Requirements

OpenCloud integrates with external OpenID Connect Identity Providers (IDPs).
The setup is opinionated, but the requirements below are provider-independent.
For a provider-specific example, see [Keycloak integration](./keycloak.md).

This is the list of minimal requirements that an IDP needs to fulfill in order
to work with OpenCloud:

- All clients provided by OpenCloud ([Web](https://github.com/opencloud-eu/web/),
  [Desktop](https://github.com/opencloud-eu/desktop/), [Android](https://github.com/opencloud-eu/android/)
  and [iOS](https://github.com/opencloud-eu/ios/)), are implemented as public clients using the
  authorization code flow with PKCE. Therefore the IDP needs to support this flow.
- All clients, except the Web client, use predefined client IDs. Therefore the IDP needs to
  be able to create clients with predefined IDs.
- OpenCloud provides client IDs and scopes for the Web, Desktop, Android, and iOS
  apps through the OpenCloud WebFinger service. Configure these values in the
  OpenCloud deployment so that clients can discover the correct OIDC settings.
- The IDP must return the claims required by OpenCloud in the access token or
  through the UserInfo endpoint. Configure scopes and claim mappings in the IDP
  accordingly.

## OpenCloud Configuration

The following environment variables are relevant when connecting OpenCloud to
an external IDP.

### Configure the OIDC issuer

```env
IDP_DOMAIN=idp.example.org
IDP_ISSUER_URL=https://idp.example.org/realms/openCloud
OC_OIDC_ISSUER=https://idp.example.org/realms/openCloud
```

Do not include the protocol in `IDP_DOMAIN`. Use `idp.example.org`, not
`https://idp.example.org`.

- `OC_OIDC_ISSUER`: Set this to the issuer URL of the external Identity Provider.
- `OC_EXCLUDE_RUN_SERVICES`: When using an external IDP, the built-in Identity
  Provider does not need to run. Add `idp` here to prevent the internal `idp`
  service from starting.
- `PROXY_OIDC_ACCESS_TOKEN_VERIFY_METHOD`: Set this to `jwt` so OpenCloud
  verifies access tokens as JWTs using the Identity Provider's published
  signing keys.
- `PROXY_OIDC_REWRITE_WELLKNOWN`: Set this to `true` to expose the Identity
  Provider's `.well-known/openid-configuration` endpoint via the OpenCloud base
  URLs.
- `PROXY_USER_OIDC_CLAIM` and `PROXY_USER_CS3_CLAIM`: These two variables
  configure how users are mapped between the Identity Provider and OpenCloud.
  `PROXY_USER_OIDC_CLAIM` defines the OIDC claim that OpenCloud uses to
  uniquely identify a user. It is matched against the OpenCloud user attribute
  defined in `PROXY_USER_CS3_CLAIM`. For example, if `PROXY_USER_OIDC_CLAIM`
  is set to `preferred_username` and `PROXY_USER_CS3_CLAIM` is set to
  `username`, then an OpenID Connect user with `preferred_username=alan` maps
  to the OpenCloud user with username `alan`.
- `PROXY_AUTOPROVISION_ACCOUNTS` and `GRAPH_USERNAME_MATCH`: When
  `PROXY_AUTOPROVISION_ACCOUNTS` is set to `true`, OpenCloud creates a new user
  account in the LDAP database for every user who logs in via OpenID Connect
  for the first time. This requires a writable LDAP server. For smaller setups,
  the built-in LDAP server provided by the `idm` service can be used. If set to
  `false`, users must already exist in LDAP.
- `PROXY_ROLE_ASSIGNMENT_DRIVER` and `GRAPH_ASSIGN_DEFAULT_USER_ROLE`: See the
  section below.

If you use Docker Compose with an external IDP, add `idm/external-idp.yml` to
`COMPOSE_FILE`.

### Configure client discovery with WebFinger

OpenCloud clients discover OIDC client settings through the OpenCloud WebFinger
service at `https://<opencloud-domain>/.well-known/webfinger`.

The WebFinger OIDC variables define which client ID and scopes are returned to
the different OpenCloud clients. They already ship with the following
defaults, so you only need to set them if your IDP requires different client
IDs or scopes:

```env
WEBFINGER_WEB_OIDC_CLIENT_ID=web
WEBFINGER_WEB_OIDC_CLIENT_SCOPES=openid profile email

WEBFINGER_ANDROID_OIDC_CLIENT_ID=OpenCloudAndroid
WEBFINGER_ANDROID_OIDC_CLIENT_SCOPES=openid profile email offline_access

WEBFINGER_IOS_OIDC_CLIENT_ID=OpenCloudIOS
WEBFINGER_IOS_OIDC_CLIENT_SCOPES=openid profile email offline_access

WEBFINGER_DESKTOP_OIDC_CLIENT_ID=OpenCloudDesktop
WEBFINGER_DESKTOP_OIDC_CLIENT_SCOPES=openid profile email offline_access
```

:::note

- Android and iOS clients use the WebFinger discovery mechanism.
- The Desktop Client does not fully support this discovery mechanism yet.
  Configure the Desktop Client WebFinger variables anyway so the setup is ready
  for client support and stays consistent.

  :::

### Automatic Role Assignments

:::note
Automatic role assignment requires the IDP to provide the configured role claim
in the access token or through the UserInfo endpoint. Make sure that the
configured scopes and claim mappings return this claim for OpenCloud clients.

If the IDP does not provide the required role claim, automatic role assignment
with the `oidc` driver will not work.
:::

When users login into OpenCloud, they get a user role assigned
automatically. The automatic role assignment can be configured in different
ways. The `PROXY_ROLE_ASSIGNMENT_DRIVER` environment variable (or the `driver`
setting in the `role_assignment` section of the configuration file) select which
mechanism to use for the automatic role assignment.

When set to `default`, all users which do not have a role assigned at the time
of first login will get the role 'user' assigned. This is also the
default behavior if `PROXY_ROLE_ASSIGNMENT_DRIVER` is unset.

When `PROXY_ROLE_ASSIGNMENT_DRIVER` is set to `oidc` the role assignment for a
user will happen based on the values of an OpenID Connect Claim of that user.
The name of the OpenID Connect Claim to be used for the role assignment can be
configured via the `PROXY_ROLE_ASSIGNMENT_OIDC_CLAIM` environment variable. It
is also possible to define a mapping of claim values to role names defined in
OpenCloud via a `yaml` configuration. See the following `proxy.yaml` snippet
for an example.

```yaml
role_assignment:
  driver: oidc
  oidc_role_mapper:
    role_claim: opencloudRoles
    role_mapping:
      - role_name: admin
        claim_value: myAdminRole
      - role_name: spaceadmin
        claim_value: mySpaceAdminRole
      - role_name: user
        claim_value: myUserRole
      - role_name: user-light
        claim_value: myGuestRole
```

This would assign the role `admin` to users with the value `myAdminRole` in the claim `opencloudRoles`.
The role `user` to users with the values `myUserRole` in the claims `opencloudRoles` and so on.

Claim values that are not mapped to a specific OpenCloud role will be ignored.

Note: An OpenCloud user can only have a single role assigned. If the configured
`role_mapping` and a user's claim values result in multiple possible roles for a user, the order in
which the role mappings are defined in the configuration is important. The first role in the
`role_mappings` where the `claim_value` matches a value from the user's roles claim will be assigned
to the user. So if e.g. a user's `opencloudRoles` claim has the values `myUserRole` and
`mySpaceAdminRole` that user will get the OpenCloud role `spaceadmin` assigned (because `spaceadmin`
appears before `user` in the above sample configuration).

If a user's claim values don't match any of the configured role mappings an error will be logged and
the user will not be able to login.

The default `role_claim` (or `PROXY_ROLE_ASSIGNMENT_OIDC_CLAIM`) is `roles`. The default `role_mapping` is:

```yaml
- role_name: admin
  claim_value: opencloudAdmin
- role_name: spaceadmin
  claim_value: opencloudSpaceAdmin
- role_name: user
  claim_value: opencloudUser
- role_name: user-light
  claim_value: opencloudGuest
```

:::note
When `PROXY_ROLE_ASSIGNMENT_DRIVER` is set to `oidc` it is recommended to set `GRAPH_ASSIGN_DEFAULT_USER_ROLE` to `false`.
:::
