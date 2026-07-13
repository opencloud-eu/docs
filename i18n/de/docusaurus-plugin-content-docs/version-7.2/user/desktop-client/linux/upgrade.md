---
sidebar_position: 5
id: upgrade-linux
title: OpenCloud Desktop Client unter Linux aktualisieren
description: OpenCloud Desktop Client unter Linux aktualisieren
draft: false
---

# OpenCloud Desktop Client unter Linux aktualisieren

Der OpenCloud Desktop Client für Linux wird als AppImage bereitgestellt.

Wenn Sie OpenCloud Desktop mit AppImageLauncher installiert haben, können Sie den Client aktualisieren, indem Sie das aktualisierte AppImage herunterladen und die vorhandene integrierte Version ersetzen.

Bestehende Konten, Synchronisierungseinstellungen, Präferenzen, zwischengespeicherte Daten und Zugangsdaten bleiben beim Upgrade erhalten.

## Neueste AppImage-Datei herunterladen

Laden Sie die neueste `.AppImage`-Datei von der offiziellen Release-Seite herunter:

- [OpenCloud Desktop Releases auf GitHub](https://github.com/opencloud-eu/desktop/releases)

Wählen Sie das AppImage, das zur Architektur Ihres Systems passt, und speichern Sie es in Ihrem Download-Ordner oder einem anderen leicht auffindbaren Ort.

## OpenCloud Desktop schließen

Schließen Sie vor Beginn des Upgrades den laufenden Desktop Client:

1. Öffnen Sie das OpenCloud Desktop-Menü.
2. Beenden Sie bei Bedarf die aktive Synchronisierung.
3. Wählen Sie OpenCloud Desktop beenden.

So wird sichergestellt, dass alle Synchronisierungsprozesse vor dem Upgrade sauber gestoppt werden.

## Vorhandenes AppImage ersetzen

So aktualisieren Sie OpenCloud Desktop mit AppImageLauncher:

1. Klicken Sie mit der rechten Maustaste auf die heruntergeladene `.AppImage`-Datei.
2. Wählen Sie Öffnen mit AppImageLauncher.
3. Bestätigen Sie bei Aufforderung, dass die vorhandene integrierte Version ersetzt werden soll.

AppImageLauncher ersetzt das vorhandene AppImage und behält den Eintrag im Anwendungsmenü bei.

## Aktualisierte Anwendung starten

Starten Sie nach Abschluss des Upgrades OpenCloud Desktop über Ihr Anwendungsmenü:

1. Öffnen Sie Ihren Anwendungsstarter.
2. Suchen Sie nach OpenCloud Desktop.
3. Starten Sie die Anwendung.

Der Client sollte normal starten und Ihre vorhandene Konfiguration verwenden.

## Installierte Version überprüfen

So überprüfen Sie, ob das Upgrade erfolgreich war:

1. Öffnen Sie OpenCloud Desktop.
2. Öffnen Sie die Einstellungen.
3. Wählen Sie Info.
4. Überprüfen Sie die angezeigte Versionsnummer.

Die aktuell installierte Versionsnummer wird im Info-Dialog angezeigt.

:::note
Durch das Upgrade werden keine synchronisierten Dateien entfernt.

Bestehende Benutzerkonten und Synchronisierungsverbindungen bleiben konfiguriert.

Ein Neustart des Systems ist nach dem Upgrade in der Regel nicht erforderlich.
:::
