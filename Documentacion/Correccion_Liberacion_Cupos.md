# Corrección: liberación de cupos al eliminar un afiliado

**Estado:** IMPLEMENTADO (Pasos 1 a 6). El Paso 7 (prueba unitaria) queda pendiente para la Semana 4.  
**Responsable:** Lucas Cragaris (`dev-lucas`)  
**Semana del plan:** 1 (05/10 – 11/10)  
**Código sobre el que se trabaja:** versión modular de `src/` (se ejecuta con `main.py`). `tp.py` ya no se usa.  
**Origen:** devolución del profesor sobre la primera entrega.

> *"Nota: Al eliminar un afiliado con una clase no se libera el cupo de la clase"*

---

## 1. El problema

[`eliminar_afiliados()`](../src/socios.py#L80-L101) llama a [`remove_enrollments_by_affiliate()`](../src/socios.py#L111-L122), que borra las inscripciones del socio pero **nunca modifica `classes`**. El cupo (`CLASS_CAPACITY`) queda descontado para siempre.

Caso de la devolución del profesor: inscribir al socio 112 en Yoga (el cupo baja en 1) y eliminarlo. Después de eliminarlo, Yoga **sigue con el cupo descontado**.

Los demás flujos ya mantienen bien los cupos:
- `baja_inscripcion()` suma 1 al cupo.
- `modify_inscripcion()` (activa → inactiva) suma 1 al cupo.
- `eliminar_clase()` no necesita devolver nada, porque la clase desaparece.

Solo la baja de socio quedó sin esa lógica.

---

## 2. Regla de negocio

Una inscripción **ocupa un cupo solo mientras está activa** (`ENR_STATUS == 1`). Una inscripción inactiva (`2`) ya devolvió su cupo al darse de baja.

| Inscripción del socio eliminado | ¿Devolver cupo? |
|---|---|
| Activa y la clase existe | **Sí**, `+1` |
| Activa pero la clase ya no existe | No (no hay dónde devolverlo) |
| Inactiva | **No** (se devolvería dos veces) |

---

## 3. Decisiones de diseño (y su relación con la consigna)

| Decisión | Motivo según la consigna |
|---|---|
| Crear una **función nueva** `liberar_cupos_de_afiliado` en lugar de agregar lógica a `remove_enrollments_by_affiliate` | §10: evitar "funciones que realicen demasiadas tareas diferentes". Cada función hace una sola cosa. |
| La función recibe `inscripciones` y `clases` **por parámetro** y devuelve un número | §10: evitar variables globales cuando se resuelve con parámetros y valores de retorno. Además permite probarla con datos propios. |
| No se agrega ningún `try/except` | §6: no usar `try/except` indiscriminadamente. No hay ninguna excepción real que controlar acá. |
| Se reutiliza `search_position` (ya existe en `utilidades.py`) | §10: evitar repetir código. |
| Nombres nuevos en castellano | Corrección de la exposición ("todo en castellano"). |
| Solo se usan `for`, `if`, funciones, `return`, `lambda` | §12: solo contenidos vistos en la materia. |
| La prueba es una **función común**, sin `class` ni `unittest.TestCase` | §12.1: las clases están prohibidas. |

### Lo que NO se toca (a propósito)
- `remove_enrollments_by_affiliate` queda **exactamente igual**.
- `remove_enrollments_by_class`: se usa al eliminar una clase, donde no hay cupo que devolver.
- Los nombres en inglés ya existentes (`affiliates`, `enrollments`, `CLASS_CAPACITY`...): los renombra Tomás en su tarea de normalización.

---

## 4. Paso a paso con líneas afectadas

Las líneas "actuales" son las del código hoy. Las líneas "después" son aproximadas, porque dependen de las inserciones anteriores.

### Paso 1: imports de datos en `socios.py`
**Archivo:** [`src/socios.py`](../src/socios.py#L1-L12), líneas **1–12**. Se agregan 4 líneas.

```diff
 from datos import (
     affiliates,
     enrollments,
+    classes,
     AFF_NAME,
     AFF_CODE,
     AFF_AGE,
     AFF_TYPE,
     AFF_PHONE,
     ENR_AFFILIATE_CODE,
     ENR_CLASS_CODE,
+    ENR_STATUS,
+    CLASS_CODE,
+    CLASS_CAPACITY,
     get_type_name
 )
```

### Paso 2: import de la búsqueda genérica
**Archivo:** [`src/socios.py`](../src/socios.py#L18), línea **18**. Se modifica 1 línea; la cantidad de líneas no cambia.

```diff
-from utilidades import search_affiliate_position
+from utilidades import search_affiliate_position, search_position
```

`search_position` está en [`utilidades.py`](../src/utilidades.py#L16-L25) y `utilidades.py` solo importa `datos`, así que no hay import circular.

### Paso 3: crear la función nueva
**Archivo:** [`src/socios.py`](../src/socios.py#L122), se inserta **después de la línea 122** (`return deleted_count` de `remove_enrollments_by_affiliate`) y antes de `remove_enrollments_by_class` (línea 124). Son unas 15 líneas nuevas, que quedan aproximadamente en las líneas 131–145.

```python
def liberar_cupos_de_afiliado(codigo_afiliado, inscripciones, clases):
    """
    Objetivo: devolver un cupo a cada clase en la que el socio tiene una inscripción activa.
    Parámetros: codigo_afiliado, código del socio; inscripciones, matriz de inscripciones; clases, matriz de clases.
    Salida: cantidad de cupos liberados.
    """
    cupos_liberados = 0
    for inscripcion in inscripciones:
        if inscripcion[ENR_AFFILIATE_CODE] == codigo_afiliado and inscripcion[ENR_STATUS] == 1:
            codigo_clase = inscripcion[ENR_CLASS_CODE]
            posicion_clase = search_position(clases, lambda fila: fila[CLASS_CODE] == codigo_clase)
            if posicion_clase != -1:
                clases[posicion_clase][CLASS_CAPACITY] += 1
                cupos_liberados += 1
    return cupos_liberados
```

### Paso 4: llamar a la función dentro de `eliminar_afiliados`
**Archivo:** [`src/socios.py`](../src/socios.py#L94-L99), líneas **94–99**. Se agrega 1 línea **antes** de la línea 95. El orden es obligatorio: si se llama después, las inscripciones ya fueron borradas y no queda nada que leer.

```diff
         if confirm.lower() == "s":
+            cupos_liberados = liberar_cupos_de_afiliado(codigo, enrollments, classes)
             inscripciones_eliminadas = remove_enrollments_by_affiliate(codigo)
             affiliates.pop(pos)
             print("Socio eliminado.")
             if inscripciones_eliminadas > 0:
                 print(f"Se eliminaron {inscripciones_eliminadas} inscripciones asociadas.")
+            if cupos_liberados > 0:
+                print(f"Se liberaron {cupos_liberados} cupos en las clases correspondientes.")
         else:
```

### Paso 5: docstring de `eliminar_afiliados`
**Archivo:** [`src/socios.py`](../src/socios.py#L81-L85), líneas **82 y 84**. Se modifican 2 líneas de texto.

```diff
-    Objetivo: eliminar un socio y sus inscripciones asociadas luego de solicitar confirmación.
+    Objetivo: eliminar un socio y sus inscripciones asociadas, liberando el cupo de las clases con inscripción activa, luego de solicitar confirmación.
 ...
-    Salida: no devuelve valores; actualiza las matrices de afiliados e inscripciones.
+    Salida: no devuelve valores; actualiza las matrices de afiliados, inscripciones y clases.
```

### Paso 6: coherencia de los cupos iniciales
**Archivo:** [`src/datos.py`](../src/datos.py#L36-L47), líneas **37, 40 y 41**. Se modifica 1 número por línea.

Las inscripciones activas precargadas no descuentan cupo. Con el arreglo, eliminar un socio precargado dejaría su clase por encima de la capacidad inicial. Cuántas inscripciones activas hay hoy:

| Clase | Inscripciones activas precargadas | Línea | Cambio |
|---|---|---|---|
| 201 Yoga | 3 (304, 305, 311) | 37 | `15` → `12` |
| 204 Pilates | 2 (302, 310) | 40 | `15` → `13` |
| 205 Musculacion | 2 (301, 309) | 41 | `10` → `8` |

```diff
-    [201, "Yoga", 1, 15],
+    [201, "Yoga", 1, 12],
 ...
-    [204, "Pilates", 1, 15],
-    [205, "Musculacion", 2, 10],
+    [204, "Pilates", 1, 13],
+    [205, "Musculacion", 2, 8],
```

La clase 203 (Boxeo) no cambia: sus 3 inscripciones precargadas están inactivas.

> Este paso es independiente de los anteriores y va en un commit aparte. Si el equipo prefiere no tocar los datos iniciales, se omite y la corrección funciona igual.

### Paso 7: prueba unitaria
**Archivo nuevo:** `src/test_gymcontrol.py` (unas 70 líneas). Se ejecuta aparte con `python src/test_gymcontrol.py`.

Es una función por prueba (sin `class`), con una función auxiliar que imprime los 5 datos que pide la consigna (§9): función probada, datos utilizados, resultado esperado, resultado obtenido y aprobada o no. Usa listas propias de cada prueba, así que no depende del estado del programa. La estructura es:

```python
from socios import liberar_cupos_de_afiliado

def mostrar_resultado(numero, tipo, funcion, datos, esperado, obtenido):
    ...  # imprime función, datos, esperado, obtenido y APROBADA / RECHAZADA; devuelve True o False

def prueba_caso_profesor(): ...
def prueba_dos_activas_una_inactiva(): ...
def prueba_socio_sin_inscripciones(): ...
def prueba_clase_inexistente(): ...

def ejecutar_pruebas(): ...  # corre todas y muestra el resumen

if __name__ == "__main__":
    ejecutar_pruebas()
```

| N.º | Tipo (§9) | Datos | Esperado |
|---|---|---|---|
| 1 | **Caso relevante del sistema** | Socio 112 con 1 inscripción activa en clase 201 con cupo 14 | Devuelve `1`; cupo de 201 = `15` |
| 2 | Válido | Socio 101 con 2 activas (clases 201 y 202) y 1 inactiva (clase 203) | Devuelve `2`; cupos de 201 y 202 `+1`; cupo de 203 sin cambios |
| 3 | Límite | Socio sin ninguna inscripción | Devuelve `0`; cupos sin cambios |
| 4 | Inválido | Inscripción activa de una clase inexistente (código 999) | Devuelve `0`; no falla |

Estas 4 pruebas cubren **una** de las funciones. Quedan por escribir (Semana 4) 6 pruebas más sobre al menos 4 funciones distintas, para llegar a las 10 de la consigna: 3 válidas, 2 inválidas y 1 límite.

---

## 5. Verificación

### Automática
1. `python src/test_gymcontrol.py`: las 4 pruebas deben salir **APROBADAS**.
2. Importar todos los módulos de `src/` y `main.py` sin errores.

### Manual (menú real: `python main.py`, usuario `admin` / `admin1234`)
Los valores suponen aplicado el Paso 6. Sin el Paso 6, Yoga muestra 14 y vuelve a 15.

1. Gestión de inscripciones → Alta → clase `201`, socio `112`.
2. Gestión de clases → Listar → Yoga muestra `11`.
3. Gestión de afiliados → Eliminar → `112` → confirmar `s`. Debe mostrar "Se liberaron 1 cupos en las clases correspondientes."
4. Gestión de clases → Listar → Yoga vuelve a `12`.
5. Eliminar un socio precargado con inscripción activa, por ejemplo el `101` (Musculación): Musculación pasa de `8` a `9`.

---

## 6. Resumen de impacto

| Archivo | Líneas actuales afectadas | Tipo de cambio |
|---|---|---|
| [`src/socios.py`](../src/socios.py) | 1–12, 18, 82, 84, antes de 95, después de 99, después de 122 | Imports, docstring, 1 llamada, 1 mensaje, 1 función nueva |
| [`src/datos.py`](../src/datos.py) | 37, 40, 41 | 3 valores iniciales |
| `src/test_gymcontrol.py` | archivo nuevo | 4 pruebas |

- **Funciones modificadas:** 1 (`eliminar_afiliados`). **Funciones nuevas:** 1 (`liberar_cupos_de_afiliado`).
- **Funciones que quedan intactas:** `remove_enrollments_by_affiliate`, `remove_enrollments_by_class`, `remove_enrollment_at`.
- **Riesgo:** bajo; los cambios son acotados.
- **Commits sugeridos (rama `dev-lucas`):**
  1. Corrección de cupos (Pasos 1 a 5).
  2. Coherencia de cupos iniciales (Paso 6).
  3. Prueba unitaria (Paso 7).
- **Conflicto con Tomás:** él renombra estas mismas funciones y constantes en la Semana 1. Conviene mergear esta corrección antes, o resolver los renombres en el merge.
- **Para el documento de entrega (§15):** esta corrección va en "Descripción de las mejoras" y "Cambios respecto de la Parte 1", y la prueba en "Pruebas unitarias".
