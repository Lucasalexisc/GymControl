# GymControl — Documentación de la segunda entrega

**Materia:** Algoritmos y Estructura de Datos 1 / Programación 1 — UADE.
**Fecha de revisión:** 10 de noviembre de 2026.
**Responsables:** Equipo GymControl (Javier Candalaft, Lucas Cragaris, Tomás van Nynatten, Edney Ribeiro, Rodrigo García Solá).
**Estado:** entrega completa con todos los requisitos obligatorios implementados y verificados.

Este documento cubre los seis apartados del punto 15 de la consigna.

## a. Mejoras respecto de la primera parte

GymControl permite administrar socios, clases e inscripciones desde una interfaz de consola. Mantiene las búsquedas, ordenamientos y reportes de la primera entrega e incorpora:

- **Autenticación:** ingreso con contraseña o pregunta de seguridad. Permite reintentar sin un límite fijo, cambiar de método o salir con la opción `0`. El usuario se busca sin distinguir mayúsculas y espacios exteriores; la contraseña se compara exactamente. La respuesta de seguridad normaliza mayúsculas y espacios redundantes.
- **Auditoría en archivo de texto:** registro persistente de accesos exitosos, fallidos y cancelados, cierre de sesión y altas, bajas y modificaciones en `auditoria.txt`. La opción `7` del menú principal permite consultar el historial y el conteo de operaciones.
- **Persistencia en archivo JSON:** carga automática de `datos_gimnasio.json` al iniciar el sistema (`cargar_datos()`) y guardado automático tras cada alta, baja o modificación de socios, clases o inscripciones (`guardar_datos()`), preservando los cambios entre ejecuciones y reconstruyendo las tuplas de horarios.
- **Horarios de clases con tuplas:** días de la semana y horas de inicio y fin, con validación de días (sin depender de `unicodedata`) y comparación de horas convertidas a minutos.
- **Modificación por atributo:** submenús para editar socios, clases e inscripciones. En inscripciones se pueden modificar las asistencias, el estado o ambos; los cambios de estado ajustan los cupos y no se permite reactivar sin cupo.
- **Liberación de cupos:** al eliminar un socio se recuperan los cupos de sus inscripciones activas y se eliminan sus inscripciones asociadas.
- **Reportes con conjuntos (`set`):** identificación de socios sin clases activas mediante diferencia de conjuntos y listado de disciplinas únicas sin duplicados en el menú de estadísticas.
- **Ordenamientos optimizados con `sorted()` y catálogos con diccionarios:** sustitución de selección, inserción y burbujeo por `sorted()` en `src/ordenamientos.py` y `src/busquedas.py`, y uso de diccionarios `NIVELES_CLASE` y `TIPOS_SOCIO`.
- **Salida controlada:** `main.py` carga el estado desde JSON, coordina el login y el menú, maneja `EOFError` y `KeyboardInterrupt` y ejecuta el cierre de sesión en `finally`.

## b. Estructuras de datos

| Estructura | Uso y ubicación | Justificación |
|---|---|---|
| Listas y matrices | `src/datos.py`: usuarios, socios, clases e inscripciones. Cada módulo opera sobre estas matrices mediante índices definidos como constantes. | Conservan la representación tabular de la primera entrega y se sincronizan con `datos_gimnasio.json`. |
| Tuplas (`tuple`) | `src/clases.py` (`pedir_horario()`), `src/persistencia.py` (`reconstruir_horario()`) y `src/datos.py`: `((dias...), hora_inicio, hora_fin)`. | Agrupan de forma inmutable los días de cursada y el rango horario de cada clase. Para cambiar el horario se reemplaza la tupla completa. |
| Diccionarios (`dict`) | `src/auditoria.py` (`resumir_auditoria()`), `src/clases.py` (`DIAS_SEMANA`) y `src/datos.py` (`NIVELES_CLASE`, `TIPOS_SOCIO`). | Contabilizan eventos por operación, normalizan días ingresados y asocian códigos numéricos con los nombres de niveles de clase y tipos de socio. |
| Conjuntos (`set`) | `src/estadisticas.py` (`obtener_socios_sin_clases_activas()`, `obtener_disciplinas_unicas()`). | Permiten obtener los socios sin inscripciones activas mediante diferencia de conjuntos (`codigos_todos - codigos_activos`) y eliminar duplicados en los nombres de disciplinas. |

Ejemplo de horario: `(("Lunes", "Miércoles"), "08:00", "09:00")`.
Ejemplo de resumen: `{"ALTA_SOCIO": 2, "BAJA_SOCIO": 1}`.

## c. Persistencia

### Archivo de texto (`auditoria.txt`)

`src/auditoria.py` utiliza `auditoria.txt` en la raíz del proyecto. El archivo se amplía en modo `a`, con codificación UTF-8. No se vacía al iniciar ni al salir.

Cada línea contiene cuatro campos separados por ` | `:

```text
2026-11-05T10:00:00-03:00 | admin | ACCESO_EXITOSO | contraseña
```

`leer_auditoria()` recupera los eventos con cuatro campos y una fecha interpretable. `mostrar_auditoria()` imprime el historial y utiliza `resumir_auditoria()` para contar las operaciones. No se registran contraseñas ni respuestas de seguridad.

### Archivo JSON (`datos_gimnasio.json`)

`src/persistencia.py` almacena las matrices `socios`, `clases` e `inscripciones` en `datos_gimnasio.json` en la raíz del proyecto con codificación UTF-8 (`indent=2`).

- **Escritura (`guardar_datos()`):** se ejecuta automáticamente tras cada alta, baja o modificación efectiva en `src/socios.py`, `src/clases.py` y `src/inscripciones.py`.
- **Lectura (`cargar_datos()`):** se ejecuta al iniciar `main.py`. Si `datos_gimnasio.json` existe y es válido, actualiza las listas `socios[:]`, `clases[:]` e `inscripciones[:]` en memoria conservando las referencias compartidas entre módulos, y utiliza `reconstruir_horario()` para restituir cada horario como tupla anidada `((dias...), hora_inicio, hora_fin)`. Si el archivo no existe en la primera ejecución, lo inicializa con los datos por defecto.

## d. Excepciones y validaciones

| Situación | Tratamiento actual |
|---|---|
| Auditoría inexistente | `FileNotFoundError`: se devuelve `[]`. |
| Fallo al escribir auditoría | `OSError`: se muestra un aviso y se devuelve `False`. |
| Fallo al leer o decodificar auditoría | `OSError` o `UnicodeError`: se avisa y se devuelve `None`, distinto de un historial vacío. |
| Fecha inválida en una línea de auditoría | `ValueError`: se omite esa línea y continúa la lectura. |
| Archivo JSON inexistente al iniciar | `FileNotFoundError`: se crea `datos_gimnasio.json` con los datos iniciales. |
| Archivo JSON corrupto o con estructura inválida | `json.JSONDecodeError`, `KeyError`, `ValueError`, `TypeError`, `OSError`, `UnicodeError`: se informa un aviso y se mantienen los datos en memoria. |
| Fallo al guardar JSON | `OSError`, `TypeError`: se informa un aviso y devuelve `False`. |
| Fin de entrada o interrupción por teclado | `main.py` captura `EOFError` y `KeyboardInterrupt` y ejecuta el cierre en `finally`. |
| Datos numéricos o de texto inválidos | Las funciones de validación y los menús solicitan un nuevo ingreso cuando corresponde. `es_entero()` y `es_flotante()` capturan específicamente `ValueError` y `TypeError`. |
| Días u horas inválidos | Se solicita un nuevo ingreso. La hora final debe ser posterior a la inicial, comparando minutos. |

## e. Pruebas unitarias

### Suite principal de pruebas unitarias (`test_gymcontrol.py`)

Se ejecuta de forma independiente desde la raíz con:

```bash
python3 -B test_gymcontrol.py
```

Incluye 12 pruebas unitarias (superando el mínimo de 10 exigido en el punto 9) sobre 9 funciones distintas del sistema, sin utilizar clases (`class`):

| N.º | Categoría | Función | Caso y resultado esperado |
|---|---|---|---|
| 1 | Válido (1/4) | `es_telefono_valido` | `11-2587-8779` → `True`. |
| 2 | Válido (2/4) | `es_nombre_clase_valido` | `Funcional Avanzado` → coincidencia válida (`True`). |
| 3 | Válido (3/4) | `socio_esta_inscripto_en_clase` | Socio 101 en clase 205, inscripción activa → `True`. |
| 4 | Válido (4/4) | `resumir_auditoria` | Dos altas y una baja → `{"ALTA_SOCIO": 2, "BAJA_SOCIO": 1}`. |
| 5 | Inválido (1/3) | `es_telefono_valido` | Teléfono sin guiones → `False`. |
| 6 | Inválido (2/3) | `es_entero` | `abc` → `False`. |
| 7 | Inválido (3/3) | `socio_esta_inscripto_en_clase` | Socio 103 en clase 201, inscripción inactiva → `False`. |
| 8 | Límite (1/2) | `es_hora_valida` | `00:00`, `23:59`, `24:00` → `(True, True, False)`. |
| 9 | Límite (2/2) | `liberar_cupos_de_afiliado` | Socio sin inscripciones → `(0, 12)`. |
| 10 | Relevante del sistema | `liberar_cupos_de_afiliado` | Una inscripción activa y otra inactiva → recupera solo el cupo activo `(1, 15, 15)`. |
| 11 | Relevante (Conjuntos) | `obtener_socios_sin_clases_activas` | Diferencia de conjuntos entre socios totales y activos → `{103, 112}`. |
| 12 | Relevante (JSON + Tuplas) | `guardar_datos` / `cargar_datos` | Guardado y recuperación en JSON temporal reconstruyendo tuplas de horarios → `(True, True, 12, True)`. |

Cada prueba muestra en consola los 5 puntos obligatorios: función probada, datos utilizados, resultado esperado, resultado obtenido y si fue aprobada o no.

### Regresión de autenticación y auditoría (`tests/test_autenticacion_auditoria.py`)

```bash
python3 -B tests/test_autenticacion_auditoria.py
```

Verifica 12 casos adicionales de lectura/escritura de auditoría, manejo de errores de archivo y flujo de inicio y cierre de sesión.

**Verificación del 10 de noviembre de 2026:** 12/12 pruebas en `test_gymcontrol.py` y 12/12 en `tests/test_autenticacion_auditoria.py` aprobadas con código de salida `0`.

## f. Cambios respecto de la primera parte

| Primera parte | Segunda parte implementada |
|---|---|
| Login con intentos limitados | Reintentos ilimitados, cambio de método y salida voluntaria. |
| Ingreso solo con contraseña | Contraseña o pregunta de seguridad. |
| Datos únicamente en memoria | Persistencia en `datos_gimnasio.json` y auditoría en `auditoria.txt`. |
| Clases sin bloque horario | Tuplas inmutables con días y horas validadas. |
| Edición secuencial de todos los atributos | Submenús de modificación por atributo en socios, clases e inscripciones. |
| Problema de cupos al eliminar socios | Recuperación automática de cupos de las inscripciones activas. |
| Ordenamientos manuales (`Selección`, `Inserción`, `Burbujeo`) | Ordenamientos con `sorted()` y catálogos en diccionarios (`NIVELES_CLASE`, `TIPOS_SOCIO`). |
| Reportes únicamente matriciales | Nuevos reportes con conjuntos (`set`) para socios sin clases activas y disciplinas únicas. |
