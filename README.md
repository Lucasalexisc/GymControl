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

Los datos de socios, clases e inscripciones se cargan automáticamente desde `datos_gimnasio.json` al iniciar el programa y se guardan tras cada alta, baja o modificación.

## Alcance implementado

- Autenticación sin límite de intentos, con contraseña o pregunta de seguridad y salida voluntaria.
- Auditoría persistente en `auditoria.txt` de accesos, cierres y altas/bajas/modificaciones; historial y resumen en la opción 7.
- Persistencia en `datos_gimnasio.json` de socios, clases e inscripciones, reconstruyendo las tuplas inmutables de horarios al iniciar.
- Gestión de socios, clases e inscripciones, con modificación por atributo individual.
- Control de cupos (incluyendo liberación al dar de baja un socio) y prevención de inscripciones activas duplicadas.
- Búsqueda secuencial y binaria.
- Ordenamientos mediante `sorted()`.
- Diccionarios para estado de sesión, conteo de auditoría, normalización de días y catálogos de niveles de clase y tipos de socio.
- Conjuntos (`set`) para identificar socios sin clases activas (diferencia de conjuntos) y disciplinas disponibles sin repetir.
- Reportes matriciales.
- Uso efectivo de `map`, `filter`, `reduce` y expresiones regulares.
- Función genérica de búsqueda con `filter` y funciones lambda para localizar socios y clases.

## Equipo y ramas

| Integrante | Rama | Aporte principal |
|---|---|---|
| Javier Candalaft | `dev-canda` | Base del sistema, login, auditoría, `reduce`, regex y documentación. |
| Lucas Cragaris | `dev-lucas` / `dev-lucas-2` | Modularización, liberación de cupos, persistencia JSON, pruebas unitarias, integración general y validaciones. |
| Rodrigo García Solá | `dev-rodri` | Refactor de las estructuras y operaciones a matrices. |
| Tomás van Nynatten | `dev-tom` / `dev-tom-2` | Incorporación y gestión del teléfono, horarios con tuplas y submenús de modificación por atributo. |
| Edney Ribeiro | `dev-ed` / `dev-ed2-entrega` | Función genérica `buscar_posicion()`, diccionarios de tipos/niveles, reportes con conjuntos y ordenamientos con `sorted()`. |

## Capturas de funcionamiento

### Inicio de sesión y menú principal

![Inicio de sesión y menú principal](docs/capturas/menu-principal.png)

### Consultas de socios y clases

![Consultas de socios y clases](docs/capturas/consultas.png)

### Reportes matriciales

![Reportes matriciales](docs/capturas/reportes.png)

## Documentación

- [Documentación de la segunda entrega (Punto 15)](Documentacion/Documentacion_TP2.md)
- [Plan de implementación actualizado](Documentacion/Plan_Implementacion_TP2.md)
- [Estado final de la entrega](Documentacion/Pendientes_Equipo_TP2.md)
- [Documentación de la primera entrega (PDF)](Documentacion/old/Documentacion_GymControl.pdf)
- [Propuesta y alcance](Documentacion/old/GymControl.md)
- [Documentación final con portada](Documentacion/old/documentacion_gymcontrol.md)
- [Estado, modificaciones y pendientes](Documentacion/old/Modificaciones.md)

Repositorio: https://github.com/Lucasalexisc/GymControl

## Autenticación, auditoría y persistencia JSON (segunda entrega)

Al iniciar, elegir 1 para contraseña, 2 para pregunta de seguridad o 0 para salir.
Para `admin`, la pregunta de demostración es «¿Cuál es tu color favorito?» y la
respuesta es `azul`. Los demás usuarios tienen sus datos de ejemplo en `src/datos.py`.
Las respuestas ignoran mayúsculas y espacios redundantes; las contraseñas son exactas.

- **Auditoría (`auditoria.txt`):** se almacena en la raíz del proyecto y se amplía entre ejecuciones. Cada línea contiene identificador de evento, usuario, operación y detalle, separados por ` | `. La opción 7 muestra el historial y un conteo por operación mediante un diccionario.
- **Persistencia (`datos_gimnasio.json`):** `src/persistencia.py` carga el estado del gimnasio al iniciar `main.py` y guarda automáticamente los cambios luego de cada alta, baja o modificación, reconstruyendo las tuplas de horarios `((dias...), hora_inicio, hora_fin)` y controlando excepciones de lectura/escritura o formato inválido.

## Pruebas unitarias

Suite de pruebas unitarias independientes (sin uso de clases `class` ni librerías no vistas en la materia):

```bash
python3 -B test_gymcontrol.py
```

Cubre 12 pruebas unitarias sobre 9 funciones del sistema (4 casos válidos, 3 inválidos, 2 límites y 3 casos relevantes de negocio: liberación de cupos, conjuntos y persistencia JSON con tuplas).
