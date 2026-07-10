---
sidebar_position: 5
id: upgrade-linux
title: Upgrade Desktop Client on Linux
description: Upgrade Desktop Client on Linux
draft: false
---

# OpenCloud Desktop Client unter Linux aktualisieren

Der OpenCloud Desktop Client für Linux wird als AppImage bereitgestellt.

Wenn Sie OpenCloud Desktop mit AppImageLauncher installiert haben, können Sie den Desktop Client aktualisieren, indem Sie die aktuelle AppImage-Datei herunterladen und die bereits integrierte Version ersetzen.

Vorhandene Konten, Synchronisierungseinstellungen, Anwendungseinstellungen, zwischengespeicherte Daten und Anmeldedaten bleiben während der Aktualisierung erhalten.

## Aktuelles AppImage herunterladen

Laden Sie die aktuelle `.AppImage`-Datei von der offiziellen Release-Seite herunter:

- [OpenCloud Desktop Releases auf GitHub](https://github.com/opencloud-eu/desktop/releases)

Wählen Sie das AppImage aus, das zu Ihrer Systemarchitektur passt, und speichern Sie die Datei in Ihrem Download-Ordner oder an einem anderen Speicherort, an dem Sie sie leicht wiederfinden.

## OpenCloud Desktop schließen

Beenden Sie den Desktop Client, bevor Sie mit der Aktualisierung beginnen:

1. Öffnen Sie das Menü von OpenCloud Desktop.
2. Beenden Sie bei Bedarf laufende Synchronisierungsvorgänge.
3. Wählen Sie **OpenCloud Desktop beenden**.

Dadurch wird sichergestellt, dass alle Synchronisierungsvorgänge vor der Aktualisierung ordnungsgemäß beendet werden.

## Vorhandenes AppImage ersetzen

So aktualisieren Sie OpenCloud Desktop mit AppImageLauncher:

1. Klicken Sie mit der rechten Maustaste auf die heruntergeladene `.AppImage`-Datei.
2. Wählen Sie **Mit AppImageLauncher öffnen**.
3. Bestätigen Sie auf Nachfrage, dass die bereits integrierte Version ersetzt werden soll.

AppImageLauncher ersetzt das vorhandene AppImage und behält den Eintrag im Anwendungsmenü bei.

## Aktualisierte Anwendung starten

Nachdem die Aktualisierung abgeschlossen wurde, starten Sie OpenCloud Desktop über Ihr Anwendungsmenü:

1. Öffnen Sie den Anwendungsstarter.
2. Suchen Sie nach **OpenCloud Desktop**.
3. Starten Sie die Anwendung.

Der Desktop Client sollte anschließend wie gewohnt starten und Ihre vorhandene Konfiguration weiterverwenden.

## Installierte Version überprüfen

So überprüfen Sie, ob die Aktualisierung erfolgreich war:

1. Öffnen Sie OpenCloud Desktop.
2. Öffnen Sie die **Einstellungen**.
3. Wählen Sie **Über**.
4. Überprüfen Sie die angezeigte Versionsnummer.

Im Dialog **Über** wird die aktuell installierte Versionsnummer angezeigt.

:::note

Bei einer Aktualisierung werden keine synchronisierten Dateien entfernt.

Vorhandene Benutzerkonten und Synchronisierungsverbindungen bleiben erhalten.

Ein Neustart des Systems ist nach der Aktualisierung in der Regel nicht erforderlich.

:::
