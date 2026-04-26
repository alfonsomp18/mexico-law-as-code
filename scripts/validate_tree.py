#!/usr/bin/env python3
"""Valida frontmatter de archivos Markdown normativos y reporta cobertura."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

import yaml

REQUIRED_FIELDS = {
    "nombre_oficial",
    "clave",
    "tipo",
    "jerarquia_nivel",
    "contenido_cargado",
}
EXCLUDED_FILES = {"README.md", "CONTRIBUTING.md"}


def extract_frontmatter(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("No se encontró delimitador inicial de frontmatter '---'.")

    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_index = i
            break

    if end_index is None:
        raise ValueError("No se encontró delimitador final de frontmatter '---'.")

    raw_yaml = "\n".join(lines[1:end_index])
    data = yaml.safe_load(raw_yaml)

    if not isinstance(data, dict):
        raise ValueError("El frontmatter no es un objeto YAML válido.")

    missing = REQUIRED_FIELDS - data.keys()
    if missing:
        raise ValueError(f"Faltan campos requeridos: {', '.join(sorted(missing))}.")

    return data


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    markdown_files = sorted(
        p
        for p in root.rglob("*.md")
        if p.name not in EXCLUDED_FILES and ".git" not in p.parts
    )

    loaded: list[tuple[str, str, Path]] = []
    pending: list[tuple[str, str, Path]] = []
    errors: list[tuple[Path, str]] = []

    for md_file in markdown_files:
        try:
            data = extract_frontmatter(md_file.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append((md_file, str(exc)))
            continue

        clave = str(data.get("clave", "")).strip() or "[sin-clave]"
        nombre = str(data.get("nombre_oficial", "")).strip() or "[sin-nombre]"
        contenido_cargado = data.get("contenido_cargado")

        if isinstance(contenido_cargado, bool):
            is_loaded = contenido_cargado
        elif isinstance(contenido_cargado, str):
            is_loaded = contenido_cargado.strip().lower() == "true"
        else:
            errors.append((md_file, "El campo 'contenido_cargado' debe ser booleano o string 'true/false'."))
            continue

        if is_loaded:
            loaded.append((clave, nombre, md_file))
        else:
            pending.append((clave, nombre, md_file))

    total_valid = len(loaded) + len(pending)
    percentage = (len(loaded) / total_valid * 100) if total_valid else 0.0

    print("LEYES CARGADAS (contenido_cargado: true)")
    if loaded:
        for clave, nombre, _ in loaded:
            print(f"- {clave}: {nombre}")
    else:
        print("- Ninguna")

    print("\nLEYES PENDIENTES (contenido_cargado: false)")
    if pending:
        for clave, nombre, _ in pending:
            print(f"- {clave}: {nombre}")
    else:
        print("- Ninguna")

    print(f"\nCobertura: {len(loaded)} de {total_valid} leyes cargadas ({percentage:.2f}%)")

    if errors:
        print("\nERROR")
        for path, message in errors:
            rel = path.relative_to(root)
            print(f"- {rel}: {message}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
