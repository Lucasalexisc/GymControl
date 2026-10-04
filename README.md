# GymControl

Sistema de gestión para gimnasios desarrollado en Python como Trabajo Práctico Integrador de Algoritmos y Estructura de Datos 1 / Programación 1.

## Ejecución

Requisitos: Python 3.9 o posterior.

```bash
python3 tp.py
```

Credenciales de demostración:

- Usuario: `admin`
- Contraseña: `admin1234`

Los datos se mantienen en memoria y vuelven a su estado inicial al reiniciar el programa.

## Alcance implementado

- Autenticación con tres intentos.
- Gestión de socios, clases e inscripciones.
- Control de cupos y prevención de inscripciones activas duplicadas.
- Búsqueda secuencial y binaria.
- Ordenamientos por selección, inserción y burbujeo.
- Reportes matriciales.
- Uso efectivo de `map`, `filter`, `reduce` y expresiones regulares.
- Función genérica de búsqueda con `filter` y funciones lambda para localizar socios y clases.

La integración final incluye la [PR #8](https://github.com/rodrings/GymControl/pull/8) de Tomás, con la gestión completa del teléfono, y la [PR #9](https://github.com/rodrings/GymControl/pull/9) de Edney, con la función genérica de búsqueda. Ambas están integradas a `main`.

## Equipo y ramas

| Integrante | Rama | Aporte principal |
|---|---|---|
| Javier Candalaft | `dev-canda` | Base del sistema, login, `reduce`, regex y documentación. |
| Lucas Cragaris | `dev-lucas` | Clases por socio, prevención de duplicados y validación de nombres. |
| Rodrigo García Solá | `dev-rodri` | Refactor de las estructuras y operaciones a matrices. |
| Tomás van Nynatten | `dev-tom` | Incorporación y gestión del teléfono de los socios. |
| Edney Ribeiro | `dev-ed` | Función genérica `search_position()` y búsquedas de socios y clases mediante `filter` y lambda. |

## Capturas de funcionamiento

### Inicio de sesión y menú principal

![Inicio de sesión y menú principal](docs/capturas/menu-principal.png)

### Consultas de socios y clases

![Consultas de socios y clases](docs/capturas/consultas.png)

### Reportes matriciales

![Reportes matriciales](docs/capturas/reportes.png)

## Documentación

- [Documentación final para entregar (PDF)](Documentacion_GymControl.pdf)
- [Propuesta y alcance](GymControl.md)
- [Documentación final con portada](documentacion_gymcontrol.md)
- [Estado, modificaciones y pendientes](Modificaciones.md)

Repositorio: https://github.com/Lucasalexisc/GymControl
