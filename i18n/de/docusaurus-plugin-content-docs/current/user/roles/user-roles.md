---
sidebar_position: 1
id: user-roles
title: Rollen für Nutzer
---

## Nutzerrollen in OpenCloud

| Rolle          | Persönlicher Space| Spaces erstellen | Spaces verwalten  | Nutzer und Gruppen verwalten  |
| :-------------| :-:           | :-:           | :-:                   | :-:                      |
| Administrator |   x           |     x         | x                     | x                        |
| Space Admin   |   x           |     x         | x                     | -                        |
| User          |   x           |     -         | x                     | -                        |
| User Light    |   -           |     -         | x                     | -                        |


### Administrator

Die Administrator-Rolle in OpenCloud hat die gleichen Fähigkeiten wie ein Space-Administrator, verfügt aber zusätzlich über spezielle Berechtigungen zur Verwaltung von Benutzern, Gruppen und Systemeinstellungen. 
Allerdings haben Administratoren keinen direkten Zugriff auf Space-Daten oder die Möglichkeit, Benutzer zu Spaces hinzuzufügen, für die sie nicht die Rolle „kann verwalten“ haben. Nachfolgend sind die wichtigsten Aktionen aufgeführt, die ein Administrator durchführen kann:

- #### Lokale Benutzer und Gruppen erstellen und löschen

    Administratoren können neue lokale Benutzer hinzufügen und bestehende lokale Benutzer aus dem System entfernen.
    Sie können auch lokale Gruppen erstellen und löschen, um Benutzer effizient zu organisieren.

- #### Benutzer und Gruppen bearbeiten

    Benutzerdetails wie Namen, E-Mail-Adressen und Rollen können geändert werden.
    Gruppen können durch Hinzufügen oder Entfernen von Mitgliedern nach Bedarf aktualisiert werden.

- #### Anmeldung verhindern

    Falls erforderlich, können Administratoren Benutzerkonten deaktivieren und so verhindern, dass sie sich anmelden können.
    Dies ist nützlich aus Sicherheitsgründen oder wenn ein Konto nicht mehr benötigt wird.

- #### Spaces verwalten (ohne Zugriff auf Space-Daten)

    Administratoren können Spaces verwalten, z. B. aktivieren, deaktivieren oder löschen, umbenennen oder die Quote anpassen, auch wenn sie nicht die Rolle „kann verwalten“ haben.
    Sie können jedoch nicht auf die Dateien innerhalb eines Spaces zugreifen oder ihm Mitglieder hinzufügen.

- #### Das Logo ändern

    Das Systemlogo kann aktualisiert werden, um das Firmenbranding widerzuspiegeln.
    Dies kann in den Admin-Einstellungen unter dem Abschnitt „Allgemein“ vorgenommen werden.


### Raumverwalter

Ein Space-Administrator hat die höchste Ebene der Kontrolle über Spaces. Er kann:
- Spaces erstellen und verwalten
- in Spaces, die er nicht erstellt hat, die Rolle „Kann bearbeiten“ zugewiesen bekommen
- Einen persönlichen Space haben, in dem er Dateien und Ordner erstellen und Daten hochladen kann


### Benutzer

Ein normaler Benutzer hat Zugang zu seinem eigenen Space und kann Teil anderer Spaces sein. Er kann:
- Dateien und Ordner in seinem persönlichen Space erstellen
- Eigene Daten hochladen und verwalten
- Als Mitglied zu einem Space hinzugefügt werden
- Kann die Rolle „Kann bearbeiten“ in einem Space haben


### Benutzer Light

Ein User Light hat einen eingeschränkten Zugang und verfügt nicht über einen eigenen Space. Er kann:
- Als Mitglied zu einem Space hinzugefügt werden
- Kann die Rolle „Kann bearbeiten“ in einem Space haben
- Er kann keine Dateien und Ordner erstellen oder Daten in einen persönlichen Space hochladen.