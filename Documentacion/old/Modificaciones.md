# GymControl - Estado, modificaciones y pendientes

**Estado documentado:** `dev-canda` basada en `main` en `071cdca`
**Integración:** PR #8 de Tomás y PR #9 de Edney incorporadas
**Comisión:** lunes por la noche - N.º 577502
**Fecha:** 3 de septiembre de 2026

## Estado de la rama

`dev-canda` contiene la documentación final sobre el estado de `main` posterior a las PR #8 y #9. La resolución de `dev-ed` conserva la función genérica en `tp.py`, corrige la versión intermedia y excluye `commit1.py` y `commit2.py` del resultado final.

## Aportes por integrante

### Javier Candalaft - `dev-canda`

- `b532a93`: primera versión funcional del sistema.
- `ce614a2`: eliminación de JSON y carga inicial en memoria.
- PR #5: `.gitignore`, PDFs, usuarios convertidos a matriz, uso real de `reduce`, login sin distinguir mayúsculas, regex de nombres y documentación interna.

### Lucas Cragaris - `dev-lucas`

- PR #1: documentación inicial, listado de clases activas por socio con `filter` y `map`, docstrings y primer documento de modificaciones.
- PR #7: bloqueo de inscripciones activas duplicadas, confirmación de alta y regex de nombres ampliada para espacios, tildes y `ñ`.

### Rodrigo García Solá - `dev-rodri`

- PR #3: refactor de socios, clases e inscripciones a matrices, índices constantes y adaptación de ABM, búsquedas, ordenamientos, reportes y menús.

### Tomás van Nynatten - `dev-tom`

- PR #4, integrada: incorporación del teléfono en las filas iniciales de socios y normalización del formato `XX-XXXX-XXXX`.
- PR #8, integrada en `main` como `aeec1c3`: regex de teléfono, captura en el alta, modificación, visualización y confirmación de baja.
- Durante la revisión se detectó un error de indentación en un head intermedio; Tomás lo corrigió antes del merge y el `tp.py` final de `92a593c` compila correctamente.

### Edney Ribeiro - `dev-ed`

- PR #9: creación de `search_position()` para reutilizar `filter` y funciones lambda en `search_class_position()` y `search_affiliate_position()`.
- Resolución en `fc103dd`: integración con `main`, corrección de la versión intermedia y exclusión de `commit1.py` y `commit2.py` del entregable final.

## Trazabilidad contra la consigna

| Requisito | Estado | Evidencia o acción |
|---|---|---|
| Equipo de 2 a 4 integrantes | Cumple con autorización | El docente confirmó que podemos presentar el trabajo entre los cinco. |
| Funciones y modularización | Cumple | 60 funciones, todas con docstring, incluida la función genérica `search_position()`. |
| Matrices | Cumple | Usuarios, socios, clases e inscripciones son listas bidimensionales. |
| Listas avanzadas con strings | Cumple | Usuarios, nombres de socios y nombres de clases. |
| `map` | Cumple | Totales por clase y nombres de clases de un socio. |
| `filter` | Cumple | Búsquedas genéricas, inscripciones duplicadas y clases activas por socio. |
| `reduce` | Cumple | Suma de asistencias por clase. |
| Expresiones regulares | Cumple | Validación de nombres de clase y búsqueda de usuario sin distinguir mayúsculas. |
| Git y commits individuales | Cumple | Las cinco ramas poseen aportes identificables; Edney figura en la PR #9 y en `ea40e12`. |
| Documentación técnica | Cumple | Propuesta, documentación técnica e historial están disponibles en Markdown desde el README. |
| Capturas de funcionamiento | Cumple | Tres capturas de ejecuciones reales en `docs/capturas/` y visibles desde el README. |
| Enlace al repositorio | Cumple | Incluido en todos los documentos principales. |
| Comisión | Cumple | Lunes por la noche - N.º 577502. |

## Decisiones de alcance

Los flujos principales de carga, consulta, modificación, búsqueda y reportes funcionan. No se incorporarán ajustes adicionales para casos límite que la consigna no exige, como recalcular cupos al eliminar un socio o resolver referencias manualmente alteradas hacia clases inexistentes. Estas mejoras de robustez no condicionan el cumplimiento académico.

La PR #8 agrega la validación del teléfono mediante regex. El requisito también está respaldado por la validación de nombres y por el login sin distinguir mayúsculas.

## Criterio de cumplimiento

El código, la documentación y la evidencia individual en Git cubren los contenidos obligatorios de la entrega escrita. La comisión está identificada y el docente confirmó que podemos presentarlo entre los cinco.
