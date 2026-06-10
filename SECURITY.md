# Política de seguridad

## Alcance

Este repositorio almacena normativa mexicana en Markdown estructurado y scripts auxiliares para validar el árbol documental. Aunque el contenido normativo es público, el repositorio debe evitar la inclusión accidental de secretos, credenciales, llaves privadas o artefactos locales de ingesta.

## Cómo reportar vulnerabilidades

Si encuentras una vulnerabilidad de seguridad, no abras un issue público con detalles explotables. Reporta el problema de forma privada al mantenedor del repositorio e incluye:

- Descripción del riesgo.
- Archivos o scripts afectados.
- Pasos mínimos para reproducirlo.
- Impacto esperado.
- Recomendación de mitigación, si la tienes.

## Reglas de seguridad para contribuciones

- No incluir credenciales, tokens, llaves privadas, certificados ni archivos `.env`.
- No versionar PDFs descargados, archivos temporales o artefactos de extracción.
- Usar únicamente fuentes oficiales públicas (`dof.gob.mx` y `diputados.gob.mx`).
- Revisar cambios con `git diff` antes de hacer commit.
- Ejecutar `python3 scripts/validate_tree.py` antes de abrir un Pull Request.

## Validación local recomendada

```bash
python3 scripts/validate_tree.py
bash -n scripts/create_repo_structure.sh
python3 -m py_compile scripts/validate_tree.py
```

## Nota sobre contenido legal

El texto normativo proviene de fuentes públicas oficiales. La política de seguridad aplica al código, metadatos, procesos de ingesta y archivos auxiliares del repositorio.
