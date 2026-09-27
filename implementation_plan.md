# Plan de Acción y Desarrollo - GymControl (2da Entrega)

**Materia:** Algoritmos y Estructura de Datos 1 / Programación 1 (UADE)  
**Fecha de Entrega:** 5 de noviembre de 2026  
**Objetivo:** Evolucionar el sistema actual (+1200 líneas en un solo archivo) hacia una arquitectura modular, robusta y alineada estrictamente a las consignas de la 2da parte del Trabajo Práctico.

---

## 📋 Respuestas a las Consultas Principales

### 1. Modularización del Código (Separación en múltiples archivos)
Actualmente, todo el sistema se encuentra en un único archivo (`tp.py` de 1243 líneas). Para estructurarlo adecuadamente sin violar las restricciones de la materia (sin utilizar clases/POO), reordenaremos el proyecto en un paquete de módulos con responsabilidades aisladas:

* **`main.py`**: Punto de entrada del sistema. Encargado de coordinar el login, mostrar el menú principal y gestionar la inicialización y el guardado final de los datos.
* **`config.py`**: Almacena constantes globales del sistema, rutas de archivos y **tuplas** inmutables con configuraciones y catálogos fijos.
* **`validations.py`**: Agrupa todas las funciones de validación de datos (expresiones regulares `re`, números enteros/flotantes y captura de excepciones iniciales de entrada).
* **`persistence.py`**: Módulo dedicado a la lectura y escritura de **archivos JSON** (socios, clases, inscripciones) y **archivos de texto TXT** (logs de auditoría y reportes).
* **`affiliates.py`**: Lógica del módulo de gestión de socios (ABM / CRUD, búsquedas de socios).
* **`classes.py`**: Lógica del módulo de gestión de clases (ABM / CRUD, control de cupos).
* **`enrollments.py`**: Lógica del módulo de inscripciones (alta/baja de inscripciones, actualización de cupos, cruce socio-clase).
* **`statistics.py`**: Funciones de cálculos matriciales/estadísticas, algoritmos de ordenamiento (burbujeo, inserción, selección) y búsquedas específicas.
* **`test_gymcontrol.py`**: Módulo independiente para la ejecución de las **10 pruebas unitarias** requeridas.

---

### 2. Mejoras sobre lo que ya está hecho
Sin salir de los contenidos habilitados por la materia, implementaremos las siguientes mejoras directas sobre el código existente:

1. **Migración de Listas/Posiciones Fijas a Diccionarios (`dict`)**:
   * *Problema actual:* Las entidades usan subíndices fijos como `row[0]`, `row[1]`, lo que dificulta la lectura y mantenimiento del código.
   * *Mejoría:* Representar socios, clases e inscripciones mediante diccionarios en Python (ej: `{"codigo": 101, "nombre": "Juan", ...}`) o diccionarios indexados por clave primaria (`socios[101] = {...}`).
2. **Eliminación de `except:` genéricos vacíos por Excepciones Específicas**:
   * Refactorizar funciones como `es_entero()` o `es_flotante()` y las operaciones de entrada/salida para capturar excepciones explícitas (`ValueError`, `FileNotFoundError`, `KeyError`, `json.JSONDecodeError`) con mensajes orientados al usuario.
3. **Uso Justificado de Tuplas (`tuple`)**:
   * Definir las listas de opciones fijas y pares clave-valor inmutables mediante tuplas (por ejemplo: tipos de socios `((1, "Mensual"), (2, "Libre"), (3, "Premium"))` y niveles de clase `((1, "Principiante"), (2, "Intermedio"), (3, "Avanzado"))`).
4. **Uso de Conjuntos (`set`) para Optimizaciones**:
   * Implementar conjuntos para validar presencia de códigos únicos sin duplicación, extraer la lista de socios únicos con inscripciones activas y comparar categorías.
5. **Limpieza de Código Muerto y Duplicado**:
   * Eliminar funciones en desuso (como la función `input_option()` observada en el código) y consolidar la lectura de datos con la nueva capa de validaciones.

---

### 3. Nuevas Funcionalidades Requeridas por la Consigna
Integración estricta de los 7 requerimientos obligatorios descritos en la consigna oficial:

1. **Persistencia de Datos en JSON (`.json`)**:
   * Archivos `socios.json`, `clases.json`, `inscripciones.json` y `usuarios.json`.
   * Carga inicial al arrancar el programa (con fallback a datos precargados si el archivo no existe).
   * Guardado persistente automático ante cambios y al salir del sistema.
2. **Persistencia en Archivos de Texto (`.txt`)**:
   * **Registro de Auditoría (`log_actividades.txt`)**: Cada acción importante (login fallido/exitoso, alta/baja de socio, inscripción) guardará una línea de texto con fecha/hora y detalle.
   * **Exportación de Reportes (`reporte_asistencias.txt`)**: Posibilidad de exportar resúmenes a un archivo `.txt`.
3. **Módulo de Pruebas Unitarias (`test_gymcontrol.py`)**:
   * Implementación de **10 pruebas unitarias de funciones clave** ejecutables de forma independiente:
     * 4 pruebas para casos válidos.
     * 3 pruebas para casos inválidos / errores.
     * 2 pruebas para casos límite (ej: cupo en 0, edad en límites 0 o 100).
     * 1 prueba para un caso de negocio relevante (prevención de inscripción duplicada).
4. **Manejo de Excepciones Personalizado (`try / except`)**:
   * Control de errores durante la lectura/escritura de archivos JSON/TXT e ingreso de datos en la consola.
5. **Documentación del Proyecto (`documentacion_gymcontrol.md`)**:
   * Actualización del informe en Markdown justificando dónde y por qué se usó cada estructura de datos (Conjuntos, Tuplas, Diccionarios), cómo funciona la persistencia y los resultados de las pruebas unitarias.

---

## 🗓️ Cronograma / Plan de Acción (Hasta el 5/11)

| Etapa | Fechas Estimadas | Tareas Principales | Entregable / Hito |
|---|---|---|---|
| **Fase 1: Modularización & Refactor** | 28 Sep - 05 Oct | - Crear la estructura de módulos (`main.py`, `config.py`, `validations.py`, etc.).<br>- Migrar datos precargados y estructuras a **Diccionarios** y **Tuplas**.<br>- Eliminar código muerto y duplicados. | Código base separado en módulos funcionando correctamente. |
| **Fase 2: Persistencia (JSON & TXT)** | 06 Oct - 15 Oct | - Crear el módulo `persistence.py`.<br>- Implementar lectura/escritura en JSON (`socios.json`, `clases.json`, `inscripciones.json`).<br>- Implementar sistema de logs de auditoría y reportes en `.txt`. | Persistencia completa y transparente al usuario. |
| **Fase 3: Excepciones & Conjuntos** | 16 Oct - 22 Oct | - Reemplazar bloques de validación por `try / except` específicos.<br>- Implementar uso de `set` para detección de elementos únicos y duplicados.<br>- Ajustar validaciones de consola. | Sistema libre de crasheos ante entradas inválidas o fallos de E/S. |
| **Fase 4: Pruebas Unitarias** | 23 Oct - 29 Oct | - Crear `test_gymcontrol.py`.<br>- Implementar la suite de 10 pruebas unitarias con reporte explícito en consola.<br>- Verificar cobertura en al menos 5 funciones. | Suite de tests automatizados aprobada. |
| **Fase 5: Documentación & Defensa** | 30 Oct - 04 Nov | - Redactar/actualizar la documentación explicativa en `documentacion_gymcontrol.md`.<br>- Realizar pruebas de integración de punta a punta.<br>- Ensayar preguntas típicas de la defensa oral según la consigna. | Entrega lista en repositorio de Git para el 5/11. |

---

## ⚠️ Restricciones Técnicas Recordatorias
* **Prohibido el uso de Clases / POO** (`class`, constructores, objetos propios).
* **Prohibido el uso de Bases de Datos** (MySQL, SQLite, etc.).
* **Prohibido el uso de librerías externas no vistas** (Pandas, Numpy, etc.). Solo librerías estándar de Python (`json`, `re`, `functools`, `unittest`, `os`, `datetime`).

---

## 📌 Próximos Pasos Recomendados
Una vez aprobado este plan de acción por el equipo/usuario, comenzaremos de inmediato con la **Fase 1**: separación del código `tp.py` en la estructura modular de archivos `.py`.
