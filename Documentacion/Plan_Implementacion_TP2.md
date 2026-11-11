# Plan de implementación — GymControl, segunda parte

**Materia:** Algoritmos y Estructura de Datos 1 / Programación 1 — UADE.
**Revisión:** 3 de noviembre de 2026.
**Entrega:** 5 de noviembre de 2026.
**Base verificada:** `main`, commit `f81342a`. El HEAD remoto coincide y no hay PR abiertas al momento de la revisión.

Este relevamiento reemplaza el estado del 24 de octubre. Conserva la asignación de tareas y actualiza los pendientes según el código integrado. La [documentación del TP2](Documentacion_TP2.md) desarrolla los seis apartados del punto 15 de la [consigna](TP_2DA%20PARTE%20(Lunes).md).

## 1. Requisitos y correcciones

| Requisito / corrección | Estado verificado | Evidencia / pendiente |
|---|---|---|
| Modularización (§10) | Implementada | `main.py` coordina módulos de `src/`. |
| Liberación de cupos al bajar un socio | Implementada | `liberar_cupos_de_afiliado()`, con pruebas de borde y negocio. |
| Login sin bloqueo y pregunta secreta | Implementado | `src/login.py`, con reintentos y salida voluntaria. |
| Archivos de texto (§7) | Implementados | Escritura, lectura y resumen de `auditoria.txt`. `pathlib` ya fue retirado. |
| Tuplas (§5.2) | Implementadas | Horarios: días, inicio y fin. |
| Diccionarios (§5.3) | Implementados; ampliación pendiente | Resumen de auditoría y días de la semana. Faltan los catálogos de tipos/niveles del plan. |
| Excepciones (§6) | Implementadas; JSON pendiente | Auditoría, interrupciones y conversiones con `ValueError` / `TypeError`. |
| Modificación por atributo | Implementada | Socios, clases e inscripciones; PR #4 integrada. |
| Diez pruebas (§9) | Implementadas y aprobadas | 4 válidas, 3 inválidas, 2 límites y 1 de negocio, sobre 7 funciones. PR #5 integrada con código de salida corregido. |
| Código en castellano y presentación | Parcial | Persisten `code` en utilidades, `(s/cantidad)` en baja de clases y horarios sin formatear en dos consultas. |
| `sorted()` en lugar de ordenamientos manuales | Pendiente | `src/ordenamientos.py` y preparación de búsqueda binaria en `src/busquedas.py`. |
| Conjuntos (§5.1) | Pendiente obligatorio | No hay reportes con `set` integrados. |
| JSON (§8) | Pendiente obligatorio | No existen módulo de persistencia ni carga/guardado de matrices. |
| Módulos autorizados (§12) | Pendiente de confirmación | Javier confirmó el 3/11 que la autorización de `datetime` todavía no está confirmada; revisar también los demás módulos. |
| Documentación (§15) | Actualizada al alcance real | Falta completar JSON/conjuntos y sus resultados después de implementarlos. |

## 2. Tareas por integrante

### Javier Candalaft (`dev-canda`)

**Hecho:** login con reintentos y pregunta secreta; auditoría de accesos y ABM; cierre de sesión controlado; reemplazo de `pathlib` por `os.path` y `open()` (PR #6 integrada). README, documentación en seis apartados y este plan actualizados al estado verificado del 3/11.

**Pendiente:**

1. Confirmar con la cátedra el uso de `datetime` y sus métodos, y los módulos usados en el sistema y las pruebas. La consulta sigue sin resolución; no se sustituye por otro módulo cuya autorización tampoco esté confirmada.
2. Después de integrar el trabajo de Edney, documentar el formato JSON real, el momento del guardado, la recuperación de horarios y el tratamiento de errores; explicar los reportes con conjuntos.
3. Incorporar el resultado real de la prueba de recuperación tras reinicio y actualizar el cierre documental.

### Lucas Cragaris (`dev-lucas-2`)

**Hecho:** modularización; liberación de cupos; diez pruebas independientes sin clases propias; captura específica de `ValueError` y `TypeError`; eliminación de `es_string()` y `pedir_opcion()` sin uso; corrección de la variable local que ocultaba la matriz de clases. La PR #5 ya está integrada y el ejecutor propaga los fallos con salida `1`.

**Pendiente individual del plan:** ninguno detectado. Participa con el equipo en la validación final.

### Tomás van Nynatten (`dev-tom-2`)

**Hecho:** traducción de la mayor parte del código; horarios con tuplas; modificación por atributo de socios, clases e inscripciones (PR #4 integrada); confirmaciones `(s/n)` en bajas de socios e inscripciones.

**Pendiente:**

1. Resolver el uso de `unicodedata` en `normalizar_dia()`: el plan propone sustituirlo por reemplazos simples de vocales acentuadas.
2. Usar `formatear_horario()` en `buscar_clase_binaria()` y `ordenar_clases_por_nivel()`, donde se imprime la tupla sin formatear.
3. Cambiar `(s/cantidad)` por `(s/n)` en la confirmación de baja de clases.
4. Renombrar `code` a `codigo` en parámetros, usos y documentación de `src/utilidades.py`.

### Edney Ribeiro (`dev-ed2`)

**Hecho:** búsqueda genérica con `filter` y lambda de la primera parte.

**Pendiente, con prioridad en JSON y conjuntos:**

1. Crear `src/persistencia.py` e integrar carga/guardado de socios, clases e inscripciones en `datos_gimnasio.json`. Manejar archivo inexistente, JSON inválido y errores de acceso sin ocultar fallos. Reconstruir cada horario como `(tuple(dias), hora_inicio, hora_fin)` y conservar las referencias de las matrices compartidas al cargar. Definir cuándo se guarda y comprobar recuperación tras reinicio.
2. Incorporar en estadísticas y menú los socios sin inscripciones activas mediante diferencia de conjuntos y las disciplinas únicas mediante eliminación de duplicados.
3. Definir `NIVELES_CLASE` y `TIPOS_SOCIO` como diccionarios y usarlos en las funciones que recuperan sus nombres. Los diccionarios existentes ya cubren el requisito básico; esta ampliación sigue asignada.
4. Sustituir selección, inserción y burbujeo por `sorted()` en los tres reportes de ordenamiento y ordenar por código antes de la búsqueda binaria. Actualizar los títulos de los reportes para que describan el algoritmo real.

## 3. Validación realizada

El 3/11/2026 se ejecutaron en macOS, con Python 3:

| Comando desde la raíz | Resultado | Código de salida |
|---|---|---|
| `python3 -B test_gymcontrol.py` | 10/10 aprobadas | `0` |
| `python3 -B tests/test_autenticacion_auditoria.py` | 12/12 aprobadas | `0` |

Las pruebas de auditoría usan archivos temporales. No ejecutar la regresión con `-O`, porque utiliza `assert`. Estas suites no prueban la persistencia JSON ni los reportes con conjuntos pendientes.

## 4. Cierre del equipo antes del 5/11

1. Integrar JSON y conjuntos, completar las correcciones asignadas y resolver las consultas de módulos autorizados.
2. Ejecutar las pruebas y comprobar que los fallos devuelven un código distinto de cero.
3. Probar ABM, cupos, horarios, auditoría y reportes; modificar datos, guardar, cerrar, abrir y verificar la recuperación desde JSON.
4. Completar la documentación con los resultados, no con funcionalidades previstas.
5. Preparar código fuente, pruebas, documentación y archivos `.txt` y `.json` requeridos por el punto 16. `auditoria.txt` está excluido de Git y se genera al ejecutar: preparar un historial de demostración sin datos personales.
6. Probar las instrucciones del README en otro equipo y practicar la defensa de estructuras, funciones, errores y archivos.
