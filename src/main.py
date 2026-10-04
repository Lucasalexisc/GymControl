"""
Punto de entrada de GymControl dentro del paquete src.
"""

from login import login
from menus import main_menu

if __name__ == "__main__":
    valid_login = login()

    if valid_login:
        main_menu()
        print("¡Gracias por usar el sistema de gestión del gimnasio! Hasta luego.")
