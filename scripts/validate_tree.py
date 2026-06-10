#!/usr/bin/env python3
"""Valida frontmatter de archivos Markdown normativos y reporta cobertura."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - depende del entorno local
    yaml = None

REQUIRED_FIELDS = {
    "nombre_oficial",
    "clave",
    "tipo",
    "jerarquia_nivel",
    "contenido_cargado",
}
EXCLUDED_FILES = {"README.md", "CONTRIBUTING.md", "SECURITY.md"}
MAX_FRONTMATTER_LINES = 200


def parse_scalar(value: str) -> Any:
    normalized = value.strip()
    if normalized.lower() == "true":
        return True
    if normalized.lower() == "false":
        return False
    if normalized.isdigit():
        return int(normalized)
    if (
        len(normalized) >= 2
        and normalized[0] == normalized[-1]
        and normalized[0] in {'"', "'"}
    ):
        return normalized[1:-1]
    return normalized


def safe_parse_frontmatter(raw_yaml: str) -> dict[str, Any]:
    if yaml is not None:
        data = yaml.safe_load(raw_yaml)
    else:
        data: dict[str, Any] = {}
        for line_number, line in enumerate(raw_yaml.splitlines(), start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if ":" not in stripped:
                raise ValueError(
                    "PyYAML no está instalado y el parser básico solo acepta "
                    f"pares clave: valor simples (línea {line_number})."
                )
            key, value = stripped.split(":", 1)
            data[key.strip()] = parse_scalar(value)

    if not isinstance(data, dict):
        raise ValueError("El frontmatter no es un objeto YAML válido.")
    return data


def extract_frontmatter(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("No se encontró delimitador inicial de frontmatter '---'.")

    end_index = None
    for i in range(1, min(len(lines), MAX_FRONTMATTER_LINES + 1)):
        if lines[i].strip() == "---":
            end_index = i
            break

    if end_index is None:
        raise ValueError(
            "No se encontró delimitador final de frontmatter '---' dentro "
            f"de las primeras {MAX_FRONTMATTER_LINES} líneas."
        )

    raw_yaml = "\n".join(lines[1:end_index])
    data = safe_parse_frontmatter(raw_yaml)

    missing = REQUIRED_FIELDS - data.keys()
    if missing:
        raise ValueError(f"Faltan campos requeridos: {', '.join(sorted(missing))}.")

    return data


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if path.name in EXCLUDED_FILES or ".git" in path.parts:
            continue
        if path.is_symlink():
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    loaded: list[tuple[str, str, Path]] = []
    pending: list[tuple[str, str, Path]] = []
    errors: list[tuple[Path, str]] = []

    for md_file in markdown_files(root):
        try:
            data = extract_frontmatter(md_file.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            errors.append((md_file, str(exc)))
            continue

        clave = str(data.get("clave", "")).strip() or "[sin-clave]"
        nombre = str(data.get("nombre_oficial", "")).strip() or "[sin-nombre]"
        contenido_cargado = data.get("contenido_cargado")

        if isinstance(contenido_cargado, bool):
            is_loaded = contenido_cargado
        elif isinstance(contenido_cargado, str):
            normalized = contenido_cargado.strip().lower()
            if normalized not in {"true", "false"}:
                errors.append((md_file, "El campo 'contenido_cargado' debe ser booleano o string 'true/false'."))
                continue
            is_loaded = normalized == "true"
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
