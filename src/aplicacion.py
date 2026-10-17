"""Punto de entrada de GymControl dentro de src."""
from login import login
from menus import main_menu
from auditoria import cerrar_sesion


def ejecutar():
    """Ejecuta el sistema y cierra la sesión también al interrumpir la entrada."""
    try:
        if login():
            main_menu()
            print("¡Gracias por usar el sistema de gestión del gimnasio! Hasta luego.")
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada interrumpida. Saliendo del sistema.")
    finally:
        cerrar_sesion()
