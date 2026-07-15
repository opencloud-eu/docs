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


def resolve_root(path_value: str) -> Path:
    """
    Löst einen angegebenen Pfad auf.

    Relative Pfade werden relativ zu PROJECT_ROOT interpretiert.
    Absolute Pfade bleiben unverändert.
    """
    path = Path(path_value).expanduser()

    if not path.is_absolute():
        path = PROJECT_ROOT / path

    return path.resolve()


def find_image_references(
    document: Path,
    text: str,
) -> list[ImageReference]:
    references: list[ImageReference] = []

    for match in PNG_PATTERN.finditer(text):
        raw_path = match.group("path")

        if raw_path.startswith(
            (
                "http://",
                "https://",
                "//",
                "data:",
            )
        ):
            continue

        absolute_path = (
            document.parent / raw_path
        ).resolve()

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
    """
    Ersetzt Bildreferenzen von hinten nach vorne, damit die
    gespeicherten Zeichenpositionen während der Ersetzung gültig
    bleiben.
    """
    updated = text

    for start, end, replacement in sorted(
        replacements,
        key=lambda item: item[0],
        reverse=True,
    ):
        updated = (
            updated[:start]
            + replacement
            + updated[end:]
        )

    return updated


def relative_reference(
    document: Path,
    image: Path,
) -> str:
    """
    Erzeugt einen relativen POSIX-Pfad vom Markdown-Dokument
    zur Bilddatei.
    """
    relative = os.path.relpath(
        image,
        start=document.parent,
    )

    value = Path(relative).as_posix()

    if not value.startswith("."):
        value = f"./{value}"

    return value


def normalize_reference(reference: str) -> str:
    """
    Normalisiert Pfade, damit beispielsweise .././img und ../img
    als identisch behandelt werden.
    """
    return os.path.normpath(reference).replace(
        os.sep,
        "/",
    )


def collect_documents(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in DOCUMENT_SUFFIXES
    )


def file_hash(path: Path) -> str:
    """
    Berechnet den SHA-256-Hash einer Datei.
    """
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
    """
    Prüft, ob sich zwei Dateinamen nur durch ihre
    Groß-/Kleinschreibung unterscheiden.
    """
    return (
        old_path.parent == new_path.parent
        and old_path.name != new_path.name
        and old_path.name.casefold()
        == new_path.name.casefold()
    )


def rename_case_safely(
    old_path: Path,
    new_path: Path,
) -> None:
    """
    Führt eine reine Groß-/Kleinschreibungsänderung sicher durch.

    Das ist insbesondere auf macOS mit einem üblicherweise nicht
    zwischen Groß- und Kleinschreibung unterscheidenden Dateisystem
    erforderlich.
    """
    temporary_path = old_path.with_name(
        f".__png-rename-temp__{old_path.name}"
    )

    counter = 1

    while temporary_path.exists():
        temporary_path = old_path.with_name(
            f".__png-rename-temp-{counter}__"
            f"{old_path.name}"
        )
        counter += 1

    old_path.rename(temporary_path)
    temporary_path.rename(new_path)


def add_document_update(
    document_updates: dict[
        Path,
        list[tuple[int, int, str]],
    ],
    document: Path,
    reference: ImageReference,
    new_reference: str,
) -> None:
    """
    Fügt eine Markdown-Änderung nur dann hinzu, wenn sich der
    normalisierte Pfad tatsächlich ändert.
    """
    old_normalized = normalize_reference(
        reference.raw_path
    )

    new_normalized = normalize_reference(
        new_reference
    )

    if old_normalized == new_normalized:
        return

    document_updates.setdefault(
        document,
        [],
    ).append(
        (
            reference.start,
            reference.end,
            new_reference,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Gleicht PNG-Dateinamen und PNG-Referenzen in einer "
            "übersetzten Docusaurus-Dokumentation an eine "
            "Referenzdokumentation an."
        )
    )

    parser.add_argument(
        "--source",
        required=True,
        help=(
            "Referenzordner mit den gewünschten PNG-Dateinamen. "
            "Relative Pfade werden relativ zum Projektordner "
            "interpretiert."
        ),
    )

    parser.add_argument(
        "--target",
        required=True,
        help=(
            "Zielordner, dessen PNG-Dateien und Markdown-Referenzen "
            "angepasst werden sollen. Relative Pfade werden relativ "
            "zum Projektordner interpretiert."
        ),
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help=(
            "Änderungen tatsächlich durchführen. Ohne diese Option "
            "wird nur eine Vorschau angezeigt."
        ),
    )

    parser.add_argument(
        "--allow-missing-documents",
        action="store_true",
        help=(
            "Erlaubt fehlende Dokumente im Zielordner. Ohne diese "
            "Option bricht --apply bei fehlenden Zieldokumenten ab."
        ),
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help=(
            "Zeigt nur Warnungen und die Zusammenfassung an."
        ),
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    source_root = resolve_root(args.source)
    target_root = resolve_root(args.target)

    if not source_root.is_dir():
        raise SystemExit(
            f"Quellverzeichnis fehlt: {source_root}"
        )

    if not target_root.is_dir():
        raise SystemExit(
            f"Zielverzeichnis fehlt: {target_root}"
        )

    if source_root == target_root:
        raise SystemExit(
            "Quell- und Zielverzeichnis dürfen nicht identisch sein."
        )

    source_documents = collect_documents(source_root)

    planned_operations: list[RenameOperation] = []
    planned_case_renames: list[RenameOperation] = []

    planned_duplicate_removals: list[
        tuple[Path, Path]
    ] = []

    document_updates: dict[
        Path,
        list[tuple[int, int, str]],
    ] = {}

    missing_target_documents: list[Path] = []
    differing_image_documents: list[
        tuple[Path, int, int]
    ] = []

    missing_source_images: list[Path] = []
    missing_target_images: list[Path] = []

    collision_items: list[
        tuple[Path, Path, Path]
    ] = []

    case_only_renames = 0
    identical_duplicates = 0
    already_correct = 0
    skipped_duplicate_reference = 0
    invalid_encoding_documents = 0

    print(
        "MODUS:",
        (
            "ÄNDERUNGEN AUSFÜHREN"
            if args.apply
            else "NUR VORSCHAU"
        ),
    )

    print(f"Referenz: {source_root}")
    print(f"Ziel:     {target_root}")
    print()

    for source_document in source_documents:
        relative_document = source_document.relative_to(
            source_root
        )

        target_document = (
            target_root / relative_document
        )

        if not target_document.is_file():
            missing_target_documents.append(
                relative_document
            )

            if not args.quiet:
                print(
                    "DEUTSCHES/ZIEL-DOKUMENT FEHLT: "
                    f"{relative_document}"
                )

            continue

        try:
            source_text = source_document.read_text(
                encoding="utf-8"
            )

            target_text = target_document.read_text(
                encoding="utf-8"
            )

        except UnicodeDecodeError:
            invalid_encoding_documents += 1

            print(
                "ÜBERSPRUNGEN, ungültige UTF-8-Kodierung: "
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
            differing_image_documents.append(
                (
                    relative_document,
                    len(source_refs),
                    len(target_refs),
                )
            )

            print(
                "UNTERSCHIEDLICHE BILDANZAHL: "
                f"{relative_document}"
            )

            print(f"  Referenz: {len(source_refs)}")
            print(f"  Ziel:     {len(target_refs)}")

            continue

        seen_target_images: set[Path] = set()

        for source_ref, target_ref in zip(
            source_refs,
            target_refs,
        ):
            source_image = source_ref.absolute_path
            target_image = target_ref.absolute_path

            if not source_image.is_file():
                missing_source_images.append(
                    source_image
                )

                print(
                    "REFERENZBILD FEHLT: "
                    f"{source_image}"
                )

                continue

            if not target_image.is_file():
                missing_target_images.append(
                    target_image
                )

                print(
                    "ZIELBILD FEHLT: "
                    f"{target_image}"
                )

                continue

            new_target_image = target_image.with_name(
                source_image.name
            )

            new_reference = relative_reference(
                target_document,
                new_target_image,
            )

            if target_image in seen_target_images:
                skipped_duplicate_reference += 1

                add_document_update(
                    document_updates,
                    target_document,
                    target_ref,
                    new_reference,
                )

                continue

            seen_target_images.add(target_image)

            if target_image.name == source_image.name:
                already_correct += 1

                add_document_update(
                    document_updates,
                    target_document,
                    target_ref,
                    new_reference,
                )

                continue

            if (
                new_target_image.exists()
                and new_target_image != target_image
            ):
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

                    planned_case_renames.append(
                        operation
                    )

                    add_document_update(
                        document_updates,
                        target_document,
                        target_ref,
                        new_reference,
                    )

                    if not args.quiet:
                        print(
                            "GROSS-/KLEINSCHREIBUNG: "
                            f"{relative_document}"
                        )

                        print(
                            f"  {target_image.name}"
                        )

                        print(
                            f"  → {new_target_image.name}"
                        )

                    continue

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

                    add_document_update(
                        document_updates,
                        target_document,
                        target_ref,
                        new_reference,
                    )

                    if not args.quiet:
                        print(
                            "IDENTISCHE DOPPELDATEI: "
                            f"{relative_document}"
                        )

                        print(
                            f"  Entfernen: {target_image}"
                        )

                        print(
                            f"  Verwenden: "
                            f"{new_target_image}"
                        )

                    continue

                collision_items.append(
                    (
                        relative_document,
                        new_target_image,
                        target_image,
                    )
                )

                print(
                    "ECHTE NAMENSKOLLISION: "
                    f"{relative_document}"
                )

                print(
                    f"  Vorhanden: "
                    f"{new_target_image}"
                )

                print(
                    f"  Sollte ersetzen: "
                    f"{target_image}"
                )

                continue

            operation = RenameOperation(
                old_path=target_image,
                new_path=new_target_image,
                document=target_document,
                old_reference=target_ref.raw_path,
                new_reference=new_reference,
            )

            planned_operations.append(operation)

            add_document_update(
                document_updates,
                target_document,
                target_ref,
                new_reference,
            )

            if not args.quiet:
                print(
                    f"UMBENENNEN: {relative_document}"
                )

                print(f"  {target_image.name}")
                print(f"  → {source_image.name}")

    if document_updates and not args.quiet:
        print()
        print(
            "DOKUMENTE, DIE NOCH GEÄNDERT WÜRDEN:"
        )

        for document, replacements in sorted(
            document_updates.items()
        ):
            print(
                f"\n{document.relative_to(target_root)}"
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
        "Fehlende Zieldokumente:           "
        f"{len(missing_target_documents)}"
    )

    print(
        "Unterschiedliche Bildanzahl:      "
        f"{len(differing_image_documents)}"
    )

    print(
        "Fehlende Referenzbilder:          "
        f"{len(missing_source_images)}"
    )

    print(
        "Fehlende Zielbilder:              "
        f"{len(missing_target_images)}"
    )

    print(
        "Echte Namenskollisionen:          "
        f"{len(collision_items)}"
    )

    print(
        "Doppelte Bildverweise:            "
        f"{skipped_duplicate_reference}"
    )

    print(
        "Ungültig kodierte Dokumente:      "
        f"{invalid_encoding_documents}"
    )

    if not args.apply:
        print()
        print("Es wurden keine Dateien verändert.")
        print(
            "Nach Kontrolle erneut mit --apply starten."
        )
        return

    blocking_errors: list[str] = []

    if (
        missing_target_documents
        and not args.allow_missing_documents
    ):
        blocking_errors.append(
            "Mindestens ein Zieldokument fehlt."
        )

    if differing_image_documents:
        blocking_errors.append(
            "Mindestens ein Dokument verwendet in Quelle "
            "und Ziel unterschiedlich viele Bilder."
        )

    if missing_source_images:
        blocking_errors.append(
            "Mindestens ein referenziertes Referenzbild fehlt."
        )

    if missing_target_images:
        blocking_errors.append(
            "Mindestens ein referenziertes Zielbild fehlt."
        )

    if collision_items:
        blocking_errors.append(
            "Es bestehen echte Namenskollisionen mit "
            "unterschiedlichem Bildinhalt."
        )

    if invalid_encoding_documents:
        blocking_errors.append(
            "Mindestens ein Dokument besitzt keine gültige "
            "UTF-8-Kodierung."
        )

    if blocking_errors:
        print()
        print("ABBRUCH:")

        for error in blocking_errors:
            print(f"- {error}")

        raise SystemExit(1)

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

        if not operation.old_path.is_file():
            raise RuntimeError(
                "Die umzubenennende Datei fehlt während "
                f"der Ausführung: {operation.old_path}"
            )

        if operation.new_path.exists():
            raise RuntimeError(
                "Das Umbenennungsziel existiert unerwartet: "
                f"{operation.new_path}"
            )

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

        if not duplicate_path.is_file():
            raise RuntimeError(
                "Die zu entfernende Doppeldatei fehlt: "
                f"{duplicate_path}"
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
        completed_removals.add(
            duplicate_path
        )

    changed_document_count = 0

    for document, replacements in document_updates.items():
        original = document.read_text(
            encoding="utf-8"
        )

        updated = replace_references(
            original,
            replacements,
        )

        if updated == original:
            continue

        document.write_text(
            updated,
            encoding="utf-8",
        )

        changed_document_count += 1

    print()
    print("Änderungen wurden erfolgreich durchgeführt.")
    print(
        "Umbenannte Bilddateien:           "
        f"{len(completed_renames)}"
    )

    print(
        "Groß-/Kleinschreibung geändert:   "
        f"{len(completed_case_renames)}"
    )

    print(
        "Identische Doppeldateien entfernt:"
        f" {len(completed_removals)}"
    )

    print(
        "Geänderte Dokumente:              "
        f"{changed_document_count}"
    )


if __name__ == "__main__":
    main()
