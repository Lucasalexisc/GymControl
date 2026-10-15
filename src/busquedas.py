from datos import (
clases ,
socios ,
CLASE_CODIGO ,
CLASE_NOMBRE ,
CLASE_NIVEL ,
CLASE_CUPOS ,
SOCIO_CODIGO ,
SOCIO_NOMBRE ,
SOCIO_EDAD ,
SOCIO_TIPO ,
obtener_nombre_tipo
)
from validaciones import pedir_entero

def buscar_clase_binaria ():
    """
    Objetivo: buscar una clase por su código y mostrar sus datos.
    Parámetros: ninguno; solicita el código por teclado.
    Salida: no devuelve valores; muestra la clase encontrada o un mensaje de error.
    """
    print ("BÚSQUEDA BINARIA DE CLASE POR CÓDIGO")
    codigo =pedir_entero ("Ingrese el código de la clase a buscar: ","Código inválido, ingrese un número.")

    codigos =[fila [CLASE_CODIGO ]for fila in clases ]
    nombres =[fila [CLASE_NOMBRE ]for fila in clases ]
    niveles =[fila [CLASE_NIVEL ]for fila in clases ]
    capacidades =[fila [CLASE_CUPOS ]for fila in clases ]

    cantidad =len (codigos )
    for indice in range (1 ,cantidad ):
        clave_codigo =codigos [indice ]
        clave_nombre =nombres [indice ]
        clave_nivel =niveles [indice ]
        clave_capacidad =capacidades [indice ]
        indice_comparacion =indice -1
        while indice_comparacion >=0 and codigos [indice_comparacion ]>clave_codigo :
            codigos [indice_comparacion +1 ]=codigos [indice_comparacion ]
            nombres [indice_comparacion +1 ]=nombres [indice_comparacion ]
            niveles [indice_comparacion +1 ]=niveles [indice_comparacion ]
            capacidades [indice_comparacion +1 ]=capacidades [indice_comparacion ]
            indice_comparacion -=1
        codigos [indice_comparacion +1 ]=clave_codigo
        nombres [indice_comparacion +1 ]=clave_nombre
        niveles [indice_comparacion +1 ]=clave_nivel
        capacidades [indice_comparacion +1 ]=clave_capacidad

    inicio =0
    fin =cantidad -1
    posicion =-1

    while inicio <=fin :
        medio =(inicio +fin )//2
        if codigos [medio ]==codigo :
            posicion =medio
            inicio =fin +1
        elif codigos [medio ]<codigo :
            inicio =medio +1
        else :
            fin =medio -1

    if posicion ==-1 :
        print ("Clase no encontrada.")
    else :
        print (f"Clase encontrada:")
        print (f"Código: {codigos[posicion]}, Nombre: {nombres[posicion]}, Nivel: {niveles[posicion]}, Cupos disponibles: {capacidades[posicion]}")

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
