---
sidebar_position: 11
id: common-issues
title: Häufige Probleme & Hilfe
description: Häufige Probleme & Hilfe
draft: false
---

# Häufige Probleme & Hilfe

## Symlinks werden mit dem Desktop-Client nicht synchronisiert

### Problem

Symbolische Links (Symlinks) werden vom OpenCloud Desktop-Client nicht synchronisiert. Nutzer stellen häufig fest, dass verlinkte Ordner oder Dateien fehlen oder nicht zugänglich sind.

### Erklärung

Symlinks werden aus mehreren wichtigen Gründen bewusst von der Synchronisation ausgeschlossen:

- Nicht portabel: Symlinks verweisen oft auf Pfade, die nur auf dem ursprünglichen Rechner existieren. Auf einem anderen Gerät ist der Zielpfad in der Regel nicht vorhanden.
- Nicht im Webinterface nutzbar: Das Webinterface kann Symlinks nicht interpretieren oder darstellen.
- Problematisch unter Windows: Die Unterstützung von Symlinks unter Windows ist eingeschränkt und inkonsistent.
- Gefahr von Endlosschleifen: Symlinks könnten aufeinander verweisen und so zu einer endlosen Synchronisationsschleife führen.
- Identitätsverlust: Wenn der Client dem Symlink folgen und das Ziel synchronisieren würde, entstünde lediglich eine reguläre Kopie. Die Eigenschaft als Symlink ginge dabei verloren.

### Lösung

#### Ordner außerhalb des Synchronisationsverzeichnisses mit Symlinks einbinden

Wenn Sie einen Ordner außerhalb Ihres Synchronisationsverzeichnisses synchronisieren möchten, können Sie diesen verschieben und am ursprünglichen Ort durch einen Symlink ersetzen.

##### Beispiel

Sie möchten den Ordner `/foo/A` synchronisieren, aber Ihr Sync-Root ist `/home/bar/OpenCloud/Personal`.

1. Verschieben Sie den Ordner in das Synchronisationsverzeichnis:

   ```bash
   mv /foo/A /home/bar/OpenCloud/Personal/foo/A
   ```

## Dateien mit "~$" im Namen werden nicht synchronisiert

Der OpenCloud Desktop Client synchronisiert keine Dateien, die mit `~$` beginnen, wie z. B. `~$document.docx`.  
Dabei handelt es sich um temporäre Sperrdateien, die von Microsoft Office-Anwendungen (Word, Excel, PowerPoint) erstellt werden, solange ein Dokument geöffnet ist.

<img src={require("./img/common-issues/desktop-excluded.png").default} alt="Anzeige, dass ~$ Dateien von der Synchronisierung ausgeschlossen sind" width="500"/>

Es sind keine eigentlichen Inhaltsdateien, sondern interne Marker, die verhindern sollen, dass mehrere Benutzer gleichzeitig dasselbe Dokument bearbeiten.  
Sobald die Datei geschlossen wird, entfernt Office die `~$`-Datei automatisch.

Weitere Informationen finden Sie in der Erklärung von Microsoft:  
[Beschreibung, wie Word temporäre Dateien erstellt](https://support.microsoft.com/de-de/topic/description-of-how-word-creates-temporary-files-66b112fb-d2c0-8f40-a0be-70a367cc4c85)
