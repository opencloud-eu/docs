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
- Schlägt der Schritt auch nach der maximalen Anzahl an Versuchen fehl, wird die Verarbeitung abgebrochen. In diesem Fall bleibt die Datei nicht verfügbar, bis ein Administrator die Verarbeitung fortsetzt.
- Findet der Virenscan Schadsoftware, wird die Datei je nach Serverkonfiguration gelöscht oder bleibt gesperrt.

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

Office-Dateien werden spätestens nach 30 Minuten automatisch freigegeben, auch wenn eine Bearbeitungssitzung nicht sauber beendet wurde.

Wenn die Datei dauerhaft gesperrt bleibt, sollte ein Administrator die Ursache prüfen.

## Wann sollte ein Administrator prüfen?

Ein Administrator sollte prüfen, wenn:

- eine Office-Datei mehr als 30 Minuten, nachdem alle Benutzer sie geschlossen haben, noch gesperrt ist
- eine hochgeladene Datei im Verarbeitungsstatus bleibt
- mehrere Dateien betroffen sind
- Benutzer trotz Bearbeitungsrechten nicht speichern können
- die Datei für alle Benutzer blockiert ist

Wenn die Verarbeitung von Uploads fehlgeschlagen ist, kann ein Administrator die Upload-Sitzungen mit den folgenden Befehlen auflisten und fehlgeschlagene Uploads fortsetzen:

```bash
opencloud storage-users uploads sessions
opencloud storage-users uploads sessions --resume
```
