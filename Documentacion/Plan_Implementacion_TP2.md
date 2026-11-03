# Plan de Implementación Actualizado - GymControl (Segunda Parte)

**Materia:** Algoritmos y Estructura de Datos 1 / Programación 1  
**Institución:** Universidad Argentina de la Empresa (UADE)  
**Año y Cuatrimestre:** 2026 - 2.º Cuatrimestre (Lunes por la noche - N.º 577502)  
**Docentes:** Lic. Gustavo E. Escandell y Lic. Facundo Marianelli  
**Fecha de Corte del Relevamiento:** 24 de Octubre de 2026  
**Fecha Límite de Entrega:** **05 de Noviembre de 2026** (Quedan 12 días)

---

## 1. Resumen de Estado General (Checklist de Consignas)

| Requisito / Corrección | Estado Actual | Módulo / Archivo |
|---|---|---|
| **Modularización del sistema (§10)** | ✅ **COMPLETADO** | `main.py` y `src/*.py` |
| **Corrección: Liberar cupos al bajar socio** | ✅ **COMPLETADO** | `src/socios.py` (`liberar_cupos_de_afiliado`) |
| **Corrección: Login sin bloqueo de 3 intentos** | ✅ **COMPLETADO** | `src/login.py` (`iniciar_sesion`) |
| **Corrección: Login con pregunta secreta** | ✅ **COMPLETADO** | `src/login.py` y `src/datos.py` |
| **Archivos de Texto `.txt` (§7)** | ✅ **COMPLETADO** *(Revisar `pathlib`)* | `src/auditoria.py` y `auditoria.txt` |
| **Tuplas `tuple` (§5.2)** | ✅ **COMPLETADO** *(Quitar `unicodedata`)* | `src/datos.py` y `src/clases.py` |
| **Corrección: Modificación granular** | 🟡 **PARCIAL (Falta en inscripciones)** | Hecho en `socios.py` y `clases.py`; falta en `inscripciones.py` |
| **Corrección: Código 100% en castellano** | 🟡 **CASI LISTO (98%)** | Falta parámetro `code` en `utilidades.py` y textos `(s/cantidad)` |
| **Diccionarios `dict` (§5.3)** | 🟡 **PARCIAL** | Usado en `auditoria.py` y `clases.py`; falta en `datos.py` |
| **Excepciones `try / except` (§6)** | 🟡 **PARCIAL** | Hecho en `auditoria.py` y `main.py`; falta especificar `ValueError` en `validaciones.py` y agregar en JSON |
| **Corrección: Usar `sorted()` nativo** | ❌ **PENDIENTE** | `src/ordenamientos.py` y `src/busquedas.py` |
| **Conjuntos `set` (§5.1)** | ❌ **PENDIENTE** | `src/estadisticas.py` y `src/menus.py` |
| **Archivos JSON `.json` (§8)** | ❌ **PENDIENTE** | `src/persistencia.py` (a crear) y `datos_gimnasio.json` |
| **10 Pruebas Unitarias (§9)** | ❌ **PENDIENTE** | `test_gymcontrol.py` (a crear, sin usar `class`) |
| **Documentación Final (§15)** | ❌ **PENDIENTE** | `Documentacion/Documentacion_TP2.md` |

---

## 2. Estado por Integrante: Lo Hecho vs. Lo que Falta

### 👤 1. Lucas Cragaris (`dev-lucas-2`)

#### ✅ Lo que ya hizo:
1. **Modularización completa (`117aacc`, `1512cd7`):** Dividió el archivo monolítico `tp.py` (1243 líneas) en los módulos de `src/` y `main.py`, documentando la arquitectura en `Documentacion/Documentacion_Modularizacion.md`.
2. **Corrección del bug de liberación de cupos (`3133e71`):** Creó `liberar_cupos_de_afiliado()` en `src/socios.py`, la integró en `eliminar_afiliados()` antes de borrar las inscripciones y ajustó la coherencia de los cupos iniciales en `src/datos.py`.
3. **Configuración de repositorio (`.gitignore`) y plan de implementación inicial.**

#### ⏳ Lo que le falta hacer:
1. **Desarrollar las 10 Pruebas Unitarias (`test_gymcontrol.py`) [Requisito §9]:**
   - Crear un archivo ejecutable de forma independiente (`python3 test_gymcontrol.py`) **sin usar `class` ni `unittest.TestCase`** (para cumplir §12.1).
   - Cubrir **al menos 5 funciones distintas** del sistema con la distribución obligatoria:
     - **4 casos válidos** (ej.: `es_telefono_valido("11-2587-8779")`, `es_nombre_clase_valido("Yoga Integral")`, `socio_esta_inscripto_en_clase(101, 205)`, `buscar_posicion_usuario("ADMIN")`).
     - **3 casos inválidos** (ej.: `es_telefono_valido("1125878779")`, `es_nombre_clase_valido("Crossfit 123")`, `es_hora_valida("25:00")`).
     - **2 casos límite** (ej.: `liberar_cupos_de_afiliado` para un socio con 0 inscripciones; `es_hora_valida("00:00")` y `"23:59"`).
     - **1 caso relevante de negocio** (comprobar que `liberar_cupos_de_afiliado` devuelve 1 cupo en inscripciones activas y no duplica cupos en inactivas).
   - Imprimir en cada prueba los 5 elementos exigidos: 1) Función probada, 2) Datos utilizados, 3) Resultado esperado, 4) Resultado obtenido, 5) Estado (`APROBADA` / `FALLIDA`).
2. **Corregir `try / except` en `src/validaciones.py` [Requisito §6]:**
   - Reemplazar el `except:` genérico en `es_entero()` y `es_flotante()` por `except (ValueError, TypeError):` (la consigna prohíbe usar `try/except` indiscriminados).
   - Eliminar `es_string()` que no se utiliza en ningún módulo.
3. **Limpieza en `src/socios.py` e `src/inscripciones.py` [Requisito §10]:**
   - Eliminar la función muerta `pedir_opcion()` en `src/socios.py` (líneas 25–51).
   - En `listar_clases_socio()` (`src/inscripciones.py`, línea 102), renombrar la variable local `clases = clases_de_socio(codigo)` a `nombres_clases = clases_de_socio(codigo)` para no sombrear la matriz global `clases`.

---

### 👤 2. Javier Candalaft (`dev-canda`)

#### ✅ Lo que ya hizo:
1. **Nuevo sistema de autenticación (`7fc6f4b`):** Eliminó el límite de 3 intentos en `src/login.py`, agregó la opción de salida voluntaria (`0`) e implementó el ingreso alternativo mediante pregunta de seguridad normalizada.
2. **Subsistema de auditoría en texto plano (`7fc6f4b`):** Creó `src/auditoria.py` y la integración con `auditoria.txt` en todos los ABM (socios, clases, inscripciones y login), incluyendo lectura (`leer_auditoria()`), conteo con diccionario (`resumir_auditoria()`) y opción 7 del menú principal (`mostrar_auditoria()`).
3. **Unificación del punto de entrada (`e3d3c66`):** Ajustó `main.py` con manejo de `EOFError`, `KeyboardInterrupt` y `finally: cerrar_sesion()`.

#### ⏳ Lo que le falta hacer:
1. **Adecuar `src/auditoria.py` a las restricciones técnicas de librerías [Requisito §12.1 y §12.3]:**
   - Quitar `from pathlib import Path` (que instancia un objeto `Path` y usa métodos orientados a objetos como `RUTA_AUDITORIA.open(...)`) y reemplazarlo por `open("auditoria.txt", ..., encoding="utf-8")` (o `os.path.join` como ya se usa en `main.py`).
   - Verificar si el módulo `datetime` (`fromisoformat`, `astimezone`) fue autorizado en clase; en caso contrario, simplificar el registro de fecha/hora o consultar al docente el lunes.
2. **Redactar la Documentación Final de Entrega (`Documentacion/Documentacion_TP2.md`) [Requisito §15]:**
   - Armar el documento explicativo obligatorio con las 6 secciones del punto 15:
     - **a. Descripción de las mejoras:** cambios e incorporaciones respecto de la Parte 1.
     - **b. Estructuras de datos:** dónde y por qué se usaron Conjuntos (`set`), Tuplas (`tuple`) y Diccionarios (`dict`).
     - **c. Persistencia:** qué se guarda en `auditoria.txt` y qué en `datos_gimnasio.json`, y cómo se recupera.
     - **d. Excepciones:** qué errores se controlan (`ValueError`, `FileNotFoundError`, `OSError`, etc.) y dónde.
     - **e. Pruebas unitarias:** tabla con las 10 pruebas, funciones testeadas y casos considerados.
     - **f. Cambios respecto de la Parte 1:** comparativa clara entre la entrega 1 y la entrega 2.
3. **Actualizar `README.md`:**
   - Actualizar la ruta del comando de pruebas unitarias (`python3 test_gymcontrol.py`) y mencionar la persistencia en JSON cuando esté integrada.

---

### 👤 3. Tomás van Nynatten (`dev-tom-2`)

#### ✅ Lo que ya hizo:
1. **Normalización del código al castellano (`c7c6b2a`):** Tradujo nombres de matrices, constantes de índices y funciones de todos los módulos principales.
2. **Implementación de Tuplas (`tuple`) para horarios (`56119e7`, `0f68f27`):** Incorporó la tupla `((dias...), hora_inicio, hora_fin)` en `src/datos.py` y programó la carga validada en `pedir_horario()` y su visualización con `formatear_horario()` en `src/clases.py`.
3. **Modificación granular por atributo en socios y clases (`56119e7`):** Reemplazó la edición secuencial obligatoria por submenús interactivos en `modificar_socio()` (`src/socios.py`) y `modificar_clase()` (`src/clases.py`).

#### ⏳ Lo que le falta hacer:
1. **Eliminar `import unicodedata` en `src/clases.py` [Requisito §12.3 y §12.4]:**
   - En `normalizar_dia()` (`src/clases.py`, líneas 1 y 21–26), reemplazar `unicodedata.normalize("NFD", ...)` por una función simple con `.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")` para no utilizar librerías no vistas en la cursada.
2. **Llevar `modificar_inscripcion()` a submenú granular en `src/inscripciones.py` [Corrección de exposición]:**
   - Actualmente `modificar_inscripcion()` (líneas 136–187) sigue pidiendo todos los datos de corrido ingresando `"si"` para mantener. Cambiarlo a un submenú con `1. Modificar asistencias`, `2. Modificar estado (Activa/Inactiva)`, `0. Salir`, manteniendo la lógica de actualización de cupos.
3. **Formateo de horarios y detalles finales de traducción:**
   - Usar `formatear_horario()` al imprimir clases en `buscar_clase_binaria()` (`src/busquedas.py`, línea 71) y en `ordenar_clases_por_nivel()` (`src/ordenamientos.py`, línea 60), donde hoy se imprime la tupla cruda.
   - Cambiar el texto `(s/cantidad)` por `(s/n)` en los prompts de confirmación de baja en `src/socios.py` (línea 98), `src/clases.py` (línea 124) y `src/inscripciones.py` (línea 126).
   - Renombrar el parámetro `code` a `codigo` en las funciones de `src/utilidades.py`.

---

### 👤 4. Edney Ribeiro (`dev-ed2`)

#### ✅ Lo que ya hizo:
1. **En Parte 1 (`ea40e12`):** Implementó la función genérica `buscar_posicion()` con `filter` y `lambda` en `src/utilidades.py`.
2. **En Parte 2 (`4099ab3`):** Sincronizó su rama `dev-ed2` con `dev-lucas-2`, pero aún no subió los commits de sus temas asignados de la Parte 2.

#### ⏳ Lo que le falta hacer *(Prioridad Alta)*:
1. **Persistencia en Archivos JSON (`src/persistencia.py` + `datos_gimnasio.json`) [Requisito §8]:**
   - Crear `src/persistencia.py` usando el módulo estándar `json`.
   - Implementar `guardar_datos_json()` que guarde `socios`, `clases` e `inscripciones` en `datos_gimnasio.json` manejando excepciones `OSError` con `try / except`.
   - Implementar `cargar_datos_json()` que recupere los datos al iniciar el sistema, controlando `FileNotFoundError` (si no existe, lo crea con los datos iniciales de `src/datos.py`) y `ValueError` / `json.JSONDecodeError`.
   - **Detalle clave:** Al cargar `clases` desde el JSON, convertir el campo horario nuevamente a tupla `(tuple(clase[4][0]), clase[4][1], clase[4][2])` para preservar el tipo `tuple` en memoria.
   - Llamar a `cargar_datos_json()` al inicio de `ejecutar()` en `main.py` y a `guardar_datos_json()` al realizar altas/bajas/modificaciones o al cerrar el programa.
2. **Implementar Conjuntos (`set`) en `src/estadisticas.py` y `src/menus.py` [Requisito §5.1]:**
   - Agregar en `src/estadisticas.py`:
     - **Socios sin clases activas (Diferencia de conjuntos):** `codigos_todos = {s[SOCIO_CODIGO] for s in socios}` menos `codigos_activos = {i[INSCRIPCION_CODIGO_SOCIO] for i in inscripciones if i[INSCRIPCION_ESTADO] == 1}`. Mostrar los socios resultantes.
     - **Disciplinas únicas (Eliminación de duplicados):** conjunto con los nombres de clases disponibles.
   - Incorporar estas opciones en el menú de Cálculos Estadísticos (`src/menus.py`).
3. **Ampliar Diccionarios (`dict`) en `src/datos.py` [Requisito §5.3]:**
   - Definir los diccionarios `NIVELES_CLASE = {1: "Principiante", 2: "Intermedio", 3: "Avanzado"}` y `TIPOS_SOCIO = {1: "Mensual", 2: "Libre", 3: "Premium"}` en `src/datos.py` y usarlos con `.get(codigo, "Desconocido")` dentro de `obtener_nombre_nivel()` y `obtener_nombre_tipo()`.
4. **Reemplazar ordenamientos manuales por `sorted()` nativo [Corrección de exposición]:**
   - En `src/ordenamientos.py`, reemplazar los bucles manuales de Selección, Inserción y Burbujeo por `sorted(socios, key=lambda fila: fila[SOCIO_EDAD])`, `sorted(clases, key=lambda fila: fila[CLASE_NIVEL])` y `sorted(inscripciones, key=lambda fila: fila[INSCRIPCION_ASISTENCIAS])`.
   - En `src/busquedas.py` (`buscar_clase_binaria`), ordenar la copia de clases con `sorted(clases, key=lambda fila: fila[CLASE_CODIGO])` antes de aplicar la búsqueda binaria.

---

## 3. Cronograma de Recta Final (24/10 al 05/11)

| Fecha | Meta / Hito | Responsables |
|---|---|---|
| **Sábado 24/10 – Martes 27/10** | Limpieza de librerías (`unicodedata`, `pathlib`), submenú en inscripciones, `sorted()` nativo, diccionarios en `datos.py` y conjuntos (`set`) en `estadisticas.py`. | Tomás, Javier, Edney |
| **Miércoles 28/10 – Viernes 30/10** | Implementación e integración de persistencia JSON (`src/persistencia.py`) y armado de las 10 pruebas unitarias (`test_gymcontrol.py`). | Edney, Lucas |
| **Sábado 31/10 – Domingo 01/11** | Merge de todas las ramas en `main`, prueba integral de punta a punta y redacción de `Documentacion_TP2.md` (§15). | Javier, Lucas, Todos |
| **Lunes 02/11 (Última clase)** | Consulta final con los profesores mostrando el sistema completo y validación de dudas sobre la defensa. | Todos |
| **Martes 03/11 – Miércoles 04/11** | Simulacro de defensa oral grupal (repaso de preguntas del punto 17) y empaquetado final de archivos (`.py`, `.txt`, `.json`, `.pdf`). | Todos |
| **Jueves 05/11** | **ENTREGA OFICIAL DEL TP2** | Todos |
