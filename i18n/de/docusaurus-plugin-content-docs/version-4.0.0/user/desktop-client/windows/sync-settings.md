---
sidebar_position: 4
id: sync-settings-win
title: Synchronisationseinstellungen unter Windows
description: Synchronisationseinstellungen unter Windows
draft: false
---

# Windows: Synchronisationseinstellungen

Der OpenCloud Desktop Client nutzt das Windows Virtual File System (VFS), um Ihre Cloud-Daten direkt in den Windows-Dateiexplorer zu integrieren.  
Dateien und Ordner werden angezeigt, ohne dass sie vollständig heruntergeladen werden müssen – das spart lokalen Speicherplatz.

## Status der Datei

Dateien und Ordner können verschiedene Stati haben, je nachdem, ob sie lokal gespeichert oder nur online verfügbar sind.

### Immer auf diesem Gerät verfügbar (full pinned)

- Lokal gespeichert und jederzeit offline zugänglich.
- Windows entfernt diese Datei nicht automatisch.

<img src={require(".././img/vfs/full-pinned.png").default} alt="Symbol vollständig angeheftet" width="400"/>

### Auf diesem Gerät verfügbar (full)

- Heruntergeladen und offline verfügbar.
- Kann von Windows entfernt werden, wenn Speicherplatz benötigt wird.
- Neu erstellte oder hinzugefügte Dateien erhalten automatisch diesen Status.

<img src={require(".././img/vfs/full.png").default} alt="Symbol vollständig" width="400"/>

### Online verfügbar (placeholder)

- Wird im Datei-Explorer angezeigt, befindet sich jedoch nur in der Cloud.
- Wird beim Öffnen automatisch heruntergeladen; Internetverbindung erforderlich.

<img src={require(".././img/vfs/placeholder.png").default} alt="Symbol Platzhalter" width="400"/>

## Elemente offline verfügbar machen

Um eine Datei, einen Ordner oder einen Space lokal zu speichern:

1. Klicken Sie im Datei-Explorer mit der rechten Maustaste auf das Element.
2. Wählen Sie „Immer auf diesem Gerät beibehalten“.

<img src={require(".././img/vfs/always-keep-on-this-device.png").default} alt="Auswahl: Immer auf diesem Gerät behalten" width="400"/>

## Speicherplatz freigeben

Um lokale Kopien zu entfernen, während die Elemente weiterhin im Datei-Explorer sichtbar bleiben:

1. Klicken Sie mit der rechten Maustaste auf das Element.
2. Wählen Sie „Speicherplatz freigeben“.

<img src={require(".././img/vfs/free-up-space.png").default} alt="Auswahl: Speicherplatz freigeben" width="400"/>

## Zugriff auf Dateien

- Online-only Dateien werden automatisch heruntergeladen, sobald Sie sie öffnen.
- Änderungen werden zurück zu OpenCloud synchronisiert.

:::note
Für Dateien, die nur online verfügbar sind, ist eine Internetverbindung erforderlich.
:::
