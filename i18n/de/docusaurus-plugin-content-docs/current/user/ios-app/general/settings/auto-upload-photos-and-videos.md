---
sidebar_position: 60
id: auto-upload-photos-and-videos
title: Automatischer Foto- und Video-Upload
description: Laden Sie Fotos und Videos von Ihrem iPhone oder iPad automatisch hoch.
draft: false
---

# Automatischer Upload

Mit **Automatischer Upload** werden neu erstellte Fotos und Videos von Ihrem iPhone oder iPad automatisch in Ihr OpenCloud-Konto hochgeladen.

Nach der Einrichtung werden neue Medien automatisch hochgeladen, sobald die OpenCloud-App geöffnet ist und im Vordergrund ausgeführt wird.

## Voraussetzungen

Bevor Sie den automatischen Upload verwenden, stellen Sie sicher, dass:

- Sie bei Ihrem OpenCloud-Konto angemeldet sind.
- Die OpenCloud-App Zugriff auf Ihre Fotomediathek hat.
- Ein Zielordner für Uploads konfiguriert wurde.

## Automatischen Upload konfigurieren

1. Öffnen Sie die **OpenCloud**-App.
2. Tippen Sie auf **Einstellungen**.

<img src={require("../../img/settings/auto-upload-photos-and-videos/settings-button.png").default} alt="Schaltfläche Einstellungen" height="650"/>

3. Scrollen Sie nach unten zum Bereich **Mediendateien**.
4. Tippen Sie auf **Medien-Upload**.

<img src={require("../../img/settings/auto-upload-photos-and-videos/media-upload-button.png").default} alt="Schaltfläche Medien-Upload" height="650"/>

## Automatischen Upload aktivieren

Foto- und Video-Uploads können unabhängig voneinander aktiviert werden.

Die folgenden Optionen stehen zur Verfügung:

- **HEIC in JPEG konvertieren** – Konvertiert HEIC-Bilder vor dem Hochladen in JPEG.
- **Videos in MP4 konvertieren** – Konvertiert Videos vor dem Hochladen in MP4.
- **Originaldateinamen beibehalten** – Behält den ursprünglichen Dateinamen bei, statt einen neuen zu erzeugen.
- **Automatischer Foto-Upload** – Lädt neu erstellte Fotos automatisch hoch.
- **Automatischer Video-Upload** – Lädt neu erstellte Videos automatisch hoch.
- **Foto-Upload-Pfad** – Legt den Zielordner für hochgeladene Fotos fest.

<img src={require("../../img/settings/auto-upload-photos-and-videos/auto-upload-photos.png").default} alt="Einstellungen für den automatischen Upload" height="650"/>

## Upload-Ziel auswählen

Bevor der automatische Upload beginnen kann, müssen Sie einen Zielordner auswählen.

1. Tippen Sie auf **Foto-Upload-Pfad**.
2. Navigieren Sie zu dem Ordner, in den Fotos hochgeladen werden sollen.
3. Tippen Sie auf **Ziel auswählen**.

<img src={require("../../img/settings/auto-upload-photos-and-videos/select-destination.png").default} alt="Upload-Ziel auswählen" height="650"/>

## Funktionsweise des automatischen Uploads

:::important Aktuelles Verhalten unter iOS

Derzeit erkennt und lädt der automatische Upload neue Fotos und Videos nur, wenn die OpenCloud-App geöffnet ist und im Vordergrund ausgeführt wird.

Wenn die App geschlossen ist oder im Hintergrund läuft, werden neue Medien **nicht** hochgeladen, bis die App erneut geöffnet wird.

Bereits das Öffnen der OpenCloud-App startet den automatischen Upload. Alle neuen Medien, die seit dem letzten erfolgreichen Upload erstellt wurden, werden automatisch erkannt und hochgeladen.

:::

Wenn der konfigurierte Upload-Ordner gelöscht wird, stoppt der automatische Upload automatisch, bis ein neuer Zielordner ausgewählt wurde.

### Doppelte Uploads verhindern

Um doppelte Uploads zu verhindern, speichert der automatische Upload den Zeitstempel des zuletzt erfolgreich hochgeladenen Elements.

Beim erstmaligen Aktivieren des automatischen Uploads wird der Aktivierungszeitpunkt gespeichert und mit dem Erstellungsdatum jedes Fotos und Videos verglichen. Nachdem eine Datei erfolgreich hochgeladen wurde, wird ihr Erstellungszeitpunkt als neuer Referenzwert verwendet.

Dieser Ansatz bietet mehrere Vorteile:

- Er verhindert, dass Fotos und Videos mehrfach hochgeladen werden.
- Er macht eine lokale Datenbank zur Verwaltung hochgeladener Dateien überflüssig.
- Bereits hochgeladene Medien werden nicht erneut hochgeladen, auch wenn sie später bearbeitet werden.

### Medienkonvertierung

Wenn die Medienkonvertierung aktiviert ist, wendet der automatische Upload die ausgewählten Konvertierungseinstellungen automatisch an, bevor Fotos und Videos hochgeladen werden.
