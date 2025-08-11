---
sidebar_position: 3
id: file-drop
title: File Drop
description: File Drop (geheim)
draft: false
---

# File Drop (geheim) - So funktioniert es

Mit dem File Drop können Personen, die einen bestimmten Link erhalten (die sogenannten "Linkempfänger"), Dateien in einen gemeinsamen Ordner hochladen
Der Trick: Die "Linkempfänger“ können die bereits im Ordner befindlichen Dateien nicht sehen.

## Erstellen Sie eine "Dateiablage"

- Klicken Sie auf das "Drei-Punkte-Menü“ neben dem Namen der Datei oder des Ordners, den Sie freigeben möchten.
  <img src={require("./img/file-drop/drei-punkte-menue.png").default} alt="Drei Punkte Menü" width="1920"/>
- Wählen Sie Teilen aus dem Dropdown-Menü.

  <img src={require("./img/file-drop/teilen-menue.png").default} alt="Drop down Menü" width="400"/>

- Auf der rechten Seite des Bildschirms öffnet sich ein Sidebar-Fenster.
  <img src={require("./img/file-drop/sidebar-fenster.png").default} width="1920"/>
- Im Seitenleistenfenster finden Sie den Bereich Öffentliche Links und klicken dort auf die Schaltfläche Link hinzufügen.
  <img src={require("./img/file-drop/link-hinzufuegen.png").default} alt="Seitenleistenfenster" width="400"/>
- Wählen Sie die Option "File Drop“ aus.
  <img src={require("./img/file-drop/file-drop-button.png").default} alt="Filedrop auswählen" width="400"/>
- Geben Sie ein Passwort ein und bestätigen Sie die Eingaben mit einem Klick auf "Link kopieren“.
- Du kannst außerdem ein „Ablaufdatum“ festlegen, wenn der Link automatisch ablaufen soll. Weitere Informationen zur Einstellung eines Ablaufdatums findest du unter [Externe Freigabe](./external).

  <img src={require("./img/file-drop/passwort-und-link-kopieren.png").default} alt="Passwort eingeben und Link kopieren" width="400"/>

- Nun senden Sie den Link und das Passwort an einen "Linkempfänger".

## To do's für den "Linkempfänger“

- Der "Linkempfänger“ öffnet den empfangenen Link in einem Browser.
  <img src={require("./img/file-drop/file-drop-website.png").default} alt="File drop website" width="1920"/>
- Der "Linkempfänger" gibt das Passwort ein und klickt dann auf "Weiter“.
  <img src={require("./img/file-drop/passwort-popup.png").default} alt="Passwort eingeben und Weiter klicken" width="400"/>
- Dateien hochladen:
  - Der "Dateiablageordner“ wird geöffnet. Der "Linkempfänger“ kann hier seine Dateien hochladen, ohne den vorhandenen Inhalt des Ordners einsehen zu können.
    <img src={require("./img/file-drop/file-drop-bildschirm.png").default} alt="File drop area" width="1920"/>
  - Zur Bestätigung, dass der Upload erfolgreich war, erscheint ein Pop-up-Fenster in der unteren rechten Ecke.
    <img src={require("./img/file-drop/hochladen-bestaedigung.png").default} alt="Upload bestätigt" width="1920"/>

:::important
Der "Linkempfänger“ hat keinen Zugriff auf bestehende Dateien - er kann nur neue Dateien hinzufügen.
:::
