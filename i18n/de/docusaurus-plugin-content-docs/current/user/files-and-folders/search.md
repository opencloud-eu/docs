---
sidebar_position: 70
id: search
title: Suche
description: Nutzen der Suche in OpenCloud
draft: false
---

# Die Suche in OpenCloud verwenden

Mit der Suchleiste in der Kopfleiste können Sie Dateien und Ordner anhand ihrer Namen, Inhalte oder zugewiesenen Tags finden. Ein Tag kann mit Ihrer Suche übereinstimmen, auch wenn der Suchbegriff weder im Namen noch im Inhalt vorkommt.

## So funktioniert die Suche

- Die Suchleiste befindet sich oben in der Kopfleiste der Weboberfläche.
  <img src={require("./img/search/searchbar.png").default} alt="Suchleiste" width="700"/>
- Tastenkürzel: Drücken Sie `/` oder geben Sie `s` ein, um die Suchleiste zu fokussieren.
- Klicken Sie auf das Dropdown-Menü neben der Suchleiste.
- Wählen Sie, ob Sie in allen Dateien oder nur im aktuellen Ordner suchen möchten.
  <img src={require("./img/search/drop-down-menu-searchbar.png").default} alt="Auswahl, wo gesucht werden soll" width="500"/>
- Geben Sie einen Suchbegriff ein. Die Suche berücksichtigt Datei- und Ordnernamen, Dateiinhalte und zugewiesene Tags.
  <img src={require("./img/search/search-example.png").default} alt="Suchbeispiel" width="700"/>

## Mit Tags suchen

Geben Sie den Namen eines zugewiesenen Tags in die Suchleiste ein. Dateien und Ordner mit diesem Tag werden in den Suchergebnissen angezeigt, auch wenn der Name des Tags weder in ihren Namen noch in ihren Inhalten vorkommt.

## Suchergebnisse nach Tags filtern

- Öffnen Sie die vollständigen Suchergebnisse.
- Öffnen Sie den Tag-Filter, um die verfügbaren Tags anzuzeigen.
- Wählen Sie einen Tag aus, um nur Elemente mit diesem Tag anzuzeigen.

<img src={require("./img/search/tag-filter-search-results.png").default} alt="Nach dem Tag Wichtig gefilterte Suchergebnisse" width="1920"/>

## Übereinstimmende Suchergebnisse anzeigen

Die Suchergebnisse zeigen, warum ein Element gefunden wurde:

- Ein übereinstimmender Tag wird unterhalb des Ergebnisses angezeigt.
- Bei Übereinstimmungen im Inhalt wird ein passender Textausschnitt unterhalb des Dateinamens angezeigt.
- Übereinstimmende Begriffe werden im Textausschnitt hervorgehoben.

<img src={require("./img/search/content-search-results.png").default} alt="Suchergebnisse mit hervorgehobenen Texttreffern" width="1920"/>
