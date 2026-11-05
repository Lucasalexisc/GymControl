from datos import (
    affiliates,
    classes,
    enrollments,
    AFF_AGE,
    AFF_CODE,
    AFF_NAME,
    AFF_TYPE,
    CLASS_LEVEL,
    CLASS_CODE,
    CLASS_NAME,
    CLASS_CAPACITY,
    ENR_ATTENDANCE,
    ENR_CODE,
    ENR_AFFILIATE_CODE,
    ENR_CLASS_CODE,
    ENR_STATUS,
    get_type_name
)

def ordenar_socios_por_edad():
    """
    Objetivo: mostrar los socios ordenados de menor a mayor edad.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de los socios.
    """
    afiliados_ordenados = sorted(affiliates, key=lambda fila: fila[AFF_AGE])

    print("SOCIOS ORDENADOS POR EDAD")
    for row in afiliados_ordenados:
        print(f"Código: {row[AFF_CODE]}, Nombre: {row[AFF_NAME]}, Edad: {row[AFF_AGE]}, Tipo: {get_type_name(row[AFF_TYPE])}")

def ordenar_clases_por_nivel():
    """
    Objetivo: mostrar las clases ordenadas de menor a mayor nivel.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de las clases.
    """
    clases_ordenadas = sorted(classes, key=lambda fila: fila[CLASS_LEVEL])

    print("CLASES ORDENADAS POR NIVEL")
    for row in clases_ordenadas:
        print(f"Código: {row[CLASS_CODE]}, Nombre: {row[CLASS_NAME]}, Nivel: {row[CLASS_LEVEL]}, Cupos disponibles: {row[CLASS_CAPACITY]}")

def ordenar_inscripciones_por_asistencias():
    """
    Objetivo: mostrar las inscripciones ordenadas de menor a mayor cantidad de asistencias.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de las inscripciones.
    """
    inscripciones_ordenadas = sorted(enrollments, key=lambda fila: fila[ENR_ATTENDANCE])

    print("INSCRIPCIONES ORDENADAS POR ASISTENCIAS")
    for row in inscripciones_ordenadas:
        print(f"Código: {row[ENR_CODE]}, Socio: {row[ENR_AFFILIATE_CODE]}, Clase: {row[ENR_CLASS_CODE]}, Asistencias: {row[ENR_ATTENDANCE]}, Estado: {row[ENR_STATUS]}")
