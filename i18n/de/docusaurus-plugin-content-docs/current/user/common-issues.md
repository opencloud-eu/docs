---
sidebar_position: 110
id: common-issues
title: Häufige Probleme & Hilfe
description: Häufige Probleme & Hilfe
draft: false
toc_max_heading_level: 2
---

# Häufige Probleme & Hilfe

## Desktop-Client kann keine Verbindung herstellen

### Problem

Nach der Eingabe der OpenCloud-Serveradresse öffnet sich der Browser nicht. Das Fenster des Desktop-Clients kann flackern und seine Speicherauslastung ansteigen.

### Ursache

Dieses Problem kann auftreten, wenn die OpenCloud-Instanz über einen externen Reverse Proxy aufgerufen wird, der die Verbindung oder die Servererkennung beeinträchtigt.

### Lösung

Wenden Sie sich an Ihre OpenCloud-Administration und bitten Sie darum, die Reverse-Proxy-Konfiguration zu überprüfen. Hinweise zur Fehlerbehebung finden Administratoren unter [Desktop-Client kann über einen externen Reverse Proxy keine Verbindung herstellen](/docs/next/admin/resources/common-issues/#desktop-client-cannot-connect-through-an-external-reverse-proxy).

## Symlinks werden mit dem Desktop-Client nicht synchronisiert

### Problem

Symbolische Links (Symlinks) werden vom OpenCloud Desktop-Client nicht synchronisiert. Nutzer stellen häufig fest, dass verlinkte Ordner oder Dateien fehlen oder nicht zugänglich sind.

### Ursache

Symlinks werden aus mehreren wichtigen Gründen bewusst von der Synchronisation ausgeschlossen:

- Nicht portabel: Symlinks verweisen oft auf Pfade, die nur auf dem ursprünglichen Rechner existieren. Auf einem anderen Gerät ist der Zielpfad in der Regel nicht vorhanden.
- Nicht im Webinterface nutzbar: Das Webinterface kann Symlinks nicht interpretieren oder darstellen.
- Problematisch unter Windows: Die Unterstützung von Symlinks unter Windows ist eingeschränkt und inkonsistent.
- Gefahr von Endlosschleifen: Symlinks könnten aufeinander verweisen und so zu einer endlosen Synchronisationsschleife führen.
- Identitätsverlust: Wenn der Client dem Symlink folgen und das Ziel synchronisieren würde, entstünde lediglich eine reguläre Kopie. Die Eigenschaft als Symlink ginge dabei verloren.

### Lösung

#### Ordner außerhalb des Synchronisationsverzeichnisses mit Symlinks einbinden

Wenn Sie einen Ordner außerhalb Ihres Synchronisationsverzeichnisses (Sync-Root) synchronisieren möchten, können Sie diesen in die Sync-Root verschieben und am ursprünglichen Ort durch einen Symlink ersetzen.

##### Beispiel

Sie möchten den Ordner `/foo/A` synchronisieren, aber Ihre Sync-Root ist `/home/bar/OpenCloud/Personal`.

1. Verschieben Sie den Ordner in die Sync-Root (in ein geeignetes Unterverzeichnis):

   ```bash
   mkdir -p /home/bar/OpenCloud/Personal/foo/
   mv /foo/A /home/bar/OpenCloud/Personal/foo/A
   ```

2. Erstellen Sie einen Symlink:

   ```bash
   ln -s /home/bar/OpenCloud/Personal/foo/A /foo/A
   ```

## Dateien mit "~$" im Namen werden nicht synchronisiert

### Problem

Der OpenCloud Desktop-Client synchronisiert keine Dateien, die mit `~$` beginnen, wie z. B. `~$document.docx`.

<img src={require("./img/common-issues/desktop-excluded.png").default} alt="Anzeige, dass ~$ Dateien von der Synchronisierung ausgeschlossen sind" width="500"/>

### Ursache

Diese Dateien sind temporäre Sperrdateien, die von Microsoft Office-Anwendungen erstellt werden, solange ein Dokument geöffnet ist. Es sind keine eigentlichen Inhaltsdateien, sondern interne Marker, die verhindern, dass mehrere Benutzer gleichzeitig dasselbe Dokument bearbeiten.

### Lösung

Schließen Sie das Dokument in Microsoft Office. Office entfernt die zugehörige `~$`-Datei automatisch.

Weitere Informationen finden Sie in dem [Microsoft-Supportartikel zu temporären Office-Sperrdateien von Word/Excel/PowerPoint](https://support.microsoft.com/en-gb/topic/-the-document-is-locked-for-editing-by-another-user-error-message-when-you-try-to-open-a-document-in-word-10b92aeb-2e23-25e0-9110-370af6edb638?).
