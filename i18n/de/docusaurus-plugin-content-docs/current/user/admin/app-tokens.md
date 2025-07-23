---
sidebar_position: 2
id: app-tokens
title: App Tokens
description: App Tokens in OpenCLoud
draft: false
---

# App-Tokens

App-Tokens ermöglichen es dir, externe Apps und Dienste (z. B. WebDAV-Clients) sicher mit OpenCloud zu verbinden – ohne dein Hauptpasswort verwenden zu müssen.

## App-Token erstellen

- Gehe in deinen OpenCloud-Kontoeinstellungen zum Bereich „App-Tokens“.
- Klicke auf „+ Neu“, um ein neues Token zu erstellen.
- Gib dem Token einen Namen (z. B. „WebDAV-Client“).
- Wähle ein Ablaufdatum für zusätzliche Sicherheit.
- Klicke auf „Erstellen“.

  <img src={require("./img/app-tokens/create.png").default} alt="App-Token erstellen" width="400"/>

## App-Token kopieren

- Nach der Erstellung wird das Token nur einmal angezeigt.
- Kopiere es sofort und speichere es an einem sicheren Ort.

  <img src={require("./img/app-tokens/copy-token.png").default} alt="Token kopieren" width="400"/>

:::note
Wenn du das Token verlierst, musst du es löschen und ein neues erstellen.
:::

## App-Token verwenden

Du kannst das Token jetzt anstelle deines Passworts nutzen, z. B. für:

- WebDAV
- Externe Anwendungen
- Dienste von Drittanbietern

## App-Token löschen

Wenn ein Token nicht mehr benötigt wird:

- Gehe zurück in den Bereich „App-Tokens“.
- Klicke auf das Papierkorb-Symbol neben dem Token, um es zu entfernen.

So stellst du sicher, dass ungenutzte Tokens nicht missbraucht werden können.

:::note
Nutze App-Tokens für mehr Sicherheit und Kontrolle bei der Verbindung externer Dienste.
:::
