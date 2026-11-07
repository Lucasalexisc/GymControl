# Plan de implementación — GymControl, segunda parte

**Materia:** Algoritmos y Estructura de Datos 1 / Programación 1 — UADE.
**Revisión:** 7 de noviembre de 2026.
**Entrega:** 5 de noviembre de 2026.
**Base verificada:** `main`, commit `a07d82c` (incluye PR #7 y PR #8). El HEAD remoto coincide y no hay PR abiertas al momento de la revisión.

Este relevamiento actualiza el estado del 3 de noviembre tras la integración de la PR #8 (`dev-ed2-entrega`) y la PR #7 (`dev-canda`). Conserva la asignación de tareas y actualiza los pendientes según el código integrado. La [documentación del TP2](Documentacion_TP2.md) desarrolla los seis apartados del punto 15 de la [consigna](TP_2DA%20PARTE%20(Lunes).md), y el resumen de pendientes para el equipo se encuentra en [Pendientes_Equipo_TP2.md](Pendientes_Equipo_TP2.md).

## 1. Requisitos y correcciones

| Requisito / corrección | Estado verificado | Evidencia / pendiente |
|---|---|---|
| Modularización (§10) | Implementada | `main.py` coordina módulos de `src/`. |
| Liberación de cupos al bajar un socio | Implementada | `liberar_cupos_de_afiliado()`, con pruebas de borde y negocio. |
| Login sin bloqueo y pregunta secreta | Implementado | `src/login.py`, con reintentos y salida voluntaria. |
| Archivos de texto (§7) | Implementados | Escritura, lectura y resumen de `auditoria.txt`. `pathlib` ya fue retirado. |
| Tuplas (§5.2) | Implementadas | Horarios: días, inicio y fin. |
| Diccionarios (§5.3) | Implementados | Resumen de auditoría, días de la semana y catálogos `NIVELES_CLASE` y `TIPOS_SOCIO` en `src/datos.py` (PR #8 integrada). |
| Excepciones (§6) | Implementadas; JSON pendiente | Auditoría, interrupciones y conversiones con `ValueError` / `TypeError`. |
| Modificación por atributo | Implementada | Socios, clases e inscripciones; PR #4 integrada. |
| Diez pruebas (§9) | Implementadas y aprobadas | 4 válidas, 3 inválidas, 2 límites y 1 de negocio, sobre 7 funciones. PR #5 integrada con código de salida corregido. |
| Presentación en consultas y bajas | Parcial | Persisten `(s/cantidad)` en baja de clases y horarios/niveles sin formatear en `buscar_clase_binaria()` y `ordenar_clases_por_nivel()`. |
| `sorted()` en lugar de ordenamientos manuales | Implementado | `src/ordenamientos.py`, `src/busquedas.py` y títulos actualizados en `src/menus.py` (PR #8 integrada). |
| Conjuntos (§5.1) | Pendiente obligatorio | No hay reportes con `set` integrados. |
| JSON (§8) | Pendiente obligatorio | No existen módulo de persistencia ni carga/guardado de matrices. |
| Módulos autorizados (§12) | En ajuste | Reemplazar `unicodedata` en `src/clases.py` por reemplazos simples de vocales acentuadas. |
| Documentación (§15) | Actualizada al alcance real | Falta completar JSON/conjuntos y sus resultados después de implementarlos. |

## 2. Tareas por integrante

### Javier Candalaft (`dev-canda`)

**Hecho:** login con reintentos y pregunta secreta; auditoría de accesos y ABM; cierre de sesión controlado; reemplazo de `pathlib` por `os.path` y `open()` (PR #6 y PR #7 integradas). README, documentación en seis apartados y este plan actualizados.

**Pendiente:**

1. Confirmar con la cátedra el uso de `datetime` y sus métodos, y los módulos usados en el sistema y las pruebas.
2. Después de integrar la persistencia JSON y los conjuntos, documentar el formato JSON real, el momento del guardado, la recuperación de horarios y el tratamiento de errores; explicar los reportes con conjuntos.
3. Incorporar el resultado real de la prueba de recuperación tras reinicio y actualizar el cierre documental.

### Lucas Cragaris (`dev-lucas-2`)

**Hecho:** modularización; liberación de cupos; diez pruebas independientes sin clases propias; captura específica de `ValueError` y `TypeError`; eliminación de `es_string()` y `pedir_opcion()` sin uso; corrección de la variable local que ocultaba la matriz de clases. La PR #5 ya está integrada y el ejecutor propaga los fallos con salida `1`.

**En progreso (cierre de pendientes del equipo en `dev-lucas-2`):**

1. Implementar reportes con conjuntos (`set`) en `src/estadisticas.py` y `src/menus.py`.
2. Implementar persistencia JSON en `src/persistencia.py` e integrarla en el flujo del sistema.
3. Incorporar los archivos de entrega (`datos_gimnasio.json` y `auditoria.txt`).
4. Reemplazar `unicodedata` en `src/clases.py`, corregir `(s/n)` en baja de clases y formatear horarios/niveles en búsquedas y ordenamientos.

### Tomás van Nynatten (`dev-tom-2`)

**Hecho:** traducción de la mayor parte del código; horarios con tuplas; modificación por atributo de socios, clases e inscripciones (PR #4 integrada); confirmaciones `(s/n)` en bajas de socios e inscripciones.

**Pendiente (cubierto en el cierre de entrega):**

1. Sustituir `unicodedata` en `normalizar_dia()` por reemplazos simples de vocales acentuadas.
2. Usar `formatear_horario()` y `obtener_nombre_nivel()` en `buscar_clase_binaria()` y `ordenar_clases_por_nivel()`.
3. Cambiar `(s/cantidad)` por `(s/n)` en la confirmación de baja de clases.

### Edney Ribeiro (`dev-ed2` / `dev-ed2-entrega`)

**Hecho:** búsqueda genérica con `filter` y lambda de la primera parte; diccionarios `NIVELES_CLASE` y `TIPOS_SOCIO` en `src/datos.py`; sustitución de selección, inserción y burbujeo por `sorted()` en `src/ordenamientos.py` y `src/busquedas.py` con actualización de títulos en `src/menus.py` (PR #8 integrada).

**Pendiente (cubierto en el cierre de entrega):**

1. Crear `src/persistencia.py` e integrar carga/guardado de socios, clases e inscripciones en `datos_gimnasio.json`, reconstruyendo cada horario como `(tuple(dias), hora_inicio, hora_fin)`.
2. Incorporar en estadísticas y menú los socios sin inscripciones activas mediante diferencia de conjuntos y las disciplinas únicas mediante eliminación de duplicados.

## 3. Validación realizada

Al 7/11/2026 sobre `a07d82c`:

| Comando desde la raíz | Resultado | Código de salida |
|---|---|---|
| `python3 -B test_gymcontrol.py` | 10/10 aprobadas | `0` |
| `python3 -B tests/test_autenticacion_auditoria.py` | 12/12 aprobadas | `0` |

Las pruebas de auditoría usan archivos temporales. No ejecutar la regresión con `-O`, porque utiliza `assert`. Estas suites no prueban todavía la persistencia JSON ni los reportes con conjuntos pendientes.

## 4. Cierre del equipo

1. Integrar JSON y conjuntos, completar las correcciones menores de presentación y quitar `unicodedata`.
2. Ejecutar las pruebas y comprobar que los fallos devuelven un código distinto de cero.
3. Probar ABM, cupos, horarios, auditoría y reportes; modificar datos, guardar, cerrar, abrir y verificar la recuperación desde JSON.
4. Completar la documentación con los resultados reales.
5. Preparar código fuente, pruebas, documentación y archivos `.txt` y `.json` requeridos por el punto 16.
6. Probar las instrucciones del README en otro equipo y practicar la defensa de estructuras, funciones, errores y archivos.
