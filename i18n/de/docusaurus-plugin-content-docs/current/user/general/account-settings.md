---
sidebar_position: 20
id: settings
title: Kontoeinstellungen
description: Verwalten Sie Ihr Profil, Ihre Einstellungen, Apps und den Kontozugriff in OpenCloud.
draft: false
---

# Kontoeinstellungen verwalten

In den Kontoeinstellungen verwalten Sie Ihr Profil, Ihre Einstellungen, Apps, den Kalenderzugriff, Ihre persönlichen Daten und App-Tokens.

## Auf die Einstellungen zugreifen

1. Wählen Sie oben rechts Ihren Avatar aus.
2. Wählen Sie „Einstellungen“.

<img src={require("./img/account-settings/access.png").default} alt="Einstellungen öffnen" width="400" style={{ display: "block", marginTop: "1rem", marginBottom: "1rem" }}/>

## Kontoinformationen

Die Kontoeinstellungen sind in mehrere Bereiche unterteilt.

### Profil

- Profilbild
- Anmeldename
- Vor- und Nachname
- E-Mail-Adresse
- Persönlicher Speicherplatz
- Gruppenzugehörigkeiten

<img src={require("./img/account-settings/account-information.png").default} alt="Kontoinformationen" width="1920"/>

### Avatar

So ändern Sie Ihren Avatar:

1. Wählen Sie unter Ihrem aktuellen Avatar „Hochladen“.

<img src={require("./img/account-settings/avatar-menu.png").default} alt="Avatar-Menü" width="400" style={{ display: "block", marginTop: "1rem", marginBottom: "1rem" }}/>

2. Wählen Sie ein Bild aus und klicken Sie auf „Hochladen“.

<img src={require("./img/account-settings/avatar-upload.png").default} alt="Avatar hochladen" width="500"/>

3. Passen Sie das Bild in der Vorschau an und wählen Sie „Festlegen“.

<img src={require("./img/account-settings/avatar-settings.png").default} alt="Avatar-Einstellungen" width="400" style={{ display: "block", marginTop: "1rem", marginBottom: "1rem" }}/>

Der neue Avatar wird nun für Ihr Konto angezeigt.

<img src={require("./img/account-settings/visible-avatar.png").default} alt="Sichtbarer Avatar" width="1920"/>

## Einstellungen

Die verfügbaren Einstellungen hängen von der Konfiguration Ihrer OpenCloud-Instanz ab.

- Sprache:  
  Wählen Sie die Sprache der OpenCloud-Benutzeroberfläche aus.
- Passwort:  
  Ändern Sie das Passwort für Ihr Konto, sofern Ihr Authentifizierungsanbieter Passwortänderungen unterstützt.
- Design:
  Wählen Sie das helle, dunkle oder Systemdesign aus.
- Anzeigeoptionen:  
  Legen Sie fest, ob WebDAV-Informationen in den Dateidetails angezeigt werden.
- Benachrichtigungen:
  Legen Sie für jedes unterstützte Ereignis fest, ob Sie eine Benachrichtigung in der App, per E-Mail, über beide Wege oder gar nicht erhalten möchten.

<img src={require("./img/account-settings/preferences.png").default} alt="Einstellungen" width="1920"/>

## Apps

Unter „Apps“ können Sie Einstellungen installierter Apps konfigurieren, beispielsweise die globale Fortschrittsanzeige, sofern verfügbar.

<img src={require("./img/account-settings/extensions.png").default} alt="App-Einstellungen" width="1920"/>

## Kalender

Unter „Kalender“ können Sie auf Ihren persönlichen Kalender zugreifen, um ihn mit Drittanbieter-Apps wie Thunderbird, Apple Kalender und anderen zu verbinden, sofern diese Funktion konfiguriert ist.

<img src={require("./img/account-settings/calendar.png").default} alt="Kalender" width="1920"/>

## DSGVO

Unter „DSGVO“ können Sie einen Export Ihrer personenbezogenen Daten anfordern.

<img src={require("./img/account-settings/gdpr.png").default} alt="DSGVO" width="1920"/>

## App-Tokens

Mit App-Tokens können Sie externe Apps und Dienste, beispielsweise WebDAV-Clients, sicher verbinden, ohne Ihr Hauptpasswort zu verwenden.

<img src={require("./img/account-settings/app-tokens.png").default} alt="App-Tokens" width="1920"/>
