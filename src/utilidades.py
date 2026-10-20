import re
from datos import (
clases ,
socios ,
inscripciones ,
usuarios_inicio_sesion ,
CLASE_CODIGO ,
SOCIO_CODIGO ,
INDICE_NOMBRE_USUARIO ,
INSCRIPCION_CODIGO ,
INSCRIPCION_CODIGO_SOCIO ,
INSCRIPCION_CODIGO_CLASE ,
INSCRIPCION_ESTADO
)

def buscar_posicion (filas ,condicion ):
    """
    Objetivo: encontrar la posición de la primera fila que cumpla una condición.
    Parámetros: filas, matriz donde buscar; condicion, función que evalúa cada fila.
    Salida: posición de la fila o -1 si ninguna cumple la condición.
    """
    posiciones =list (filter (lambda indice :condicion (filas [indice ]),range (len (filas ))))
    if len (posiciones )>0 :
        return posiciones [0 ]
    return -1

def buscar_posicion_clase (code ):
    """
    Objetivo: encontrar la posición de una clase a partir de su código.
    Parámetros: code, código de la clase buscada.
    Salida: posición de la clase o -1 si no existe.
    """
    return buscar_posicion (clases ,lambda fila :fila [CLASE_CODIGO ]==code )

def buscar_posicion_socio (code ):
    """
    Objetivo: encontrar la posición de un socio a partir de su código.
    Parámetros: code, código del socio buscado.
    Salida: posición del socio o -1 si no existe.
    """
    return buscar_posicion (socios ,lambda fila :fila [SOCIO_CODIGO ]==code )

def buscar_posicion_usuario (nombre_usuario ):
    """
    Objetivo: encontrar la posición de un usuario sin distinguir mayúsculas de minúsculas.
    Parámetros: nombre_usuario, nombre de usuario buscado.
    Salida: posición del usuario o -1 si no existe.
    """
    posicion =-1
    for indice in range (len (usuarios_inicio_sesion )):
        if usuarios_inicio_sesion [indice ][INDICE_NOMBRE_USUARIO ].casefold ()==nombre_usuario .strip ().casefold ():
            posicion =indice
    return posicion

def existe_codigo_clase (code ):
    """
    Objetivo: determinar si existe una clase con un código específico.
    Parámetros: code, código de la clase buscada.
    Salida: True si la clase existe; False en caso contrario.
    """
    for fila in clases :
        if fila [CLASE_CODIGO ]==code :
            return True
    return False

def existe_codigo_socio (code ):
    """
    Objetivo: determinar si existe un socio con un código específico.
    Parámetros: code, código del socio buscado.
    Salida: True si el socio existe; False en caso contrario.
    """
    for fila in socios :
        if fila [SOCIO_CODIGO ]==code :
            return True
    return False

def socio_esta_inscripto_en_clase (codigo_socio ,codigo_clase ):
    """
    Objetivo: determinar si un socio ya posee una inscripción activa en una clase utilizando lambda y filter.
    Parámetros: codigo_socio (int), codigo_clase (int).
    Salida: True si el afiliado ya está inscripto activamente; False en caso contrario.
    """
    inscripciones_previas =list (filter (
    lambda inscripcion :inscripcion [INSCRIPCION_CODIGO_SOCIO ]==codigo_socio and inscripcion [INSCRIPCION_CODIGO_CLASE ]==codigo_clase and inscripcion [INSCRIPCION_ESTADO ]==1 ,
    inscripciones
    ))
    return len (inscripciones_previas )>0

def buscar_posicion_inscripcion (code ):
    """
    Objetivo: encontrar la posición de una inscripción a partir de su código.
    Parámetros: code, código de la inscripción buscada.
    Salida: posición de la inscripción o -1 si no existe.
    """
    posicion =-1
    for indice in range (len (inscripciones )):
        if inscripciones [indice ][INSCRIPCION_CODIGO ]==code :
            posicion =indice
    return posicion
