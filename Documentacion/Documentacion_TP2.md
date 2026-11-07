# GymControl — Documentación de la segunda entrega

**Materia:** Algoritmos y Estructura de Datos 1 / Programación 1 — UADE.
**Fecha de revisión:** 3 de noviembre de 2026.
**Responsable de esta documentación:** Javier Candalaft.
**Estado:** documentación del alcance implementado; la entrega completa tiene pendientes de integración.

Este documento cubre los seis apartados del punto 15 de la consigna. Describe el código de `main` en `f81342a` y esta actualización documental. El 3 de noviembre se verificó que el HEAD remoto coincide con esa versión y que no hay PR abiertas. La entrega es el 5 de noviembre. JSON y conjuntos siguen pendientes; esta documentación no da por cumplidos esos requisitos.

## a. Mejoras respecto de la primera parte

GymControl permite administrar socios, clases e inscripciones desde una interfaz de consola. Mantiene las búsquedas, ordenamientos y reportes de la primera entrega e incorpora:

- **Autenticación:** ingreso con contraseña o pregunta de seguridad. Permite reintentar sin un límite fijo, cambiar de método o salir con la opción `0`. El usuario se busca sin distinguir mayúsculas y espacios exteriores; la contraseña se compara exactamente. La respuesta de seguridad normaliza mayúsculas y espacios redundantes.
- **Auditoría:** registro persistente de accesos exitosos, fallidos y cancelados, cierre de sesión y altas, bajas y modificaciones. La opción `7` del menú principal permite consultar el historial y el conteo de operaciones.
- **Horarios de clases:** días de la semana y horas de inicio y fin, con validación de días y comparación de horas convertidas a minutos.
- **Modificación por atributo:** submenús para editar socios, clases e inscripciones. En inscripciones se pueden modificar las asistencias, el estado o ambos; los cambios de estado ajustan los cupos y no se permite reactivar sin cupo.
- **Liberación de cupos:** al eliminar un socio se recuperan los cupos de sus inscripciones activas y se eliminan sus inscripciones asociadas.
- **Salida controlada:** `main.py` coordina el login y el menú, maneja `EOFError` y `KeyboardInterrupt` y ejecuta el cierre de sesión en `finally`.

Se reemplazó `pathlib.Path` por `os.path` y `open()` en auditoría. La ruta sigue siendo absoluta y relativa al archivo del módulo: ejecutar el programa desde otra carpeta no cambia la ubicación de `auditoria.txt`.

La modificación por atributo de inscripciones ([PR #4](https://github.com/Lucasalexisc/GymControl/pull/4)), las diez pruebas generales y la limpieza de funciones sin uso ([PR #5](https://github.com/Lucasalexisc/GymControl/pull/5)), y la adecuación de auditoría ([PR #6](https://github.com/Lucasalexisc/GymControl/pull/6)) ya están integradas en `main`.

## b. Estructuras de datos

| Estructura | Uso y ubicación | Justificación y estado |
|---|---|---|
| Listas y matrices | `src/datos.py`: usuarios, socios, clases e inscripciones. Cada módulo opera sobre estas matrices mediante índices definidos como constantes. | Conservan la representación de la primera entrega. Se comparten en memoria; no se recuperan de JSON. |
| Tuplas | `src/clases.py`, `pedir_horario()`, y `src/datos.py`: `((dias...), hora_inicio, hora_fin)`. | Agrupan los datos de un bloque horario. Para cambiarlo se reemplaza la tupla completa. |
| Diccionarios | `src/auditoria.py`, `resumir_auditoria()`: operación → cantidad de eventos. | Permiten acumular y consultar los conteos mostrados en el historial. |
| Diccionarios | `src/clases.py`, `DIAS_SEMANA`: día normalizado → nombre para mostrar. | Permiten validar los días ingresados y recuperar una representación uniforme. |
| Conjuntos | Pendiente de incorporación en reportes. | El plan propone identificar socios sin clases activas y disciplinas únicas. El requisito todavía no está implementado en esta base. |

Ejemplo de horario: `(("Lunes", "Miércoles"), "08:00", "09:00")`.
Ejemplo de resumen: `{"ALTA_SOCIO": 2, "BAJA_SOCIO": 1}`.

## c. Persistencia

### Archivo de texto implementado

`src/auditoria.py` utiliza `auditoria.txt` en la raíz del proyecto. El archivo se crea con el primer evento y se amplía en modo `a`, con codificación UTF-8. No se vacía al iniciar ni al salir.

Cada línea contiene cuatro campos separados por ` | `:

```text
2026-10-26T18:30:00-03:00 | admin | ALTA_SOCIO | Código=113
```

La fecha y la zona horaria provienen del equipo que ejecuta el programa. Los campos de texto se limpian para que un salto de línea o un separador ingresado por el usuario no cree registros adicionales.

`leer_auditoria()` recupera los eventos con cuatro campos y una fecha interpretable. `mostrar_auditoria()` imprime el historial y utiliza `resumir_auditoria()` para contar las operaciones. El historial sigue disponible en la siguiente ejecución. Si el archivo todavía no existe, la lectura devuelve una lista vacía.

No se registran contraseñas ni respuestas de seguridad. Los cambios de socios y clases se identifican por código; los accesos registran el nombre de usuario. El archivo es local y editable: no garantiza que terceros no lo alteren. Un fallo de escritura genera un aviso, pero no revierte la operación del gimnasio.

### Archivos JSON pendientes

Todavía no existen `src/persistencia.py` ni `datos_gimnasio.json` en esta base. Los socios, clases e inscripciones se inicializan desde `src/datos.py` y se restablecen al reiniciar. El historial de auditoría no reconstruye esas matrices.

El plan asigna a Edney la carga y el guardado en JSON. Cuando se integre, habrá que documentar el formato real, cuándo se guarda, qué ocurre ante archivos inválidos y cómo se reconstruyen las tuplas de horarios. También se deberá verificar el ciclo completo: modificar datos, cerrar, volver a abrir y recuperar los cambios. No se da por cumplido el requisito de JSON antes de esa comprobación.

## d. Excepciones y validaciones

| Situación | Tratamiento actual |
|---|---|
| Auditoría inexistente | `FileNotFoundError`: se devuelve `[]`. |
| Fallo al escribir auditoría | `OSError`: se muestra un aviso y se devuelve `False`. |
| Fallo al leer o decodificar auditoría | `OSError` o `UnicodeError`: se avisa y se devuelve `None`, distinto de un historial vacío. |
| Fecha inválida en una línea | `ValueError`: se omite esa línea y continúa la lectura. |
| Fin de entrada o interrupción por teclado | `main.py` captura `EOFError` y `KeyboardInterrupt` y ejecuta el cierre en `finally`. |
| Datos numéricos inválidos | Las funciones de validación y los menús solicitan un nuevo ingreso cuando corresponde. `es_entero()` y `es_flotante()` capturan específicamente `ValueError` y `TypeError`. |
| Días u horas inválidos | Se solicita un nuevo ingreso. La hora final debe ser posterior a la inicial, comparando minutos. |

### Restricciones de la cátedra pendientes de confirmar

La implementación elimina `pathlib` de auditoría y conserva `datetime` para generar y validar las fechas existentes. No hay evidencia en el repositorio de que `datetime` y sus métodos hayan sido autorizados en clase. Javier confirmó el 3 de noviembre que la consulta todavía no está resuelta. Debe confirmarlo con el docente y adaptar el registro si corresponde.

La consigna exige usar módulos vistos o autorizados: pertenecer a la biblioteca estándar no alcanza para afirmar que un módulo está permitido. También queda pendiente la revisión de `unicodedata` en horarios, asignada a Tomás. Las pruebas complementarias usan módulos estándar para aislar archivos y simular entradas; su uso también debe poder explicarse y validarse con la cátedra. No se incorporan clases propias, bases de datos ni paquetes externos.

## e. Pruebas

### Regresión de autenticación y auditoría

Desde la raíz del proyecto:

```bash
python3 -B tests/test_autenticacion_auditoria.py
```

Las pruebas usan archivos temporales y no modifican `auditoria.txt` del gimnasio. El proceso termina con código `0` si todas pasan y `1` si alguna falla. No ejecutar con `-O`, porque estas comprobaciones usan `assert`.

| Caso | Funciones principales | Resultado comprobado |
|---|---|---|
| Archivo inexistente | `leer_auditoria` | Devuelve una lista vacía. |
| Escritura acumulativa | `registrar_auditoria`, `leer_auditoria`, `resumir_auditoria` | Conserva dos eventos y sus conteos. |
| Separadores y saltos | `registrar_auditoria`, `limpiar_campo` | Una entrada genera una sola línea con cuatro campos. |
| Líneas inválidas | `leer_auditoria` | Omite líneas incompletas o con fecha inválida y conserva las válidas. |
| UTF-8 inválido | `leer_auditoria` | Devuelve `None` sin interrumpir el programa. |
| Error de archivo | Lectura y escritura de auditoría | Avisan y devuelven `None` o `False`. |
| Contraseña | `iniciar_sesion` | Autentica y no registra la contraseña. |
| Pregunta de seguridad | `iniciar_sesion`, `normalizar_respuesta` | Normaliza la respuesta y no la registra. |
| Reintentos | `iniciar_sesion` | Permite cuatro fallos y luego ingreso por otro método. |
| Usuario inexistente y cancelación | `iniciar_sesion` | Rechaza el acceso y permite salir sin sesión. |
| Cierre | `cerrar_sesion` | Registra un único cierre y limpia la identidad. |
| Otra carpeta de ejecución | Inicialización de la ruta de auditoría | Conserva la ruta de la raíz del proyecto. |

### Diez pruebas generales integradas

Se ejecutan desde la raíz con `python3 -B test_gymcontrol.py`. Son independientes del programa principal y complementan las pruebas de regresión anteriores.

| N.º | Categoría | Función | Caso y resultado esperado |
|---|---|---|---|
| 1 | Válido | `es_telefono_valido` | `11-2587-8779` → `True`. |
| 2 | Válido | `es_nombre_clase_valido` | `Funcional Avanzado` → coincidencia válida. |
| 3 | Válido | `socio_esta_inscripto_en_clase` | Socio 101 en clase 205, inscripción activa → `True`. |
| 4 | Válido | `resumir_auditoria` | Dos altas y una baja → conteos 2 y 1. |
| 5 | Inválido | `es_telefono_valido` | Teléfono sin guiones → `False`. |
| 6 | Inválido | `es_entero` | `abc` → `False`. |
| 7 | Inválido | `socio_esta_inscripto_en_clase` | Socio 103 en clase 201, inscripción inactiva → `False`. |
| 8 | Límite | `es_hora_valida` | `00:00`, `23:59`, `24:00` → `True`, `True`, `False`. |
| 9 | Límite | `liberar_cupos_de_afiliado` | Socio sin inscripciones → cero cupos liberados. |
| 10 | Negocio | `liberar_cupos_de_afiliado` | Una inscripción activa y otra inactiva → recupera solo el cupo activo. |

La distribución implementada es 4 válidos, 3 inválidos, 2 límites y 1 caso de negocio, sobre 7 funciones. Cada prueba muestra la función, los datos, el resultado esperado, el obtenido y su estado. El ejecutor devuelve código `0` si todas pasan y `1` si alguna falla.

**Verificación del 3 de noviembre de 2026:** 10/10 pruebas generales y 12/12 de autenticación y auditoría aprobadas, ambas suites con código de salida `0`. Se ejecutaron con Python 3 en macOS. Este resultado no valida JSON ni conjuntos, que todavía no existen en el sistema.

## f. Cambios respecto de la primera parte y cierre de entrega

| Primera parte | Segunda parte implementada |
|---|---|
| Login con intentos limitados | Reintentos, cambio de método y salida voluntaria. |
| Ingreso con contraseña | Contraseña o pregunta de seguridad. |
| Operaciones sin historial persistente | Auditoría en texto, consulta y conteos. |
| Clases sin bloque horario | Tuplas con días y horas validadas. |
| Edición secuencial de atributos | Submenús para socios, clases e inscripciones. |
| Problema de cupos al eliminar socios | Recuperación de cupos de las inscripciones activas. |

### Pendientes para cerrar la entrega

| Responsable | Pendiente verificado |
|---|---|
| Javier | Confirmar con la cátedra la autorización de `datetime` y los módulos utilizados. Completar las secciones de JSON y conjuntos cuando se integre y pruebe su implementación. README y documentación actualizados al estado comprobado. |
| Lucas | Las diez pruebas y la limpieza asignadas ya están integradas. Participar de la prueba integral final. |
| Tomás | Resolver `unicodedata`; formatear horarios en búsqueda binaria y ordenamiento por nivel; cambiar `(s/cantidad)` por `(s/n)` en la baja de clases; traducir `code` a `codigo` en utilidades. El submenú de inscripciones y las confirmaciones de baja de socios e inscripciones ya están integrados. |
| Edney | Implementar carga/guardado JSON y recuperación de tuplas, reportes con conjuntos, diccionarios de niveles/tipos y reemplazo de ordenamientos manuales por `sorted()`. |
| Equipo | Validar el ciclo modificar → guardar → cerrar → abrir → recuperar; probar en otro equipo, preparar los archivos de entrega y practicar la defensa. |

Los diccionarios ya se utilizan en auditoría y días de la semana: el requisito existe, aunque la ampliación de Edney sigue pendiente. JSON y conjuntos son los principales requisitos obligatorios todavía ausentes.

### Preparación y comprobación final (§16 y §17)

1. Integrar las tareas pendientes del [plan de implementación](Plan_Implementacion_TP2.md).
2. Ejecutar ambas suites de pruebas y comprobar sus códigos de salida.
3. Validar la persistencia JSON tras reiniciar, incluidos horarios y cupos; documentar los resultados reales y el tratamiento de archivos inválidos o inexistentes.
4. Entregar código, pruebas, documentación y los archivos de texto y JSON necesarios. `auditoria.txt` se genera al ejecutar y está excluido de Git: incluir un historial de demostración sin datos personales. El JSON de entrega queda pendiente de su implementación.
5. Seguir el README en otro equipo con Python 3.9 o posterior y comprobar login, ABM, reportes y recuperación de datos.
6. Repasar entre todos las estructuras, validaciones, excepciones, archivos y pruebas para la defensa.

La documentación describe lo comprobado; el cierre definitivo depende de integrar y verificar las funcionalidades faltantes y confirmar las restricciones de módulos con la cátedra.
