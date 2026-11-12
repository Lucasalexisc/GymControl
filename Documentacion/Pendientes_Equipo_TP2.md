# Estado final de la entrega TP2 — GymControl

**Fecha de actualización:** 11 de noviembre de 2026  
**Rama:** `dev-lucas-2` (lista para Pull Request hacia `main`)

---

## Resumen de implementación completada

Todos los requisitos obligatorios de la consigna (Segunda Parte) y las correcciones de la devolución de la Primera Parte se encuentran integrados y probados:

1. **Conjuntos (`set`) — §5.1:**
   - Integrados en `src/estadisticas.py` (`obtener_socios_sin_clases_activas`, `socios_sin_clases_activas`, `obtener_disciplinas_unicas`, `disciplinas_unicas`) mediante `set()`, `.add()` y diferencia de conjuntos, expuestos en las opciones `5` y `6` del menú de Cálculos Estadísticos (`src/menus.py`).
2. **Archivos JSON (Persistencia) — §8:**
   - Creado `src/persistencia.py` con `guardar_datos()`, `cargar_datos()` y `reconstruir_horario()`.
   - Carga automática al iniciar en `main.py` y guardado automático tras cada alta, baja o modificación en `src/socios.py`, `src/clases.py` y `src/inscripciones.py`.
3. **Archivos exigidos en la entrega — §16:**
   - Incluidos `datos_gimnasio.json` y `auditoria.txt` en la raíz del repositorio.
4. **Restricciones técnicas y mejoras de consistencia — §10, §11 y §12:**
   - Eliminadas todas las librerías no vistas en la materia (`tempfile`, `datetime`, `os`, `builtins`, `contextlib`, `io`, `subprocess`) y expresiones generadoras.
   - Reemplazado `global usuario_actual` por el diccionario `SESION_ACTUAL` en `src/auditoria.py`.
   - Reutilización de `pedir_entero()` en `eliminar_clase()` y `modificar_clase()` (`src/clases.py`).
   - Visualización de nombres de socio/clase y estado (`Activa`/`Inactiva`) en `ordenar_inscripciones_por_asistencias()` (`src/ordenamientos.py`).
5. **Pruebas unitarias — §9:**
   - `test_gymcontrol.py`: 12/12 pruebas aprobadas (incluyendo casos válidos, inválidos, límite y pruebas de liberación de cupos, conjuntos y persistencia JSON con reconstrucción de tuplas), sin clases (`class`) ni librerías externas.
