# Documentación de Modularización: GymControl

**Materia:** Algoritmos y Estructura de Datos 1 / Programación 1  
**Institución:** Universidad Argentina de la Empresa (UADE)  
**Año y Cuatrimestre:** 2026 - 2.º Cuatrimestre  
**Docentes:** Lic. Gustavo E. Escandell y Lic. Facundo Marianelli  
**Comisión:** Lunes por la noche - N.º 577502  

---

## 1. Propósito de la Modularización

El archivo original [`tp.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/tp.py) concentraba la totalidad del sistema en un único archivo de 1243 líneas. 

Para facilitar el mantenimiento, la división de tareas en Git y la incorporación progresiva de los nuevos temas a medida que se dicten en la cursada, se realizó una **modularización 1 a 1 del código existente**.

> **IMPORTANTE:**
> - El archivo original [`tp.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/tp.py) se conservó **completamente intacto, sin modificar una sola línea**.
> - En la versión modularizada **no se alteró la lógica, los nombres de variables ni el comportamiento de ninguna función**.
> - Cada módulo conserva exactamente el código, comentarios y docstrings originales de la primera entrega.

---

## 2. Mapa de Módulos y Distribución de Responsabilidades

El sistema se organizó en 11 archivos modulares interconectados más el punto de entrada:

```
GymControl/
├── tp.py                 # Código original completo de la primera entrega (INTACTO)
├── main.py               # Punto de entrada desde la raíz (ejecuta src/main.py)
├── Documentacion_Modularizacion.md
└── src/                  # Carpeta con todos los módulos organizados del sistema
    ├── main.py           # Punto de entrada dentro de src
    ├── datos.py          # Estructuras matriciales, constantes de índices y conversores
    ├── validaciones.py   # Funciones de validación y entrada segura por teclado
    ├── utilidades.py     # Búsquedas genéricas de posiciones y verificación de existencia
    ├── login.py          # Sistema de autenticación de usuarios (3 intentos)
    ├── socios.py         # Gestión de afiliados (Altas, Bajas, Modificaciones y Listados)
    ├── clases.py         # Gestión de clases (Altas, Bajas, Modificaciones y Listados)
    ├── inscripciones.py  # Gestión de inscripciones, cupos y clases por socio
    ├── busquedas.py      # Búsqueda binaria de clases y secuencial de socios
    ├── ordenamientos.py  # Algoritmos de ordenamiento (Selección, Inserción y Burbujeo)
    ├── estadisticas.py   # Cálculos estadísticos matriciales (reduce, map)
    └── menus.py          # Menús de consola y flujo de navegación interactivo
```

---

## 3. Trazabilidad Detallada de Funciones por Módulo

A continuación se detalla qué funciones de [`tp.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/tp.py) fueron ubicadas en cada módulo correspondiente:

### 3.1 [`datos.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/datos.py)
Contiene las matrices en memoria y las constantes numéricas de índices de columna:
* **Constantes:** `LOGIN_USERNAME`, `LOGIN_PASSWORD`, `AFF_NAME`, `AFF_CODE`, `AFF_AGE`, `AFF_TYPE`, `AFF_PHONE`, `CLASS_CODE`, `CLASS_NAME`, `CLASS_LEVEL`, `CLASS_CAPACITY`, `ENR_CODE`, `ENR_AFFILIATE_CODE`, `ENR_CLASS_CODE`, `ENR_ATTENDANCE`, `ENR_STATUS`.
* **Matrices:** `login_users`, `affiliates`, `classes`, `enrollments`.
* **Funciones:**
  * `get_level_name(level_code)`
  * `get_type_name(type_code)`

### 3.2 [`validaciones.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/validaciones.py)
Reúne las validaciones de tipo de dato y expresiones regulares:
* `es_entero(valor)`
* `es_flotante(valor)`
* `es_string(valor)`
* `es_nombre_clase_valido(nombre)`
* `pedir_entero(mensaje, mensaje_error, minimo, maximo)`
* `es_telefono_valido(telefono)`

### 3.3 [`utilidades.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/utilidades.py)
Concentra las funciones auxiliares de búsqueda por código y condición:
* `search_position(rows, condition)`
* `search_class_position(code)`
* `search_affiliate_position(code)`
* `search_user_position(username)`
* `does_class_code_exist(code)`
* `does_affiliate_code_exist(code)`
* `is_affiliate_enrolled_in_class(affiliate_code, class_code)`
* `search_inscription_position(code)`

### 3.4 [`login.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/login.py)
Responsable del acceso inicial al sistema:
* `login()`

### 3.5 [`socios.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/socios.py)
Agrupa las operaciones sobre la entidad socios y la eliminación de inscripciones vinculadas:
* `input_option()`
* `sumar_afiliados()`
* `eliminar_afiliados()`
* `remove_enrollment_at(position)`
* `remove_enrollments_by_affiliate(affiliate_code)`
* `remove_enrollments_by_class(class_code)`
* `modify_affiliate()`
* `list_affiliates()`

### 3.6 [`clases.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/clases.py)
Agrupa las operaciones del catálogo de clases:
* `sumar_clase()`
* `eliminar_clase()`
* `modify_clase()`
* `list_clases()`

### 3.7 [`inscripciones.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/inscripciones.py)
Agrupa las operaciones de registro de inscripciones, control de cupos y asistencias:
* `alta_inscripcion()`
* `list_inscripciones()`
* `clases_de_socio(affiliate_code)`
* `listar_clases_socio()`
* `baja_inscripcion()`
* `modify_inscripcion()`

### 3.8 [`busquedas.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/busquedas.py)
Implementa los algoritmos de búsqueda requeridos por la cátedra:
* `buscar_clase_binaria()`
* `buscar_socio_secuencial()`

### 3.9 [`ordenamientos.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/ordenamientos.py)
Implementa los tres algoritmos clásicos de ordenamiento de listas:
* `ordenar_socios_por_edad()` (Método de Selección)
* `ordenar_clases_por_nivel()` (Método de Inserción)
* `ordenar_inscripciones_por_asistencias()` (Método de Burbujeo)

### 3.10 [`estadisticas.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/estadisticas.py)
Contiene las funciones estadísticas matriciales y el uso de `map` y `reduce`:
* `affiliates_by_class_matrix()`
* `affiliates_by_class()`
* `attendances_by_class_matrix()`
* `total_attendances_by_class()`
* `enrollment_by_class_level_matrix()`
* `affiliates_by_type_and_class_matrix()`

### 3.11 [`menus.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/menus.py)
Maneja las pantallas interactivas de opciones para el usuario:
* `input_clases_option()`, `clases_menu()`
* `input_affiliate_option()`, `affiliate_menu()`
* `input_inscription_option()`, `inscription_menu()`
* `menu_busqueda()`, `opcion_menu_busqueda()`
* `menu_ordenamiento()`, `opcion_menu_ordenamiento()`
* `input_matrix_option()`, `matrix_menu()`
* `input_main_option()`, `main_menu()`

### 3.12 [`main.py`](file:///c:/Users/lucas/OneDrive/Escritorio/UADE/2026/Segundo%20cuatrimestre/1.%20Algoritmos/GymControl/GymControl/main.py)
Punto de entrada general que orquesta la ejecución del programa:
```python
from login import login
from menus import main_menu

if __name__ == "__main__":
    valid_login = login()

    if valid_login:
        main_menu()
        print("¡Gracias por usar el sistema de gestión del gimnasio! Hasta luego.")
```

---

## 4. Instrucciones de Ejecución

### Para ejecutar la versión modularizada:
```bash
python main.py
```

### Para ejecutar la versión monolítica original de la primera entrega:
```bash
python tp.py
```

*Ambas versiones son 100% equivalentes en su funcionamiento y datos precargados:*
* **Usuario:** `admin`
* **Contraseña:** `admin1234`

---

## 5. Ventajas para el Trabajo en Equipo

Con esta estructura de archivos:
1. **Trabajo en paralelo:** Cada integrante puede trabajar sobre un módulo específico en su rama de Git sin generar conflictos de fusión (*merge conflicts*) en un archivo monolítico.
2. **Modificaciones ordenadas:** Cuando vean en clase los temas pendientes (excepciones, JSON, archivos de texto, tuplas, diccionarios, sets y pruebas unitarias), podrán incorporarlos de manera limpia y gradual en los módulos correspondientes.
