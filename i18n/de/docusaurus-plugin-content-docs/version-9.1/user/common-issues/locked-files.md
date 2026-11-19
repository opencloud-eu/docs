---
sidebar_position: 80
id: locked-files
title: Gesperrte Dateien
description: Wann Dateien in OpenCloud gesperrt sein können, wann sie wieder freigegeben werden und wie sich das für Benutzer auswirkt.
---

# Gesperrte Dateien

OpenCloud kann Dateien vorübergehend als gesperrt oder nicht verfügbar markieren. Für Benutzer bedeutet das: Die Datei kann in diesem Zustand nicht wie gewohnt geöffnet, bearbeitet, gespeichert oder synchronisiert werden.

Eine Datei kann aus verschiedenen Gründen gesperrt sein. Häufige Ursachen sind eine aktive Office-Bearbeitung oder eine noch laufende Verarbeitung nach dem Upload.

## Wann kann eine Datei gesperrt sein?

Eine Datei kann gesperrt sein, wenn:

- sie gerade in einer integrierten Office-Anwendung geöffnet oder bearbeitet wird
- mehrere Benutzer gemeinsam an derselben Office-Datei arbeiten
- eine Office-Bearbeitungssitzung noch nicht sauber beendet wurde
- ein Upload noch verarbeitet wird, zum Beispiel durch einen Virenscan
- ein WebDAV-Client sie gesperrt hat, zum Beispiel eine Desktop-Office-Anwendung, die Dateien über WebDAV öffnet, oder der macOS Finder

## Office-Bearbeitung

Office-Dateien können während der Bearbeitung gesperrt werden.

Das betrifft typischerweise Dateien wie:

- `.odt`
- `.ods`
- `.odp`
- `.docx`
- `.xlsx`
- `.pptx`

Während der Bearbeitung schützt die Sperre die Datei vor konkurrierenden Schreibzugriffen. Dadurch wird verhindert, dass Änderungen durch andere Schreibvorgänge überschrieben werden.

Bei gemeinsamer Office-Bearbeitung können mehrere Benutzer gleichzeitig in derselben Datei arbeiten. Auch in diesem Fall kann die Datei technisch gesperrt sein. Die Sperre verhindert dabei nicht die gemeinsame Bearbeitung innerhalb der Office-Anwendung, sondern schützt die Datei vor Schreibzugriffen außerhalb dieser Sitzung.

## WebDAV-Clients

Auch Anwendungen, die über WebDAV auf OpenCloud zugreifen, können Dateien sperren. Beispiele sind Desktop-Office-Anwendungen, die Dateien über WebDAV öffnen, oder der macOS Finder. Solange eine solche Sperre aktiv ist, können andere Benutzer und Anwendungen die Datei nicht ändern.

## Verarbeitung nach dem Upload

Je nach Serverkonfiguration verarbeitet OpenCloud eine Datei nach dem Upload, bevor sie verfügbar ist. Solange diese Verarbeitung läuft, kann die Datei weder geöffnet noch heruntergeladen werden.

Zu den Verarbeitungsschritten können gehören:

- ein Virenscan
- Prüfungen anhand von Richtlinien, die der Administrator festgelegt hat

## Wann wird eine Datei wieder freigegeben?

Wann eine Sperre aufgehoben wird, hängt von ihrer Ursache ab.

### Office-Bearbeitung

- Die Sperre wird aufgehoben, wenn der letzte Benutzer das Dokument oder den Browser-Tab schließt.
- Solange das Dokument geöffnet ist, erneuert die Office-Anwendung die Sperre regelmäßig. Die Sperre bleibt daher aktiv, solange jemand an dem Dokument arbeitet.
- Wenn die Bearbeitungssitzung nicht sauber beendet wird, zum Beispiel weil der Browser abgestürzt ist oder die Netzwerkverbindung unterbrochen wurde, läuft die Sperre spätestens nach 30 Minuten automatisch ab.

### Verarbeitung nach dem Upload

- Die Datei wird freigegeben, sobald alle Verarbeitungsschritte abgeschlossen sind. Das dauert in der Regel nur wenige Sekunden.
- Es gibt keine feste Zeitgrenze. Wenn ein Verarbeitungsschritt fehlschlägt, wiederholt OpenCloud ihn automatisch nach einer zunehmenden Wartezeit.
- Schlägt der Schritt auch nach der maximalen Anzahl an Versuchen fehl, wird die Verarbeitung abgebrochen und der Upload rückgängig gemacht. Eine neue Datei verschwindet wieder aus dem Ordner. Wurde eine vorhandene Datei überschrieben, kehrt sie zu ihrer vorherigen Version zurück. Benutzer sehen also keine gesperrte Datei, sondern der Upload fehlt oder ihre Änderungen wurden nicht gespeichert.
- Findet der Virenscan Schadsoftware, hängt das Ergebnis von der Serverkonfiguration ab:
  - Die Datei wird gelöscht. Das ist die Standardeinstellung.
  - Die Datei wird für eine Prüfung durch den Administrator aufbewahrt, aber nicht in den Ordner übernommen.
  - Die Datei wird als infiziert markiert, ist aber wie gewohnt verfügbar.

### WebDAV-Clients

Die Sperre wird aufgehoben, wenn der WebDAV-Client die Datei schließt und die Sperre entfernt oder wenn die vom Client festgelegte Sperrzeit abläuft.

## Wie wirkt sich eine Sperre aus?

Eine gesperrte Datei kann je nach Situation nicht oder nur eingeschränkt verwendet werden.

Mögliche Auswirkungen sind:

- die Datei wird mit einem Schloss-Symbol oder einem Verarbeitungsstatus angezeigt
- die Datei kann nicht bearbeitet werden
- die Datei kann nicht gespeichert werden
- die Datei kann nur lesend geöffnet werden
- die Datei ist vorübergehend nicht verfügbar
- beim Öffnen oder Speichern kann eine Fehlermeldung angezeigt werden

## Was können Benutzer tun?

In vielen Fällen ist eine Sperre nur vorübergehend. Benutzer können:

1. warten, bis die Verarbeitung eines Uploads abgeschlossen ist
2. die Dateiliste neu laden
3. prüfen, ob die Datei noch in einem anderen Browser-Tab geöffnet ist
4. prüfen, ob die Datei auf einem anderen Gerät geöffnet ist
5. prüfen, ob ein Sync-Client die Datei gerade hochlädt oder synchronisiert
6. die Office-Datei schließen und erneut öffnen
7. die Datei erneut hochladen, wenn ein Upload fehlt oder Änderungen nach dem Upload nicht gespeichert wurden

Office-Dateien werden spätestens nach 30 Minuten automatisch freigegeben, auch wenn eine Bearbeitungssitzung nicht sauber beendet wurde.

Wenn die Datei dauerhaft gesperrt bleibt, sollte ein Administrator die Ursache prüfen.

## Wann sollte ein Administrator prüfen?

Ein Administrator sollte prüfen, wenn:

- eine Office-Datei mehr als 30 Minuten, nachdem alle Benutzer sie geschlossen haben, noch gesperrt ist
- eine hochgeladene Datei im Verarbeitungsstatus bleibt
- Uploads wieder verschwinden oder Änderungen nach dem Upload zurückgesetzt werden
- mehrere Dateien betroffen sind
- Benutzer trotz Bearbeitungsrechten nicht speichern können
- die Datei für alle Benutzer blockiert ist

Wenn die Verarbeitung eines Uploads fehlgeschlagen ist, kann ein Administrator die Upload-Sitzungen auflisten und einen fehlgeschlagenen Upload neu starten. Listen Sie zuerst die Upload-Sitzungen auf und ermitteln Sie die ID des fehlgeschlagenen Uploads:

```bash
opencloud storage-users uploads sessions
```

Starten Sie diesen Upload anschließend neu:

```bash
opencloud storage-users uploads sessions --id <upload-id> --restart
```

Ersetzen Sie `<upload-id>` durch die ID des fehlgeschlagenen Uploads.

:::caution
Führen Sie den Befehl mit `--restart` nicht ohne einen Filter wie `--id` aus. Andernfalls betrifft der Befehl alle Upload-Sitzungen, auch Uploads, die gerade noch verarbeitet werden.

Die Option `--resume` hilft bei fehlgeschlagenen Uploads nicht. Nach der maximalen Anzahl an Versuchen gilt ein Upload als abgeschlossen, und `--resume` überspringt abgeschlossene Uploads.
:::
