---
sidebar_position: 3
id: share-roles
title: Rollen beim Teilen
description: Rollen beim Teilen in OpenCloud
draft: false
---

# Rollen beim Teilen in OpenCloud

| Rolle                           | anzeigen | hochladen | bearbeiten | hinzufügen | löschen | nur doc, img, pdf mit Wasserzeichen anzeigen |
| :------------------------------ | :------: | :-------: | :--------: | :--------: | :-----: | :------------------------------------------: |
| Kann anzeigen (sichere Ansicht) |    -     |     -     |     -      |     -      |    -    |                      x                       |
| Kann anzeigen                   |    x     |     -     |     -      |     -      |    -    |                      -                       |
| Kann hochladen                  |    x     |     x     |     -      |     -      |    -    |                      -                       |
| Kann bearbeiten                 |    x     |     x     |     x      |     x      |    x    |                      -                       |

## Kann anzeigen (sichere Ansicht)

Die Rolle `Kann anzeigen (sichere Ansicht)` erlaubt Empfängern, unterstützte
Dateien in einem eingeschränkten Viewer anzuzeigen.

Empfänger mit dieser Rolle können:

- Dokumente, Bilder und PDF-Dateien anzeigen
- Dateien mit Wasserzeichen anzeigen

Empfänger mit dieser Rolle können keine Dateien und Ordner hochladen, bearbeiten,
hinzufügen oder löschen.

## Kann anzeigen

Die Rolle `Kann anzeigen` erlaubt Empfängern, gemeinsam genutzte Dateien und
Ordner anzuzeigen.

Im Vergleich zu `Kann anzeigen (sichere Ansicht)` können Empfänger mit dieser
Rolle geteilte Inhalte ohne den eingeschränkten Viewer und ohne Wasserzeichen
anzeigen.

Empfänger mit dieser Rolle können keine Dateien und Ordner hochladen, bearbeiten,
hinzufügen oder löschen.

## Kann hochladen

Die Rolle `Kann hochladen` enthält die Berechtigungen von `Kann anzeigen` und
erlaubt Empfängern, Dateien und Ordner hochzuladen.

Empfänger mit dieser Rolle können:

- Dateien und Ordner anzeigen
- Dateien und Ordner herunterladen
- Dateien und Ordner hochladen

Empfänger mit dieser Rolle können keine Dateien und Ordner bearbeiten, hinzufügen
oder löschen.

## Kann bearbeiten

Die Rolle `Kann bearbeiten` enthält die Berechtigungen von `Kann anzeigen` und
erlaubt Empfängern, gemeinsam genutzte Inhalte zu ändern.

Empfänger mit dieser Rolle können:

- Dateien hochladen
- Dateien und Ordner erstellen
- Dateien und Ordner bearbeiten
- Dateien und Ordner löschen

Jede Rolle bietet eine andere Zugriffsstufe, damit jeder Benutzer die richtigen
Berechtigungen erhält.
