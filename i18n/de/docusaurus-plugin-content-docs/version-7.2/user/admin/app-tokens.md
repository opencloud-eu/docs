---
sidebar_position: 2
id: app-tokens
title: App Tokens
description: App Tokens in OpenCLoud
draft: false
---

# App-Tokens

App-Tokens ermöglichen es Ihnen, externe Apps und Dienste (z. B. WebDAV-Clients) zu verbinden, ohne Ihr Hauptpasswort zu verwenden.

Dies verbessert die Sicherheit auf mehrere Arten:

- Ihr Login-Passwort muss nicht an Drittanbieter-Anwendungen weitergegeben werden.
- App-Tokens können widerrufen werden. Wenn Sie befürchten, dass ein Token kompromittiert wurde, löschen Sie es einfach.
- App-Tokens können ein Ablaufdatum haben. Das reduziert potenzielle Angriffsflächen.

Zusätzlich zur erhöhten Sicherheit verbessern App-Tokens auch die Kompatibilität mit Drittanbieter-Anwendungen. Viele
Anwendungen unterstützen moderne Login-Verfahren wie OpenID Connect nicht und akzeptieren nur Standard-Logins mit Benutzername
und Passwort. Ihr Benutzername in Kombination mit einem App-Token dient genau diesem Zweck.

:::important
App-Tokens ermöglichen Drittanbieter-Anwendungen Zugriff auf all Ihre Daten. Erstellen Sie daher
für jede Anwendung ein eigenes App-Token und wählen Sie ein angemessenes Ablaufdatum.  
Wenn Sie keinen vollständigen Zugriff gewähren möchten, verwenden Sie stattdessen einen öffentlichen Link.
:::

## App-Token erstellen

- Gehen Sie in Ihren OpenCloud-Kontoeinstellungen zum Bereich „App-Tokens“.
- Klicken Sie auf „+ Neu“, um ein neues Token zu erstellen.

  <img src={require("./img/app-tokens/create.png").default} alt="Create App Token" width="400"/>

- Geben Sie einen Namen für das Token ein (z. B. „WebDAV Client“).
- Wählen Sie ein Ablaufdatum, um die Sicherheit zu erhöhen.
- Klicken Sie auf „Bestätigen“.

  <img src={require("./img/app-tokens/enter-name.png").default} alt="Namen eingeben und Ablaufdatum wählen" width="400"/>

## App-Token kopieren

- Nach der Erstellung wird das Token nur ein einziges Mal angezeigt.
- Kopieren Sie es sofort und bewahren Sie es sicher auf.

  <img src={require("./img/app-tokens/copy-token.png").default} alt="Copy Token" width="400"/>

:::note
Wenn Sie das Token verlieren, müssen Sie es löschen und ein neues erstellen.
:::

## App-Token verwenden

Sie können das Token nun anstelle Ihres Passworts verwenden, zum Beispiel bei:

- WebDAV
- Externen Apps
- Drittanbieter-Diensten

:::info
Der Benutzername entspricht in der Regel dem Benutzernamen Ihres regulären Logins.  
Wenn der Identity Provider jedoch im Autoprovisioning-Modus läuft, kann nur die UUID verwendet werden.  
Diese finden Sie in der Übersicht der Einstellungen.
:::

## App-Token löschen

Wenn ein Token nicht mehr benötigt wird:

- Gehen Sie erneut zum Bereich „App-Tokens“.
- Klicken Sie auf das Papierkorb-Symbol neben dem entsprechenden Token, um es zu entfernen.

So stellen Sie sicher, dass ungenutzte Tokens nicht missbraucht werden können.
