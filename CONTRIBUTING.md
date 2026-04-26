# Cómo contribuir a mexico-law-as-code

## Antes de empezar
- Lee el README para entender la jerarquía normativa y la estructura del repo
- Verifica que la ley que quieres cargar esté en el mapa normativo del README (tabla de leyes)
- Usa siempre como fuente primaria el DOF (dof.gob.mx) o la Cámara de Diputados (diputados.gob.mx)

## Proceso para cargar el contenido de una ley

### Paso 1 — Crea una rama
git checkout -b feat/[clave-ley]
Ejemplo: git checkout -b feat/lisr

### Paso 2 — Usa el script de ingesta (recomendado)
python3 scripts/law_to_markdown.py --ley [clave] --output .
El script descarga el PDF oficial, extrae el texto y genera el Markdown estructurado.

### Paso 3 — Verifica manualmente
Compara al menos 10 artículos del Markdown generado contra el PDF oficial.
Asegúrate de que Títulos, Capítulos y Artículos estén correctamente identificados.

### Paso 4 — Actualiza el frontmatter
En el archivo .md correspondiente, actualiza:
- ultima_reforma_dof: con la fecha de la última reforma (formato YYYY-MM-DD)
- contenido_cargado: true

### Paso 5 — Actualiza el README
Cambia el emoji de estado en la tabla de leyes: ⏳ Pendiente → ✅ Cargada

### Paso 6 — Commit y Pull Request
git commit -m "feat: publicación inicial [CLAVE] — DOF [FECHA]"
Abre un Pull Request describiendo: ley cargada, fuente utilizada, fecha DOF de la versión.

## Estándares de calidad del contenido
- Nunca modificar el texto legal — solo transcribir fielmente
- Preservar la numeración exacta de artículos, fracciones e incisos
- El texto debe ser la versión vigente más reciente publicada en el DOF
- Indicar siempre la fecha de la última reforma en el frontmatter

## Formato Markdown requerido
- Títulos de la ley → ## Título [Número]
- Capítulos → ### Capítulo [Número]
- Secciones → #### Sección [Número]
- Artículos → **Artículo [N].** [texto]
- Fracciones → usar listas con I., II., III. o a), b), c)
- Transitorios → sección ## Artículos Transitorios al final

## Qué NO hacer
- No usar IA para generar o inferir texto legal — solo transcripción fiel
- No cargar versiones desactualizadas de leyes
- No mezclar varias leyes en un solo commit
- No modificar archivos fuera del scope de la ley que estás cargando
