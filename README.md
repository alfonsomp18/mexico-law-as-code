# México Law as Code — Fiscal

Repositorio abierto para **versionar, auditar y analizar** normativa fiscal mexicana bajo el enfoque **Law as Code**.

---

## Descripción

Este repositorio organiza leyes fiscales mexicanas en archivos de texto estructurados (Markdown) para tratarlas como código fuente:

- Cada ley vive en una ruta predecible.
- Cada reforma se refleja como un commit trazable.
- Cada diferencia normativa se analiza con herramientas de diff.
- Cada versión puede integrarse en pipelines de software fiscal y sistemas de IA.

### ¿Qué problema resuelve?

En la práctica fiscal, es común perder trazabilidad de cambios entre reformas, criterios o reglas misceláneas. Este repositorio permite:

- Conservar historial normativo de forma transparente.
- Comparar texto anterior vs. texto reformado con precisión.
- Reducir ambigüedad al construir lógica de negocio fiscal.
- Habilitar fuentes estructuradas para búsqueda semántica y automatización.

### ¿Por qué es útil?

- **Desarrolladores:** base estable para motores de cálculo, validaciones y reglas tributarias.
- **Fiscalistas:** seguimiento claro de modificaciones por fecha y fuente.
- **Sistemas de IA:** insumo limpio para RAG, agentes legales y extracción de conocimiento.

---

## Principios del proyecto

1. **Las leyes como código**
   - La norma se modela como artefacto versionable.
2. **Transparencia y trazabilidad**
   - Cada ajuste debe quedar asociado a un commit y referencia oficial.
3. **Versionamiento claro**
   - Reformas, correcciones y mejoras de estructura se distinguen por tipo de cambio.
4. **Fuente oficial (DOF)**
   - El Diario Oficial de la Federación (DOF) es la referencia primaria obligatoria.

---

## Estructura del repositorio

La organización sigue la jerarquía normativa mexicana:

1. **Constitución Política de los Estados Unidos Mexicanos**
   - `constitucion/`
2. **Tratados Internacionales**
   - `tratados-internacionales/`
3. **Leyes Federales**
   - `leyes-federales/`
4. **Reglamentos**
   - `reglamentos/`
5. **Resolución Miscelánea Fiscal**
   - `resolucion-miscelanea-fiscal/`
6. **Criterios del SAT (opcional)**
   - `criterios-sat/`
7. **Otros (tesis, jurisprudencia - opcional)**
   - Puede agregarse posteriormente (`otros/`)

### Árbol base

```text
/constitucion/
/tratados-internacionales/
/leyes-federales/
    /codigo-fiscal-de-la-federacion/
    /ley-del-isr/
    /ley-del-iva/
/reglamentos/
/resolucion-miscelanea-fiscal/
/criterios-sat/
```

---

## Organización de leyes

- Una carpeta por ordenamiento jurídico.
- Dentro de cada carpeta:
  - Opción A: archivo único principal + historial vía commits.
  - Opción B: versiones fechadas (si el proyecto requiere snapshots).
- Recomendación inicial: **archivo único por ley** y uso intensivo de historial Git para diffs.

Ejemplo:

```text
leyes-federales/
  ley-del-isr/
    ley-del-isr.md
  codigo-fiscal-de-la-federacion/
    codigo-fiscal-de-la-federacion.md
```

---

## Convenciones de nombres

Usar minúsculas, guiones medios y nombres descriptivos:

- `ley-del-isr.md`
- `codigo-fiscal-de-la-federacion.md`
- `ley-del-iva.md`

Reglas sugeridas:

- Sin acentos ni caracteres especiales en nombres de archivo.
- Nombres estables para facilitar automatización.
- Una ley = un nombre canónico.

---

## Convenciones de commits

Formato recomendado (Conventional Commits adaptado):

- `feat: publicación inicial Ley del ISR`
- `reform: artículo 27 actualizado (DOF 2025-01-01)`
- `fix: corrección de formato artículo 5`
- `docs: mejora de metadata de fuente DOF`

Sugerencias:

- Incluir fecha DOF cuando aplique.
- Separar cambios de forma (`fix`, `docs`) de cambios normativos (`reform`).
- Evitar commits masivos con múltiples leyes sin relación.

---

## Plantilla recomendada para archivos Markdown

```markdown
# Ley del Impuesto sobre la Renta

## Metadata
- Nombre oficial: Ley del Impuesto sobre la Renta
- Clave corta: LISR
- Última reforma considerada: 2025-01-01
- Fuente oficial: Diario Oficial de la Federación (DOF)
- URL fuente: https://www.dof.gob.mx/
- Estatus: Vigente

## Texto normativo

### Artículo 1
Texto del artículo...

### Artículo 2
Texto del artículo...

## Historial de cambios del repositorio
- 2026-04-21: Versión inicial estructurada en markdown.
```

---

## Uso con IA

Este repositorio está diseñado para integrarse con sistemas inteligentes:

### 1) RAG (Retrieval-Augmented Generation)

- Indexar archivos `.md` por ley, capítulo y artículo.
- Recuperar contexto normativo exacto antes de generar respuestas.
- Citar artículo y fecha de reforma en respuestas automatizadas.

### 2) Agentes legales

- Definir herramientas que consulten artículos específicos.
- Comparar redacciones entre commits para explicar impactos normativos.
- Automatizar flujos de revisión legal/técnica para software fiscal.

### 3) Automatización fiscal

- Alimentar motores de reglas con texto versionado.
- Ejecutar validaciones de cumplimiento con referencia normativa.
- Monitorear cambios regulatorios para alertas y actualización de sistemas.

---

## Buenas prácticas de mantenimiento

### Actualización continua

- Revisar publicaciones del DOF en ciclos definidos (diario/semanal).
- Registrar cada reforma relevante como commit independiente.
- Mantener metadata de fecha de última reforma por archivo.

### Contribución

1. Crear rama descriptiva (`reform/lisr-articulo-27-2025-01-01`).
2. Actualizar texto y metadata en el archivo correspondiente.
3. Incluir referencia DOF en el commit o PR.
4. Abrir PR con resumen del cambio normativo y alcance técnico.

### Validación contra DOF

- Confirmar coincidencia literal del texto cuando sea posible.
- Verificar fecha de publicación y entrada en vigor.
- Documentar notas cuando existan artículos transitorios relevantes.

### Calidad documental

- Mantener encabezados consistentes (`#`, `##`, `### Artículo X`).
- Evitar formatos ambiguos.
- Preferir cambios pequeños y auditables.

---

## Disclaimer legal

- Este repositorio es un recurso técnico-documental y **no sustituye asesoría legal, fiscal o profesional**.
- La **fuente oficial y vinculante** de la normatividad es el **Diario Oficial de la Federación (DOF)** y demás fuentes oficiales aplicables.
- Cualquier uso en producción debe incluir validación jurídica especializada.

---

## Licencia y uso

Se recomienda incorporar una licencia open source (por ejemplo, MIT o Apache-2.0) y lineamientos de contribución (`CONTRIBUTING.md`) en siguientes iteraciones.
