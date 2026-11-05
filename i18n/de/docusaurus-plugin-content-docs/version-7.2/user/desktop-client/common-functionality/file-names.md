---
sidebar_position: 50
id: file-names
title: Dateinamensbeschränkungen
description: Dateinamensbeschränkungen im OpenCloud Desktop-Client
draft: false
---

# Dateinamensbeschränkungen im OpenCloud Desktop-Client

Bei der Verwendung des OpenCloud Desktop-Clients müssen Datei- und Ordnernamen bestimmte Anforderungen des Betriebssystems (OS) erfüllen, um eine reibungslose Synchronisierung zwischen verschiedenen Plattformen zu gewährleisten.  
Diese Einschränkungen werden nicht von OpenCloud erzwungen, sondern stammen aus systembedingten Beschränkungen.

## Wichtige Richtlinien

- Verwenden Sie keine verbotenen Zeichen oder reservierten Namen in Dateinamen – unabhängig vom Betriebssystem.
- Wenn Sie von Linux/macOS zu einer Windows-basierten Freigabe synchronisieren, stellen Sie sicher, dass die Dateinamen mit den Windows-Benennungsregeln kompatibel sind.
- Um unter Linux/macOS beim Synchronisieren mit Windows nur die Groß-/Kleinschreibung zu ändern (z. B. `File.txt` → `file.txt`), benennen Sie die Datei zunächst in einen komplett neuen Namen um, lassen Sie sie synchronisieren und benennen Sie sie danach in den gewünschten Namen um.

## Häufige Einschränkungen

### a. Maximale Pfadlänge

Windows begrenzt Dateipfade standardmäßig auf 260 Zeichen.  
Wenn Ihr Synchronisierungs-Stammverzeichnis diesen Wert überschreitet, zeigt der Desktop-Client folgende Warnung an:  
„The path 'YOUR.LONG.PATH' is too long. Please enable long paths in the Windows settings or choose a different folder.“

Unter Windows 10 und neuer kann diese Beschränkung aufgehoben werden, indem "Long Paths" aktiviert werden. Siehe [Microsoft-Dokumentation](https://learn.microsoft.com/de-de/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later).

### b. Verbotene Zeichen

| Betriebssystem | Verbotene Zeichen               |
| -------------- | ------------------------------- | ------------ |
| Windows        | `<`, `>`, `:`, `"`, `/`, `\`, ` | `, `?`, `\*` |

### c. Nicht druckbare ASCII-Zeichen

- Linux/macOS: NUL (Zeichencode 0)
- Windows: ASCII 0 – 31

Auch wenn diese Zeichen auf manchen Systemen gültig sind, führen sie häufig zu Problemen bei der Synchronisierung.

### d. Reservierte Dateinamen (Windows)

Vermeiden Sie die Verwendung folgender Dateinamen:  
`CON`, `PRN`, `AUX`, `NUL`, `COM1` – `COM9`, `LPT1` – `LPT9`

### e. Besondere Regeln

- Unter Linux/macOS beim Synchronisieren zu SMB können Dateinamen, die sich nur in der Groß-/Kleinschreibung unterscheiden, zu Konflikten führen – benennen Sie Dateien eindeutig, um Fehler zu vermeiden.
- Unter Windows dürfen Dateinamen nicht mit einem Leerzeichen oder Punkt (`.`) enden.

## Beispiel

Das Erstellen einer Datei mit dem Namen `example.` oder `example.LPT1` unter macOS kann zwar erfolgreich mit OpenCloud synchronisiert werden.  
Beim Zugriff über einen Windows-Client werden diese Dateien jedoch möglicherweise abgelehnt, da sie gegen reservierte Namens- oder Formatregeln verstoßen, was zu inkonsistentem Synchronisierungsverhalten zwischen Geräten führt.

## Zusammenfassung

| Einschränkungstyp         | Maßnahme                                               |
| ------------------------- | ------------------------------------------------------ |
| Pfadlänge                 | Pfade unter ~260 Zeichen halten (außer bei Long Paths) |
| Verbotene Zeichen         | Nicht erlaubte Zeichen aus Namen entfernen             |
| Steuerzeichen             | Nicht druckbare ASCII-Zeichen vermeiden                |
| Reservierte Dateinamen    | Keine Windows-reservierten Namen verwenden             |
| Nur Groß-/Kleinschreibung | Vorher temporär umbenennen, dann synchronisieren       |
| Endzeichen                | Keine Dateinamen mit Leerzeichen oder Punkt beenden    |
