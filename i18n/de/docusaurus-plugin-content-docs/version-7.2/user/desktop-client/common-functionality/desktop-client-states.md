---
sidebar_position: 5
id: desktop-client-states
title: Status des Desktop-Clients
description: Symbole des Desktop-Client-Status
draft: false
---

## Symbole des Desktop-Client-Status verstehen

Der OpenCloud Desktop-Client verwendet Tray-Symbole, um den aktuellen Synchronisations- und Verbindungsstatus anzuzeigen. So erkennen Sie schnell, ob alles normal funktioniert oder ob Handlungsbedarf besteht.

## Kurzübersicht

| Symbol                                                                                                                                | Status                 | Bedeutung                                                                             | Typische Aktion                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| <img src={require(".././img/desktop-client-states/ocl-ui_logo-petrol.png").default} alt="Bereit-Status" width="28"/>                  | Bereit                 | Der Client ist verbunden und alle Dateien sind auf dem neuesten Stand.                | Keine Aktion erforderlich.                                             |
| <img src={require(".././img/desktop-client-states/ocl-ui_sync-petrol-colour.png").default} alt="Synchronisierung-Status" width="28"/> | Synchronisierung läuft | Dateien werden gerade hoch- oder heruntergeladen.                                     | Warten Sie, bis die Synchronisierung abgeschlossen ist.                |
| <img src={require(".././img/desktop-client-states/ocl-ui_pause-petrol-colour.png").default} alt="Pausiert-Status" width="28"/>        | Pausiert               | Die Synchronisierung wurde vorübergehend angehalten.                                  | Setzen Sie die Synchronisierung fort, wenn Sie bereit sind.            |
| <img src={require(".././img/desktop-client-states/ocl-ui_offline-petrol-colour.png").default} alt="Offline-Status" width="28"/>       | Offline                | Der Client kann keine Verbindung zum OpenCloud-Server herstellen.                     | Prüfen Sie Ihre Netzwerkverbindung und die Erreichbarkeit des Servers. |
| <img src={require(".././img/desktop-client-states/ocl-ui_info-petrol-colour.png").default} alt="Informations-Status" width="28"/>     | Information            | Der Client zeigt eine nicht kritische Informationsmeldung an.                         | Lesen Sie die Meldung bei Bedarf im Detail.                            |
| <img src={require(".././img/desktop-client-states/ocl-ui_error-petrol-colour.png").default} alt="Fehler-Status" width="28"/>          | Fehler                 | Der Client ist auf ein Problem gestoßen, das die normale Synchronisierung verhindert. | Öffnen Sie den Client und beheben Sie das gemeldete Problem.           |

## Bereit

Das Symbol „Bereit“ wird angezeigt, wenn der Desktop-Client mit OpenCloud verbunden ist und keine Synchronisierung stattfindet.

- Mit OpenCloud verbunden
- Keine aktiven Dateiübertragungen
- Alle Dateien sind auf dem neuesten Stand

<img src={require(".././img/desktop-client-states/ocl-ui_logo-petrol.png").default} alt="Bereit-Status" width="100"/>

Es ist keine Aktion erforderlich. Ihre Dateien sind vollständig synchronisiert.

## Synchronisierung

Das Symbol „Synchronisierung“ zeigt an, dass Dateien gerade hoch- oder heruntergeladen werden.

- Dateien werden synchronisiert
- Änderungen werden gerade verarbeitet
- Der Client kommuniziert mit dem Server

<img src={require(".././img/desktop-client-states/ocl-ui_sync-petrol-colour.png").default} alt="Synchronisierung-Status" width="100"/>

Warten Sie, bis die Synchronisierung abgeschlossen ist, bevor Sie Ihr Gerät herunterfahren.

## Pausiert

Das Symbol „Pausiert“ erscheint, wenn die Synchronisierung vorübergehend vom Benutzer angehalten wurde.

- Die Synchronisierung ist gestoppt
- Es werden keine Dateien übertragen
- Lokale und entfernte Änderungen werden nicht synchronisiert

<img src={require(".././img/desktop-client-states/ocl-ui_pause-petrol-colour.png").default} alt="Pausiert-Status" width="100"/>

Setzen Sie die Synchronisierung über das Menü des Desktop-Clients fort, wenn Sie wieder synchronisieren möchten.

## Offline

Das Symbol „Offline“ zeigt an, dass der Desktop-Client derzeit keine Verbindung zum OpenCloud-Server herstellen kann.

- Keine Verbindung zum Server
- Synchronisierung ist nicht verfügbar
- Lokale Dateien bleiben zugänglich (Windows-Ordner müssen [vollständig angeheftet](../windows/sync-settings.md#immer-auf-diesem-gerat-verfugbar-full-pinned) sein)

<img src={require(".././img/desktop-client-states/ocl-ui_offline-petrol-colour.png").default} alt="Offline-Status" width="100"/>

Häufige Ursachen sind:

- Keine Internetverbindung
- Server nicht verfügbar
- DNS- oder Netzwerkprobleme
- Firewall-Einschränkungen

Prüfen Sie Ihre Netzwerkverbindung und stellen Sie sicher, dass der OpenCloud-Server erreichbar ist.

## Information

Das Symbol „Information“ wird für Hinweise verwendet, die keine sofortige Aktion erfordern.

- Allgemeine Hinweise
- Nicht kritische Ereignisse
- Informationsmeldungen des Clients

<img src={require(".././img/desktop-client-states/ocl-ui_info-petrol-colour.png").default} alt="Informations-Status" width="100"/>

Prüfen Sie die Meldung bei Bedarf für weitere Details.

## Fehler

Das Symbol „Fehler“ zeigt an, dass der Desktop-Client auf ein Problem gestoßen ist, das die normale Synchronisierung verhindert.

- Synchronisierung fehlgeschlagen
- Probleme mit der Authentifizierung
- Konfigurationsprobleme
- Fehler beim Dateizugriff oder bei Berechtigungen

<img src={require(".././img/desktop-client-states/ocl-ui_error-petrol-colour.png").default} alt="Fehler-Status" width="100"/>

Öffnen Sie den Desktop-Client und prüfen Sie den gemeldeten Fehler. Die Synchronisierung kann erst fortgesetzt werden, wenn das Problem behoben wurde.

:::info
Das visuelle Erscheinungsbild und die Farbgebung der Symbole in der Taskleiste (Windows), im Dock (macOS) oder im System-Tray bzw. Panel (Linux) können je nach Betriebssystem variieren.
:::
