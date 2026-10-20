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

Los datos se mantienen en memoria y vuelven a su estado inicial al reiniciar el programa.

## Alcance implementado

- Autenticación sin límite de intentos, con contraseña o pregunta de seguridad y salida voluntaria.
- Auditoría persistente de accesos, cierres y altas/bajas/modificaciones; historial y resumen en la opción 7.
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

- [Documentación final para entregar (PDF)](Documentacion/old/Documentacion_GymControl.pdf)
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
El archivo es local y editable, no un registro a prueba de manipulaciones.
Los datos del gimnasio siguen en memoria; únicamente la auditoría persiste.

Pruebas automáticas sin dependencias externas ni clases:

```bash
python3 tests/test_autenticacion_auditoria.py
```
