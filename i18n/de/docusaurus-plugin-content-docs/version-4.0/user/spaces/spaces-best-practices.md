---
sidebar_position: 90
id: best-practice
title: Best practice
description: Best Practices zur Organisation von Spaces in OpenCloud
---

# Best Practices zur Organisation von Spaces in OpenCloud

Spaces sind kollaborative Bereiche, die von mehreren Nutzern verwendet
werden. Anders als persönlicher Speicher müssen sie so aufgebaut sein,
dass sie Klarheit, Zusammenarbeit und Skalierbarkeit unterstützen.
Dieser Leitfaden hilft dir dabei, Spaces gut organisiert und langfristig
nutzbar einzurichten und zu pflegen.

## Allgemeine Grundsätze

- Erst planen -- Behandle Spaces nicht wie spontanen Ablagespeicher.
  Denke voraus.
- In Rollen und Teams denken -- Strukturiere anhand der Zusammenarbeit
  von Personen.
- Skalierbarkeit beachten -- Wähle eine Struktur, die jetzt _und_
  später mit mehr Nutzern funktioniert.
- Konsistenz anwenden -- Benennung, Zugriffsrechte und Aufbau sollten
  gemeinsamen Regeln folgen.

## Ordnerstruktur: Empfohlene Muster

### Beispiel: Familie

```plaintext
📁 Familien-Space
 ├── 📂 Dokumente
 │    ├── 🧾 Versicherungen
 │    └── 📑 Verträge
 ├── 📂 Fotos
 │    ├── 📸 2024
 │    └── 📸 2023
 └── 📂 Gemeinsame Notizen
```

### Schule / Kindergarten

```plaintext
📁 2024
 ├── 📂 Klasse 3B
 │    ├── 📂 Unterrichtsmaterial
 │    ├── 📂 Elternkommunikation
 │    ├── 📂 Hausaufgaben
 │    └── 📂 Veranstaltungen & Fotos
 ├── 📂 Klasse 4C
 │    ├── 📂 Unterrichtsmaterial
 │    ├── 📂 Elternkommunikation
 │    ├── 📂 Hausaufgaben
 │    └── 📂 Veranstaltungen & Fotos
```

### Unternehmen / Team

```plaintext
📁 Marketing-Team
 ├── 📂 Kampagnen
 │    ├── 📂 Q1-2025
 │    └── 📂 Q2-2025
 ├── 📂 Vorlagen
 ├── 📂 Berichte
 └── 📂 Meeting-Notizen
```

## Namenskonventionen

- Klare, beschreibende Namen verwenden -- vermeide „Neuer Ordner" oder
  kryptische Titel
- Bevorzuge lowercase-mit-bindestrichen oder Title Case
- Relevante Daten hinzufügen: `bericht-2025-Q2.pdf` oder
  `Budget 2024.xlsx`
- Sonderzeichen vermeiden: `& % $ § !` können Integrationen stören

## Richtlinien für Eigentümerschaft & Zugriffe

- Space Owner festlegen: verantwortlich für Struktur und
  Berechtigungen
- Wenn möglich Gruppen für Zugriffskontrolle nutzen (z. B. `staff`,
  `students`, `parents`)
- Sensible Inhalte in separate Ordner mit eingeschränktem Zugriff
  auslagern
- Bearbeitungs- und Leserechte klar definieren

## Archivierung & Aufräumen

- Einen Archiv-Ordner für alte oder ungenutzte Dateien einrichten
- Den Space jährlich überprüfen und veraltete Inhalte entfernen
- Bei Unsicherheit Versionierung nutzen oder vor dem Löschen
  exportieren

## Häufige Stolperfallen

| ❌ Nicht tun                               | ✅ Besser so                               |
| ------------------------------------------ | ------------------------------------------ |
| Alle Dateien im Root-Ordner ablegen        | Klare Unterordner verwenden                |
| Persönliche und gemeinsame Inhalte mischen | Persönliche Daten in „Persönlich" belassen |
| Allen Nutzern Vollzugriff geben            | Least-Privilege-Prinzip anwenden           |
| Uneinheitliche Benennungen nutzen          | Konventionen definieren & einhalten        |

## Schnellstart-Vorlage zum Teilen

Du kannst diese Vorlage für neue Spaces verwenden:

```plaintext
📁 [Team-/Projektname]
 ├── 📂 Dokumente
 ├── 📂 Planung
 ├── 📂 Ressourcen
 ├── 📂 Archiv
 └── README.md (Zweck, Struktur, Regeln des Spaces)
```

## Zusammenfassung

---

Ziel Vorgehen

---

Spaces leicht navigierbar Klare Ordnernamen & Hierarchie nutzen
machen

Berechtigungschaos vermeiden Eigentümer und Rollen definieren

Ordnung behalten Regelmäßig prüfen und archivieren

Zusammenarbeit fördern Gruppenrechte & standardisierte Benennung

---
