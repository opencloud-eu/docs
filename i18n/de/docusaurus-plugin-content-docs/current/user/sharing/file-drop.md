---
sidebar_position: 3
id: file-drop
title: File Drop
description: File Drop (geheim)
draft: false
---

# File Drop (geheim) - So funktioniert es

File Drop ermöglicht es Personen, die einen bestimmten Link erhalten, Dateien in einen freigegebenen Ordner hochzuladen.
Die Linkempfänger können die Dateien, die sich bereits im Ordner befinden, nicht sehen.

## Einen File Drop erstellen

- Klicken Sie mit der rechten Maustaste auf die Datei oder den Ordner oder klicken Sie auf das Drei-Punkte-Menü neben dem Namen, um das Kontextmenü zu öffnen.
- Wählen Sie im Kontextmenü „Teilen“ aus.
  <img src={require("./img/file-drop/share-drop-down-menu.png").default} alt="Dropdown-Menü" width="1920" />
- Auf der rechten Seite des Bildschirms wird eine Seitenleiste geöffnet.
  <img src={require("./img/file-drop/sidebar-window.png").default} alt="Seitenleiste" width="400" />
- Suchen Sie in der Seitenleiste den Bereich „Öffentliche Links“ und klicken Sie auf „Link hinzufügen“.
  <img src={require("./img/file-drop/add-link-button.png").default} alt="Link hinzufügen" width="400" />
- Klicken Sie auf „Optionen“, um die Linkeinstellungen zu öffnen.
- Öffnen Sie das Dropdown-Menü für die Zugriffsrechte und wählen Sie „File Drop (geheim)“.
  <img src={require("./img/file-drop/file-drop-button.png").default} alt="File Drop auswählen" width="1920" />

- Geben Sie ein Passwort ein und klicken Sie auf „Link kopieren“, um zu bestätigen.
- Sie können auch ein „Ablaufdatum“ festlegen, wenn der Link ablaufen soll.
  <img src={require("./img/file-drop/password-and-copy-link-button.png").default} alt="Passwort eingeben und Link kopieren" width="1920" />
- Teilen Sie den Link und das Passwort mit dem Empfänger.

## Was der Empfänger macht

- Der Empfänger öffnet den erhaltenen Link in einem Browser und gibt das Passwort ein. Anschließend klickt er auf „Weiter“.
  <img src={require("./img/file-drop/password-and-continue.png").default} alt="Passwort eingeben und weiter" width="1920" />
- Dateien hochladen:
  - Der File-Drop-Ordner wird geöffnet. Der Empfänger kann Dateien hochladen, ohne den vorhandenen Inhalt des Ordners zu sehen.
    <img src={require("./img/file-drop/file-drop-area.png").default} alt="File-Drop-Bereich" width="1920" />
  - Unten rechts erscheint ein Pop-up-Fenster, das bestätigt, dass der Upload erfolgreich war.
    <img src={require("./img/file-drop/upload-confirmation.png").default} alt="Upload-Bestätigung" width="1920" />

:::important
Empfänger haben keinen Zugriff auf vorhandene Dateien. Sie können nur neue Dateien hinzufügen.
:::

Jetzt wissen Sie, wie Sie einen File-Drop-Link freigeben.
