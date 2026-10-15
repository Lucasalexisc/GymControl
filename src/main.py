"""
Punto de entrada de GymControl dentro del paquete src.
"""

from login import iniciar_sesion
from menus import menu_principal

if __name__ =="__main__":
    inicio_sesion_valido =iniciar_sesion ()

    if inicio_sesion_valido :
        menu_principal ()
        print ("¡Gracias por usar el sistema de gestión del gimnasio! Hasta luego.")
