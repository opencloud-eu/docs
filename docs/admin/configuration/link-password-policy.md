---
sidebar_position: 90
id: link-password-policy
title: Public link password policy
description: Configure the requirements for passwords for public links
draft: false
---

# Configure the requirements for passwords for public links

OpenCloud can enforce strong(er) passwords by requiring occurrences of characters across different classes. It is possible to individually configure the number of

- lower-case characters
- upper-case characters
- digits
- special characters

that have to appear in a valid password.

Here is how to configure the policy:

## Edit the `.env` File

Open the environment configuration file located in your `opencloud-compose` directory:

```bash
nano opencloud-compose/.env
```

Modify the following environment variables to reflect your desired policy:

```env
OC_PASSWORD_POLICY_DISABLED=true # Disable the password policy
OC_PASSWORD_POLICY_MIN_CHARACTERS=8 # Define the minimum password length.
OC_PASSWORD_POLICY_MIN_LOWERCASE_CHARACTERS=1 # Define the minimum number of uppercase letters.
OC_PASSWORD_POLICY_MIN_UPPERCASE_CHARACTERS=1 # Define the minimum number of lowercase letters.
OC_PASSWORD_POLICY_MIN_DIGITS=1 # Define the minimum number of digits.
OC_PASSWORD_POLICY_MIN_SPECIAL_CHARACTERS=1 # Define the minimum number of special characters.
OC_PASSWORD_POLICY_BANNED_PASSWORDS_LIST="" # Path to the 'banned passwords list' file.
```

## Restart Docker Services

After saving the file, shut down and restart the Docker containers to apply the changes:

```bash
docker compose down
docker compose up -d
```

:::note
This change applies globally to all public shares created after the restart.
:::

:::info
More information is available in the [developer documentation on password policy](../../dev/server/services/frontend/info.mdx#the-password-policy).
:::
