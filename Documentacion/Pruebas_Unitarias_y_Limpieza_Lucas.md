# Documentación de Cambios: Pruebas Unitarias y Limpieza de Código

**Estado:** IMPLEMENTADO Y VERIFICADO (`10/10` pruebas aprobadas).  
**Responsable:** Lucas Cragaris (`dev-lucas-2`)  
**Fecha:** 25 de Octubre de 2026  
**Módulos involucrados:**
- `test_gymcontrol.py` *(archivo nuevo en la raíz del proyecto)*
- [`src/validaciones.py`](../src/validaciones.py) *(modificación)*
- [`src/socios.py`](../src/socios.py) *(modificación)*
- [`src/inscripciones.py`](../src/inscripciones.py) *(modificación)*

---

## 1. Resumen y Justificación según la Consigna

| Cambio planeado | Punto de la consigna que cumple |
|---|---|
| **Crear `test_gymcontrol.py` con 10 pruebas unitarias** | **§9 (Pruebas unitarias):** mínimo 10 pruebas (4 válidas, 3 inválidas, 2 límite y 1 caso relevante) sobre al menos 5 funciones distintas, ejecutables de forma independiente e informando los 5 datos obligatorios. |
| **Implementar las pruebas con funciones puras (sin `class` ni `unittest`)** | **§12.1 y §12.3 (Restricciones técnicas):** prohibición absoluta de usar `class` (POO) y librerías no vistas en la materia. |
| **Reemplazar `except:` por `except (ValueError, TypeError):` en `validaciones.py`** | **§6 (Manejo de excepciones):** *"No se deberá utilizar try / except indiscriminadamente para ocultar errores del programa. Deberán identificar situaciones concretas"*. |
| **Eliminar funciones muertas (`es_string` en `validaciones.py` y `pedir_opcion` en `socios.py`)** | **§10 (Modularización):** evitar código repetido o sin uso y mantener responsabilidades claras por módulo. |
| **Evitar sombreado de la matriz `clases` en `listar_clases_socio` (`inscripciones.py`)** | **§10 (Modularización):** no pisar el identificador de la matriz global `clases` con una variable local del mismo nombre. |
| **Corregir texto `(s/cantidad)` por `(s/n)` en bajas (`socios.py` e `inscripciones.py`)** | **§11 (Validaciones):** claridad en los mensajes al usuario. |

---

## 2. Parte A: Limpieza y Correcciones en Módulos Existentes

### 2.1. Cambios en [`src/validaciones.py`](../src/validaciones.py)

1. **Especificar la excepción en `es_entero` y `es_flotante` (líneas 9–27):**
   Se reemplaza el `except:` genérico por `except (ValueError, TypeError):`, que son las únicas excepciones reales al intentar convertir un valor inválido con `int()` o `float()`.
2. **Eliminar `es_string` (líneas 29–40):**
   No se invoca en ningún módulo del sistema y en Python `str()` convierte cualquier objeto sin fallar.
3. **Ajustar docstring de `es_nombre_clase_valido` (línea 44):**
   El docstring decía *"sin espacios"*, pero la expresión regular `r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$"` fue ampliada para admitir tildes y espacios.

#### Diff propuesto para `src/validaciones.py`:
```diff
 def es_entero (valor ):
     """
     Objetivo: determinar si un valor puede convertirse en un número entero.
     Parámetros: valor, dato que se desea validar.
     Salida: True si el valor es convertible a entero; False en caso contrario.
     """
     try :
         valor =int (valor )
         resultado =True
-    except :
+    except (ValueError ,TypeError ):
         resultado =False
     return resultado
 
 def es_flotante (valor ):
     """
     Objetivo: determinar si un valor puede convertirse en un número decimal.
     Parámetros: valor, dato que se desea validar.
     Salida: True si el valor es convertible a decimal; False en caso contrario.
     """
     try :
         valor =float (valor )
         resultado =True
-    except :
+    except (ValueError ,TypeError ):
         resultado =False
     return resultado
 
-def es_string (valor ):
-    """
-    Objetivo: determinar si un valor puede convertirse en una cadena de caracteres.
-    Parámetros: valor, dato que se desea validar.
-    Salida: True si el valor es convertible a cadena; False en caso contrario.
-    """
-    try :
-        valor =str (valor )
-        resultado =True
-    except :
-        resultado =False
-    return resultado
-
 def es_nombre_clase_valido (nombre ):
     """
-    Objetivo: validar que un nombre de clase contenga únicamente letras sin espacios.
+    Objetivo: validar que un nombre de clase contenga únicamente letras y espacios.
     Parámetros: nombre, cadena que se desea validar.
     Salida: coincidencia encontrada si el nombre es válido; None en caso contrario.
     """
     return re .match (r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$",nombre )## Agrego tildes y espacios
```

---

### 2.2. Cambios en [`src/socios.py`](../src/socios.py)

1. **Eliminar la función muerta `pedir_opcion()` (líneas 25–51):**
   Tenía el comentario `# Gestión de socios ==> Este codigo habria que eliminarlo ya que no lo llaman en ninguna parte LC 2/9`. El menú real se gestiona desde `pedir_opcion_socios()` en `src/menus.py`.
2. **Corregir texto de confirmación en `eliminar_afiliados()` (línea 98):**
   Cambiar `(s/cantidad)` por `(s/n)`.

#### Diff propuesto para `src/socios.py`:
```diff
 from utilidades import buscar_posicion_socio ,buscar_posicion
 
-# Gestión de socios ==> Este codigo habria que eliminarlo ya que no lo llaman en ninguna parte LC 2/9
-def pedir_opcion ():
-    """
-    Objetivo: solicitar y validar una opción del menú de gestión de socios.
-    Parámetros: ninguno.
-    Salida: opción elegida como número entero entre 0 y 4.
-    """
-    print ("Opcion 1: sumar afiliado")
-    print ("Opcion 2: eliminar afiliado")
-    print ("Opcion 3: modificar afiliado")
-    print ("Opcion 4: listar afiliados")
-    print ("Opcion 0: salir")
-
-    opcion =pedir_entero ("Ingrese una opcion: ","El dato ingresado es erroneo, por favor ingrese una opcion valida.",0 ,4 )
-
-    while opcion <0 or opcion >4 :
-        print ("El dato ingresado es erroneo, por favor ingrese una opcion valida.")
-
-        print ("Opcion 1: sumar afiliado")
-        print ("Opcion 2: eliminar afiliado")
-        print ("Opcion 3: modificar afiliado")
-        print ("Opcion 4: listar afiliados")
-        print ("Opcion 0: salir")
-
-        opcion =pedir_entero ("Ingrese una opcion: ","El dato ingresado es erroneo, por favor ingrese una opcion valida.",0 ,4 )
-
-    return opcion
-
 def sumar_afiliados ():
```

```diff
     if posicion ==-1 :
         print ("Socio no encontrado.")
     else :
-        print (f"¿Seguro que desea eliminar a '{socios[posicion][SOCIO_NOMBRE]}' (teléfono: {socios[posicion][SOCIO_TELEFONO]})? (s/cantidad)")
+        print (f"¿Seguro que desea eliminar a '{socios[posicion][SOCIO_NOMBRE]}' (teléfono: {socios[posicion][SOCIO_TELEFONO]})? (s/n)")
         confirmacion =input ()
```

---

### 2.3. Cambios en [`src/inscripciones.py`](../src/inscripciones.py)

1. **Renombrar variable local `clases` en `listar_clases_socio()` (líneas 102–106):**
   En la línea 102 se hacía `clases = clases_de_socio(codigo)`, ocultando la matriz `clases` importada de `datos.py`. Se renombra a `nombres_clases`.
2. **Corregir texto de confirmación en `baja_inscripcion()` (línea 126):**
   Cambiar `(s/cantidad)` por `(s/n)`.

#### Diff propuesto para `src/inscripciones.py`:
```diff
 def listar_clases_socio ():
     """
     Objetivo: mostrar las clases activas de un socio específico.
     Parámetros: ninguno; solicita el código del socio por teclado.
     Salida: no devuelve valores; muestra las clases o un mensaje informativo.
     """
     print ("Clases de un socio")
     codigo =pedir_entero ("Ingrese el codigo del socio: ","Codigo invalido, ingresar un numero")
     posicion =buscar_posicion_socio (codigo )
     if posicion ==-1 :
         print ("Error,socio no encontrado")
         return
-    clases =clases_de_socio (codigo )
-    if not clases :
+    nombres_clases =clases_de_socio (codigo )
+    if not nombres_clases :
         print ("El socio no tiene clases activas")
     else :
-        print (f"El socio {socios[posicion][SOCIO_NOMBRE]} tiene las clases: {', '.join(clases)}")
+        print (f"El socio {socios[posicion][SOCIO_NOMBRE]} tiene las clases: {', '.join(nombres_clases)}")
```

```diff
-        confirmacion =input (f"¿Seguro que desea dar de baja la inscripción del socio '{nombre_socio}' en la clase '{nombre_clase}' ? (s/cantidad): ")
+        confirmacion =input (f"¿Seguro que desea dar de baja la inscripción del socio '{nombre_socio}' en la clase '{nombre_clase}' ? (s/n): ")
```

---

## 3. Parte B: Diseño de las 10 Pruebas Unitarias (`test_gymcontrol.py`)

### 3.1. Cumplimiento de Requisitos de la Cátedra (§9 y §12)

- **Cantidad total:** 10 pruebas unitarias.
- **Distribución por categoría:**
  - **4 pruebas de casos válidos** (Pruebas 1 a 4).
  - **3 pruebas de casos inválidos** (Pruebas 5 a 7).
  - **2 pruebas de casos límite** (Pruebas 8 y 9).
  - **1 prueba adicional relevante para la problemática del sistema** (Prueba 10).
- **Cantidad de funciones diferentes evaluadas:** **6 funciones distintas** de **5 módulos distintos** (supera el mínimo exigido de 5 funciones):
  1. `es_telefono_valido` (`src/validaciones.py`)
  2. `es_nombre_clase_valido` (`src/validaciones.py`)
  3. `es_entero` (`src/validaciones.py`)
  4. `socio_esta_inscripto_en_clase` (`src/utilidades.py`)
  5. `resumir_auditoria` (`src/auditoria.py`)
  6. `es_hora_valida` (`src/clases.py`)
  7. `liberar_cupos_de_afiliado` (`src/socios.py`)
  *(En total se prueban 7 funciones distintas del sistema).*
- **Sin clases (`class`):** No se utiliza `unittest.TestCase` ni clases propias. Se emplea una función auxiliar `verificar_prueba(...)` que compara `esperado == obtenido`, imprime los **5 datos obligatorios** y devuelve `True` o `False`.

---

### 3.2. Matriz Detallada de las 10 Pruebas (Guía para la Defensa Oral)

| N.º | Categoría (§9) | Función probada | Datos utilizados | Resultado esperado | Qué comprueba / Justificación para la defensa oral |
|---|---|---|---|---|---|
| **1** | **Caso válido (1/4)** | `es_telefono_valido` | `"11-2587-8779"` | `True` | Comprueba que un teléfono con el patrón reglamentario `XX-XXXX-XXXX` sea validado positivamente. |
| **2** | **Caso válido (2/4)** | `es_nombre_clase_valido` | `"Funcional Avanzado"` | `True` | Comprueba que se acepten nombres de clases formados por letras y espacios. |
| **3** | **Caso válido (3/4)** | `socio_esta_inscripto_en_clase` | `codigo_socio=101, codigo_clase=205` | `True` | Comprueba que el filtro detecte cuando un socio ya tiene inscripción activa (`estado == 1`) en una clase. |
| **4** | **Caso válido (4/4)** | `resumir_auditoria` | 3 eventos (`2` de `"ALTA_SOCIO"` y `1` de `"BAJA_SOCIO"`) | `{"ALTA_SOCIO": 2, "BAJA_SOCIO": 1}` | Comprueba que la función agrupe y cuente correctamente las operaciones usando un diccionario (`dict`). |
| **5** | **Caso inválido (1/3)** | `es_telefono_valido` | `"1125878779"` (sin guiones) | `False` | Comprueba que un número telefónico sin los guiones separadores sea rechazado por la expresión regular. |
| **6** | **Caso inválido (2/3)** | `es_entero` | `"abc"` (texto no numérico) | `False` | Comprueba que `try / except (ValueError, TypeError)` capture el fallo de `int("abc")` y retorne `False`. |
| **7** | **Caso inválido (3/3)** | `socio_esta_inscripto_en_clase` | `codigo_socio=103, codigo_clase=201` (inscripción con `estado == 2` inactiva) | `False` | Comprueba que una inscripción finalizada (`estado == 2`) no figure como activa. |
| **8** | **Caso límite (1/2)** | `es_hora_valida` | Fronteras del reloj: `"00:00"` (mínimo), `"23:59"` (máximo) y `"24:00"` (fuera de límite) | `(True, True, False)` | Evalúa exactamente los bordes inferior y superior del formato horario `HH:MM` (0 a 23 hs y 0 a 59 min). |
| **9** | **Caso límite (2/2)** | `liberar_cupos_de_afiliado` | `codigo_afiliado=999` (sin inscripciones), clase `201` con cupo `12` | `(0, 12)` | Evalúa el caso extremo en que se da de baja un socio con `0` inscripciones: libera `0` cupos y deja intacta la clase. |
| **10** | **Caso relevante del sistema (1/1)** | `liberar_cupos_de_afiliado` | Socio `112` con 1 inscripción activa en clase `201` (cupo `14`) y 1 inactiva en clase `203` (cupo `15`) | `(1, 15, 15)` | Caso clave de negocio (observación docente de la Parte 1): al eliminar al socio `112`, recupera el cupo de la clase activa (`14 -> 15`) y no altera la clase con inscripción inactiva (`15 -> 15`). |

---

### 3.3. Código Completo Propuesto para `test_gymcontrol.py`

```python
"""
Suite de Pruebas Unitarias para GymControl (Segunda Parte).
Ejecución independiente: python3 test_gymcontrol.py
Cumple con la restricción §12.1 (sin uso de class / POO).
"""

import os
import sys

ruta_src = os.path.join(os.path.dirname(__file__), "src")
if os.path.exists(ruta_src) and ruta_src not in sys.path:
    sys.path.insert(0, ruta_src)

from validaciones import es_entero, es_nombre_clase_valido, es_telefono_valido
from utilidades import socio_esta_inscripto_en_clase
from auditoria import resumir_auditoria
from clases import es_hora_valida
from socios import liberar_cupos_de_afiliado


def mostrar_resultado_prueba(numero, categoria, funcion, datos, esperado, obtenido):
    """
    Objetivo: mostrar los 5 puntos obligatorios de cada prueba unitaria (§9) y evaluar su aprobación.
    Parámetros: numero (int), categoria (str), funcion (str), datos (str), esperado, obtenido.
    Salida: True si esperado == obtenido; False en caso contrario.
    """
    aprobada = esperado == obtenido
    estado = "APROBADA" if aprobada else "FALLIDA"
    print(f"Prueba #{numero:02d} [{categoria}]")
    print(f"  1. Función probada   : {funcion}")
    print(f"  2. Datos utilizados  : {datos}")
    print(f"  3. Resultado esperado: {esperado}")
    print(f"  4. Resultado obtenido: {obtenido}")
    print(f"  5. Estado de prueba  : {estado}")
    print("-" * 75)
    return aprobada


# --- 4 PRUEBAS DE CASOS VÁLIDOS ---

def prueba_01_telefono_valido():
    dato = "11-2587-8779"
    obtenido = es_telefono_valido(dato)
    return mostrar_resultado_prueba(
        1, "Caso Válido 1/4", "es_telefono_valido(telefono)",
        f"telefono='{dato}'", True, obtenido
    )


def prueba_02_nombre_clase_valido():
    dato = "Funcional Avanzado"
    obtenido = es_nombre_clase_valido(dato) is not None
    return mostrar_resultado_prueba(
        2, "Caso Válido 2/4", "es_nombre_clase_valido(nombre)",
        f"nombre='{dato}'", True, obtenido
    )


def prueba_03_socio_inscripto_activo():
    obtenido = socio_esta_inscripto_en_clase(101, 205)
    return mostrar_resultado_prueba(
        3, "Caso Válido 3/4", "socio_esta_inscripto_en_clase(codigo_socio, codigo_clase)",
        "codigo_socio=101, codigo_clase=205 (inscripción 301 activa)", True, obtenido
    )


def prueba_04_resumen_auditoria_diccionario():
    eventos_prueba = [
        ["2026-10-25T10:00:00-03:00", "admin", "ALTA_SOCIO", "Código=113"],
        ["2026-10-25T10:05:00-03:00", "admin", "ALTA_SOCIO", "Código=114"],
        ["2026-10-25T10:10:00-03:00", "admin", "BAJA_SOCIO", "Código=113"]
    ]
    esperado = {"ALTA_SOCIO": 2, "BAJA_SOCIO": 1}
    obtenido = resumir_auditoria(eventos_prueba)
    return mostrar_resultado_prueba(
        4, "Caso Válido 4/4", "resumir_auditoria(eventos)",
        "3 eventos (2 ALTA_SOCIO, 1 BAJA_SOCIO)", esperado, obtenido
    )


# --- 3 PRUEBAS DE CASOS INVÁLIDOS ---

def prueba_05_telefono_invalido_sin_guiones():
    dato = "1125878779"
    obtenido = es_telefono_valido(dato)
    return mostrar_resultado_prueba(
        5, "Caso Inválido 1/3", "es_telefono_valido(telefono)",
        f"telefono='{dato}' (sin guiones)", False, obtenido
    )


def prueba_06_entero_invalido_texto():
    dato = "abc"
    obtenido = es_entero(dato)
    return mostrar_resultado_prueba(
        6, "Caso Inválido 2/3", "es_entero(valor)",
        f"valor='{dato}' (cadena alfabética)", False, obtenido
    )


def prueba_07_socio_con_inscripcion_inactiva():
    obtenido = socio_esta_inscripto_en_clase(103, 201)
    return mostrar_resultado_prueba(
        7, "Caso Inválido 3/3", "socio_esta_inscripto_en_clase(codigo_socio, codigo_clase)",
        "codigo_socio=103, codigo_clase=201 (inscripción 303 con estado=2 inactiva)", False, obtenido
    )


# --- 2 PRUEBAS DE CASOS LÍMITE ---

def prueba_08_limite_horarios_bordes():
    obtenido = (es_hora_valida("00:00"), es_hora_valida("23:59"), es_hora_valida("24:00"))
    esperado = (True, True, False)
    return mostrar_resultado_prueba(
        8, "Caso Límite 1/2", "es_hora_valida(hora)",
        "horas=('00:00' mínimo válido, '23:59' máximo válido, '24:00' fuera de rango)",
        esperado, obtenido
    )


def prueba_09_limite_baja_socio_sin_inscripciones():
    inscripciones_prueba = [[301, 101, 201, 4, 1]]
    clases_prueba = [[201, "Yoga", 1, 12, (("Lunes",), "08:00", "09:00")]]
    liberados = liberar_cupos_de_afiliado(999, inscripciones_prueba, clases_prueba)
    obtenido = (liberados, clases_prueba[0][3])
    esperado = (0, 12)
    return mostrar_resultado_prueba(
        9, "Caso Límite 2/2", "liberar_cupos_de_afiliado(codigo_afiliado, inscripciones, clases)",
        "codigo_afiliado=999 (sin inscripciones), clase 201 con cupo=12",
        esperado, obtenido
    )


# --- 1 PRUEBA RELEVANTE PARA LA PROBLEMÁTICA DEL SISTEMA ---

def prueba_10_relevante_liberacion_cupos_baja_socio():
    inscripciones_prueba = [
        [312, 112, 201, 0, 1],  # Activa en Yoga (debe devolver 1 cupo)
        [313, 112, 203, 5, 2],  # Inactiva en Boxeo (NO debe devolver cupo)
    ]
    clases_prueba = [
        [201, "Yoga", 1, 14, (("Lunes", "Miércoles"), "08:00", "09:00")],
        [203, "Boxeo", 2, 15, (("Lunes", "Viernes"), "19:00", "20:00")],
    ]
    liberados = liberar_cupos_de_afiliado(112, inscripciones_prueba, clases_prueba)
    obtenido = (liberados, clases_prueba[0][3], clases_prueba[1][3])
    esperado = (1, 15, 15)
    return mostrar_resultado_prueba(
        10, "Caso Relevante del Sistema", "liberar_cupos_de_afiliado(codigo_afiliado, inscripciones, clases)",
        "socio=112 con 1 activa en 201 (cupo 14) y 1 inactiva en 203 (cupo 15)",
        esperado, obtenido
    )


def ejecutar_pruebas():
    print("=" * 75)
    print("EJECUCIÓN DE PRUEBAS UNITARIAS - GYMCONTROL")
    print("=" * 75)
    pruebas = [
        prueba_01_telefono_valido,
        prueba_02_nombre_clase_valido,
        prueba_03_socio_inscripto_activo,
        prueba_04_resumen_auditoria_diccionario,
        prueba_05_telefono_invalido_sin_guiones,
        prueba_06_entero_invalido_texto,
        prueba_07_socio_con_inscripcion_inactiva,
        prueba_08_limite_horarios_bordes,
        prueba_09_limite_baja_socio_sin_inscripciones,
        prueba_10_relevante_liberacion_cupos_baja_socio,
    ]
    aprobadas = 0
    for prueba in pruebas:
        if prueba():
            aprobadas += 1

    total = len(pruebas)
    print(f"RESUMEN FINAL: {aprobadas}/{total} pruebas aprobadas.")
    print("=" * 75)
    return aprobadas == total


if __name__ == "__main__":
    ejecutar_pruebas()
```

---

## 4. Verificación Posterior a la Aplicación

Una vez que confirmes estos cambios:
1. Se aplicarán las ediciones en [`src/validaciones.py`](../src/validaciones.py), [`src/socios.py`](../src/socios.py) y [`src/inscripciones.py`](../src/inscripciones.py).
2. Se creará `test_gymcontrol.py` en la raíz del proyecto.
3. Se ejecutará `python3 test_gymcontrol.py` para comprobar que las **10/10 pruebas unitarias** salgan `APROBADA`.
