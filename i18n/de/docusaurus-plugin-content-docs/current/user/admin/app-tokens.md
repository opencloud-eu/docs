---
sidebar_position: 20
id: app-tokens
title: App Tokens
description: App-Tokens in OpenCloud
draft: false
---

# App-Tokens

App-Tokens ermöglichen es Ihnen, externe Apps und Dienste (z. B. WebDAV-Clients) zu verbinden, ohne Ihr Hauptpasswort zu verwenden.

Dies verbessert die Sicherheit auf mehrere Arten:

- Sie müssen Ihr Anmeldepasswort nicht gegenüber Drittanbieter-Anwendungen offenlegen.
- App-Tokens können widerrufen werden. Wenn Sie vermuten, dass ein Token kompromittiert wurde, löschen Sie es einfach.
- App-Tokens haben ein konfigurierbares Ablaufdatum. Dadurch verringert sich das Missbrauchsrisiko.

Zusätzlich zur erhöhten Sicherheit verbessern App-Tokens die Kompatibilität mit Drittanbieter-Anwendungen. Viele Anwendungen unterstützen moderne Anmeldeverfahren wie OpenID Connect nicht, sondern akzeptieren nur eine Standardanmeldung mit Benutzername und Passwort. Ihr Benutzername und eines Ihrer App-Tokens dienen dabei als Anmeldedaten.

:::important
App-Tokens ermöglichen Drittanbieter-Anwendungen den Zugriff auf all Ihre Daten. Erstellen Sie für jede Anwendung ein eigenes App-Token und wählen Sie einen angemessenen Gültigkeitszeitraum. Wenn Sie nicht den Zugriff auf all Ihre Daten ermöglichen möchten, verwenden Sie stattdessen einen öffentlichen Link.
:::

## App-Token erstellen

- Gehen Sie in Ihren OpenCloud-Kontoeinstellungen zum Bereich „App-Tokens“.
- Klicken Sie auf „Neu“, um ein Token zu erstellen.

  <img src={require("./img/app-tokens/create.png").default} alt="App-Token erstellen" width="1920"/>

- Geben Sie einen Namen für das Token ein, beispielsweise `WebDAV Client`.
- Wählen Sie ein Ablaufdatum, um die Sicherheit zu erhöhen.
- Klicken Sie auf „Bestätigen“.

  <img src={require("./img/app-tokens/enter-name.png").default} alt="Name und Ablaufdatum eingeben" width="1920"/>

## App-Token kopieren

- Nach der Erstellung wird das Token nur ein einziges Mal angezeigt.
- Kopieren Sie es sofort und bewahren Sie es sicher auf.

  <img src={require("./img/app-tokens/copy-token.png").default} alt="App-Token kopieren" width="1920"/>

:::note
Wenn Sie das Token verlieren, müssen Sie es löschen und ein neues erstellen.
:::

## App-Token verwenden

Sie können das Token nun anstelle Ihres Passworts für folgende Verbindungen verwenden:

- WebDAV
- externe Apps
- Drittanbieter-Dienste

:::info
Der Benutzername entspricht in der Regel dem Benutzernamen, den Sie für Ihre reguläre Anmeldung verwenden.
Wenn der Identity Provider jedoch im Autoprovisioning-Modus betrieben wird, kann nur die UUID verwendet werden.
Sie finden diese UUID auf der Übersichtsseite der Einstellungen.
:::

## App-Token löschen

Wenn ein Token nicht mehr benötigt wird:

- Gehen Sie erneut zum Bereich „App-Tokens“.
- Klicken Sie neben dem zu entfernenden Token auf die Schaltfläche „Löschen“.

  <img src={require("./img/app-tokens/delete-token.png").default} alt="App-Token löschen" width="1920"/>

Dadurch wird verhindert, dass ungenutzte Tokens missbraucht werden können.
