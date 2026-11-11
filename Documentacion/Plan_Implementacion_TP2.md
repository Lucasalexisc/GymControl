# Plan de implementación — GymControl, segunda parte

**Materia:** Algoritmos y Estructura de Datos 1 / Programación 1 — UADE.
**Revisión:** 10 de noviembre de 2026.
**Base verificada:** `dev-lucas-2`, lista para integrar en `main`.

Este documento refleja el cierre completo de los requisitos del TP2. El detalle técnico de cada apartado se encuentra en [Documentacion_TP2.md](Documentacion_TP2.md).

## 1. Estado de requisitos y correcciones

| Requisito / corrección | Estado verificado | Evidencia |
|---|---|---|
| Modularización (§10) | Implementada | `main.py` coordina los módulos de `src/`. |
| Liberación de cupos al bajar un socio | Implementada | `liberar_cupos_de_afiliado()` en `src/socios.py`. |
| Login sin bloqueo y pregunta secreta | Implementado | `src/login.py`, con reintentos y salida voluntaria. |
| Archivos de texto (§7) | Implementados | Escritura, lectura y resumen de `auditoria.txt` en `src/auditoria.py`. |
| Tuplas (§5.2) | Implementadas | Horarios `((dias...), inicio, fin)` en `src/clases.py` y `src/datos.py`. |
| Diccionarios (§5.3) | Implementados | `resumir_auditoria()`, `DIAS_SEMANA`, `NIVELES_CLASE` y `TIPOS_SOCIO`. |
| Conjuntos (§5.1) | Implementados | `obtener_socios_sin_clases_activas()` y `obtener_disciplinas_unicas()` en `src/estadisticas.py` y opciones 5 y 6 en `src/menus.py`. |
| Archivos JSON (§8) | Implementados | `guardar_datos()` y `cargar_datos()` en `src/persistencia.py` con `datos_gimnasio.json` y reconstrucción de tuplas. |
| Excepciones (§6) | Implementadas | Control en auditoría, persistencia JSON, interrupciones y validaciones numéricas (`ValueError`, `TypeError`). |
| Modificación por atributo | Implementada | Submenús en socios, clases e inscripciones. |
| `sorted()` en ordenamientos y búsqueda | Implementado | `src/ordenamientos.py` y `src/busquedas.py`. |
| Eliminación de `unicodedata` (§12.3) | Implementada | `normalizar_dia()` en `src/clases.py` utiliza `.replace()`. |
| Pruebas unitarias (§9) | Implementadas y aprobadas | 12/12 en `test_gymcontrol.py` y 12/12 en `tests/test_autenticacion_auditoria.py`. |
| Archivos de entrega (§16) | Incluidos | `auditoria.txt` y `datos_gimnasio.json` versionados en la raíz del proyecto. |
| Documentación (§15) | Completa | `Documentacion/Documentacion_TP2.md` y `README.md` actualizados. |

## 2. Validación ejecutada

| Comando desde la raíz | Resultado | Código de salida |
|---|---|---|
| `python3 -B test_gymcontrol.py` | 12/12 aprobadas | `0` |
| `python3 -B tests/test_autenticacion_auditoria.py` | 12/12 aprobadas | `0` |
