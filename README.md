# GymControl

Sistema de gestión para gimnasios desarrollado en Python como Trabajo Práctico Integrador de Algoritmos y Estructura de Datos 1 / Programación 1.

## Ejecución

Requisitos: Python 3.9 o posterior.

```bash
python3 main.py
```

Credenciales de demostración:

- Usuario: `admin`
- Contraseña: `admin1234`

Los datos se mantienen en memoria y vuelven a su estado inicial al reiniciar el programa (persistencia JSON en proceso de integración).

## Alcance implementado

- Autenticación sin límite de intentos, con contraseña o pregunta de seguridad y salida voluntaria.
- Auditoría persistente de accesos, cierres y altas/bajas/modificaciones; historial y resumen en la opción 7.
- Gestión de socios, clases e inscripciones, con modificación por atributo.
- Control de cupos y prevención de inscripciones activas duplicadas.
- Búsqueda secuencial y binaria.
- Ordenamientos mediante `sorted()`.
- Diccionarios para conteo de auditoría, normalización de días y catálogos de niveles de clase y tipos de socio.
- Reportes matriciales.
- Uso efectivo de `map`, `filter`, `reduce` y expresiones regulares.
- Función genérica de búsqueda con `filter` y funciones lambda para localizar socios y clases.

## Equipo y ramas

| Integrante | Rama | Aporte principal |
|---|---|---|
| Javier Candalaft | `dev-canda` | Base del sistema, login, auditoría, `reduce`, regex y documentación. |
| Lucas Cragaris | `dev-lucas` / `dev-lucas-2` | Modularización, liberación de cupos, pruebas unitarias, clases por socio, prevención de duplicados y validación de nombres. |
| Rodrigo García Solá | `dev-rodri` | Refactor de las estructuras y operaciones a matrices. |
| Tomás van Nynatten | `dev-tom` / `dev-tom-2` | Incorporación y gestión del teléfono, horarios con tuplas y submenús de modificación por atributo. |
| Edney Ribeiro | `dev-ed` / `dev-ed2-entrega` | Función genérica `buscar_posicion()`, diccionarios de tipos/niveles y ordenamientos con `sorted()`. |

## Capturas de funcionamiento

### Inicio de sesión y menú principal

![Inicio de sesión y menú principal](docs/capturas/menu-principal.png)

### Consultas de socios y clases

![Consultas de socios y clases](docs/capturas/consultas.png)

### Reportes matriciales

![Reportes matriciales](docs/capturas/reportes.png)

## Documentación

- [Estado actual y pendientes del equipo (7/11)](Documentacion/Pendientes_Equipo_TP2.md)
- [Plan de implementación actualizado (7/11)](Documentacion/Plan_Implementacion_TP2.md)
- [Documentación de la segunda entrega y pendientes](Documentacion/Documentacion_TP2.md)
- [Documentación de la primera entrega (PDF)](Documentacion/old/Documentacion_GymControl.pdf)
- [Propuesta y alcance](Documentacion/old/GymControl.md)
- [Documentación final con portada](Documentacion/old/documentacion_gymcontrol.md)
- [Estado, modificaciones y pendientes](Documentacion/old/Modificaciones.md)

Repositorio: https://github.com/Lucasalexisc/GymControl

## Autenticación y auditoría (segunda entrega)

Al iniciar, elegir 1 para contraseña, 2 para pregunta de seguridad o 0 para salir.
Para `admin`, la pregunta de demostración es «¿Cuál es tu color favorito?» y la
respuesta es `azul`. Los demás usuarios tienen sus datos de ejemplo en `src/datos.py`.
Las respuestas ignoran mayúsculas y espacios redundantes; las contraseñas son exactas.
Estas credenciales públicas son para el trabajo práctico, no para uso en producción.

`auditoria.txt` se crea en la raíz del proyecto y se amplía entre ejecuciones.
Cada línea contiene fecha/hora con zona, usuario, operación y detalle, separados
por ` | `. No se guardan contraseñas ni respuestas, ni datos personales de socios:
los cambios se identifican por código. Solo se auditan mutaciones efectivas;
las bajas en cascada también registran las inscripciones eliminadas.
La opción 7 muestra el historial y un conteo por operación. Las líneas con formato
inválido se omiten. Ante errores de lectura/escritura se avisa y el programa continúa;
una operación puede completarse aunque no pueda registrarse en el archivo.

## Pruebas y estado de la segunda entrega

Pruebas de regresión de autenticación y auditoría, sin paquetes externos ni clases propias:

```bash
python3 -B tests/test_autenticacion_auditoria.py
```

Las diez pruebas generales ya están integradas y se ejecutan con:

```bash
python3 -B test_gymcontrol.py
```

Cubren 7 funciones: 4 casos válidos, 3 inválidos, 2 límites y 1 de negocio.
El proceso devuelve `0` si todas pasan y `1` si alguna falla.

**Verificación al 7 de noviembre de 2026:** sobre `main` en `a07d82c`, pasaron
10/10 pruebas generales y 12/12 de autenticación y auditoría, con salida `0`.
Las PR #4 (inscripciones), #5 (pruebas y limpieza), #6/#7 (auditoría y documentación)
y #8 (diccionarios de tipos/niveles y `sorted()`) ya están integradas.

## Qué falta para cerrar la entrega

Ver el detalle en [Documentacion/Pendientes_Equipo_TP2.md](Documentacion/Pendientes_Equipo_TP2.md) y en el [plan actualizado](Documentacion/Plan_Implementacion_TP2.md):

1. Reportes con conjuntos (`set`) en `src/estadisticas.py` y `src/menus.py`.
2. Persistencia JSON (`src/persistencia.py` y `datos_gimnasio.json`) con recuperación de tuplas de horarios.
3. Inclusión de los archivos `.txt` y `.json` de entrega (§16).
4. Reemplazo de `unicodedata` en `src/clases.py`, confirmación `(s/n)` en baja de clases y formato de horarios/niveles en búsquedas y ordenamientos.
5. Actualización final de la documentación tras integrar JSON y conjuntos.
