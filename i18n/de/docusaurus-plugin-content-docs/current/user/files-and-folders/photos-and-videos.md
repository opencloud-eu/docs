---
sidebar_position: 60
title: Fotos und Videos
description: Erfahren Sie, wie OpenCloud Fotos in der Vorschau anzeigt und Videos direkt im Web abspielt.
---

# Fotos und Videos

OpenCloud kann Fotos, Motion Photos, Live Photos und Videos direkt in der Weboberfläche anzeigen beziehungsweise abspielen. Sie können Medien aus dem aktuellen Ordner durchsuchen, ohne jede Datei zuerst herunterzuladen.

## Fotovorschau

Öffnen Sie ein Foto, um es in der Vorschau anzuzeigen. Die Fotogalerie zeigt die anderen Mediendateien im Ordner an, für die eine Vorschau verfügbar ist. Wählen Sie eine Miniaturansicht aus oder verwenden Sie „Vorherige Mediendatei im Ordner anzeigen“ und „Nächste Mediendatei im Ordner anzeigen“, um zwischen den Dateien zu wechseln.

Mit den Steuerelementen der Vorschau können Sie:

- Das Bild vergrößern oder verkleinern. Sie können dazu auch `Ctrl` beziehungsweise `⌘` unter macOS gedrückt halten und das Mausrad verwenden.
- Das Bild um 90 Grad nach links oder rechts drehen.
- „Zurücksetzen“ auswählen, um die ursprüngliche Vergrößerung und Drehung wiederherzustellen.
- Die Fotogalerie ein- oder ausblenden.
- Den Vollbildmodus aufrufen oder verlassen.

<!-- TODO: photo-roll-screenshot.png aktualisieren, um die aktuelle Fotovorschau, die Fotogalerie und die gruppierten Steuerelemente zu zeigen. -->

<img src={require("./img/photos-and-videos/photo-roll-screenshot.png").default} alt="Photo-Roll-Ansicht in OpenCloud" width="1920"/>

## Unterstützte Bildformate

Die Vorschau unterstützt Dateien in den Formaten JPEG, PNG, GIF, HEIC, HEIF, AVIF und SVG.

- Für die Vorschau von HEIC-, HEIF- und AVIF-Dateien wird eine vom Server erzeugte Miniaturansicht verwendet. Wenn keine Vorschau erzeugt werden kann, bietet OpenCloud die Datei zum Herunterladen an.
- SVG-Dateien können in der Vorschau geöffnet werden, sind jedoch nicht in der Fotogalerie enthalten. Einige ungewöhnliche SVG-Dateien, beispielsweise Dateien mit eingebetteten Bitmap-Bildern, werden möglicherweise nicht dargestellt.
- In Ende-zu-Ende-verschlüsselten Ordnern dekodiert der Browser die Bilder anstelle des Servers. Die Unterstützung für die Vorschau von HEIC-, HEIF- und AVIF-Dateien hängt daher vom Browser ab. HEIC-Vorschauen sind beispielsweise in Safari verfügbar. Wenn der Browser das Bild nicht dekodieren kann, zeigt die Vorschau eine Meldung an.

:::note
Die Vorschau von HEIC-, HEIF- und AVIF-Dateien hängt von der serverseitigen Erzeugung von Miniaturansichten und der Serverkonfiguration ab.
:::

<!--
Weitere Informationen finden Sie in der Dokumentation zur [Konfiguration von Miniaturansichten](/docs/admin/configuration/thumbnail-configuration).
-->

## Motion Photos und Live Photos

### Motion Photos anzeigen

OpenCloud unterstützt Live Photos, die mit Apple-Geräten erstellt wurden, und Motion Photos von Android-Geräten.

- Ein Wiedergabesymbol kennzeichnet Motion Photos und Live Photos in der Tabellen- und Kachelansicht.
- Bewegen Sie den Mauszeiger in der Kachelansicht über das Foto, um es in einer Schleife abzuspielen. Verwenden Sie das Wiedergabesymbol, um die Wiedergabe zu starten oder anzuhalten.
- Wenn Sie das Foto in der Vorschau öffnen, wird es einmal automatisch abgespielt. Anschließend wird das Standbild angezeigt.
- Wählen Sie in der Vorschau „Live Photo abspielen“ oder „Bewegungsaufnahme abspielen“ aus, um es erneut abzuspielen. Während der Wiedergabe ändert sich das Steuerelement in „Live Photo pausieren“ beziehungsweise „Bewegungsaufnahme pausieren“.

<!-- TODO: Screenshot einer erkannten Live Photo in der Kachelansicht hinzufügen. -->

<!-- TODO: Screenshot der Steuerelemente für die Wiedergabe einer Live Photo in der Vorschau hinzufügen. -->

<video controls width="960" style={{ maxWidth: "100%" }} aria-label="Wiedergabe einer Motion Photo in OpenCloud">

  <source src={require("./img/photos-and-videos/motion-photo-playback.mp4").default} type="video/mp4" />
  Ihr Browser unterstützt keine eingebetteten Videos.
</video>

### Live Photos hochladen

Eine Apple Live Photo besteht aus einem Standbild im HEIC- oder JPG-Format und einem dazugehörigen MOV-Video. So laden Sie eine Live Photo manuell über die OpenCloud-Weboberfläche hoch:

1. Öffnen Sie den Ordner, in dem Sie die Live Photo speichern möchten.
2. Laden Sie sowohl das Standbild (`.HEIC` oder `.JPG`) als auch das dazugehörige Video (`.MOV`) in diesen Ordner hoch.
3. Stellen Sie sicher, dass beide Dateien denselben Basisdateinamen haben. Sie können beide Dateien umbenennen, solange die Basisdateinamen identisch bleiben.

Sie können beispielsweise jede Live Photo in einem eigenen Ordner ablegen:

```text
IMG_0762/
├── IMG_0762.HEIC
└── IMG_0762.MOV
```

Der umgebende Ordner ist optional, kann die Organisation von Live Photos jedoch vereinfachen. Die beiden Dateien können auch gemeinsam umbenannt werden, zum Beispiel:

```text
Earth.HEIC
Earth.MOV
```

Wenn OpenCloud die Dateien als Live Photo erkennt, öffnen Sie das Standbild in der Vorschau, um die Animation abzuspielen.

## Videowiedergabe

Videos werden in der Vorschau geöffnet und verwenden die Videosteuerung des Browsers. Sie können das Video abspielen oder anhalten, durch die Zeitleiste navigieren, die Lautstärke anpassen und den Vollbildmodus aufrufen. Die verfügbaren Steuerelemente und deren Darstellung können je nach Browser variieren.

Die Symbolleiste unterhalb der Vorschau gruppiert zusammengehörige Aktionen: die Navigation zwischen Mediendateien, Steuerelemente für die Ansicht und Dateiaktionen wie das Hinzufügen zu den Favoriten oder das Löschen der Datei, sofern verfügbar.

<video controls width="960" style={{ maxWidth: "100%" }} aria-label="Videowiedergabe in OpenCloud">

  <source src={require("./img/photos-and-videos/video-playback.mp4").default} type="video/mp4" />
  Ihr Browser unterstützt keine eingebetteten Videos.
</video>

## Hinweise

- Das Laden sehr großer Mediendateien kann länger dauern.
