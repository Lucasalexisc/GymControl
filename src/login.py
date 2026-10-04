from datos import login_users, LOGIN_PASSWORD
from utilidades import search_user_position

def login():
    """
    Objetivo: autenticar a un usuario con un máximo de tres intentos.
    Parámetros: ninguno; solicita el usuario y la contraseña por teclado.
    Salida: True si las credenciales son correctas; False si se agotan los intentos.
    """
    attempts = 1
    max_attempts = 3

    input_user = input("ingrese su nombre de usuario: ")
    input_passw = input("ingrese su contraseña: ")
    user_position = search_user_position(input_user)

    while (user_position == -1 or login_users[user_position][LOGIN_PASSWORD] != input_passw) and attempts < max_attempts:
        print("El nombre de usuario o la contraseña son incorrectos, por favor vuelva a intentarlo.")
        input_user = input("ingrese su nombre de usuario: ")
        input_passw = input("ingrese su contraseña: ")
        user_position = search_user_position(input_user)
        attempts += 1

    if user_position == -1 or login_users[user_position][LOGIN_PASSWORD] != input_passw:
        print("Has superado el número de intentos permitidos. Acceso bloqueado.")
        return False
    else:
        print("¡Bienvenido al sistema de gestión del gimnasio!")
        return True
