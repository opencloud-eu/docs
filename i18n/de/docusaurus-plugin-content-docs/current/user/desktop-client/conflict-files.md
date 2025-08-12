---
sidebar_position: 10
id: file-conflicts
title: Dateikonflikte handhaben
description: Wie Dateikonflikte handhaben
draft: false
---

# Behebung von Dateikonflikten im OpenCloud Desktop-Client

Wenn Dateien sowohl lokal als auch auf dem Server geändert werden, bevor eine Synchronisierung stattfindet, erstellt der Desktop-Client sogenannte „Konfliktkopien“. Beispiele:

- `conflict.txt` (Server-Version)
- `conflict (conflicted copy  JJJJ-MM-TT HHMMSS).txt` (lokale Version)

<img src={require("./img/conflict-files/conflict-file.png").default} alt="Konfliktdateien im Explorer" width="1920"/>

Dies passiert in der Regel, wenn:

- sich die lokale und die Server-Version einer Datei gleichzeitig verändern,
- und die App diese Änderungen nicht automatisch zusammenführen kann.

## Wie Sie benachrichtigt werden

In der Übersicht des Desktop-Clients erscheint eine Benachrichtigung, wenn Konfliktdateien erkannt wurden.  
Das bedeutet, dass mehrere Versionen derselben Datei existieren – häufig, weil Änderungen auf verschiedenen Geräten vorgenommen wurden, bevor eine Synchronisierung erfolgen konnte.  
Die Benachrichtigung dient als Hinweis, dass Sie die Konflikte prüfen und entscheiden sollten, wie die Versionen zusammengeführt oder behalten werden.

<img src={require("./img/conflict-files/conflict-info.png").default} alt="Benachrichtigung zu Dateikonflikten im Desktop-Client" width="500"/>

## So lösen Sie Dateikonflikte manuell

1. Öffnen Sie beide Dateien (das Original und die Konfliktkopie).
2. Vergleichen und kombinieren Sie die Unterschiede manuell.
3. Bearbeiten Sie die ursprüngliche Datei (`conflict.txt`), um alle relevanten Änderungen zu übernehmen.
4. Löschen Sie die Konfliktkopie, sobald die Änderungen zusammengeführt wurden.
5. Lassen Sie die aktualisierte Originaldatei bestehen – die Synchronisierung wird dann wie gewohnt fortgesetzt.

## Good Practices zur Vermeidung von Konflikten

- Vermeiden Sie es, dieselbe Datei gleichzeitig auf mehreren Geräten zu bearbeiten.
- Warten Sie immer, bis die Synchronisierung abgeschlossen ist, bevor Sie lokale Änderungen vornehmen.

## Warum Konfliktdateien entstehen

Der Desktop-Client erkennt einen Konflikt, wenn:

- sowohl die lokale als auch die Server-Version einer Datei seit der letzten Synchronisierung geändert wurden,
- der Abgleich anhand von Datei-IDs und Checksummen erfolgt – nicht nur anhand von Zeitstempeln.
- zur Sicherheit beide Versionen erhalten bleiben, wobei die lokale Datei mit `"(conflicted copy ...)"` umbenannt wird.

Konfliktdateien entstehen lokal und erscheinen nicht automatisch auf dem Server – es sei denn, sie werden ausdrücklich hochgeladen.

Treten Konflikte häufig auf – auch bei einfachen Änderungen – kann dies auf Berechtigungsprobleme, schreibgeschützte Dateien oder darauf hinweisen, dass dieselben Dateien zusätzlich über andere Tools synchronisiert werden. In diesem Fall sollten Sie die Protokolle und Dateiattribute prüfen.
