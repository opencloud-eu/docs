---
sidebar_position: 2
id: space-roles
title: Rollen für Spaces
---

### Rollen für Spaces in OpenCloud

| Role       | anzeigen  | herunterladen | hochladen     | bearbeiten  | erstellen   | löschen    | Mitglieder verwalten    |
| :----------| :-:   | :-:      | :-:        | :-:   | :-:   | :-:       | :-:               |
| kann anzeigen   |   x   |     x    | -          | -     | -     | -         | -                 |
| kann bearbeiten   |   x   |     x    | x          | x     | x     | x         | -                 |
| kann verwalten |   x   |     x    | x          | x     | x     | x         | x                 |


In einem Space können Mitglieder verschiedene Rollen haben, die ihnen unterschiedliche Zugriffsebenen geben.

### Kann anzeigen
Mit dieser Rolle kann das Mitglied Dateien im Space ansehen und herunterladen, aber keine Änderungen vornehmen, keine Dateien und Ordner hochladen oder neue erstellen.

### Kann bearbeiten
Mit dieser Rolle kann das Mitglied alles tun, was ein „Can View“-Mitglied tun kann, plus:
- Dateien in den Space hochladen
- Hinzufügen von neuen Dateien und Ordnern
- Löschen von Dateien und Ordnern, einschließlich ihrer Historie
- Gelöschte Dateien wiederherstellen

### Verwalten können
Diese Rolle gibt dem Mitglied alle Fähigkeiten von „Kann bearbeiten“, plus:
- Hinzufügen oder Entfernen von Mitgliedern aus dem Space
- Ändern der Rollen anderer Mitglieder im Space

**Jede Rolle bestimmt, was ein Mitglied innerhalb des Spaces tun kann!**

