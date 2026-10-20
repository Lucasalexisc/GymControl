from datos import (
    usuarios_inicio_sesion,
    INDICE_NOMBRE_USUARIO,
    INDICE_CONTRASENA,
    INDICE_PREGUNTA,
    INDICE_RESPUESTA,
)
from utilidades import buscar_posicion_usuario
from auditoria import establecer_usuario, registrar_auditoria

def normalizar_respuesta(respuesta):
    return " ".join(respuesta.split()).casefold()


def iniciar_sesion():
    """Autentica con contraseña o pregunta de seguridad hasta salir."""
    establecer_usuario("sin_sesion")
    while True:
        print("--- INICIO DE SESIÓN ---")
        print("1: Ingresar con contraseña")
        print("2: Ingresar con pregunta de seguridad")
        print("0: Salir")
        opcion = input("Ingrese una opción: ").strip()
        if opcion == "0":
            registrar_auditoria("ACCESO_CANCELADO", "Salida voluntaria")
            return False
        if opcion not in ("1", "2"):
            print("Opción inválida. Elija 1, 2 o 0.")
            continue

        usuario = input("Ingrese su nombre de usuario: ").strip()
        posicion = buscar_posicion_usuario(usuario)
        metodo = "contraseña" if opcion == "1" else "pregunta de seguridad"
        if opcion == "1":
            credencial = input("Ingrese su contraseña: ")
            valido = posicion != -1 and usuarios_inicio_sesion[posicion][INDICE_CONTRASENA] == credencial
        elif posicion == -1:
            valido = False
        else:
            print(usuarios_inicio_sesion[posicion][INDICE_PREGUNTA])
            credencial = normalizar_respuesta(input("Respuesta: "))
            valido = bool(credencial) and credencial == normalizar_respuesta(
                usuarios_inicio_sesion[posicion][INDICE_RESPUESTA]
            )

        if valido:
            establecer_usuario(usuarios_inicio_sesion[posicion][INDICE_NOMBRE_USUARIO])
            registrar_auditoria("ACCESO_EXITOSO", metodo)
            print("¡Bienvenido al sistema de gestión del gimnasio!")
            return True
        registrar_auditoria("ACCESO_FALLIDO", metodo, usuario=usuario)
        print("Credenciales incorrectas. Puede reintentar, cambiar de método o salir.")
