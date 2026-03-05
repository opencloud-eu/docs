---
sidebar_position: 90
id: link-password-policy
title: Public Links - Password Enforcement and Configuration
description: Remove the password enforcement and configure the passwords requirements for public links
draft: false
---

# Public Links: Password Enforcement and Policy

OpenCloud provides two related controls for passwords on public links:

1. Password enforcement for public links (whether a password is required at all).
2. Password policy (how strong a password must be, if a password is used/required).

This guide shows how to configure both via `opencloud-compose/.env`.

## Configure Password Enforcement for Public Links

By default, OpenCloud requires a password for public shares. You can disable that requirement globally and (optionally) still require passwords for writable public links.

### Disable the password requirement for all public links

```env
OC_SHARING_PUBLIC_SHARE_MUST_HAVE_PASSWORD=false
```

Require a password for writable public links only

```env
OC_SHARING_PUBLIC_WRITEABLE_SHARE_MUST_HAVE_PASSWORD=true
```

This setting only applies when `OC_SHARING_PUBLIC_SHARE_MUST_HAVE_PASSWORD` is set to false.

## Configure Password Policy for Public Link Passwords

OpenCloud can enforce strong(er) passwords by requiring occurrences of characters across different classes. You can individually configure the minimum number of:

- lower-case characters

- upper-case characters

- digits

- special characters

that must appear in a valid password (and also set a minimum length).

Add or adjust these variables in your .env file:

### Enable/disable password policy checks

- true = policy disabled (no complexity requirements enforced)
- false = policy enabled (requirements below are enforced)

```env
OC_PASSWORD_POLICY_DISABLED=false
```

### Minimum password length

```env
OC_PASSWORD_POLICY_MIN_CHARACTERS=8
```

### Minimum character-class requirements

```env
OC_PASSWORD_POLICY_MIN_LOWERCASE_CHARACTERS=1
OC_PASSWORD_POLICY_MIN_UPPERCASE_CHARACTERS=1
OC_PASSWORD_POLICY_MIN_DIGITS=1
OC_PASSWORD_POLICY_MIN_SPECIAL_CHARACTERS=1
```

### Optional: Path to a 'banned passwords list' file

```env
OC_PASSWORD_POLICY_BANNED_PASSWORDS_LIST=""
```

The password policy only applies when a password is set/required for a public link.

More information is available in the [developer documentation on password policy](../../dev/server/services/frontend/information#passwords).

## Edit the .env File

Open the environment configuration file located in your opencloud-compose directory:

```bash
nano opencloud-compose/.env
```

Add or modify the variables from the sections above as needed, then save the file.

## Restart Docker Services

After saving the file, shut down and restart the Docker containers to apply the changes:

```bash
docker compose down
docker compose up -d
```

:::note
This change applies globally to all public shares created after the restart.
:::
