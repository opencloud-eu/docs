---
sidebar_position: 3
id: desktop-client-office-lock-files
title: Microsoft-Office-Sperrdateien werden nicht synchronisiert
description: Warum der Desktop-Client Microsoft-Office-Sperrdateien ausschließt
draft: false
hide_table_of_contents: true
---

# Microsoft-Office-Sperrdateien werden nicht synchronisiert

## Problem

Der OpenCloud Desktop-Client synchronisiert keine Dateien, die mit `~$` beginnen, wie z. B. `~$document.docx`.

<img src={require("../common-issues/img/desktop-excluded.png").default} alt="Anzeige, dass ~$ Dateien von der Synchronisierung ausgeschlossen sind" width="500"/>

## Ursache

Diese Dateien sind temporäre Sperrdateien, die von Microsoft-Office-Anwendungen erstellt werden, solange ein Dokument geöffnet ist. Es sind keine Inhaltsdateien, sondern interne Marker, die verhindern, dass mehrere Benutzer gleichzeitig dasselbe Dokument bearbeiten.

## Lösung

Schließen Sie das Dokument in Microsoft Office. Office entfernt die zugehörige `~$`-Datei automatisch.

Weitere Informationen finden Sie im [Microsoft-Supportartikel zu temporären Office-Sperrdateien von Word, Excel und PowerPoint](https://support.microsoft.com/en-gb/topic/-the-document-is-locked-for-editing-by-another-user-error-message-when-you-try-to-open-a-document-in-word-10b92aeb-2e23-25e0-9110-370af6edb638?).
