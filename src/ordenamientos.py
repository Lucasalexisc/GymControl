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
obtener_nombre_tipo ,
obtener_nombre_nivel
)
from clases import formatear_horario

def ordenar_socios_por_edad ():
    """
    Objetivo: mostrar los socios ordenados de menor a mayor edad.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de los socios.
    """
    afiliados_ordenados = sorted(socios, key=lambda fila: fila[SOCIO_EDAD])

    print ("SOCIOS ORDENADOS POR EDAD")
    for fila in afiliados_ordenados :
        print (f"Código: {fila[SOCIO_CODIGO]}, Nombre: {fila[SOCIO_NOMBRE]}, Edad: {fila[SOCIO_EDAD]}, Tipo: {obtener_nombre_tipo(fila[SOCIO_TIPO])}")

def ordenar_clases_por_nivel ():
    """
    Objetivo: mostrar las clases ordenadas de menor a mayor nivel.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de las clases.
    """
    clases_ordenadas = sorted(clases, key=lambda fila: fila[CLASE_NIVEL])

    print ("CLASES ORDENADAS POR NIVEL")
    for fila in clases_ordenadas :
        print (f"Código: {fila[CLASE_CODIGO]}, Nombre: {fila[CLASE_NOMBRE]}, Nivel: {obtener_nombre_nivel(fila[CLASE_NIVEL])}, Cupos disponibles: {fila[CLASE_CUPOS]}, Horario: {formatear_horario(fila[CLASE_HORARIO])}")

def ordenar_inscripciones_por_asistencias ():
    """
    Objetivo: mostrar las inscripciones ordenadas de menor a mayor cantidad de asistencias.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de las inscripciones.
    """
    inscripciones_ordenadas = sorted(inscripciones, key=lambda fila: fila[INSCRIPCION_ASISTENCIAS])

    print ("INSCRIPCIONES ORDENADAS POR ASISTENCIAS")
    for fila in inscripciones_ordenadas :
        print (f"Código: {fila[INSCRIPCION_CODIGO]}, Socio: {fila[INSCRIPCION_CODIGO_SOCIO]}, Clase: {fila[INSCRIPCION_CODIGO_CLASE]}, Asistencias: {fila[INSCRIPCION_ASISTENCIAS]}, Estado: {fila[INSCRIPCION_ESTADO]}")
