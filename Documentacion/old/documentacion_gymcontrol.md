# Documentación de GymControl (`tp.py`)

## 1. ¿Qué es este programa?

Es un sistema de gestión de gimnasio por consola (sin base de datos, sin clases/POO).
Todo se guarda en **listas paralelas**: en vez de tener un objeto `Afiliado` con sus atributos,
hay varias listas separadas donde la posición `i` de cada lista corresponde al mismo afiliado.

Ejemplo: el afiliado en la posición 2 de `affiliate_names` tiene su edad en `affiliate_ages[2]`
y su tipo en `affiliate_types[2]`. Esto se repite para clases e inscripciones. Es clave entender
esto antes de leer las funciones, porque casi todo el código consiste en recorrer estas listas
con el mismo índice.

### Datos (líneas 1–32)

| Entidad | Listas paralelas | Significado |
|---|---|---|
| Login | `login_usernames`, `login_passwords` | Usuarios válidos del sistema |
| Afiliados | `affiliate_names`, `affiliate_codes`, `affiliate_ages`, `affiliate_types` | `affiliate_types`: 1=Mensual, 2=Libre, 3=Premium |
| Clases | `gym_class_codes`, `gym_class_names`, `gym_class_levels`, `gym_class_capacities` | `gym_class_levels`: 1=Principiante, 2=Intermedio, 3=Avanzado. `capacities` = cupos disponibles |
| Inscripciones | `enrollment_codes`, `enrollment_affiliate_codes`, `enrollment_gym_class_codes`, `enrollment_attendances`, `enrollment_status` | `status`: 1=Activa, 2=Inactiva |

Una inscripción conecta un afiliado con una clase (relación muchos a muchos, modelada como una
"tabla intermedia" con listas paralelas).

---

## 2. Funciones auxiliares de validación (líneas 246–279)

Estas se usan en TODOS lados para validar lo que el usuario tipea.

- **`es_entero(valor)`**: intenta hacer `int(valor)`. Si no tira excepción, es un entero válido → `True`, sino `False`. Es la base de casi toda la validación de inputs numéricos.
- **`es_flotante(valor)`**: igual que la anterior pero con `float()`. (Está definida pero en la práctica no se usa mucho en el flujo principal, ya que todo el sistema trabaja con enteros).
- **`es_string(valor)`**: siempre devuelve `True` en la práctica (todo puede convertirse a `str`), no aporta validación real.
- **`pedir_entero(mensaje, mensaje_error, minimo, maximo)`**: pide un input por teclado y repite el pedido hasta que sea un entero válido (opcionalmente dentro de un rango `minimo`–`maximo`). Es un "wrapper" reutilizable para no repetir el `while not es_entero(...)` en cada función. Devuelve el valor ya convertido a `int`.

---

## 3. Funciones de búsqueda de posición (helpers internos)

No hay que confundirlas con las del punto 6 (que son la funcionalidad "Búsqueda" del menú).
Estas son **utilidades internas** para encontrar el índice de un elemento dentro de las listas
paralelas, dado su código.

- **`search_affiliate_position(code)`** (línea 415): recorre `affiliate_codes` y devuelve la posición donde coincide el código, o `-1` si no existe.
- **`search_class_position(code)`** (línea 294): igual, pero sobre `gym_class_codes`.
- **`search_inscription_position(code)`** (línea 728): igual, pero sobre `enrollment_codes`.
- **`search_user_position(username)`** (línea 302): igual, pero busca un nombre de usuario en `login_usernames` (para el login).
- **`does_class_code_exist(code)`** / **`does_affiliate_code_exist(code)`** (líneas 569, 575): versión booleana simple (recorren la lista y devuelven `True`/`False`), usadas al dar de alta una inscripción para validar que el código ingresado exista.

Todas estas funciones son **búsqueda secuencial lineal** (`for` recorriendo toda la lista):
son O(n), y se usan como "motor interno" en casi todas las operaciones CRUD.

- **`get_type_name(type_code)`** (línea 404) y **`get_level_name(level_code)`** (línea 282): traducen los códigos numéricos (1/2/3) a su nombre legible ("Mensual", "Principiante", etc.), para mostrar por pantalla.

---

## 4. Login (líneas 302–330)

- **`login()`**: pide usuario y contraseña hasta 3 intentos (`max_attempts = 3`). Usa `search_user_position` para ubicar el usuario y compara la contraseña en `login_passwords[user_position]`. Si se agotan los intentos sin éxito, devuelve `False` (acceso bloqueado); si acierta, imprime bienvenida y devuelve `True`. Este valor de retorno es el que decide, al final del archivo, si se ejecuta `main_menu()`.

---

## 5. Gestión de Afiliados (CRUD)

- **`sumar_afiliados()`** (línea 356): pide nombre, edad (0–100) y tipo (1–3), valida cada dato con bucles `while not es_entero(...)`. Genera el código automáticamente como `último código + 1` (o `101` si la lista está vacía) y hace `.append()` en las 4 listas paralelas a la vez, manteniendo la sincronización de índices.
- **`eliminar_afiliados()`** (línea 382): pide el código, busca la posición con `search_affiliate_position`, pide confirmación (`s/n`) y, si confirma, llama a **`remove_enrollments_by_affiliate(codigo)`** (borra en cascada todas las inscripciones de ese socio) y luego hace `.pop(pos)` en las 4 listas de afiliados.
- **`modify_affiliate()`** (línea 449): busca por código y permite modificar nombre, edad y tipo uno por uno. El patrón es: "si escribís `si`, se mantiene el valor actual; si no, se valida el nuevo valor". Este patrón de "si = mantener" se repite en todas las funciones `modify_*`.
- **`list_affiliates()`** (línea 476): recorre las listas e imprime cada afiliado con `get_type_name` para mostrar el tipo en texto.

### Borrado en cascada de inscripciones
- **`remove_enrollment_at(position)`** (línea 423): hace `.pop(position)` en las 5 listas de inscripción a la vez (función interna de bajo nivel).
- **`remove_enrollments_by_affiliate(affiliate_code)`** (línea 431) y **`remove_enrollments_by_class(class_code)`** (línea 440): recorren `enrollment_codes` **de atrás para adelante** (`range(len(...)-1, -1, -1)`) — esto es importante: al hacer `.pop()` mientras se recorre una lista, si fueras de adelante hacia atrás te "comerías" elementos (los índices se corren). Yendo de atrás para adelante se evita ese bug clásico. Devuelven cuántas inscripciones se borraron, dato que después se muestra al usuario.

---

## 6. Gestión de Clases (CRUD)

- **`sumar_clase()`** (línea 482): pide nombre, nivel (1–3) y capacidad (>0), genera código automático (`201 + n` o siguiente al último) y hace `.append()` en las 4 listas de clases.
- **`eliminar_clase()`** (línea 508): busca por código, pide confirmación, borra en cascada las inscripciones asociadas con `remove_enrollments_by_class` y luego `.pop()` en las 4 listas de clases.
- **`modify_clase()`** (línea 533): mismo patrón "si = mantener" que `modify_affiliate`, pero sobre nombre/nivel/capacidad.
- **`list_clases()`** (línea 562): imprime una tabla con formato alineado (usa `:<10`, `:<20`, etc. para el ancho de columnas) mostrando código, nombre, nivel (con `get_level_name`) y cupos.

---

## 7. Gestión de Inscripciones (CRUD)

- **`alta_inscripcion()`** (línea 582): primero lista las clases y pide un código de clase válido (con `does_class_code_exist`), chequea que tenga cupos (`gym_class_capacities[class_pos] <= 0` → corta), luego lista los afiliados y pide un código de afiliado válido. Crea la inscripción con estado `1` (Activa) y `0` asistencias, y **descuenta un cupo** de la clase (`gym_class_capacities[class_pos] -= 1`).
- **`baja_inscripcion()`** (línea 710): busca la inscripción por código, si ya estaba inactiva avisa y no hace nada, si está activa pide confirmación y, al confirmar, pone `status = 2` y **devuelve el cupo** a la clase (`+= 1`).
- **`modify_inscripcion()`** (línea 735): permite cambiar asistencias y/o estado. Lo más particular es la lógica de cupos al cambiar el estado:
  - Si pasa de Activa (1) a Inactiva (2): libera un cupo (`+= 1`).
  - Si pasa de Inactiva (2) a Activa (1): valida que haya cupo disponible antes de permitir el cambio, y si hay, lo descuenta (`-= 1`).
  - Esto mantiene siempre sincronizados los cupos de la clase con el número real de inscripciones activas.
- **`list_inscripciones()`** (línea 606): imprime una tabla con el nombre del socio y de la clase (resueltos vía `search_affiliate_position` / `search_class_position`), mostrando "Socio inexistente"/"Clase inexistente" si el código ya no existe (caso raro, pero contemplado).

---

## 8. Ordenamiento (líneas 172–244)

Estas tres funciones implementan a mano tres algoritmos clásicos de ordenamiento, cada uno
sobre **copias** de las listas originales (`lista[:]`) para no alterar los datos reales.

- **`ordenar_socios_por_edad()`** — **Selección**: en cada vuelta busca el índice con la edad mínima del resto no ordenado (`pos_min`) y lo intercambia con la posición actual. Repite esto para las 4 listas en paralelo (nombres, códigos, edades, tipos) para no perder la correspondencia entre ellas.
- **`ordenar_clases_por_nivel()`** — **Inserción**: toma cada elemento y lo va "insertando" hacia atrás en la parte ya ordenada, corriendo los demás una posición hasta encontrar su lugar (comparando por `nivel`).
- **`ordenar_inscripciones_por_asistencias()`** — **Burbujeo (bubble sort)**: compara pares consecutivos y los intercambia si están en el orden incorrecto (`asistencias[j] > asistencias[j+1]`), repitiendo pasadas hasta que queda ordenado.

En los tres casos, el detalle importante es que cada intercambio se hace **simultáneamente
en todas las listas paralelas involucradas**, para que el orden de nombre/código/edad/tipo
(o nivel, o asistencias) siga correspondiéndose.

---

## 9. Búsqueda (líneas 106–169)

Esta es la funcionalidad de "Búsqueda" del menú (distinta de los helpers `search_*_position`
del punto 3, aunque el objetivo final es similar).

- **`buscar_clase_binaria()`** — **Búsqueda binaria**: primero ordena copias de las listas de clases por código usando inserción (para poder aplicar binaria, que requiere datos ordenados), y después aplica el algoritmo clásico: compara contra el elemento del medio (`medio = (inicio+fin)//2`) y descarta la mitad que no corresponde en cada paso, hasta encontrarlo o agotar el rango.
- **`buscar_socio_secuencial()`** — **Búsqueda secuencial**: recorre `affiliate_codes` de punta a punta comparando uno por uno hasta encontrar el código (o terminar sin encontrarlo).

---

## 10. Cálculos estadísticos matriciales (líneas 36–102)

Esta sección arma "matrices" (listas de listas) para generar estadísticas cruzando datos de
inscripciones con clases o tipos de afiliado.

- **`affiliates_by_class_matrix()`** / **`affiliates_by_class()`**: arma una lista de listas donde `matrix[i]` contiene los códigos de los afiliados inscriptos en la clase `i`. La función `affiliates_by_class()` imprime cuántos afiliados hay por clase (`len(matrix[i])`).
- **`attendances_by_class_matrix()`** / **`total_attendances_by_class()`**: igual, pero agrupando las asistencias por clase, y luego sumando el total de asistencias de cada clase.
- **`enrollment_by_class_level_matrix()`**: arma una matriz de 3 filas (una por nivel de clase: 1, 2, 3) y agrupa los códigos de inscripción según el nivel de la clase a la que pertenecen. Imprime cuántas inscripciones hay por nivel.
- **`affiliates_by_type_and_class_matrix()`**: la más compleja — arma una matriz de 3 filas (tipo de afiliado) x N columnas (clases), y en `matrix[tipo][clase]` guarda los códigos de afiliados de ese tipo inscriptos en esa clase. Imprime un cruce completo tipo × clase.

En todos los casos, el patrón es: recorrer `enrollment_codes`, para cada inscripción resolver
la posición de clase/afiliado con los helpers del punto 3, y acumular en la matriz según
corresponda.

---

## 11. Menús y flujo del programa (líneas 773–924)

El programa tiene una estructura de **menú principal con submenús**, todos con el mismo patrón repetido:

1. Una función `input_X_option()` (o `menu_X()`) que imprime las opciones, pide un número, y repite el pedido con un `while` hasta que sea válido (dentro del rango de opciones).
2. Una función `X_menu()` (o `opcion_menu_X()`) que llama a la anterior, y con un `if/elif` ejecuta la función correspondiente a la opción elegida, repitiendo el ciclo hasta que el usuario elige `0` (volver).

Jerarquía:

```
main_menu()
 ├─ 1 → affiliate_menu()      (sumar/eliminar/modificar/listar afiliados)
 ├─ 2 → clases_menu()         (sumar/eliminar/modificar/listar clases)
 ├─ 3 → inscription_menu()    (alta/baja/modificar/listar inscripciones)
 ├─ 4 → opcion_menu_ordenamiento()  (selección/inserción/burbujeo)
 ├─ 5 → opcion_menu_busqueda()      (binaria/secuencial)
 └─ 6 → matrix_menu()               (los 4 cálculos estadísticos)
```

### Punto de entrada (líneas 918–923)

```python
valid_login = login()
if valid_login:
    main_menu()
    print("¡Gracias por usar el sistema de gestión del gimnasio! Hasta luego.")
```

Esto es lo primero que se ejecuta al correr el archivo: pide login, y solo si es válido entra
al menú principal. Cuando el usuario sale del menú principal (opción 0), se despide.

---

## 12. Ideas para entenderlo mejor / posibles preguntas de tu grupo

- Si te preguntan "¿por qué no usan diccionarios o clases (POO)?": porque el trabajo práctico pide resolverlo con **listas paralelas**, arrays y algoritmos de búsqueda/ordenamiento "a mano" (fines didácticos), no con estructuras más avanzadas.
- Si te preguntan por qué se recorre de atrás para adelante en los `remove_enrollments_by_*`: es para evitar el bug de saltearse elementos al hacer `.pop()` mientras se itera con índices crecientes.
- Los "cupos disponibles" de una clase (`gym_class_capacities`) se actualizan en tiempo real cada vez que se da de alta/baja/modifica una inscripción — no es un valor fijo, es parte de la lógica de negocio.

¿Querés que arme también un diagrama de flujo del menú, o que profundice en alguna función puntual (por ejemplo la búsqueda binaria o el borrado en cascada) con un ejemplo paso a paso?
