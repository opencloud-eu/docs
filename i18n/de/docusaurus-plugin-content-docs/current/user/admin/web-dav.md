---
sidebar_position: 30
id: web-dav
title: WebDAV
description: Über WebDAV mit einem Space verbinden
draft: false
---

# Über WebDAV mit einem Space verbinden

Mit WebDAV können Sie OpenCloud-Spaces und -Ordner als Netzlaufwerke auf Ihrem Gerät einbinden und Ihre Dateien ohne Browser direkt über den Dateimanager verwalten.

## Voraussetzungen

- Ein gültiges OpenCloud-Konto mit aktivierter WebDAV-Information in den Einstellungen
- Zugriff auf eine Ressource in OpenCloud, entweder einen Space, einen Ordner oder das Stammverzeichnis Ihres Kontos
- Ein WebDAV-Client, beispielsweise die integrierte Unterstützung Ihres Betriebssystems oder [Mountain Duck](https://mountainduck.io/)
- Falls Ihr WebDAV-Client dies erfordert, ein App-Token
  → [So erstellen Sie ein App-Token](./app-tokens)

## Schritt-für-Schritt-Anleitung

### WebDAV-Informationen in der Oberfläche aktivieren

So zeigen Sie die WebDAV-Informationen für einen Space an:

- Öffnen Sie das Kontomenü und wählen Sie „Konto verwalten“.
- Öffnen Sie „Einstellungen“.
- Aktivieren Sie unter „Ansichtsoptionen“ die Option „WebDAV-Informationen anzeigen“.

  <img src={require("./img/webdav/preferences.png").default} alt="WebDAV-Info aktivieren" width="1920"/>

### WebDAV-URL abrufen

Öffnen Sie in der OpenCloud-Weboberfläche das Info-Panel des Spaces, Ordners oder Konto-Stammverzeichnisses, auf das Sie zugreifen möchten.

In der Detail-Seitenleiste werden der WebDAV-Pfad und die vollständige WebDAV-URL angezeigt. Verwenden Sie die Schaltfläche zum Kopieren neben der WebDAV-URL. Sie sieht beispielsweise so aus:

`https://cloud.example.com/remote.php/dav/spaces/12345678-abcd-efgh-ijkl-987654321000/`

<img src={require("./img/webdav/webdav-url.png").default} alt="WebDAV-URL" width="1920"/>

### Verbindung über WebDAV herstellen

Verbinden Sie nun Ihr Gerät über die WebDAV-URL:

- Benutzername: Ihr OpenCloud-Benutzername
- Passwort: ein App-Token oder Ihr OpenCloud-Passwort, falls die Passwortauthentifizierung in Ihrer Bereitstellung aktiviert ist

Je nach Betriebssystem können Sie unterschiedliche Clients verwenden:

## Windows

- Öffnen Sie den Datei-Explorer.
- Klicken Sie auf „Dieser PC“ und wählen Sie „Netzlaufwerk verbinden“.
- Geben Sie die WebDAV-URL ein.
- Authentifizieren Sie sich mit Ihrem Benutzernamen und Passwort oder App-Token.

## macOS

- Wählen Sie im Finder „Gehe zu“ > „Mit Server verbinden …“.
- Geben Sie die WebDAV-URL ein.
- Melden Sie sich mit Ihren Anmeldedaten oder Ihrem App-Token an.

## Linux

- Verwenden Sie die Funktion „Mit Server verbinden“ Ihres Dateimanagers.
- Verwenden Sie für die URL das folgende Format:
  `davs://cloud.example.com/remote.php/dav/spaces/<SPACE-ID>/`

:::note
Nach der Verbindungsherstellung verhält sich Ihr Space wie ein normaler Ordner.

- Wenn Ihr Client OIDC unterstützt, benötigen Sie möglicherweise kein App-Token.
- Verwenden Sie `https://`, um einen sicheren Zugriff zu gewährleisten.

:::
