from datos import (
    login_users, LOGIN_USERNAME, LOGIN_PASSWORD, LOGIN_QUESTION, LOGIN_ANSWER,
)
from utilidades import search_user_position
from auditoria import establecer_usuario, registrar_auditoria


def normalizar_respuesta(respuesta):
    """Ignora mayúsculas y espacios redundantes, pero conserva las tildes."""
    return " ".join(respuesta.split()).casefold()


def login():
    """Permite reintentar ambos métodos sin límite o salir voluntariamente."""
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
        posicion = search_user_position(usuario)
        metodo = "contraseña" if opcion == "1" else "pregunta de seguridad"
        if opcion == "1":
            clave = input("Ingrese su contraseña: ")
            valido = posicion != -1 and login_users[posicion][LOGIN_PASSWORD] == clave
        else:
            if posicion == -1:
                registrar_auditoria("ACCESO_FALLIDO", metodo, usuario=usuario)
                print("No se pudo iniciar sesión. Revise el usuario o utilice contraseña.")
                continue
            print(login_users[posicion][LOGIN_QUESTION])
            respuesta = normalizar_respuesta(input("Respuesta: "))
            valido = bool(respuesta) and respuesta == normalizar_respuesta(login_users[posicion][LOGIN_ANSWER])
        if valido:
            establecer_usuario(login_users[posicion][LOGIN_USERNAME])
            registrar_auditoria("ACCESO_EXITOSO", metodo)
            print("¡Bienvenido al sistema de gestión del gimnasio!")
            return True
        registrar_auditoria("ACCESO_FALLIDO", metodo, usuario=usuario)
        print("Credenciales incorrectas. Puede reintentar, cambiar de método o salir.")
