---
sidebar_position: 2
id: desktop-client-symlinks
title: Symlinks werden nicht synchronisiert
description: Umgang des Desktop-Clients mit symbolischen Links
draft: false
hide_table_of_contents: true
---

# Symlinks werden mit dem Desktop-Client nicht synchronisiert

## Problem

Symbolische Links (Symlinks) werden vom OpenCloud Desktop-Client nicht synchronisiert. Verlinkte Ordner oder Dateien können fehlen oder nicht zugänglich sein.

## Ursache

Symlinks werden aus mehreren Gründen bewusst von der Synchronisation ausgeschlossen:

- Nicht portabel: Symlinks verweisen oft auf Pfade, die nur auf dem ursprünglichen Rechner existieren. Auf einem anderen Gerät ist der Zielpfad in der Regel nicht vorhanden.
- Nicht im Webinterface nutzbar: Das Webinterface kann Symlinks nicht interpretieren oder darstellen.
- Problematisch unter Windows: Die Unterstützung von Symlinks unter Windows ist eingeschränkt und inkonsistent.
- Gefahr von Endlosschleifen: Symlinks könnten aufeinander verweisen und so zu einer endlosen Synchronisationsschleife führen.
- Identitätsverlust: Würde der Client dem Link folgen und das Ziel synchronisieren, entstünde eine reguläre Kopie der Daten. Die ursprüngliche Eigenschaft als Symlink ginge verloren.

## Lösung

### Ordner außerhalb des Synchronisationsverzeichnisses mit Symlinks einbinden

Um einen Ordner außerhalb Ihres Synchronisationsverzeichnisses zu synchronisieren, verschieben Sie ihn in das Synchronisationsverzeichnis und ersetzen seinen ursprünglichen Speicherort durch einen Symlink.

#### Beispiel

Sie möchten den Ordner `/foo/A` synchronisieren, aber Ihr Synchronisationsverzeichnis ist `/home/bar/OpenCloud/Personal`.

1. Verschieben Sie den Ordner in ein Unterverzeichnis Ihres Synchronisationsverzeichnisses:

   ```bash
   mkdir -p /home/bar/OpenCloud/Personal/foo/
   mv /foo/A /home/bar/OpenCloud/Personal/foo/A
   ```

2. Erstellen Sie am ursprünglichen Speicherort einen Symlink:

   ```bash
   ln -s /home/bar/OpenCloud/Personal/foo/A /foo/A
   ```
