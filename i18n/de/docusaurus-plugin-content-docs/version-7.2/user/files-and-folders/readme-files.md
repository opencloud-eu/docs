---
sidebar_position: 50
title: README-Dateien in Ordnern
description: Erfahren Sie, wie README.md-Dateien in Ordnern in OpenCloud gerendert werden.
---

# README-Dateien in Ordnern

Wenn ein Ordner eine Datei mit dem Namen `README.md` enthält, rendert OpenCloud deren Markdown-Inhalt oberhalb der Dateiliste.

<img src={require("./img/readme-files/readme-list-view.png").default} alt="README in der Listenansicht gerendert, während die Datei noch sichtbar ist" width="1920"/>

## README-Datei erstellen

1. Öffnen Sie den Ordner, in dem Sie das README hinzufügen möchten.
2. Erstellen oder laden Sie eine Datei mit dem Namen `README.md` hoch.
3. Fügen Sie Ihren Markdown-Inhalt hinzu und speichern Sie die Datei.

OpenCloud rendert den Inhalt, wenn der Ordner geöffnet oder aktualisiert wird.

## Unterstützter Dateiname

Der Dateiname muss genau so lauten:

```text
README.md
```

## Beispiel

Eine `README.md`-Datei kann zum Beispiel folgenden Markdown-Inhalt enthalten:

```markdown
# Fotos

Dieser Ordner enthält visuelle Beispiele für Vorschauen und Doku-Screenshots.

Die Bilder werden verwendet, um das Verhalten der Listenansicht, der Kachelansicht und der Bildvorschau in OpenCloud zu zeigen.

## Dateien

- moon-surface-public-domain.jpg
- rotated-chessboard-photo.jpg
- vintage-computer-terminal.jpg
- Space-Nebula.jpg
```

## README-Bereich entfernen

Löschen oder benennen Sie `README.md` um, um den gerenderten Bereich zu entfernen.

<img src={require("./img/readme-files/readme-removed.png").default} alt="Ordner ohne den gerenderten README-Bereich" width="1920"/>
