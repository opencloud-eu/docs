---
sidebar_position: 1
id: external-idp
title: External OpenID Connect Identity Provider
description: Integrating external OpenID Connect Identity Providers
draft: false
---

# Integrating external OpenID Connect Identity Providers

The following environment variables are relevant when connecting OpenCloud to an external IDP

## OpenCloud Configuration

- `OC_OIDC_ISSUER`: Set this to the issuer URL of the external Identity Provider
- `OC_EXCLUDE_RUN_SERVICES`: To disable the built-in Identity Provider set this to `idp`
- `PROXY_OIDC_REWRITE_WELLKNOWN`: Set this to `true` to expose the Identity
  Providers `.well-known/openid-configuration` via the OpenCloud base url. This
  help the oidc client, that do not yet support discovery via webfinger to
  locate the Identity Provider's configuration.
- `PROXY_USER_OIDC_CLAIM` and `PROXY_USER_CS3_CLAIM`: These two variables
  configure how the users mapped between the Identity Provider and OpenCloud.
  `PROXY_USER_OIDC_CLAIM` defines the OIDC claim that OpenCloud uses to
  uniquely identify a user. It is matched against the OpenCloud user attribute
  defined in `PROXY_USER_CS3_CLAIM`. E.g. if `PROXY_USER_OIDC_CLAIM` is set to
  `preferred_username` and `PROXY_USER_CS3_CLAIM` is set to `username` then an
  OpenID Connect user, that has the `preferred_username` set to `alan` will map
  to the OpenCloud user with username `alan`.
- `PROXY_AUTOPROVISION_ACCOUNTS` and `GRAPH_USERNAME_MATCH`: When
  `PROXY_AUTOPROVISION_ACCOUNTS` is set to `true`, OpenCloud will create a new
  user account in the LDAP Database for every user who logs in via OpenID
  Connect for the first time. Enabling this requires access to a writable LDAP
  server. For smaller setups this can be the built-in LDAP server provided by
  the `idm` service. If set to `false` all users logging in must already be
  existing in the LDAP server. (The mapping between the OIDC and LDAP users
  happens based on the aforementioned `PROXY_USER_OIDC_CLAIM` and
  `PROXY_USER_CS3_CLAIM` settings. Set `GRAPH_USERNAME_MATCH` to `none` when
  `PROXY_AUTOPROVISION_ACCOUNTS` is set to `true` to disable OpenCloud's
  default restrictions on allowed characters in usernames.
- `PROXY_ROLE_ASSIGNMENT_DRIVER` and `GRAPH_ASSIGN_DEFAULT_USER_ROLE`: For
  details see below

### Automatic Role Assignments

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
      - role_name: guest
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
- role_name: guest
  claim_value: opencloudGuest
```

:::note
When `PROXY_ROLE_ASSIGNMENT_DRIVER` is set to `oidc` it is recommended to set `GRAPH_ASSIGN_DEFAULT_USER_ROLE` to `false`.
:::

## Client Configuration

OpenCloud requires several OIDC clients to be configured in the Identity Provider.

### Web Client

The web client is used for browser-based access to OpenCloud:

- Client ID: `web`
- Client Type: Public client
- Redirect URIs:
  - `https://your-domain.example.com/`
  - `https://your-domain.example.com/oidc-callback.html`
  - `https://your-domain.example.com/oidc-silent-redirect.html`

### Desktop Client

The desktop client is used for the OpenCloud desktop application:

- Client ID: `OpenCloudDesktop`
- Client Type: Public client
- Redirect URIs:
  - `http://127.0.0.1`
  - `http://localhost`

### Mobile App Clients

#### Android App

- Client ID: `OpenCloudAndroid`
- Client Type: Public client
- Redirect URIs: `oc://android.opencloud.eu`
- Post Logout Redirect URIs: `oc://android.opencloud.eu`

#### iOS App

- Client ID: `OpenCloudIOS`
- Client Type: Public client
- Redirect URIs: `oc://ios.opencloud.eu`
- Post Logout Redirect URIs: `oc://ios.opencloud.eu`

### Additional Clients

#### Cyberduck File Transfer Client

- Client ID: `Cyberduck`
- Client Type: Public client
- Redirect URIs:
  - `x-cyberduck-action:oauth`
  - `x-mountainduck-action:oauth`
