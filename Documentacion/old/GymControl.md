# GymControl - Propuesta y alcance

**Materia:** Algoritmos y Estructura de Datos 1 / Programación 1
**Docentes:** Lic. Gustavo E. Escandell y Lic. Facundo Marianelli
**Comisión:** lunes por la noche - N.º 577502
**Fecha:** 3 de septiembre de 2026

## Integrantes

- García Solá, Rodrigo Nahuel - referente del grupo - `dev-rodri`.
- Cragaris, Lucas - `dev-lucas`.
- van Nynatten, Tomás - `dev-tom`.
- Candalaft, Javier - `dev-canda`.
- Ribeiro, Edney - `dev-ed`.

El docente confirmó que podemos presentar el trabajo entre los cinco integrantes.

## Problemática

Los gimnasios pequeños suelen registrar socios, clases e inscripciones en cuadernos o planillas separadas. Esto dificulta mantener información consistente, evitar inscripciones duplicadas, controlar cupos y obtener indicadores básicos de asistencia.

GymControl centraliza esas operaciones en un programa de consola y valida los datos antes de modificar las estructuras del sistema.

## Objetivo

Desarrollar un sistema en Python que permita administrar socios, clases e inscripciones; consultar y ordenar información; controlar cupos; y generar estadísticas utilizando únicamente los contenidos habilitados por la materia.

## Alcance implementado

El sistema incluye:

- Login con usuarios precargados, comparación sin distinguir mayúsculas y minúsculas, y bloqueo después de tres intentos fallidos.
- Alta, baja, modificación y listado de socios.
- Alta, baja, modificación y listado de clases.
- Alta, baja, modificación y listado de inscripciones.
- Prevención de una segunda inscripción activa del mismo socio en la misma clase.
- Descuento y devolución de cupos al activar o desactivar inscripciones.
- Listado de las clases activas de un socio.
- Búsqueda binaria de clases por código y búsqueda secuencial de socios por código.
- Función genérica para obtener la posición de socios y clases mediante `filter` y funciones lambda.
- Ordenamiento de socios por edad, clases por nivel e inscripciones por asistencias.
- Reportes de socios por clase, inscripciones por nivel, asistencias por clase y socios por tipo y clase.
- Matrices, listas de cadenas, expresiones regulares y funciones lambda con `map`, `filter` y `reduce`.

## Datos administrados

| Entidad | Estructura de cada fila |
|---|---|
| Usuarios | `[usuario, contraseña]` |
| Socios | `[nombre, código, edad, tipo, teléfono]` |
| Clases | `[código, nombre, nivel, cupos_disponibles]` |
| Inscripciones | `[código, código_socio, código_clase, asistencias, estado]` |

Los teléfonos se incorporaron a los datos iniciales mediante la PR #4. La PR #8 de Tomás completó la validación en formato `XX-XXXX-XXXX` y su gestión durante el alta, modificación, listado y confirmación de baja. Esa versión ya forma parte de la integración final.

## Fuera del alcance

- Interfaz gráfica.
- Base de datos o persistencia en archivos.
- Pagos, cuotas, deudas y reportes monetarios.
- DNI, correo electrónico, profesores, días y horarios.
- Clases, objetos, herencia, decoradores, generadores u otros conceptos no habilitados por la materia.

Al cerrar el programa, los cambios realizados durante la ejecución se pierden y se recuperan los datos precargados.

## Ejemplos de uso

1. Un operador inicia sesión, agrega un socio y consulta el listado.
2. El operador crea una clase e inscribe un socio. El sistema verifica que ambos códigos existan, que haya cupo y que no exista otra inscripción activa equivalente.
3. El operador consulta las clases activas de un socio.
4. El sistema ordena socios por edad o genera totales de asistencia por clase.

## Distribución del trabajo

La siguiente distribución resume las responsabilidades de cada integrante.

- **Javier Candalaft (`dev-canda`):** base, matriz de usuarios, `reduce`, login, regex y documentación.
- **Lucas Cragaris (`dev-lucas`):** clases por socio, prevención de duplicados y regex con tildes.
- **Rodrigo García Solá (`dev-rodri`):** refactor a matrices y adaptación de las operaciones.
- **Tomás van Nynatten (`dev-tom`):** teléfonos precargados y CRUD del teléfono en las PRs #4 y #8.
- **Edney Ribeiro (`dev-ed`):** función genérica `search_position()` y reutilización de `filter` y funciones lambda en las búsquedas de socios y clases.

**Organización en Git:** `main` es la rama de integración y cada integrante trabaja en su rama `dev-*`. Repositorio: https://github.com/rodrings/GymControl
