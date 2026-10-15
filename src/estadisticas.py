from functools import reduce
from datos import (
clases ,
inscripciones ,
socios ,
INSCRIPCION_CODIGO_SOCIO ,
INSCRIPCION_CODIGO_CLASE ,
INSCRIPCION_ASISTENCIAS ,
INSCRIPCION_CODIGO ,
CLASE_NOMBRE ,
CLASE_NIVEL ,
SOCIO_TIPO ,
obtener_nombre_tipo
)
from utilidades import (
buscar_posicion_clase ,
buscar_posicion_socio
)

# Cálculos estadísticos matriciales
def matriz_socios_por_clase ():
    """
    Objetivo: agrupar los códigos de los socios inscriptos en cada clase.
    Parámetros: ninguno.
    Salida: matriz donde cada fila contiene los códigos de socios de una clase.
    """
    matriz =[[]for _ in range (len (clases ))]
    for indice in range (len (inscripciones )):
        codigo_socio =inscripciones [indice ][INSCRIPCION_CODIGO_SOCIO ]
        codigo_clase =inscripciones [indice ][INSCRIPCION_CODIGO_CLASE ]
        posicion_clase =buscar_posicion_clase (codigo_clase )
        if posicion_clase !=-1 :
            matriz [posicion_clase ].append (codigo_socio )
    return matriz

def socios_por_clase ():
    """
    Objetivo: mostrar la cantidad de socios inscriptos en cada clase.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra las cantidades por pantalla.
    """
    print ("AFILIADOS POR CLASE")
    matriz =matriz_socios_por_clase ()
    for indice in range (len (clases )):
        print (f"Clase: {clases[indice][CLASE_NOMBRE]} - Afiliados: {len(matriz[indice])}")

def matriz_asistencias_por_clase ():
    """
    Objetivo: agrupar las cantidades de asistencias registradas en cada clase.
    Parámetros: ninguno.
    Salida: matriz donde cada fila contiene las asistencias de una clase.
    """
    matriz =[[]for _ in range (len (clases ))]
    for indice in range (len (inscripciones )):
        codigo_clase =inscripciones [indice ][INSCRIPCION_CODIGO_CLASE ]
        posicion_clase =buscar_posicion_clase (codigo_clase )
        if posicion_clase !=-1 :
            matriz [posicion_clase ].append (inscripciones [indice ][INSCRIPCION_ASISTENCIAS ])
    return matriz

def total_asistencias_por_clase ():
    """
    Objetivo: calcular y mostrar el total de asistencias de cada clase.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra los totales por pantalla.
    """
    print ("TOTAL DE ASISTENCIAS POR CLASE")
    matriz =matriz_asistencias_por_clase ()
    totales =list (map (lambda asistencias_clase :reduce (lambda acumulado ,asistencia :acumulado +asistencia ,asistencias_clase ,0 ),matriz ))
    for indice in range (len (matriz )):
        print (f"Clase: {clases[indice][CLASE_NOMBRE]} - Total de asistencias: {totales[indice]}")

def matriz_inscripciones_por_nivel_clase ():
    """
    Objetivo: agrupar las inscripciones según el nivel de la clase correspondiente.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra la cantidad de inscripciones por nivel.
    """
    matriz =[[]for _ in range (3 )]
    for indice in range (len (inscripciones )):
        codigo_clase =inscripciones [indice ][INSCRIPCION_CODIGO_CLASE ]
        posicion_clase =buscar_posicion_clase (codigo_clase )
        if posicion_clase ==-1 :
            continue
        nivel =clases [posicion_clase ][CLASE_NIVEL ]
        if 1 <=nivel <=3 :
            matriz [nivel -1 ].append (inscripciones [indice ][INSCRIPCION_CODIGO ])
    print ("INSCRIPCIONES POR NIVEL DE CLASE")
    for indice in range (len (matriz )):
        print (f"Nivel {indice + 1}: {len(matriz[indice])} inscripciones")

def matriz_socios_por_tipo_y_clase ():
    """
    Objetivo: agrupar y mostrar los socios según su tipo y la clase en la que están inscriptos.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra las cantidades por tipo y clase.
    """
    matriz =[[[]for _ in range (len (clases ))]for _ in range (3 )]
    for indice in range (len (inscripciones )):
        codigo_socio =inscripciones [indice ][INSCRIPCION_CODIGO_SOCIO ]
        codigo_clase =inscripciones [indice ][INSCRIPCION_CODIGO_CLASE ]
        posicion_socio =buscar_posicion_socio (codigo_socio )
        posicion_clase =buscar_posicion_clase (codigo_clase )
        if posicion_socio ==-1 or posicion_clase ==-1 :
            continue
        tipo_socio =socios [posicion_socio ][SOCIO_TIPO ]
        if 1 <=tipo_socio <=3 :
            matriz [tipo_socio -1 ][posicion_clase ].append (codigo_socio )
    print ("AFILIADOS POR TIPO Y CLASE")
    for indice in range (len (matriz )):
        for indice_comparacion in range (len (matriz [indice ])):
            print (f"Socio {obtener_nombre_tipo(indice + 1)} - Clase {clases[indice_comparacion][CLASE_NOMBRE]}: {len(matriz[indice][indice_comparacion])} afiliados")
