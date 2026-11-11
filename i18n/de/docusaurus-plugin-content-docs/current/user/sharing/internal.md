---
sidebar_position: 10
id: internal
title: Intern
description: Organisationsinterne Freigabe von Dateien und Ordnern in OpenCloud
draft: false
---

# Organisationsinterne Freigabe von Dateien und Ordnern in OpenCloud

Dateien und Ordner können innerhalb der Organisation mit einzelnen Mitgliedern oder Gruppen geteilt werden. Dabei können unterschiedliche Zugriffsrechte vergeben werden.

Zum Erstellen einer internen Freigabe ist die systemweite Nutzerrolle `Person`, `Space Admin` oder `Administrator` erforderlich. Ein User Light kann keine internen Freigaben erstellen, auch wenn ihm in einem Space die Rolle `Kann verwalten` zugewiesen wurde. User-Light-Konten können weiterhin Freigaben erhalten und entsprechend den zugewiesenen Berechtigungen mit freigegebenen Inhalten arbeiten. Weitere Informationen finden Sie unter [Nutzerrollen in OpenCloud](../roles/user-roles.md#user-light).

## Interne Freigabe erstellen

- Öffnen Sie das Drei-Punkte-Menü neben der Datei oder dem Ordner, den Sie freigeben möchten.

- Wählen Sie im Kontextmenü die Option „Teilen“ aus.

  <img src={require("./img/intern/share-drop-down-menu.png").default} alt="Teilen auswählen" width="1920"/>

- Die Seitenleiste wird auf der rechten Seite des Bildschirms geöffnet.

  <img src={require("./img/intern/sidebar-window.png").default} alt="Seitenleiste anzeigen" width="1920"/>

- Verwenden Sie das Feld „Mit Personen teilen“ am oberen Rand der Seitenleiste.

  <img src={require("./img/intern/share-with-people-section.png").default} alt="Mit Personen teilen" width="400"/>

- Geben Sie mindestens drei Zeichen in das Suchfeld ein, um nach Mitgliedern oder Gruppen zu suchen.

  <img src={require("./img/intern/searchbar.png").default} alt="Nach Personen oder Gruppen suchen" width="400"/>

- Wählen Sie die gewünschte Person oder Gruppe aus der Vorschlagsliste aus.

- Legen Sie die Zugriffsrechte für die ausgewählten Mitglieder oder Gruppen fest:

  <img src={require("./img/intern/rights-options.png").default} alt="Rechte auswählen" width="400"/>

  | Berechtigung                        | Beschreibung                                                                                                                                                        |
  | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **Kann anzeigen**                   | Mitglieder können die freigegebenen Inhalte anzeigen und herunterladen.                                                                                             |
  | **Kann anzeigen (sichere Ansicht)** | Mitglieder können Dokumente, Bilder und PDF-Dateien nur im Browser anzeigen. Das Herunterladen ist nicht möglich und die Inhalte werden mit Wasserzeichen versehen. |
  | **Kann hochladen**                  | Mitglieder können die freigegebenen Inhalte anzeigen und herunterladen sowie neue Dateien hochladen. Diese Berechtigung ist nur für freigegebene Ordner verfügbar.  |
  | **Kann bearbeiten**                 | Mitglieder können Inhalte anzeigen, herunterladen, hochladen, erstellen, bearbeiten und löschen.                                                                    |

- Optional: Öffnen Sie das Drei-Punkte-Menü neben der Schaltfläche „Teilen“ und wählen Sie „Ablaufdatum festlegen“. Wählen Sie das Datum aus, an dem die Freigabe automatisch ablaufen soll.

  <img src={require("./img/intern/expiration-date.png").default} alt="Ablaufdatum für eine interne Freigabe festlegen" width="400"/>

- Klicken Sie auf „Teilen“, um die interne Freigabe zu erstellen.

Die freigegebenen Mitglieder oder Gruppen werden anschließend im Bereich „Freigegeben mit“ angezeigt.

<img src={require("./img/intern/shared-with-alan.png").default} alt="Freigegebene Mitglieder anzeigen" width="400"/>

## Interne Freigabe entfernen

Eine bestehende interne Freigabe kann jederzeit entfernt werden.

- Öffnen Sie im Bereich „Freigegeben mit“ das Drei-Punkte-Menü neben der Person oder Gruppe.

- Wählen Sie die Option „Freigabe entfernen“ aus.

<img src={require("./img/intern/remove-share.png").default} alt="Freigabe entfernen" width="400"/>

Der Zugriff wird sofort entfernt. Die betroffene Person oder Gruppe kann danach nicht mehr über diese Freigabe auf die Datei oder den Ordner zugreifen.
