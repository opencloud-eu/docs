---
sidebar_position: 60
id: not-allowed-upload-files
title: Dateien, die nicht hochgeladen werden dürfen
description: Erfahren Sie, was passiert, wenn der Desktop Client bestimmte Dateien nicht hochladen kann.
draft: false
---

# Dateien, die nicht hochgeladen werden dürfen

Einige Dateien können nicht nach OpenCloud hochgeladen oder synchronisiert werden. Das kann zum Beispiel passieren, wenn eine Datei nicht den Regeln für Dateinamen entspricht, nicht unterstützte Zeichen enthält oder durch serverseitige Einschränkungen blockiert wird.

Wenn der Desktop Client eine Datei erkennt, die nicht hochgeladen werden darf, wird diese Datei nicht nach OpenCloud hochgeladen.

## Was passiert mit diesen Dateien?

Dateien, die nicht hochgeladen werden dürfen, werden in den lokalen Papierkorb Ihres Betriebssystems verschoben.

Das bedeutet:

- Die Datei wird aus dem lokalen Sync-Ordner entfernt.
- Die Datei wird nicht nach OpenCloud hochgeladen.
- Die Datei ist nicht in der Weboberfläche verfügbar.
- Die Datei kann möglicherweise aus dem lokalen Papierkorb wiederhergestellt werden.

## Warum wird die Datei in den Papierkorb verschoben?

Durch das Verschieben in den lokalen Papierkorb wird verhindert, dass der Desktop Client wiederholt versucht, eine Datei hochzuladen, die von OpenCloud nicht akzeptiert wird.

Dadurch werden außerdem wiederkehrende Synchronisierungsfehler vermieden, die durch dieselbe Datei verursacht werden.

## Wo finde ich die Datei?

Je nach Betriebssystem können Sie die Datei aus dem lokalen Papierkorb wiederherstellen:

- **Windows**: Papierkorb
- **macOS**: Papierkorb
- **Linux**: Papierkorb oder der von Ihrer Desktop-Umgebung verwendete Papierkorb-Speicherort

## Empfohlene Vorgehensweise

Wenn eine Datei in den Papierkorb verschoben wurde, weil sie nicht hochgeladen werden konnte:

1. Öffnen Sie den lokalen Papierkorb Ihres Betriebssystems.
2. Stellen Sie die Datei wieder her, wenn Sie sie weiterhin benötigen.
3. Prüfen Sie, ob der Dateiname, der Dateipfad oder der Dateityp erlaubt ist.
4. Benennen Sie die Datei um oder passen Sie sie bei Bedarf an.
5. Verschieben Sie die Datei zurück in den Sync-Ordner.

Nachdem die Datei angepasst wurde, kann der Desktop Client erneut versuchen, sie zu synchronisieren.

:::important

Prüfen Sie vor dem Leeren des lokalen Papierkorbs, ob sich darin Dateien befinden, die vom Desktop Client dorthin verschoben wurden.

:::

:::note

Dateien, die nicht hochgeladen werden dürfen, werden lokal vom Desktop Client verarbeitet. Sie werden erst dann in OpenCloud gespeichert, wenn sie erfolgreich synchronisiert wurden.

:::
