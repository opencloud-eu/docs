---
sidebar_position: 3
title: Protokollierung
description: Aktivieren Sie die Anwendungsprotokollierung und durchsuchen Sie erzeugte Protokolldateien zur Fehlerbehebung.
draft: false
---

# Protokollierung

Mit den **Protokollierungseinstellungen** können Sie die Diagnoseprotokollierung aktivieren, erzeugte Protokolldateien durchsuchen und diese zur Fehlerbehebung weitergeben.

## Protokollierung öffnen

1. Öffnen Sie die **OpenCloud**-App.
2. Tippen Sie auf **Einstellungen**.
3. Tippen Sie im Bereich **Benutzeroberfläche** auf **Protokollierung**.

Auf der Seite **Protokollierung** können Sie die Protokollierung aktivieren oder deaktivieren und die erzeugten Protokolldateien verwalten.

<img src={require("../../img/settings/logging/logging-button.png").default} alt="Schaltfläche Protokollierung" height="650"/>

## Protokollierung aktivieren

Die Diagnoseprotokollierung kann dabei helfen, Probleme mit der OpenCloud-App zu erkennen und zu beheben.

- Aktivieren Sie **Protokollierung aktivieren**, um Diagnoseinformationen zu erfassen.
- Tippen Sie auf **Durchsuchen**, um gespeicherte Protokolldateien anzuzeigen.

<img src={require("../../img/settings/logging/logging-menu.png").default} alt="Menü Protokollierung" height="650"/>

:::warning

Die Protokollierung kann die Leistung der App geringfügig beeinflussen und sensible Informationen enthalten, zum Beispiel Server-URLs oder benutzerbezogene Daten.

Aktivieren Sie die Protokollierung nur, wenn Sie ein Problem untersuchen.

:::

## Protokolldateien durchsuchen und teilen

Wenn Sie **Durchsuchen** auswählen, wird die Liste der auf Ihrem Gerät gespeicherten Protokolldateien geöffnet.

Auf dieser Seite können Sie:

- verfügbare Protokolldateien anzeigen,
- eine Protokolldatei über die Schaltfläche **Teilen** weitergeben,
- alle gespeicherten Protokolldateien über **Alle löschen** entfernen.

<img src={require("../../img/settings/logging/log-files-list.png").default} alt="Liste der Protokolldateien" height="650"/>

:::note

Stelle für die Fehlerbehebung und Protokollanalyse sicher, dass **HTTPS aktiviert** ist, bevor du Protokolldateien mit dem Support teilst.

:::

## Funktionsweise der Protokollierung

Die OpenCloud iOS-App speichert Protokolldateien lokal auf Ihrem Gerät.

:::tip

Aktivieren Sie die Protokollierung nur, während Sie ein Problem reproduzieren. Nachdem die benötigten Informationen erfasst wurden, sollten Sie die Protokollierung wieder deaktivieren, um Auswirkungen auf Leistung und Speicherverbrauch zu minimieren.

:::

:::note

- Protokolldateien bleiben auf Ihrem Gerät gespeichert, bis Sie sie löschen.
- Sie werden **nicht automatisch** auf OpenCloud-Server hochgeladen.
- Es werden maximal die **10 zuletzt archivierten Protokolldateien** gespeichert.
- Jede Protokolldatei kann bis zu **24 Stunden** App-Aktivität enthalten.

:::
