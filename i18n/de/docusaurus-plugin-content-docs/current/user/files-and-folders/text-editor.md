---
id: text-editor
sidebar_position: 40
title: Texteditor
description: Textdokumente und Notizen in OpenCloud erstellen, formatieren, gemeinsam bearbeiten und speichern.
---

# Den Texteditor verwenden

Ab OpenCloud 8.0 können Sie mit dem integrierten, auf Tiptap basierenden Texteditor verschiedene Textdateien direkt im Browser bearbeiten. Erstellen und formatieren Sie Markdown-Dokumente und OpenCloud-Notizen, ohne zusätzliche Software zu installieren. Wenn die gemeinsame Bearbeitung aktiviert ist, können mehrere Personen gleichzeitig an einem Dokument arbeiten.

## Dokument erstellen oder öffnen

So erstellen Sie ein Dokument:

1. Öffnen Sie den Ordner oder Space, in dem Sie das Dokument speichern möchten.
2. Wählen Sie `Neu`.
3. Wählen Sie `Notiz` für eine `.ocnote`-Datei oder `Markdown-Datei` für eine `.md`-Datei.
4. Geben Sie einen Dateinamen ein und bestätigen Sie die Erstellung.

Das neue Dokument wird automatisch im Texteditor geöffnet.

Um ein vorhandenes Dokument zu öffnen, wählen Sie es in der Dateiliste aus. Falls es nicht standardmäßig im Texteditor geöffnet wird, öffnen Sie das Kontextmenü der Datei und wählen Sie `Öffnen mit ...` und anschließend `Texteditor`.

<img src={require("./img/text-editor/editor-overview.png").default} alt="Texteditor mit einem formatierten Markdown-Dokument" width="1920"/>

:::note

Zum Bearbeiten einer Datei benötigen Sie die entsprechende Berechtigung. Mit Leseberechtigung können Sie das Dokument ansehen und bei gemeinsamer Bearbeitung die Änderungen anderer mitverfolgen, aber selbst keine Änderungen vornehmen.

:::

## Dateiformat auswählen

Welches Format sich am besten eignet, hängt davon ab, wie Sie das Dokument verwenden möchten.

| Format | Geeignet für | Formatierungsmöglichkeiten |
| --- | --- | --- |
| Markdown (`.md`) | Dokumente, die Sie auch außerhalb von OpenCloud mit anderen Markdown-Editoren bearbeiten möchten | Überschriften, Textauszeichnungen, Listen, Zitate, Links, Bilder, Tabellen und Code |
| OpenCloud-Notiz (`.ocnote`) | Notizen mit zusätzlichen Formatierungsmöglichkeiten, die Sie hauptsächlich in OpenCloud bearbeiten | Markdown-ähnliche Funktionen sowie Schriftgröße, Text- und Hintergrundfarben, Zeilenabstand, Textausrichtung, Unterstreichung, Tief- und Hochstellung |
| Einfacher Text (`.txt`) | Texte ohne Formatierung, beispielsweise Protokolle oder einfache Notizen | Keine Textformatierung; Suchen, Ersetzen und Drucken sind weiterhin möglich |

OpenCloud-Notizen werden als `.ocnote`-Dateien im JSON-Format gespeichert. Sie sind keine Markdown-Dateien und bieten zusätzliche Formatierungsmöglichkeiten.

<img src={require("./img/text-editor/note-formatting.png").default} alt="OpenCloud-Notiz mit erweiterten Formatierungsoptionen und geöffnetem Menü für die Textfarbe" width="1920"/>

## Inhalte formatieren

Über die Formatierungsleiste können Sie Änderungen rückgängig machen oder wiederherstellen, Text formatieren, Listen erstellen und weitere Inhalte einfügen. Wenn nicht alle Schaltflächen in das Fenster passen, finden Sie die übrigen Funktionen unter `Weitere Aktionen`.

<img src={require("./img/text-editor/formatting-toolbar.png").default} alt="Formatierungsleiste des OpenCloud-Texteditors" width="1505"/>

So formatieren Sie Text:

1. Markieren Sie den gewünschten Text oder setzen Sie den Cursor in den Absatz, den Sie ändern möchten.
2. Über `Umwandeln in` können Sie beispielsweise einen Absatz, eine Überschrift, ein Zitat oder einen Codeblock auswählen.
3. Verwenden Sie die Formatierungsleiste, um Text beispielsweise fett, kursiv oder durchgestrichen darzustellen oder eine Liste zu erstellen.

### Slash-Menü verwenden

Geben Sie am Anfang einer Zeile `/` ein, um das Slash-Menü zu öffnen. Sie können anschließend nach einer Funktion suchen oder direkt einen Eintrag auswählen, beispielsweise eine Überschrift, eine Liste, ein Zitat, einen Codeblock, einen Link, ein Bild oder eine Tabelle.

<img src={require("./img/text-editor/slash-menu.png").default} alt="Slash-Menü mit Funktionen zum Formatieren und Einfügen von Inhalten" width="900"/>

Wenn Sie den Mauszeiger neben einen Inhaltsblock bewegen, können Sie über `Inhalt hinzufügen` einen weiteren Block einfügen. Mit `Zum Verschieben ziehen` können Sie Blöcke am Computer an eine andere Position verschieben.

### Link einfügen

1. Markieren Sie den Text, den Sie verlinken möchten, oder setzen Sie den Cursor an die gewünschte Stelle.
2. Wählen Sie `Link` in der Formatierungsleiste oder im Slash-Menü.
3. Geben Sie die Zieladresse und den Linktext ein.

<img src={require("./img/text-editor/insert-link.png").default} alt="Dialog zum Einfügen eines Links mit Feldern für die Adresse und den Linktext" width="900"/>

### Code einfügen

Verwenden Sie `Inline-Code`, um einzelne Codeelemente innerhalb eines Satzes darzustellen. Für längere Codeabschnitte wählen Sie `Codeblock` über `Umwandeln in` oder das Slash-Menü. Der Editor bietet Syntaxhervorhebung für unterstützte Programmiersprachen. Er erkennt die Sprache nach Möglichkeit automatisch; Sie können sie auch selbst auswählen.

<img src={require("./img/text-editor/code-block.png").default} alt="Codeblock mit Syntaxhervorhebung und Auswahl der Programmiersprache" width="900"/>

## Bilder und Tabellen einfügen

### Bild einfügen

1. Setzen Sie den Cursor an die Stelle, an der Sie das Bild einfügen möchten.
2. Wählen Sie `Bild einfügen` in der Formatierungsleiste oder geben Sie `/image` ein.
3. Wählen Sie eine der verfügbaren Optionen:
   - `Bild aus Datei`: Laden Sie ein Bild von Ihrem Gerät hoch.
   - `Bild von URL`: Fügen Sie ein Bild über eine `http://`- oder `https://`-Adresse ein.
   - `Aus Cloud einfügen`: Wählen Sie ein Bild aus, das bereits in OpenCloud gespeichert ist. Diese Option steht beim Zugriff über einen öffentlichen Link nicht zur Verfügung.
4. Klicken Sie auf das eingefügte Bild, um seine Größe mithilfe der Ziehpunkte anzupassen.

<img src={require("./img/text-editor/insert-image.png").default} alt="Menü mit den verfügbaren Optionen zum Einfügen eines Bildes" width="900"/>

### Tabelle einfügen

1. Setzen Sie den Cursor an die Stelle, an der Sie die Tabelle einfügen möchten.
2. Wählen Sie `Tabelle erstellen` in der Formatierungsleiste oder im Slash-Menü.
3. Legen Sie die Anzahl der Zeilen und Spalten fest.
4. Klicken Sie in eine Tabellenzelle, um die Bearbeitungsfunktionen aufzurufen.

Mit den Tabellenfunktionen können Sie Zeilen und Spalten hinzufügen oder entfernen, die Kopfzeile aktivieren oder deaktivieren und die Tabelle löschen.

<img src={require("./img/text-editor/insert-table.png").default} alt="Tabelle in einem Dokument" width="900"/>

## Text suchen und im Dokument navigieren

### Text suchen und ersetzen

Öffnen Sie `Suchen und Ersetzen` über die Formatierungsleiste oder mit `Strg + F` (`Cmd + F` unter macOS). Geben Sie den Suchbegriff und bei Bedarf den Text ein, durch den Sie ihn ersetzen möchten. Sie können die Suche auf ganze Wörter beschränken oder die Groß- und Kleinschreibung berücksichtigen.

<img src={require("./img/text-editor/find-replace.png").default} alt="Such- und Ersetzen-Funktion im OpenCloud-Texteditor" width="1920"/>

### Über das Inhaltsverzeichnis navigieren

Für Markdown-Dateien und OpenCloud-Notizen erstellt der Editor automatisch ein Inhaltsverzeichnis aus den Überschriften des Dokuments. Öffnen Sie dazu den Bereich `Gliederung`.

Klicken Sie auf eine Überschrift, um direkt zur entsprechenden Stelle zu springen. Beim Scrollen wird die aktuelle Position im Inhaltsverzeichnis hervorgehoben. Wenn Sie Überschriften ändern, wird das Inhaltsverzeichnis automatisch aktualisiert.

<img src={require("./img/text-editor/table-of-contents.png").default} alt="Markdown-Dokument mit geöffnetem Bereich Gliederung" width="1920"/>

## Dokumente gemeinsam bearbeiten

Markdown-Dateien und OpenCloud-Notizen können von mehreren Personen gleichzeitig bearbeitet werden. Änderungen werden in Echtzeit zwischen den geöffneten Editoren synchronisiert. In der Formatierungsleiste sehen Sie, wer das Dokument gerade geöffnet hat. Farbige Cursor zeigen an, an welcher Stelle andere Personen arbeiten.

Personen mit Bearbeitungsberechtigung können Änderungen vornehmen. Mit Leseberechtigung können Sie die gemeinsame Bearbeitung mitverfolgen, ohne selbst Inhalte zu ändern.

<img src={require("./img/text-editor/collaboration.png").default} alt="Gemeinsame Bearbeitung eines Markdown-Dokuments mit zwei aktiven Personen" width="1920"/>

### Andere Personen erwähnen

Geben Sie in einem Markdown-Dokument oder einer OpenCloud-Notiz `@` ein und wählen Sie eine Person aus der Vorschlagsliste. Angezeigt werden nur Personen, die bereits Zugriff auf das Dokument haben.

Die Benachrichtigung über die Erwähnung wird nach dem Speichern des Dokuments versendet. Ob die erwähnte Person eine Benachrichtigung erhält, hängt von den Benachrichtigungseinstellungen ab.

Über öffentliche Links können Sie keine Personen erwähnen.

<img src={require("./img/text-editor/mentions.png").default} alt="Vorschlagsliste für die Erwähnung einer Person im Texteditor" width="1920"/>

:::note

Für die gemeinsame Bearbeitung in Echtzeit muss der Yjs-Dienst eingerichtet sein. Informationen zur Einrichtung finden Administratoren unter [Gemeinsames Bearbeiten mit dem Yjs-Server](../../admin/configuration/collaborative-editing).

:::

Bei der gemeinsamen Bearbeitung gelten folgende Einschränkungen:

- Über öffentliche Links ist keine gemeinsame Bearbeitung in Echtzeit möglich. Personen mit Schreibberechtigung können das Dokument weiterhin bearbeiten und speichern. Ihre Änderungen werden jedoch nicht unmittelbar in anderen geöffneten Editoren angezeigt.
- In Ende-zu-Ende-verschlüsselten Ordnern ist die gemeinsame Bearbeitung deaktiviert.
- Während der gemeinsamen Bearbeitung ist der Quelltextmodus schreibgeschützt, da sich direkte Änderungen am Quelltext nicht mit der gemeinsamen Bearbeitung zusammenführen lassen.

## Änderungen speichern

Bei der gemeinsamen Bearbeitung ist zwischen der Synchronisierung der Änderungen und dem Speichern der Datei zu unterscheiden:

- Änderungen werden sofort zwischen den Personen synchronisiert, die gemeinsam am Dokument arbeiten.
- Die Datei wird gespeichert, wenn jemand `Speichern` auswählt, `Strg + S` (`Cmd + S` unter macOS) drückt oder die automatische Speicherung erfolgt.
- Das Intervall für die automatische Speicherung legt der Administrator fest. Wenn die automatische Speicherung aktiviert ist, wird das Intervall im Editor angezeigt.

Wenn eine andere Anwendung, beispielsweise der Desktop Client, die geöffnete Datei verändert, erhalten Sie im Editor einen Hinweis. Liegen keine ungespeicherten Änderungen vor, lädt der Editor automatisch die neuere Version.

Haben Sie noch ungespeicherte Änderungen, können Sie diese mit `Speichern unter` in einer separaten Datei sichern. Alternativ können Sie die Seite neu laden. Dabei werden Ihre ungespeicherten Änderungen verworfen und die extern geänderte Version geöffnet.

Bei jedem Speichern wird die Datei in OpenCloud aktualisiert. Frühere Dateistände stehen entsprechend den Regeln der [Dateiversionierung](./versions.md) zur Verfügung.

## Gut zu wissen

- Markdown-Dateien können auch mit anderen Markdown-Editoren bearbeitet werden. Die Darstellung kann sich je nach Anwendung leicht unterscheiden.
- OpenCloud-Notizen (`.ocnote`) unterstützen Formatierungen, die Markdown nicht abbilden kann. Sie sind für die Bearbeitung im OpenCloud-Texteditor vorgesehen.
- Codeblöcke bieten Syntaxhervorhebung für gängige Programmier- und Konfigurationssprachen.
- Über `Drucken` öffnen Sie den Druckdialog des Systems. Je nach Betriebssystem können Sie das Dokument dort auch als PDF speichern. Die PDF-Datei wird lokal gespeichert und nicht automatisch in OpenCloud abgelegt.
- Wie Sie eine `README.md` oberhalb der Dateiliste eines Ordners anzeigen, erfahren Sie unter [README-Dateien in Ordnern](./readme-files.md).