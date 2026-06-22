---
sidebar_position: 2
id: space-roles
title: Rollen für Spaces
---

# Rollen für Spaces in OpenCloud

In einem Space können Mitglieder verschiedene Rollen haben. Jede Rolle legt
fest, was ein Mitglied innerhalb dieses Spaces tun kann.

| Rolle           | anzeigen | herunterladen | hochladen | bearbeiten | erstellen | löschen | Mitglieder verwalten | Space deaktivieren / aktivieren | Quota bearbeiten | Space löschen |
| :-------------- | :------: | :-----------: | :-------: | :--------: | :-------: | :-----: | :------------------: | :-----------------------------: | :--------------: | :-----------: |
| Kann anzeigen   |    x     |       x       |     -     |     -      |     -     |    -    |          -           |                -                |        -         |       -       |
| Kann bearbeiten |    x     |       x       |     x     |     x      |     x     |    x    |          -           |                -                |        -         |       -       |
| Kann verwalten  |    x     |       x       |     x     |     x      |     x     |    x    |          x           |                x                |        x         |       -       |

## Kann anzeigen

Die Rolle `Kann anzeigen` erlaubt es Mitgliedern, Dateien im Space anzuzeigen und
herunterzuladen.

Mit dieser Rolle können Mitglieder keine Dateien und Ordner hochladen,
erstellen, bearbeiten oder löschen.

## Kann bearbeiten

Die Rolle `Kann bearbeiten` enthält die Berechtigungen von `Kann anzeigen` und erlaubt es
Mitgliedern, mit Inhalten im Space zu arbeiten.

Mit dieser Rolle können Mitglieder:

- Dateien in den Space hochladen
- Dateien und Ordner erstellen
- Dateien und Ordner bearbeiten
- Dateien und Ordner löschen, einschließlich ihrer Historie
- Gelöschte Dateien wiederherstellen

## Kann verwalten

Die Rolle `Kann verwalten` enthält die Berechtigungen von `Kann bearbeiten` und erlaubt es
Mitgliedern, den Space zu verwalten.

Mit dieser Rolle können Mitglieder:

- Mitglieder zum Space hinzufügen
- Mitglieder aus dem Space entfernen
- Die Rollen anderer Space-Mitglieder ändern
- Den Space aktivieren und deaktivieren
- Die Space-Quote bearbeiten

:::note
Mit der Rolle `Kann verwalten` kann ein Space verwaltet werden, aber er kann nicht
gelöscht werden.

Das Löschen eines Spaces erfordert die OpenCloud-Nutzerrolle `Admin` oder
`Space Admin`. Weitere Informationen findest du unter [Nutzerrollen in
OpenCloud](./user-roles.md).
:::
