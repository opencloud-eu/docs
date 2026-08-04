---
sidebar_position: 100
id: default-language
title: Default Language
description: Set the default language
draft: false
---

# Set the default language

By default, OpenCloud uses English (en) as its interface language, unless a different language is explicitly configured.
OpenCloud relies on ISO 639-1 language codes for language selection.
You can find the complete list of supported languages here: [Supported languages](../resources/faq#miscellaneous)

## Edit the `.env` File

Open the environment configuration file located in your `opencloud-compose` directory:

```bash
nano opencloud-compose/.env
```

Configure the default language using the following environment variable:

```env
# The default language used by services and the WebUI.
# Uses ISO 639-1 language codes (e.g. "en", "de", "fr").
# Defaults to English if not set.
DEFAULT_LANGUAGE="language code"
```

## Restart Docker Services

After saving the file, shut down and restart the Docker containers to apply the changes:

```bash
docker compose down
docker compose up -d
```

## Result

OpenCloud is now fully displayed in the language configured in the .env file.
