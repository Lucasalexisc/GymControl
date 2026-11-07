# Estado actual y pendientes para cerrar el TP2 — GymControl

**Fecha de relevamiento:** 7 de noviembre de 2026  
**Base verificada:** `main` / `dev-lucas-2` (commit `a07d82c`, incluye PR #4, #5, #6, #7 y #8)

---

## 1. ¿Qué ya está listo e integrado en `main`?

- **Modularización (§10):** `main.py` coordina los módulos separados en `src/`.
- **Autenticación y sesión:** Ingreso por contraseña o pregunta de seguridad, reintentos ilimitados, cambio de método y salida voluntaria (`src/login.py`).
- **Archivos de texto y Auditoría (§7):** Escritura, lectura y resumen en `auditoria.txt` usando `os.path` y `open()` (`src/auditoria.py`), consultable desde la opción `7` del menú principal.
- **Tuplas (§5.2):** Horarios de clases representados como `((dias...), hora_inicio, hora_fin)` con validación de días y rangos horarios (`src/clases.py` y `src/datos.py`).
- **Diccionarios (§5.3):**
  - Conteo de operaciones en `resumir_auditoria()` (`src/auditoria.py`).
  - Normalización de días en `DIAS_SEMANA` (`src/clases.py`).
  - Catálogos `NIVELES_CLASE` y `TIPOS_SOCIO` integrados en `obtener_nombre_nivel()` y `obtener_nombre_tipo()` (`src/datos.py`, PR #8).
- **Ordenamientos con `sorted()`:** Reemplazo de selección, inserción y burbujeo por `sorted()` en `src/ordenamientos.py`, `src/busquedas.py` y actualización de etiquetas en `src/menus.py` (PR #8).
- **Modificación por atributo individual:** Submenús para socios, clases e inscripciones (PR #2 y PR #4).
- **Liberación de cupos al eliminar socio:** Implementada en `liberar_cupos_de_afiliado()` (`src/socios.py`).
- **Pruebas unitarias (§9):**
  - `test_gymcontrol.py`: 10 pruebas (4 casos válidos, 3 inválidos, 2 límite y 1 caso relevante del negocio sobre 7 funciones) sin uso de clases (`class`).
  - `tests/test_autenticacion_auditoria.py`: 12 pruebas de regresión para login y auditoría.

---

## 2. ¿Qué está faltando para cumplir el 100% de la consigna?

### A. Requisitos obligatorios faltantes (Críticos)

1. **Conjuntos (`set`) — Puntos 2, 5.1 y 14 de la consigna**
   - **Problema:** Actualmente no se utiliza ningún `set` en todo el proyecto.
   - **Qué implementar:**
     - En `src/estadisticas.py`:
       - `socios_sin_clases_activas()`: usar diferencia de conjuntos (`set` de todos los códigos de socios menos `set` de socios con inscripciones activas) para listar qué afiliados no cursan ninguna actividad.
       - `disciplinas_unicas()`: usar un `set` con los nombres de las clases para eliminar duplicados y mostrar las disciplinas únicas disponibles.
     - En `src/menus.py`: agregar estas dos opciones (`5` y `6`) al menú de Cálculos Estadísticos.

2. **Archivos JSON (Persistencia de datos) — Puntos 2, 8 y 14 de la consigna**
   - **Problema:** No existe `src/persistencia.py` ni `datos_gimnasio.json`. Al cerrar el programa, las altas, bajas y modificaciones de socios, clases e inscripciones se pierden porque solo están en memoria.
   - **Qué implementar:**
     - Crear `src/persistencia.py` con funciones `guardar_datos()` y `cargar_datos()` utilizando `json` y `os.path`.
     - Al cargar desde `datos_gimnasio.json`, reconstruir la tupla de horarios `(tuple(dias), hora_inicio, hora_fin)` de cada clase (ya que JSON transforma las tuplas en listas) y actualizar las listas `socios`, `clases` e `inscripciones` *in-place* (`[:]`) para mantener las referencias entre módulos.
     - Manejar excepciones (`FileNotFoundError`, `json.JSONDecodeError`, `KeyError`, `ValueError`, `OSError`).
     - Llamar a `cargar_datos()` al iniciar `main.py` y a `guardar_datos()` luego de cada alta, baja o modificación en `src/socios.py`, `src/clases.py` y `src/inscripciones.py`.

3. **Archivos exigidos en la entrega — Punto 16 (ítems 3 y 4)**
   - **Problema:** El punto 16 pide incluir en la entrega los archivos `.txt` y `.json` utilizados por el sistema. Hoy no están versionados en el repositorio (`auditoria.txt` está en `.gitignore`).
   - **Qué hacer:** Generar `datos_gimnasio.json` y un `auditoria.txt` de demostración limpio, y quitar `auditoria.txt` de `.gitignore` para que ambos formen parte de la entrega.

---

### B. Restricciones técnicas y detalles de código / presentación

4. **Quitar `unicodedata` en `src/clases.py` — Punto 12.3 (Librerías no vistas en la materia)**
   - En `normalizar_dia()` (`src/clases.py`) se importa `unicodedata`. Para evitar observaciones por librerías no vistas en clase, reemplazarlo por un reemplazo simple de vocales acentuadas (`á->a`, `é->e`, `í->i`, `ó->o`, `ú->u`).

5. **Mensaje de confirmación y formato de horarios en consultas**
   - En `eliminar_clase()` (`src/clases.py`): cambiar el texto `(s/cantidad):` por `(s/n):`.
   - En `buscar_clase_binaria()` (`src/busquedas.py`) y `ordenar_clases_por_nivel()` (`src/ordenamientos.py`): se está imprimiendo `fila[CLASE_HORARIO]` como tupla cruda `(('Lunes', 'Miércoles'), '08:00', '09:00')` y `fila[CLASE_NIVEL]` como número. Usar `formatear_horario()` y `obtener_nombre_nivel()`.

---

### C. Documentación final — Punto 15

6. **Actualizar la documentación de entrega (`Documentacion/Documentacion_TP2.md` y `README.md`)**
   - Una vez integrados los conjuntos (`set`), la persistencia JSON y las correcciones anteriores, actualizar la documentación para describir el funcionamiento real implementado y el resultado de las pruebas.
