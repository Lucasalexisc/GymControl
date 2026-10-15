from datos import (
socios ,
clases ,
inscripciones ,
SOCIO_EDAD ,
SOCIO_CODIGO ,
SOCIO_NOMBRE ,
SOCIO_TIPO ,
CLASE_NIVEL ,
CLASE_CODIGO ,
CLASE_NOMBRE ,
CLASE_CUPOS ,
CLASE_HORARIO ,
INSCRIPCION_ASISTENCIAS ,
INSCRIPCION_CODIGO ,
INSCRIPCION_CODIGO_SOCIO ,
INSCRIPCION_CODIGO_CLASE ,
INSCRIPCION_ESTADO ,
obtener_nombre_tipo
)

def ordenar_socios_por_edad ():
    """
    Objetivo: mostrar los socios ordenados de menor a mayor edad.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de los socios.
    """
    afiliados_ordenados =[fila [:]for fila in socios ]
    cantidad =len (afiliados_ordenados )
    for indice in range (cantidad -1 ):
        posicion_minima =indice
        for indice_comparacion in range (indice +1 ,cantidad ):
            if afiliados_ordenados [indice_comparacion ][SOCIO_EDAD ]<afiliados_ordenados [posicion_minima ][SOCIO_EDAD ]:
                posicion_minima =indice_comparacion
        afiliados_ordenados [indice ],afiliados_ordenados [posicion_minima ]=afiliados_ordenados [posicion_minima ],afiliados_ordenados [indice ]

    print ("SOCIOS ORDENADOS POR EDAD (Selección)")
    for fila in afiliados_ordenados :
        print (f"Código: {fila[SOCIO_CODIGO]}, Nombre: {fila[SOCIO_NOMBRE]}, Edad: {fila[SOCIO_EDAD]}, Tipo: {obtener_nombre_tipo(fila[SOCIO_TIPO])}")

def ordenar_clases_por_nivel ():
    """
    Objetivo: mostrar las clases ordenadas de menor a mayor nivel.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de las clases.
    """
    clases_ordenadas =[fila [:]for fila in clases ]
    cantidad =len (clases_ordenadas )
    for indice in range (1 ,cantidad ):
        clave_nivel =clases_ordenadas [indice ][CLASE_NIVEL ]
        clave_fila =clases_ordenadas [indice ][:]
        indice_comparacion =indice -1
        while indice_comparacion >=0 and clases_ordenadas [indice_comparacion ][CLASE_NIVEL ]>clave_nivel :
            clases_ordenadas [indice_comparacion +1 ]=clases_ordenadas [indice_comparacion ][:]
            indice_comparacion -=1
        clases_ordenadas [indice_comparacion +1 ]=clave_fila

    print ("CLASES ORDENADAS POR NIVEL (Inserción)")
    for fila in clases_ordenadas :
        print (f"Código: {fila[CLASE_CODIGO]}, Nombre: {fila[CLASE_NOMBRE]}, Nivel: {fila[CLASE_NIVEL]}, Cupos disponibles: {fila[CLASE_CUPOS]}, Horario: {fila[CLASE_HORARIO]}")

def ordenar_inscripciones_por_asistencias ():
    """
    Objetivo: mostrar las inscripciones ordenadas de menor a mayor cantidad de asistencias.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de las inscripciones.
    """
    inscripciones_ordenadas =[fila [:]for fila in inscripciones ]
    cantidad =len (inscripciones_ordenadas )
    for indice in range (cantidad -1 ):
        for indice_comparacion in range (0 ,cantidad -1 -indice ):
            if inscripciones_ordenadas [indice_comparacion ][INSCRIPCION_ASISTENCIAS ]>inscripciones_ordenadas [indice_comparacion +1 ][INSCRIPCION_ASISTENCIAS ]:
                inscripciones_ordenadas [indice_comparacion ],inscripciones_ordenadas [indice_comparacion +1 ]=inscripciones_ordenadas [indice_comparacion +1 ],inscripciones_ordenadas [indice_comparacion ]

    print ("INSCRIPCIONES ORDENADAS POR ASISTENCIAS (Burbujeo)")
    for fila in inscripciones_ordenadas :
        print (f"Código: {fila[INSCRIPCION_CODIGO]}, Socio: {fila[INSCRIPCION_CODIGO_SOCIO]}, Clase: {fila[INSCRIPCION_CODIGO_CLASE]}, Asistencias: {fila[INSCRIPCION_ASISTENCIAS]}, Estado: {fila[INSCRIPCION_ESTADO]}")
