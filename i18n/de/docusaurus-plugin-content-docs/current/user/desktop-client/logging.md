---
sidebar_position: 5
id: logging
title: Logfiles sammeln
description: Logfiles sammeln in OpenCloud
draft: false
---

# Protokollierung in einem temporären Verzeichnis in OpenCloud Desktop

Wenn Sie Protokolle für die Fehlersuche erstellen müssen, gehen Sie wie folgt vor:

## Öffnen Sie die Log-Einstellungen

- Klicken Sie auf Einstellungen → Erweitert → Log-Einstellungen

<img src={require("./img/logging/logging-access.png").default} alt="logging access" width="400"/>

## Aktivieren Sie die Protokollierung

- Aktivieren Sie im Fenster Protokollausgabe das Kontrollkästchen Protokollierung in temporärem Ordner aktivieren.
- Um dem Support-Team und den Entwicklern zu helfen, ist es hilfreich, das Log Http traffic zu aktivieren

<img src={require("./img/logging/logging-enable.png").default} alt="enable logging" width="400"/>

## Finden Sie die Log-Dateien

- Klicken Sie auf Ordner öffnen, um auf die Protokolle zuzugreifen.

<img src={require("./img/logging/logging-open-folder.png").default} alt="open logfile folder" width="400"/>

- Wählen Sie die Protokolldateien für den Zeitraum aus, in dem das Problem aufgetreten ist.

<img src={require("./img/logging/logging-logfiles.png").default} alt="logfiles overview" width="400"/>

:::note
Diese Protokolle können helfen, Probleme mit OpenCloud Desktop zu diagnostizieren und zu beheben.
:::

### Log Inhalt Beschreibung

`25-02-17 09:02:35:174 [ info sync.httplogger ]: REQUEST 3710cc12-7391-4793-8e89-00499dc11983 {„request“:{„body“:{„length“:0},„header“:{„accept“:„*/*“,„accept-language“:„en_DE“,„original-request-id“:„3710cc12-7391-4793-8e89-00499dc11983“,„user-agent“:"Mozilla/5. 0 (Macintosh) mirall/1.0.0-git (OpenCloud, macos-24. 3.0 ClientArchitecture: x86_64 OsArchitecture: arm64)„,“x-request-id„:“3710cc12-7391-4793-8e89-00499dc11983„},“info„:{“cached„:false,“id„:“3710cc12-7391-4793-8e89-00499dc11983„,“method„:“GET„,“url„:“https://cloud.opencloud.test/.well-known/openid-configuration"}}}`

| Log Inhalt                           | Beschreibung                                                          |
| ------------------------------------ | --------------------------------------------------------------------- |
| 25-02-17 09:02:35:174                | Zeitstempel der Anfrage                                               |
| [ info sync.httplogger ]             | Bezeichnung der Protokollkategorie                                    |
| 3710cc12-7391-4793-8e89-00499dc11983 | X-REQUEST-ID (wird verwendet, um Anfragen und Antworten abzugleichen) |
| Header: { }                          | Liste der HTTP-Header                                                 |
| Data: []                             | HTTP-Bodies (JSON, XML)                                               |
| (112ms)                              | Antwortzeit (seit Absenden der Anfrage)                               |

### X-REQUEST-ID für die Fehlersuche verwenden

- Die OpenCloud-Desktop-Anwendung sendet mit jeder Anfrage einen X-REQUEST-ID-Header.
- Diese ID hilft bei der Suche nach entsprechenden Anfragen und Antworten in den Protokollen.
- Sie können Ihren Webserver so konfigurieren, dass er die X-REQUEST-ID zu seinen Protokollen hinzufügt, um eine tiefere Analyse zu ermöglichen.

:::note
Diese Funktion ist nützlich für die Fehlersuche bei Synchronisationsproblemen, die Überwachung von Netzwerkaktivitäten und die Behebung von Verbindungsproblemen.
:::
