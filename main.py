"""
Punto de entrada principal para GymControl (Versión Modularizada).
Permite ejecutar el sistema desde la raíz del proyecto.
"""

import sys

if "src" not in sys.path:
    sys.path.insert(0, "src")

from login import iniciar_sesion
from menus import menu_principal
from auditoria import cerrar_sesion
from persistencia import cargar_datos


def ejecutar():
    cargar_datos()
    try:
        if iniciar_sesion():
            menu_principal()
            print("¡Gracias por usar el sistema de gestión del gimnasio! Hasta luego.")
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada interrumpida. Saliendo del sistema.")
    finally:
        cerrar_sesion()


if __name__ == "__main__":
    ejecutar()
