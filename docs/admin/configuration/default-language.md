---
sidebar_position: 100
id: default-language
title: Default Language
description: Set the default language
draft: false
---

# Set the default language

The system default language applies when a user has not selected an individual language. It is used by the WebUI and services such as notifications and userlog, and can determine the language of notification and invitation emails. If no system default is configured, OpenCloud uses English (`en`).

Users can select their preferred language in the WebUI under Account > Language. This individual preference takes precedence over the system default.

OpenCloud uses ISO 639-1 language codes. See [Supported languages](../resources/faq#miscellaneous) for the available languages. If a requested locale includes a territory and no matching translation is available, OpenCloud first tries the base language. If a translation for a user's preferred language is unavailable, OpenCloud falls back to the configured system default and then to English. Without a configured system default, it falls back directly to English. For details, see the [settings service translation rules](../../dev/server/services/settings/information#translation-rules).

## Edit the `.env` File

Open the environment configuration file located in your `opencloud-compose` directory:

```bash
nano opencloud-compose/.env
```

In `opencloud-compose`, `DEFAULT_LANGUAGE` maps to `OC_DEFAULT_LANGUAGE` inside the OpenCloud container. Set the system default to German, for example:

```env
DEFAULT_LANGUAGE=de
```

When configuring OpenCloud directly without `opencloud-compose`, set `OC_DEFAULT_LANGUAGE=de` instead.

## Restart Docker Services

After saving the file, shut down and restart the Docker containers to apply the changes:

```bash
docker compose down
docker compose up -d
```

## Result

The configured language is now the system default. It applies to users without an individual language preference and to services that use the default language. A user's language selected under Account > Language takes precedence. If translations are unavailable or incomplete, OpenCloud applies the fallback behavior described above, so some text can appear in English.
