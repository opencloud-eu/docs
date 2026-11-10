---
sidebar_position: 20
id: external
title: Extern
description: Externes Teilen von Dateien und Ordnern in OpenCloud
draft: false
---

# Öffentliche Links - Externes Teilen von Dateien und Ordnern in OpenCloud

Öffentliche Links ermöglichen es Ihnen, Dateien und Ordner mit Personen außerhalb Ihrer Organisation zu teilen.

Öffentliche Links verwenden Link-Berechtigungen und identifizieren keine einzelnen Empfänger. Sie unterscheiden sich von internen Freigaberollen und dem [Gastzugang](./guest-access.md). Ein User Light kann einen öffentlichen Link erstellen, wenn öffentliche Links verfügbar sind und die Berechtigungen für die Ressource dies zulassen. Einen Vergleich finden Sie unter [Freigabemethoden](./index.md).

## Schritte zum Erstellen eines öffentlichen Links

- Klicken Sie mit der rechten Maustaste auf die Datei oder den Ordner oder klicken Sie auf das Drei-Punkte-Menü neben dem Namen, um das Kontextmenü zu öffnen.
- Wählen Sie im Kontextmenü die Option „Teilen“ aus.

  <img src={require("./img/extern/share-drop-down-menu.png").default} alt="Teilen auswählen" width="1920"/>

- Auf der rechten Seite des Bildschirms wird eine Seitenleiste geöffnet.
  <img src={require("./img/extern/sidebar-window.png").default} alt="Seitenleiste zum Teilen" width="400"/>

- Klicken Sie auf „Link hinzufügen“, um das Fenster zur Link-Konfiguration zu öffnen.

  <img src={require("./img/extern/public-link-option-pop-up.png").default} alt="Konfiguration eines öffentlichen Links" width="1920"/>

- Klicken Sie auf „Optionen“, um den Link zu konfigurieren.
- Wählen Sie die gewünschten Zugriffsrechte für die Empfänger aus:

  <img src={require("./img/extern/access-rights.png").default} alt="Verfügbare Berechtigungen für einen öffentlichen Link" width="1920"/>

  | Berechtigung           | Beschreibung                                                                                                                                     |
  | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
  | **Kann anzeigen**      | Empfänger können die freigegebenen Inhalte anzeigen und herunterladen, aber nicht verändern oder Dateien hochladen.                              |
  | **Kann bearbeiten**    | Empfänger können Inhalte anzeigen, herunterladen, hochladen, bearbeiten und löschen.                                                             |
  | **File Drop (geheim)** | Empfänger können Dateien in einen freigegebenen Ordner hochladen, ohne dessen vorhandene Inhalte anzuzeigen, herunterzuladen oder zu bearbeiten. |

- Geben Sie ein Passwort in das Feld unter „Passwort“ ein. Ein Passwort ist erforderlich, sofern ein Administrator die Einstellung nicht geändert hat.
- Optional können Sie ein Ablaufdatum festlegen.
- Nachdem Sie die Link-Optionen konfiguriert haben, klicken Sie auf „Link kopieren“, um den öffentlichen Link zu erstellen und zu kopieren.
  Um das Passwort mit einzuschließen, öffnen Sie das Menü neben „Link kopieren“ und wählen Sie „Link und Passwort kopieren“.

  <img src={require("./img/extern/password-section.png").default} alt="Passwort, Ablaufdatum und Kopieroptionen für einen öffentlichen Link" width="1920"/>

- Der Link ist jetzt erstellt und kann mit den Empfängern geteilt werden.
  <img src={require("./img/extern/copy-link-button.png").default} alt="Erstellter öffentlicher Link" width="1920"/>

- Sie können den Link später bearbeiten, indem Sie auf das Drei-Punkte-Menü rechts neben dem Link klicken.

  <img src={require("./img/extern/link-actions-menu.png").default} alt="Aktionen für einen öffentlichen Link" width="1920"/>

  Dort können Sie den Link umbenennen, das Ablaufdatum ändern, das Passwort aktualisieren, das Passwort entfernen oder den Link löschen.
