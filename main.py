"""
Punto de entrada principal para GymControl (Versión Modularizada).
Permite ejecutar el sistema desde la raíz del proyecto.
"""

import os
import sys

# Agrega la carpeta 'src' al path de Python para importar los módulos limpios
ruta_src = os.path.join(os.path.dirname(__file__), "src")
if os.path.exists(ruta_src) and ruta_src not in sys.path:
    sys.path.insert(0, ruta_src)

from login import login
from menus import main_menu

if __name__ == "__main__":
    valid_login = login()

    if valid_login:
        main_menu()
        print("¡Gracias por usar el sistema de gestión del gimnasio! Hasta luego.")
