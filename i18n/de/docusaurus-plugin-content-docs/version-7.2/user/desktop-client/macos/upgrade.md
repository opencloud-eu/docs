---
sidebar_position: 4
id: upgrade-macos
title: Upgrade Desktop Client on macOS
description: Upgrade Desktop Client on macOS
draft: false
---

# OpenCloud Desktop Client unter macOS aktualisieren

Der OpenCloud Desktop Client für macOS kann mit dem offiziellen signierten `.pkg`-Installationsprogramm aktualisiert werden.

Bei der Aktualisierung wird die vorhandene Anwendung ersetzt, während Ihre Kontoeinstellungen, Synchronisierungskonfiguration, Anwendungseinstellungen, zwischengespeicherte Daten und Anmeldedaten erhalten bleiben.

## Aktuelles Installationsprogramm herunterladen

Laden Sie das aktuelle `.pkg`-Installationsprogramm von der offiziellen Release-Seite herunter:

- [OpenCloud Desktop Releases auf GitHub](https://github.com/opencloud-eu/desktop/releases)

Wählen Sie das Installationsprogramm aus, das zu der Architektur Ihres Macs passt:

- Apple Silicon Macs (M1, M2, M3): `arm64`
- Intel Macs: `x86_64`

Speichern Sie das Installationsprogramm in Ihrem Download-Ordner oder an einem anderen Speicherort, an dem Sie es leicht wiederfinden.

## OpenCloud Desktop schließen

Beenden Sie den Desktop Client, bevor Sie mit der Aktualisierung beginnen:

1. Klicken Sie auf das Symbol von OpenCloud Desktop in der macOS-Menüleiste.
2. Öffnen Sie das Menü.
3. Wählen Sie **OpenCloud Desktop beenden**.

Dadurch wird sichergestellt, dass alle Synchronisierungsvorgänge vor der Aktualisierung ordnungsgemäß beendet werden.

## Installationsprogramm ausführen

So aktualisieren Sie OpenCloud Desktop:

1. Doppelklicken Sie auf die heruntergeladene `.pkg`-Datei.
2. Folgen Sie den Anweisungen des macOS-Installationsprogramms.
3. Bestätigen Sie auf Nachfrage, dass die vorhandene Installation ersetzt werden soll.

Das Installationsprogramm aktualisiert die Anwendung im Ordner **Programme**.

Vorhandene Konten, Synchronisierungsordner, Anwendungseinstellungen, zwischengespeicherte Daten und Anmeldedaten bleiben dabei automatisch erhalten.

## Aktualisierte Anwendung starten

Nachdem die Installation abgeschlossen wurde, können Sie OpenCloud Desktop auf eine der folgenden Arten starten:

- Über den Ordner **Programme**
- Über das **Launchpad**
- Über **Spotlight**

Der Desktop Client sollte anschließend wie gewohnt starten und Ihre vorhandene Konfiguration weiterverwenden.

## Installierte Version überprüfen

So überprüfen Sie, ob die Aktualisierung erfolgreich war:

1. Öffnen Sie OpenCloud Desktop.
2. Öffnen Sie die **Einstellungen**.
3. Wählen Sie **Über** und überprüfen Sie die angezeigte Versionsnummer.

Im Dialog **Über** wird die aktuell installierte Versionsnummer angezeigt.

:::note

Bei einer Aktualisierung werden keine synchronisierten Dateien entfernt.

Vorhandene Benutzerkonten und Synchronisierungsverbindungen bleiben erhalten.

Ein Neustart des Systems ist nach der Aktualisierung in der Regel nicht erforderlich.

:::
