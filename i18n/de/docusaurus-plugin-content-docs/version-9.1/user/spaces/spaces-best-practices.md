---
sidebar_position: 90
id: best-practice
title: Best Practices für die Organisation von Spaces
description: Erfahren Sie, wie Sie Dateien und Ordner in Spaces organisieren, damit Inhalte leicht zu finden, verständlich und übersichtlich bleiben.
draft: false
---

# Best Practices für die Organisation von Spaces

Spaces sind kollaborative Bereiche für Inhalte, die von mehreren Personen gemeinsam genutzt und gepflegt werden.

Eine gute Struktur hilft Nutzern, Inhalte schnell zu finden, und sorgt dafür, dass ein Space auch bei wachsenden Datenmengen übersichtlich bleibt.

Beachten Sie beim Organisieren eines Spaces zwei wesentliche Grundsätze:

1. Halten Sie Ordnerstrukturen flach.
2. Verwenden Sie aussagekräftige, eigenständig verständliche Dateinamen.

Als allgemeine Regel gilt:

> Die Ordnerstruktur sollte zusätzlichen Kontext liefern. Dateien sollten jedoch auch ohne diesen Kontext verständlich sein.

## Ordnerstrukturen flach halten

Vermeiden Sie tief verschachtelte Ordnerstrukturen.

Verwenden Sie als allgemeine Richtlinie höchstens drei Ordnerebenen. Halten Sie die Struktur nach Möglichkeit noch flacher.

Tiefe Strukturen erschweren die Navigation und setzen voraus, dass Nutzer genau wissen, wo eine Datei gespeichert wurde.

Vermeiden Sie Strukturen wie diese:

```text
Kunden/
└── Acme/
    └── Verträge/
        └── 2026/
            └── Final/
                └── vertrag.pdf
```

Reduzieren Sie stattdessen die Anzahl der Ebenen und nehmen Sie wichtige Informationen in den Dateinamen auf:

```text
Kunden/
└── Acme/
    └── Verträge/
        └── Acme - Dienstleistungsvertrag - 2026.pdf
```

Dadurch bleibt die Ordnerstruktur leicht navigierbar und die zum Identifizieren der Datei erforderlichen Informationen bleiben erhalten.

Erstellen Sie keine zusätzlichen Ordnerebenen, nur um Eigenschaften wie die folgenden abzubilden:

- Jahr
- Dokumentstatus
- Dokumenttyp
- Version
- verantwortliche Person

Prüfen Sie, ob Sie diese Informationen stattdessen in den Dateinamen aufnehmen können.

## Aussagekräftige Dateinamen verwenden

Ein Dateiname sollte den Inhalt beschreiben, ohne dass Nutzer den ursprünglichen Speicherort der Datei kennen müssen.

Dateien können außerhalb ihrer Ordnerstruktur erscheinen, wenn sie:

- in Suchergebnissen ausgegeben werden
- in einer Liste zuletzt verwendeter Dateien angezeigt werden
- heruntergeladen werden
- an eine E-Mail angehängt werden
- mit anderen Nutzern geteilt werden
- in einen anderen Ordner oder Space verschoben werden

Ein Dateiname wie:

```text
vertrag.pdf
```

liefert außerhalb seines ursprünglichen Ordners nur sehr wenige Informationen.

Ein aussagekräftigerer Dateiname ist:

```text
Acme - Dienstleistungsvertrag - 2026.pdf
```

Die Datei kann nun unabhängig von ihrem Speicherort identifiziert werden.

### Relevanten Kontext aufnehmen

Je nach Art des Inhalts können folgende Bestandteile im Dateinamen hilfreich sein:

- Kunden-, Team- oder Projektname
- Dokumenttyp
- Datum oder Jahr
- Berichtszeitraum
- Thema
- Status, falls relevant

Beispiele:

```text
Acme - Dienstleistungsvertrag - 2026.pdf
Marketing - Kampagnenbericht - 2026-Q2.pdf
Projekt Atlas - Besprechungsnotizen - 2026-08-11.odt
Klasse 3B - Elterninformation - Sommerausflug.pdf
```

Nehmen Sie nur Informationen auf, die beim Identifizieren der Datei helfen. Vermeiden Sie unnötig lange oder schwer lesbare Dateinamen.

## Einheitliche Namenskonventionen verwenden

Legen Sie eine Namenskonvention für einen Space fest und wenden Sie diese konsequent an.

Zum Beispiel:

```text
[Projekt] - [Dokumenttyp] - [Datum]
```

Daraus könnten folgende Dateinamen entstehen:

```text
Projekt Atlas - Budget - 2026.xlsx
Projekt Atlas - Besprechungsnotizen - 2026-08-11.odt
Projekt Atlas - Statusbericht - 2026-Q3.pdf
```

Einheitliche Dateinamen sind leichter zu erkennen und zeigen Nutzern, wie sie neue Dateien benennen sollten.

Wenn ein Dateiname ein Datum enthält, verwenden Sie ein einheitliches Format. Ein Format wie `JJJJ-MM-TT` sorgt außerdem dafür, dass Dateien chronologisch sortiert werden:

```text
2026-08-11 - Besprechungsnotizen.odt
2026-08-18 - Besprechungsnotizen.odt
2026-08-25 - Besprechungsnotizen.odt
```

## Inhalte nach Zweck organisieren

Ordner sollten sinnvolle Arbeitsbereiche abbilden und nicht jede mögliche Eigenschaft einer Datei.

Ein Team-Space könnte beispielsweise so aufgebaut sein:

```text
Marketing/
├── Kampagnen/
├── Berichte/
├── Vorlagen/
└── Archiv/
```

Die Dateien in diesen Ordnern sollten weiterhin aussagekräftige Namen verwenden:

```text
Marketing/
├── Kampagnen/
│   ├── Produkteinführung - Kampagnenplan - 2026.odt
│   └── Sommerkampagne - Ergebnisse - 2026.pdf
├── Berichte/
│   ├── Marketing - Monatsbericht - 2026-07.pdf
│   └── Marketing - Monatsbericht - 2026-08.pdf
├── Vorlagen/
│   └── Marketing - Kampagnenbriefing - Vorlage.odt
└── Archiv/
```

So ergänzen sich Ordnerstruktur und Dateinamen gegenseitig.

## Beispiele

Die geeignete Struktur hängt davon ab, wie ein Space genutzt wird. Die folgenden Beispiele dienen als Ausgangspunkt und können an Ihre Organisation angepasst werden.

### Unternehmen oder Team

```text
Marketing/
├── Kampagnen/
│   ├── Produkteinführung - Kampagnenplan - 2026.odt
│   └── Sommerkampagne - Ergebnisse - 2026.pdf
├── Berichte/
│   └── Marketing - Quartalsbericht - 2026-Q2.pdf
├── Vorlagen/
│   └── Marketing - Kampagnenbriefing - Vorlage.odt
└── Archiv/
```

### Projekt

```text
Projekt Atlas/
├── Planung/
│   ├── Projekt Atlas - Projektplan.odt
│   └── Projekt Atlas - Budget - 2026.xlsx
├── Besprechungen/
│   ├── Projekt Atlas - Besprechungsnotizen - 2026-08-04.odt
│   └── Projekt Atlas - Besprechungsnotizen - 2026-08-11.odt
└── Ergebnisse/
    └── Projekt Atlas - Abschlussbericht.pdf
```

### Schule oder Kindergarten

```text
Klasse 3B/
├── Unterrichtsmaterialien/
│   └── Klasse 3B - Mathematik - Bruchrechnung.pdf
├── Elterninformationen/
│   └── Klasse 3B - Elterninformation - Sommerausflug.pdf
└── Veranstaltungen/
    └── Klasse 3B - Sommerfest - 2026.pdf
```

### Familie

```text
Familie/
├── Haushalt/
│   ├── Versicherung - Haus - 2026.pdf
│   └── Strom - Vertrag - Beispiel Energie.pdf
├── Fotos/
│   └── Sommerurlaub - 2026/
└── Archiv/
```

In allen Fällen gelten dieselben Grundsätze: Halten Sie die Hierarchie verständlich und nehmen Sie genügend Informationen in Dateinamen auf, damit Dateien auch außerhalb ihrer Ordner identifiziert werden können.

## Zugriff unabhängig von der Struktur verwalten

Verwenden Sie keine tief verschachtelten Ordner, nur um organisatorische Zuständigkeiten oder Zugriffsmodelle abzubilden.

Wenn möglich:

- weisen Sie geeignete Space-Rollen zu
- verwenden Sie Gruppen für wiederkehrende Nutzerkreise
- gewähren Sie Nutzern nur die erforderlichen Berechtigungen
- verwenden Sie für sensible Inhalte einen separaten Space, wenn ein anderer Personenkreis darauf zugreifen soll

Ein Ordner sollte in erster Linie dabei helfen, Inhalte zu organisieren und zu finden.

## Inhalte regelmäßig archivieren

Spaces werden unübersichtlicher, wenn veraltete und aktuelle Inhalte miteinander vermischt sind.

Erstellen Sie gegebenenfalls einen Ordner namens `Archiv` für Inhalte, die nicht mehr aktiv verwendet, aber weiterhin aufbewahrt werden sollen:

```text
Projekt Atlas/
├── Planung/
├── Besprechungen/
├── Ergebnisse/
└── Archiv/
```

Überprüfen Sie Spaces regelmäßig und verschieben Sie veraltete Inhalte bei Bedarf in das Archiv.

Vermeiden Sie unnötig verschachtelte Archivstrukturen. Aussagekräftige Dateinamen sorgen dafür, dass archivierte Dateien auch dann identifiziert werden können, wenn Inhalte aus mehreren Jahren gemeinsam gespeichert sind.

## Häufige Stolperfallen

| Vermeiden                                               | Stattdessen                                                     |
| ------------------------------------------------------- | --------------------------------------------------------------- |
| Tiefe Ordnerhierarchien                                 | Strukturen auf etwa drei Ebenen begrenzen                       |
| Allgemeine Dateinamen wie `dokument.pdf`                | Genügend Kontext in den Dateinamen aufnehmen                    |
| Alle Informationen im Ordnerpfad abbilden               | Wichtige identifizierende Informationen in Dateinamen aufnehmen |
| Ordner für jedes Jahr, jeden Status oder jede Version   | Diese Eigenschaften bei Bedarf in Dateinamen aufnehmen          |
| Unterschiedliche Benennungsstile innerhalb eines Spaces | Eine Konvention festlegen und einhalten                         |
| Veraltete und aktuelle Inhalte mischen                  | Inaktive Inhalte in ein Archiv verschieben                      |
| Ordner als primäres Modell für die Zugriffskontrolle    | Zugriff über geeignete Rollen und Berechtigungen verwalten      |

## Schnellstart

Wenn Sie einen neuen Space erstellen:

1. Bestimmen Sie die wichtigsten Arbeitsbereiche.
2. Erstellen Sie nur die für diese Bereiche erforderlichen Ordner.
3. Halten Sie die Hierarchie so flach wie möglich.
4. Legen Sie eine Namenskonvention für Dateien fest.
5. Verwenden Sie Dateinamen, die auch ohne den Ordnerpfad verständlich sind.
6. Legen Sie fest, wer für die Pflege des Spaces verantwortlich ist.
7. Überprüfen und archivieren Sie Inhalte regelmäßig.

Eine einfache Ausgangsstruktur könnte so aussehen:

```text
[Space-Name]/
├── Dokumente/
├── Planung/
├── Ressourcen/
└── Archiv/
```

Passen Sie die Ordnernamen an den Zweck des Spaces an, anstatt zusätzliche Hierarchieebenen hinzuzufügen.

Das Ziel besteht nicht darin, eine möglichst detaillierte Ordnerstruktur zu erstellen. Inhalte sollen leicht zu finden, zu verstehen, zu teilen und zu pflegen sein.
