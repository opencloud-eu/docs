---
sidebar_position: 5
id: desktop-client-states
title: Desktop-Client Statussymbole
description: Die Statussymbole des Desktop-Clients verstehen
draft: false
---

# Die Statussymbole des Desktop-Clients verstehen

Der OpenCloud Desktop-Client verwendet verschiedene Symbole im Infobereich (System Tray), um den aktuellen Synchronisations- und Verbindungsstatus anzuzeigen. Anhand dieser Symbole können Sie schnell erkennen, ob die Synchronisierung ordnungsgemäß funktioniert oder ob Handlungsbedarf besteht.

## Schnellübersicht

| Symbol                                                                                                                               | Status                 | Bedeutung                                                         | Typische Aktion                                           |
| ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- | ----------------------------------------------------------------- | --------------------------------------------------------- |
| <img src={require(".././img/desktop-client-states/ocl-ui_logo-petrol.png").default} alt="Bereit" width="28"/>                        | Bereit                 | Der Client ist verbunden und alle Dateien sind aktuell.           | Keine Aktion erforderlich.                                |
| <img src={require(".././img/desktop-client-states/ocl-ui_sync-petrol-colour.png").default} alt="Synchronisierung läuft" width="28"/> | Synchronisierung läuft | Dateien werden derzeit hoch- oder heruntergeladen.                | Warten, bis die Synchronisierung abgeschlossen ist.       |
| <img src={require(".././img/desktop-client-states/ocl-ui_pause-petrol-colour.png").default} alt="Pausiert" width="28"/>              | Pausiert               | Die Synchronisierung wurde vorübergehend angehalten.              | Synchronisierung fortsetzen, wenn Sie fortfahren möchten. |
| <img src={require(".././img/desktop-client-states/ocl-ui_offline-petrol-colour.png").default} alt="Offline" width="28"/>             | Offline                | Der Client kann keine Verbindung zum OpenCloud-Server herstellen. | Netzwerkverbindung und Server prüfen.                     |
| <img src={require(".././img/desktop-client-states/ocl-ui_info-petrol-colour.png").default} alt="Information" width="28"/>            | Information            | Der Client zeigt eine nicht kritische Informationsmeldung an.     | Meldung bei Bedarf prüfen.                                |
| <img src={require(".././img/desktop-client-states/ocl-ui_error-petrol-colour.png").default} alt="Fehler" width="28"/>                | Fehler                 | Ein Problem verhindert die normale Synchronisierung.              | Desktop-Client öffnen und das gemeldete Problem beheben.  |

## Bereit

Das Symbol **Bereit** wird angezeigt, wenn der Desktop-Client mit OpenCloud verbunden ist und aktuell keine Synchronisierung stattfindet.

- Mit OpenCloud verbunden
- Keine aktiven Dateiübertragungen
- Alle Dateien sind auf dem neuesten Stand

<img src={require(".././img/desktop-client-states/ocl-ui_logo-petrol.png").default} alt="Ready state" width="100"/>

Es ist keine Aktion erforderlich. Ihre Dateien sind vollständig synchronisiert.

## Synchronisierung läuft

Das Symbol **Synchronisierung läuft** zeigt an, dass Dateien aktuell hoch- oder heruntergeladen werden.

- Dateien werden synchronisiert
- Änderungen werden verarbeitet
- Der Client kommuniziert mit dem Server

<img src={require(".././img/desktop-client-states/ocl-ui_sync-petrol-colour.png").default} alt="Synchronizing state" width="100"/>

Warten Sie, bis die Synchronisierung abgeschlossen ist, bevor Sie Ihr Gerät ausschalten.

## Pausiert

Das Symbol **Pausiert** erscheint, wenn die Synchronisierung vorübergehend angehalten wurde.

- Die Synchronisierung ist pausiert
- Es werden keine Dateien übertragen
- Lokale und entfernte Änderungen werden nicht synchronisiert

<img src={require(".././img/desktop-client-states/ocl-ui_pause-petrol-colour.png").default} alt="Paused state" width="100"/>

Setzen Sie die Synchronisierung über das Menü des Desktop-Clients fort, sobald Sie die Synchronisierung wieder aufnehmen möchten.

## Offline

Das Symbol **Offline** zeigt an, dass der Desktop-Client derzeit keine Verbindung zum OpenCloud-Server herstellen kann.

- Keine Verbindung zum Server
- Synchronisierung nicht verfügbar
- Lokale Dateien bleiben weiterhin zugänglich

<img src={require(".././img/desktop-client-states/ocl-ui_offline-petrol-colour.png").default} alt="Offline state" width="100"/>

Mögliche Ursachen:

- Keine Internetverbindung
- Server nicht erreichbar
- DNS- oder Netzwerkprobleme
- Firewall-Einschränkungen

Überprüfen Sie Ihre Netzwerkverbindung und stellen Sie sicher, dass der OpenCloud-Server erreichbar ist.

## Information

Das Symbol **Information** wird für Hinweise und Meldungen verwendet, die keine unmittelbare Aktion erfordern.

- Allgemeine Benachrichtigungen
- Nicht kritische Ereignisse
- Informative Meldungen des Clients

<img src={require(".././img/desktop-client-states/ocl-ui_info-petrol-colour.png").default} alt="Information state" width="100"/>

Lesen Sie die Meldung, wenn Sie weitere Informationen benötigen.

## Fehler

Das Symbol **Fehler** zeigt an, dass der Desktop-Client auf ein Problem gestoßen ist, das eine normale Synchronisierung verhindert.

- Synchronisierung fehlgeschlagen
- Authentifizierungsprobleme
- Konfigurationsfehler
- Fehler beim Dateizugriff oder Berechtigungsprobleme

<img src={require(".././img/desktop-client-states/ocl-ui_error-petrol-colour.png").default} alt="Error state" width="100"/>

Öffnen Sie den Desktop-Client und prüfen Sie die angezeigte Fehlermeldung. Die Synchronisierung kann erst fortgesetzt werden, nachdem das zugrunde liegende Problem behoben wurde.

:::info
Die farbliche Darstellung der Icons in der Taskleiste (Windows), Dock (macOS) oder Systemleiste/Panel (Linux) sind vom jeweiligen Betriebssystem abhängig!
:::
