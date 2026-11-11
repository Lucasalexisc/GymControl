from datos import (
clases ,
socios ,
CLASE_CODIGO ,
CLASE_NOMBRE ,
CLASE_NIVEL ,
CLASE_CUPOS ,
CLASE_HORARIO ,
SOCIO_CODIGO ,
SOCIO_NOMBRE ,
SOCIO_EDAD ,
SOCIO_TIPO ,
obtener_nombre_tipo
)
from validaciones import pedir_entero
from clases import formatear_horario

def buscar_clase_binaria ():
    """
    Objetivo: buscar una clase por su código y mostrar sus datos.
    Parámetros: ninguno; solicita el código por teclado.
    Salida: no devuelve valores; muestra la clase encontrada o un mensaje de error.
    """
    print ("BÚSQUEDA BINARIA DE CLASE POR CÓDIGO")
    codigo =pedir_entero ("Ingrese el código de la clase a buscar: ","Código inválido, ingrese un número.")

    clases_ordenadas = sorted(clases, key=lambda fila: fila[CLASE_CODIGO])
    cantidad = len(clases_ordenadas)

    inicio =0
    fin =cantidad -1
    posicion =-1

    while inicio <=fin :
        medio =(inicio +fin )//2
        if clases_ordenadas [medio ][CLASE_CODIGO ]==codigo :
            posicion =medio
            inicio =fin +1
        elif clases_ordenadas [medio ][CLASE_CODIGO ]<codigo :
            inicio =medio +1
        else :
            fin =medio -1

    if posicion ==-1 :
        print ("Clase no encontrada.")
    else :
        print (f"Clase encontrada:")
        fila = clases_ordenadas[posicion]
        print (f"Código: {fila[CLASE_CODIGO]}, Nombre: {fila[CLASE_NOMBRE]}, Nivel: {fila[CLASE_NIVEL]}, Cupos disponibles: {fila[CLASE_CUPOS]}, Horario: {formatear_horario(fila[CLASE_HORARIO])}")

def buscar_socio_secuencial ():
    """
    Objetivo: buscar un socio por su código y mostrar sus datos.
    Parámetros: ninguno; solicita el código por teclado.
    Salida: no devuelve valores; muestra el socio encontrado o un mensaje de error.
    """
    print ("BÚSQUEDA SECUENCIAL DE SOCIO POR CÓDIGO")
    codigo =pedir_entero ("Ingrese el código del socio a buscar: ","Código inválido, ingrese un número.")

    posicion =-1
    for indice in range (len (socios )):
        if socios [indice ][SOCIO_CODIGO ]==codigo :
            posicion =indice

    if posicion ==-1 :
        print ("Socio no encontrado.")
    else :
        print (f"Socio encontrado en posición {posicion}:")
        print (f"Código: {socios[posicion][SOCIO_CODIGO]}, Nombre: {socios[posicion][SOCIO_NOMBRE]}, Edad: {socios[posicion][SOCIO_EDAD]}, Tipo: {obtener_nombre_tipo(socios[posicion][SOCIO_TIPO])}")