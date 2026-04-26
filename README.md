# mexico-law-as-code

![Licencia: MIT](https://img.shields.io/badge/licencia-MIT-green.svg) ![Contribuciones bienvenidas](https://img.shields.io/badge/contribuciones-bienvenidas-brightgreen.svg)

## ¿Qué es esto?

Repositorio open source que versiona la normativa fiscal y financiera de México en formato Markdown estructurado, para ser consumible por sistemas RAG, motores de cálculo fiscal, agentes de IA, y cualquier herramienta que requiera normativa legal como código versionable.

## Casos de uso

- RAG / LLMs: alimentar modelos de lenguaje con normativa actualizada y versionada
- Motores de cálculo: tablas de tasas ISR, IVA, IEPS referenciadas como código
- Alertas de reforma: git diff para detectar cambios normativos automáticamente
- Auditoría: historial completo de cambios en cada artículo vía git blame
- Investigación legal: búsqueda full-text y referencias cruzadas entre leyes
- EdTech: material estructurado para plataformas de educación fiscal

## Jerarquía normativa de México

- Nivel 1: Constitución Política (CPEUM) — Base constitucional
- Nivel 2: Tratados Internacionales — CDIs, TIEAs, BEPS-OCDE  
- Nivel 3: Leyes Federales — CFF, LISR, LIVA, LIEPS y demás
- Nivel 4: Reglamentos — Reglamentos de cada ley principal
- Nivel 5: Resolución Miscelánea Fiscal — RMF anual + modificaciones + anexos
- Nivel 6: Criterios SAT y Jurisprudencia — Normativos, SCJN, TFJA, TCC

## Mapa normativo completo

| Nivel | Clave | Nombre oficial | Tipo | Estado | Archivo |
|---|---|---|---|---|---|
| 1 | CPEUM | Constitución Política de los Estados Unidos Mexicanos | Constitución | ⏳ Pendiente | constitucion/cpeum.md |
| 1 | CDIs | Convenios para Evitar la Doble Imposición (62+ países) | Tratado | ⏳ Pendiente | tratados-internacionales/convenios-doble-imposicion/ |
| 1 | TIEAs | Acuerdos de Intercambio de Información Fiscal | Tratado | ⏳ Pendiente | tratados-internacionales/acuerdos-intercambio-informacion/ |
| 1 | BEPS | Acciones BEPS-OCDE adoptadas por México | Acuerdo int. | ⏳ Pendiente | tratados-internacionales/beps-ocde/ |
| 2 | CFF | Código Fiscal de la Federación | Ley federal | ⏳ Pendiente | leyes-federales/codigo-fiscal-de-la-federacion/cff.md |
| 2 | LISR | Ley del Impuesto sobre la Renta | Ley federal | ⏳ Pendiente | leyes-federales/ley-del-isr/lisr.md |
| 2 | LIVA | Ley del Impuesto al Valor Agregado | Ley federal | ⏳ Pendiente | leyes-federales/ley-del-iva/liva.md |
| 2 | LIEPS | Ley del Impuesto Especial sobre Producción y Servicios | Ley federal | ⏳ Pendiente | leyes-federales/ley-del-ieps/lieps.md |
| 2 | LA | Ley Aduanera | Ley federal | ⏳ Pendiente | leyes-federales/ley-aduanera/ley-aduanera.md |
| 2 | LIF-2025 | Ley de Ingresos de la Federación 2025 | Ley federal | ⏳ Pendiente | leyes-federales/ley-de-ingresos-de-la-federacion/lif-2025.md |
| 2 | LFD | Ley Federal de Derechos | Ley federal | ⏳ Pendiente | leyes-federales/ley-federal-de-derechos/lfd.md |
| 2 | LCF | Ley de Coordinación Fiscal | Ley federal | ⏳ Pendiente | leyes-federales/ley-de-coordinacion-fiscal/lcf.md |
| 2 | LCE | Ley de Comercio Exterior | Ley federal | ⏳ Pendiente | leyes-federales/ley-de-comercio-exterior/lce.md |
| 2 | LSS | Ley del Seguro Social | Ley federal | ⏳ Pendiente | leyes-federales/ley-del-seguro-social/lss.md |
| 2 | LINFONAVIT | Ley del INFONAVIT | Ley federal | ⏳ Pendiente | leyes-federales/ley-del-infonavit/linfonavit.md |
| 2 | LISSSTE | Ley del ISSSTE | Ley federal | ⏳ Pendiente | leyes-federales/ley-del-issste/lissste.md |
| 2 | LGSM | Ley General de Sociedades Mercantiles | Ley federal | ⏳ Pendiente | leyes-federales/ley-general-de-sociedades-mercantiles/lgsm.md |
| 2 | LMV | Ley del Mercado de Valores | Ley federal | ⏳ Pendiente | leyes-federales/ley-del-mercado-de-valores/lmv.md |
| 2 | LGTOC | Ley General de Títulos y Operaciones de Crédito | Ley federal | ⏳ Pendiente | leyes-federales/ley-general-titulos-operaciones-credito/lgtoc.md |
| 2 | LSAR | Ley de los Sistemas de Ahorro para el Retiro | Ley federal | ⏳ Pendiente | leyes-federales/ley-de-los-sistemas-de-ahorro-para-el-retiro/lsar.md |
| 2 | LFPIORPI | Ley Federal para la Prevención e Identificación de Operaciones con Recursos de Procedencia Ilícita | Ley federal | ⏳ Pendiente | leyes-federales/ley-antilavado-lfpiorpi/lfpiorpi.md |
| 2 | LFDC | Ley Federal de los Derechos del Contribuyente | Ley federal | ⏳ Pendiente | leyes-federales/ley-federal-derechos-del-contribuyente/lfdc.md |
| 2 | LFPCA | Ley Federal de Procedimiento Contencioso Administrativo | Ley federal | ⏳ Pendiente | leyes-federales/ley-federal-procedimiento-contencioso-administrativo/lfpca.md |
| 3 | RCFF | Reglamento del CFF | Reglamento | ⏳ Pendiente | reglamentos/reglamento-cff/rcff.md |
| 3 | RISR | Reglamento de la LISR | Reglamento | ⏳ Pendiente | reglamentos/reglamento-isr/risr.md |
| 3 | RIVA | Reglamento de la LIVA | Reglamento | ⏳ Pendiente | reglamentos/reglamento-iva/riva.md |
| 3 | RIEPS | Reglamento de la LIEPS | Reglamento | ⏳ Pendiente | reglamentos/reglamento-ieps/rieps.md |
| 3 | RLA | Reglamento de la Ley Aduanera | Reglamento | ⏳ Pendiente | reglamentos/reglamento-ley-aduanera/rla.md |
| 3 | RLSS | Reglamento de la Ley del Seguro Social | Reglamento | ⏳ Pendiente | reglamentos/reglamento-lss/rlss.md |
| 4 | RMF-2025 | Resolución Miscelánea Fiscal 2025 | RMF | ⏳ Pendiente | resolucion-miscelanea-fiscal/2025/rmf-2025.md |
| 4 | RMF-2024 | Resolución Miscelánea Fiscal 2024 | RMF | ⏳ Pendiente | resolucion-miscelanea-fiscal/2024/rmf-2024.md |
| 5 | Criterios SAT | Criterios normativos, no vinculativos e internos del SAT | Criterio | ⏳ Pendiente | criterios-sat/ |
| 6 | Jurisprudencia | SCJN, TFJA, TCC — materia fiscal | Jurisprudencia | ⏳ Pendiente | jurisprudencia/ |

## Convención de commits

- feat: publicación inicial de una ley
- reform: actualización por reforma DOF (indicar fecha DOF y artículos afectados)
- fix: corrección de formato o error de transcripción
- docs: cambios al README u otros archivos de documentación
- chore: mantenimiento del repositorio

## Convención de nombres de rama

- main: siempre estable, solo leyes verificadas
- feat/[clave-ley]: para carga de una ley nueva
- reform/[clave-ley]-[fecha-dof]: para reformas

## Cómo contribuir

Consulta `CONTRIBUTING.md` (próximamente) para lineamientos de colaboración.

## Licencia

MIT — con nota aclaratoria: el contenido normativo es de dominio público (DOF/Cámara de Diputados). El código de procesamiento y estructura es MIT.
