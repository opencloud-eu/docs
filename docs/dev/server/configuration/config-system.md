---
title: Configuration System
sidebar_position: 2
slug: /dev/server/configuration/config-system
---

The Opencloud configuration system is designed for cloud‑native deployments and follows the 12‑Factor App principles. It provides a predictable override pattern, clear configuration locations, and a consistent approach across all services.

- Cloud‑native: configuration is externalized from code and deployable via files, ConfigMaps/Secrets, or environment variables.
- 12‑Factor friendly: environment variables are first‑class citizens; immutable images with runtime configuration injected at deploy time.
- Composable: a global base config can be refined by per‑service files and finally overridden by environment variables.

## Defaults

The Opencloud services come with sensible default settings for most configuration options. These defaults are configured within each service and are listed in the service documentation for each individual service.

:::tip
Default values for all configuration options are built into each service. You only need to provide values for settings that differ from the defaults.
:::

### Configuration locations

- Containers (default): `/etc/opencloud`
  - Mount this directory into containers (Docker, Kubernetes) via ConfigMaps/Secrets or volumes.
- Binary releases and local installs: `$HOME/.opencloud/config/`
  - Useful when running downloaded binaries on developer laptops or bare hosts without container mounts.
- The location for the configuration files can be changed by setting the environment variable `OC_CONFIG_PATH` to point to a different directory.
- Typical files inside either location:
  - `opencloud.yaml` — global defaults shared by all services
  - `<service-name>.yaml` — overrides specific to a service (e.g. `activitylog.yaml`, `proxy.yaml`)

### Override pattern (precedence)

From lowest to highest precedence:

1. `opencloud.yaml` (global defaults)
2. `<service-name>.yaml` (service‑specific overrides)
3. Environment variables (highest precedence)

Environment variables always win over file values. If a key is not set at a higher level, it falls back to the next level down.

### Config via YAML files

- YAML is used for both the global file and per‑service files.
- Keep keys lowercase with hyphens or underscores, matching service documentation.
- Secrets should be provided via environment variables or secret mounts rather than committed files.
- Simple bash substitution is supported. E.g. `https://${COLLABORA_DOMAIN|collabora.opencloud.test}/` will use the value of `COLLABORA_DOMAIN` env var or default to `collabora.opencloud.test` if not set.

#### Bash substitution syntax

| **Expression**     | **Meaning**                                                          |
| ------------------ | -------------------------------------------------------------------- |
| `${var}`           | Value of var (same as `$var`)                                        |
| `${var-$DEFAULT}`  | If var not set, evaluate expression as $DEFAULT                      |
| `${var:-$DEFAULT}` | If var not set or is empty, evaluate expression as $DEFAULT          |
| `${var=$DEFAULT}`  | If var not set, evaluate expression as $DEFAULT                      |
| `${var:=$DEFAULT}` | If var not set or is empty, evaluate expression as $DEFAULT          |
| `${var+$OTHER}`    | If var set, evaluate expression as $OTHER, otherwise as empty string |
| `${var:+$OTHER}`   | If var set, evaluate expression as $OTHER, otherwise as empty string |
| `$$var`            | Escape expressions. Result will be `$var`.                           |

#### Example: `opencloud.yaml`

```yaml
# /etc/opencloud/opencloud.yaml
# Global OpenCloud configuration defaults
token_manager:
  jwt_secret: 'x8Kz$3vQw9!Rb7#NfU2^BgT%Lp1@Hm0'
machine_auth_api_key: 'X7gH2k9Vb4q!S6dP'
system_user_api_key: 'mS9#cR4pZx7%aL1t'
transfer_secret: 'Tq6!vB2^nY8@wF5z'
url_signing_secret: 'U9p$R0e!K3#sH7cQ'
system_user_id: d3b1f5a2-7c9d-4e2f-a1b2-3c4d5e6f7a8b
admin_user_id: a1f2e3d4-5b6c-7d8e-9f01-23456789abcd
## Service-specific configurations, same as in <service-name>.yaml files
graph:
  application:
    id: a72387e1-fb22-49c9-9c94-12ff0abf9b38
  events:
    tls_insecure: true
  spaces:
    insecure: true
```

#### Example: `proxy.yaml`

```yaml
# /etc/opencloud/proxy.yaml
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

### Environment variables

- Global scope: variables prefixed with `OC_` apply to more than one service (shared/global settings).
- Service scope: variables prefixed with `<SERVICENAME>_` apply only to that specific service (e.g. `ACTIVITYLOG_`, `PROXY_`, `FRONTEND_`).
- When both are present for the same setting, the service‑scoped variable wins for that service.
- Booleans: `true`/`false` (case‑insensitive).
- Numbers: plain integers/floats.
- Lists: comma‑separated values unless otherwise specified by the service.

Examples:

```bash
# Raise log level globally for all services
export OC_LOG_LEVEL=debug

# Override only the Proxy service log level
export PROXY_LOG_LEVEL=info

# Make public shares not require a password globally
export OC_SHARING_PUBLIC_SHARE_MUST_HAVE_PASSWORD=false
```

Environment variables take precedence over both `opencloud.yaml` and `<service-name>.yaml`. See the list of [global variables](./global-environment-variables)

### More information

- [Global environment variable reference](./global-environment-variables)
- Individual service pages for service‑specific options and examples (e.g. [Activity Log](/docs/dev/server/services/activitylog), [Proxy](/docs/dev/server/services/proxy), [Frontend](/docs/dev/server/services/frontend)).
