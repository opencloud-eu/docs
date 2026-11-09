---
sidebar_position: 10
id: settings
title: Einstellungen
description: Einstellungen
draft: false
---

# Überblick über den Admin-Bereich

Der Admin-Bereich von OpenCloud bietet die wichtigsten Werkzeuge zur Verwaltung Ihrer Organisation. Er steht nur Benutzern mit der Administratorrolle zur Verfügung. Andere Benutzer sehen die Admin-Einstellungen nicht im App-Umschalter.

Um den Admin-Bereich zu öffnen, wählen Sie oben rechts den App-Umschalter und anschließend „Admin-Einstellungen“. Die wichtigsten Bereiche werden im Folgenden beschrieben.

<img src={require("./img/settings/admin_settings.png").default} alt="Admin-Einstellungen" width="1920"/>

## Allgemein

- Versionsübersicht:
  Im Bereich „Allgemein“ können Sie Ihre aktuelle OpenCloud-Version einsehen und prüfen, ob eine neuere Version verfügbar ist.
- Ankündigungsbanner:
  Administratoren können allen Benutzern eine organisationsweite Nachricht anzeigen. Eine Anleitung zur Konfiguration finden Sie unter [Ankündigungsbanner](../../admin/configuration/announcement-banner.md).
  <img src={require("./img/settings/admin_general.png").default} alt="Allgemeine Admin-Einstellungen" width="1920"/>

:::note
Wenn ein sicherheitskritisches Upgrade verfügbar ist, können Administratoren zusätzlich eine Warnung unten links in der Weboberfläche sehen.
Ein Administrator kann die Versionsprüfung deaktivieren. Wenn diese Option ausgeschaltet ist, werden keine Informationen über neuere Versionen angezeigt.
:::

## Benutzer

- Benutzerübersicht:
  Hier sehen Sie alle Benutzer Ihrer OpenCloud-Instanz.
- Benutzerverwaltung:
  Abhängig von Ihren Benutzerverwaltungseinstellungen können Sie:
  - Benutzer erstellen oder löschen
  - Benutzer bearbeiten, beispielsweise Rechte oder Einstellungen ändern
  - Benutzerquoten ändern
  - Benutzer zu Gruppen hinzufügen oder aus Gruppen entfernen
  - die Anmeldung einzelner Benutzer erlauben oder sperren
    <img src={require("./img/settings/admin_users.png").default} alt="Benutzerverwaltung" width="1920"/>

:::note
Wenn OpenCloud mit einem externen IdP verbunden ist, können Sie die Benutzer hier weiterhin sehen. Die Benutzerverwaltung muss jedoch im IdP erfolgen.
:::

## Gruppen

- Gruppenübersicht:
  Hier sehen Sie die vorhandenen Gruppen Ihrer OpenCloud-Instanz.
- Gruppenverwaltung:
  Sie können lokale Gruppen erstellen, bearbeiten oder löschen und Mitglieder hinzufügen oder entfernen.
- Importierte Gruppen:
  Externe Gruppen, die über ein externes Benutzerverwaltungssystem importiert wurden, können hier nicht bearbeitet werden. Diese Gruppen sind mit einem Sperrsymbol als gesperrt gekennzeichnet.
  <img src={require("./img/settings/admin_groups.png").default} alt="Gruppenverwaltung" width="1920"/>

## Spaces

- Space-Übersicht:
  Hier sehen Sie alle vorhandenen Spaces Ihrer OpenCloud-Instanz.
- Space-Verwaltung:
  Als Administrator können Sie:
  - Spaces umbenennen
  - Beschreibungen, Untertitel, Bilder und Symbole anpassen
  - Space-Quoten ändern
  - Spaces deaktivieren oder aktivieren
  - deaktivierte Spaces löschen
    <img src={require("./img/settings/admin_spaces.png").default} alt="Space-Verwaltung" width="1920"/>

## Apps

- App-Übersicht:
  Hier sehen Sie die installierten Apps, deren Versionen, die kompatiblen OpenCloud-Versionen und den aktuellen Status.
  <img src={require("./img/settings/admin_apps.png").default} alt="Admin-Apps" width="1920"/>
