---
sidebar_position: 1
id: user-roles
title: Rollen für Nutzer
---

# Nutzerrollen in OpenCloud

| Rolle         | kann Space-Manager sein | Persönlicher Space | Spaces erstellen/löschen | Nutzer und Gruppen verwalten |
| :------------ | :---------------------: | :----------------: | :----------------------: | :--------------------------: |
| User Light    |            x            |         -          |            -             |              -               |
| Person        |            x            |         x          |            -             |              -               |
| Space Admin   |            x            |         x          |            x             |              -               |
| Administrator |            x            |         x          |            x             |              x               |

## User Light

Ein User Light hat standardmäßig eingeschränkten Zugriff und keinen eigenen
Space.

Ein User Light kann:

- Zu einem Space hinzugefügt werden
- Die Rolle „Kann bearbeiten“ in einem Space erhalten

:::note
Wenn ein Nutzer zuvor die Rolle Person oder höher hatte und später wieder auf
User Light gesetzt wird, behält er seinen bestehenden persönlichen Space.
:::

## Person

Eine Person hat dieselben Möglichkeiten zur Mitgliedschaft in Spaces wie ein
User Light und zusätzlich einen eigenen persönlichen Space für eigene Dateien
und Ordner.

Eine Person kann:

- Dateien und Ordner im persönlichen Space erstellen
- Eigene Daten hochladen und verwalten

## Space Admin

Ein Space Admin kann alles tun, was eine Person kann. Zusätzlich kann ein Space
Admin Spaces auf administrativer Ebene verwalten.

Ein Space Admin kann:

- Spaces erstellen, löschen, aktivieren und deaktivieren
- Spaces umbenennen
- Space-Quoten anpassen
- Spaces verwalten, ohne auf deren Inhalte zuzugreifen

Space Admins können den Space selbst verwalten, auch wenn sie nicht Mitglied
des Spaces sind. Dazu gehören administrative Aktionen wie Aktivieren,
Deaktivieren, Löschen, Umbenennen oder Anpassen der Quote eines Spaces.

Space Admins können nicht auf die Dateien innerhalb eines Spaces zugreifen,
außer sie wurden mit der erforderlichen Space-Rolle zum Space hinzugefügt. Sie
können auch keine Mitglieder hinzufügen oder entfernen, außer sie haben in dem
Space die Rolle „Kann verwalten“.

## Administrator

Die Administrator-Rolle in OpenCloud hat die Rechte eines Space Admins und kann
zusätzlich Benutzer, Gruppen und Systemeinstellungen verwalten.

Ein Administrator kann:

- Lokale Benutzer erstellen und löschen
- Lokale Gruppen erstellen und löschen
- Benutzerdetails wie Namen, E-Mail-Adressen und Rollen bearbeiten
- Benutzer zu Gruppen hinzufügen oder aus Gruppen entfernen
- Benutzerkonten deaktivieren, um die Anmeldung zu verhindern
