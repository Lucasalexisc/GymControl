from datos import usuarios_inicio_sesion ,INDICE_CONTRASENA
from utilidades import buscar_posicion_usuario

def iniciar_sesion ():
    """
    Objetivo: autenticar a un usuario con un máximo de tres intentos.
    Parámetros: ninguno; solicita el usuario y la contraseña por teclado.
    Salida: True si las credenciales son correctas; False si se agotan los intentos.
    """
    intentos =1
    maximo_intentos =3

    usuario_ingresado =input ("ingrese su nombre de usuario: ")
    contrasena_ingresada =input ("ingrese su contraseña: ")
    posicion_usuario =buscar_posicion_usuario (usuario_ingresado )

    while (posicion_usuario ==-1 or usuarios_inicio_sesion [posicion_usuario ][INDICE_CONTRASENA ]!=contrasena_ingresada )and intentos <maximo_intentos :
        print ("El nombre de usuario o la contraseña son incorrectos, por favor vuelva a intentarlo.")
        usuario_ingresado =input ("ingrese su nombre de usuario: ")
        contrasena_ingresada =input ("ingrese su contraseña: ")
        posicion_usuario =buscar_posicion_usuario (usuario_ingresado )
        intentos +=1

    if posicion_usuario ==-1 or usuarios_inicio_sesion [posicion_usuario ][INDICE_CONTRASENA ]!=contrasena_ingresada :
        print ("Has superado el número de intentos permitidos. Acceso bloqueado.")
        return False
    else :
        print ("¡Bienvenido al sistema de gestión del gimnasio!")
        return True
