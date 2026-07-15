#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path("/Users/h.pohl/Documents/Docusaurus/docs")

SOURCE_ROOT = (
    PROJECT_ROOT
    / "versioned_docs/version-4.0/user"
)

TARGET_ROOT = (
    PROJECT_ROOT
    / "i18n/de/docusaurus-plugin-content-docs/version-4.0/user"
)

DOCUMENT_SUFFIXES = {".md", ".mdx"}

PNG_PATTERN = re.compile(
    r"""(?P<quote>["'(])(?P<path>[^"'()\n]+?\.png)(?P=quote)""",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ImageReference:
    raw_path: str
    absolute_path: Path
    start: int
    end: int


@dataclass(frozen=True)
class RenameOperation:
    old_path: Path
    new_path: Path
    document: Path
    old_reference: str
    new_reference: str


def find_image_references(
    document: Path,
    text: str,
) -> list[ImageReference]:
    references: list[ImageReference] = []

    for match in PNG_PATTERN.finditer(text):
        raw_path = match.group("path")

        if raw_path.startswith(("http://", "https://", "//")):
            continue

        absolute_path = (document.parent / raw_path).resolve()

        references.append(
            ImageReference(
                raw_path=raw_path,
                absolute_path=absolute_path,
                start=match.start("path"),
                end=match.end("path"),
            )
        )

    return references


def replace_references(
    text: str,
    replacements: Iterable[tuple[int, int, str]],
) -> str:
    updated = text

    for start, end, replacement in sorted(
        replacements,
        key=lambda item: item[0],
        reverse=True,
    ):
        updated = updated[:start] + replacement + updated[end:]

    return updated


def relative_reference(
    document: Path,
    image: Path,
) -> str:
    relative = os.path.relpath(
        image,
        start=document.parent,
    )

    value = Path(relative).as_posix()

    if not value.startswith("."):
        value = f"./{value}"

    return value


def normalize_reference(reference: str) -> str:
    return os.path.normpath(reference).replace(os.sep, "/")


def collect_documents(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in DOCUMENT_SUFFIXES
    )


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for block in iter(
            lambda: file.read(1024 * 1024),
            b"",
        ):
            digest.update(block)

    return digest.hexdigest()


def is_case_only_rename(
    old_path: Path,
    new_path: Path,
) -> bool:
    return (
        old_path.parent == new_path.parent
        and old_path.name != new_path.name
        and old_path.name.casefold() == new_path.name.casefold()
    )


def rename_case_safely(
    old_path: Path,
    new_path: Path,
) -> None:
    temporary_path = old_path.with_name(
        f".__png-rename-temp__{old_path.name}"
    )

    counter = 1

    while temporary_path.exists():
        temporary_path = old_path.with_name(
            f".__png-rename-temp-{counter}__{old_path.name}"
        )
        counter += 1

    old_path.rename(temporary_path)
    temporary_path.rename(new_path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Gleicht PNG-Dateinamen im deutschen user-Bereich "
            "der OpenCloud-Dokumentation Version 4.0 an die "
            "englischen Namen aus versioned_docs/version-4.0/user an."
        )
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help=(
            "Änderungen tatsächlich durchführen. "
            "Ohne diese Option wird nur eine Vorschau angezeigt."
        ),
    )

    args = parser.parse_args()

    if not SOURCE_ROOT.is_dir():
        raise SystemExit(
            f"Quellverzeichnis fehlt: {SOURCE_ROOT}"
        )

    if not TARGET_ROOT.is_dir():
        raise SystemExit(
            f"Zielverzeichnis fehlt: {TARGET_ROOT}"
        )

    source_documents = collect_documents(SOURCE_ROOT)

    planned_operations: list[RenameOperation] = []
    planned_case_renames: list[RenameOperation] = []

    planned_duplicate_removals: list[
        tuple[Path, Path]
    ] = []

    document_updates: dict[
        Path,
        list[tuple[int, int, str]],
    ] = {}

    missing_target_document = 0
    differing_image_count = 0
    missing_source_image = 0
    missing_target_image = 0
    collisions = 0
    case_only_renames = 0
    identical_duplicates = 0
    already_correct = 0
    skipped_duplicate_reference = 0

    print(
        "MODUS:",
        (
            "ÄNDERUNGEN AUSFÜHREN"
            if args.apply
            else "NUR VORSCHAU"
        ),
    )

    print(f"Referenz: {SOURCE_ROOT}")
    print(f"Ziel:     {TARGET_ROOT}")
    print()

    for source_document in source_documents:
        relative_document = source_document.relative_to(
            SOURCE_ROOT
        )

        target_document = TARGET_ROOT / relative_document

        if not target_document.is_file():
            missing_target_document += 1
            continue

        try:
            source_text = source_document.read_text(
                encoding="utf-8"
            )

            target_text = target_document.read_text(
                encoding="utf-8"
            )

        except UnicodeDecodeError:
            print(
                "ÜBERSPRUNGEN, ungültige Kodierung: "
                f"{relative_document}"
            )
            continue

        source_refs = find_image_references(
            source_document,
            source_text,
        )

        target_refs = find_image_references(
            target_document,
            target_text,
        )

        if not source_refs and not target_refs:
            continue

        if len(source_refs) != len(target_refs):
            differing_image_count += 1

            print(
                "UNTERSCHIEDLICHE BILDANZAHL: "
                f"{relative_document}"
            )

            print(f"  Englisch: {len(source_refs)}")
            print(f"  Deutsch:  {len(target_refs)}")

            continue

        seen_target_images: set[Path] = set()

        for source_ref, target_ref in zip(
            source_refs,
            target_refs,
        ):
            source_image = source_ref.absolute_path
            target_image = target_ref.absolute_path

            if not source_image.is_file():
                missing_source_image += 1

                print(
                    f"ENGLISCHES BILD FEHLT: {source_image}"
                )

                continue

            if not target_image.is_file():
                missing_target_image += 1

                print(
                    f"DEUTSCHES BILD FEHLT: {target_image}"
                )

                continue

            new_target_image = target_image.with_name(
                source_image.name
            )

            new_reference = relative_reference(
                target_document,
                new_target_image,
            )

            old_reference_normalized = normalize_reference(
                target_ref.raw_path
            )

            new_reference_normalized = normalize_reference(
                new_reference
            )

            # Dasselbe Bild kann mehrfach in einer Markdown-Datei
            # referenziert werden.
            if target_image in seen_target_images:
                skipped_duplicate_reference += 1

                if (
                    old_reference_normalized
                    != new_reference_normalized
                ):
                    document_updates.setdefault(
                        target_document,
                        [],
                    ).append(
                        (
                            target_ref.start,
                            target_ref.end,
                            new_reference,
                        )
                    )

                continue

            seen_target_images.add(target_image)

            # Dateiname ist bereits korrekt.
            if target_image.name == source_image.name:
                already_correct += 1

                if (
                    old_reference_normalized
                    != new_reference_normalized
                ):
                    document_updates.setdefault(
                        target_document,
                        [],
                    ).append(
                        (
                            target_ref.start,
                            target_ref.end,
                            new_reference,
                        )
                    )

                continue

            # Der gewünschte Zielname existiert bereits.
            if (
                new_target_image.exists()
                and new_target_image != target_image
            ):
                # Nur Groß-/Kleinschreibung unterscheidet sich.
                if is_case_only_rename(
                    target_image,
                    new_target_image,
                ):
                    case_only_renames += 1

                    operation = RenameOperation(
                        old_path=target_image,
                        new_path=new_target_image,
                        document=target_document,
                        old_reference=target_ref.raw_path,
                        new_reference=new_reference,
                    )

                    planned_case_renames.append(operation)

                    if (
                        old_reference_normalized
                        != new_reference_normalized
                    ):
                        document_updates.setdefault(
                            target_document,
                            [],
                        ).append(
                            (
                                target_ref.start,
                                target_ref.end,
                                new_reference,
                            )
                        )

                    print(
                        "GROSS-/KLEINSCHREIBUNG: "
                        f"{relative_document}"
                    )

                    print(f"  {target_image.name}")
                    print(f"  → {new_target_image.name}")

                    continue

                # Der gewünschte Name existiert bereits und beide
                # Bilddateien sind inhaltlich identisch.
                if (
                    file_hash(target_image)
                    == file_hash(new_target_image)
                ):
                    identical_duplicates += 1

                    planned_duplicate_removals.append(
                        (
                            target_image,
                            new_target_image,
                        )
                    )

                    if (
                        old_reference_normalized
                        != new_reference_normalized
                    ):
                        document_updates.setdefault(
                            target_document,
                            [],
                        ).append(
                            (
                                target_ref.start,
                                target_ref.end,
                                new_reference,
                            )
                        )

                    print(
                        "IDENTISCHE DOPPELDATEI: "
                        f"{relative_document}"
                    )

                    print(f"  Entfernen: {target_image}")
                    print(f"  Verwenden: {new_target_image}")

                    continue

                collisions += 1

                print(
                    "ECHTE NAMENSKOLLISION: "
                    f"{relative_document}"
                )

                print(f"  Vorhanden: {new_target_image}")
                print(f"  Sollte ersetzen: {target_image}")

                continue

            # Normale Umbenennung.
            operation = RenameOperation(
                old_path=target_image,
                new_path=new_target_image,
                document=target_document,
                old_reference=target_ref.raw_path,
                new_reference=new_reference,
            )

            planned_operations.append(operation)

            if (
                old_reference_normalized
                != new_reference_normalized
            ):
                document_updates.setdefault(
                    target_document,
                    [],
                ).append(
                    (
                        target_ref.start,
                        target_ref.end,
                        new_reference,
                    )
                )

            print(f"UMBENENNEN: {relative_document}")
            print(f"  {target_image.name}")
            print(f"  → {source_image.name}")

    if document_updates:
        print()
        print("DOKUMENTE, DIE NOCH GEÄNDERT WÜRDEN:")

        for document, replacements in sorted(
            document_updates.items()
        ):
            print(
                f"\n{document.relative_to(TARGET_ROOT)}"
            )

            for _, _, new_reference in replacements:
                print(f"    -> {new_reference}")

    print()
    print("=" * 80)
    print("ZUSAMMENFASSUNG")

    print(
        "Geplante Umbenennungen:          "
        f"{len(planned_operations)}"
    )

    print(
        "Groß-/Kleinschreibungswechsel:   "
        f"{case_only_renames}"
    )

    print(
        "Identische Doppeldateien:         "
        f"{identical_duplicates}"
    )

    print(
        "Zu ändernde Dokumente:            "
        f"{len(document_updates)}"
    )

    print(
        "Bereits korrekt benannt:          "
        f"{already_correct}"
    )

    print(
        "Fehlende deutsche Dokumente:      "
        f"{missing_target_document}"
    )

    print(
        "Unterschiedliche Bildanzahl:      "
        f"{differing_image_count}"
    )

    print(
        "Fehlende englische Bilder:        "
        f"{missing_source_image}"
    )

    print(
        "Fehlende deutsche Bilder:         "
        f"{missing_target_image}"
    )

    print(
        "Echte Namenskollisionen:          "
        f"{collisions}"
    )

    print(
        "Doppelte Bildverweise:            "
        f"{skipped_duplicate_reference}"
    )

    if not args.apply:
        print()
        print("Es wurden keine Dateien verändert.")
        print(
            "Nach Kontrolle erneut mit --apply starten."
        )
        return

    if differing_image_count:
        raise SystemExit(
            "Abbruch: Mindestens eine englische und deutsche "
            "Markdown-Datei verwendet unterschiedlich viele Bilder."
        )

    if missing_source_image or missing_target_image:
        raise SystemExit(
            "Abbruch: Mindestens eine referenzierte Bilddatei fehlt."
        )

    if collisions:
        raise SystemExit(
            "Abbruch: Es bestehen echte Namenskollisionen mit "
            "unterschiedlichem Bildinhalt. Diese müssen zuerst "
            "manuell geprüft werden."
        )

    completed_case_renames: set[
        tuple[Path, Path]
    ] = set()

    for operation in planned_case_renames:
        key = (
            operation.old_path,
            operation.new_path,
        )

        if key in completed_case_renames:
            continue

        rename_case_safely(
            operation.old_path,
            operation.new_path,
        )

        completed_case_renames.add(key)

    completed_renames: set[
        tuple[Path, Path]
    ] = set()

    for operation in planned_operations:
        key = (
            operation.old_path,
            operation.new_path,
        )

        if key in completed_renames:
            continue

        operation.old_path.rename(
            operation.new_path
        )

        completed_renames.add(key)

    completed_removals: set[Path] = set()

    for (
        duplicate_path,
        canonical_path,
    ) in planned_duplicate_removals:
        if duplicate_path in completed_removals:
            continue

        if not canonical_path.is_file():
            raise RuntimeError(
                "Erwartete Zieldatei fehlt: "
                f"{canonical_path}"
            )

        if (
            file_hash(duplicate_path)
            != file_hash(canonical_path)
        ):
            raise RuntimeError(
                "Dateiinhalte haben sich während der "
                "Ausführung geändert: "
                f"{duplicate_path}"
            )

        duplicate_path.unlink()
        completed_removals.add(duplicate_path)

    for document, replacements in document_updates.items():
        original = document.read_text(
            encoding="utf-8"
        )

        updated = replace_references(
            original,
            replacements,
        )

        if updated != original:
            document.write_text(
                updated,
                encoding="utf-8",
            )

    print()
    print("Änderungen wurden erfolgreich durchgeführt.")


if __name__ == "__main__":
    main()
