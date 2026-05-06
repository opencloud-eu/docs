---
sidebar_position: 80
id: locked-files
title: Gesperrte Dateien
description: Wann Dateien in OpenCloud gesperrt sein können und wie sich das für Benutzer auswirkt.
---

# Gesperrte Dateien

OpenCloud kann Dateien vorübergehend als gesperrt oder nicht verfügbar markieren. Für Benutzer bedeutet das: Die Datei kann in diesem Zustand nicht wie gewohnt geöffnet, bearbeitet, gespeichert oder synchronisiert werden.

Eine Datei kann aus verschiedenen Gründen gesperrt sein. Häufige Ursachen sind eine aktive Office-Bearbeitung oder eine noch laufende Verarbeitung nach dem Upload.

## Wann kann eine Datei gesperrt sein?

Eine Datei kann gesperrt sein, wenn:

- sie gerade in einer integrierten Office-Anwendung geöffnet oder bearbeitet wird
- mehrere Benutzer gemeinsam an derselben Office-Datei arbeiten
- eine Office-Bearbeitungssitzung noch nicht sauber beendet wurde
- ein Upload noch verarbeitet wird
- ein Virenscan noch läuft
- ein Verarbeitungsschritt nach dem Upload noch nicht abgeschlossen ist

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

Eine Datei kann auch nach einem Upload gesperrt sein, während OpenCloud sie verarbeitet.

Zu diesen Verarbeitungsschritten können gehören:

- Virenscan
- Metadatenverarbeitung
- Vorschauerstellung
- Aktualisierung des Suchindex

Solange diese Verarbeitung nicht abgeschlossen ist, kann die Datei für Benutzer gesperrt oder nur eingeschränkt verfügbar sein.

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

1. einige Minuten warten
2. die Dateiliste neu laden
3. prüfen, ob die Datei noch in einem anderen Browser-Tab geöffnet ist
4. prüfen, ob die Datei auf einem anderen Gerät geöffnet ist
5. prüfen, ob ein Sync-Client die Datei gerade hochlädt oder synchronisiert
6. die Office-Datei schließen und erneut öffnen

Wenn die Datei dauerhaft gesperrt bleibt, sollte ein Administrator die Ursache prüfen.

## Wann sollte ein Administrator prüfen?

Ein Administrator sollte prüfen, wenn:

- die Datei über längere Zeit gesperrt bleibt
- mehrere Dateien betroffen sind
- Dateien nach dem Upload nicht freigegeben werden
- Office-Dateien nach dem Schließen weiterhin gesperrt bleiben
- Benutzer trotz Bearbeitungsrechten nicht speichern können
- die Datei für alle Benutzer blockiert ist
