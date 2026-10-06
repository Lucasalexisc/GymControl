from functools import reduce
from datos import (
    classes,
    enrollments,
    affiliates,
    ENR_AFFILIATE_CODE,
    ENR_CLASS_CODE,
    ENR_ATTENDANCE,
    ENR_CODE,
    CLASS_NAME,
    CLASS_LEVEL,
    AFF_TYPE,
    get_type_name
)
from utilidades import (
    search_class_position,
    search_affiliate_position
)

# Cálculos estadísticos matriciales
def affiliates_by_class_matrix():
    """
    Objetivo: agrupar los códigos de los socios inscriptos en cada clase.
    Parámetros: ninguno.
    Salida: matriz donde cada fila contiene los códigos de socios de una clase.
    """
    matrix = [[] for _ in range(len(classes))]
    for i in range(len(enrollments)):
        affilate_code = enrollments[i][ENR_AFFILIATE_CODE]
        class_code = enrollments[i][ENR_CLASS_CODE]
        class_pos = search_class_position(class_code)
        if class_pos != -1:
            matrix[class_pos].append(affilate_code)
    return matrix
    
def affiliates_by_class():
    """
    Objetivo: mostrar la cantidad de socios inscriptos en cada clase.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra las cantidades por pantalla.
    """
    print("AFILIADOS POR CLASE")
    matrix = affiliates_by_class_matrix()
    for i in range(len(classes)):
        print(f"Clase: {classes[i][CLASS_NAME]} - Afiliados: {len(matrix[i])}")

def attendances_by_class_matrix():
    """
    Objetivo: agrupar las cantidades de asistencias registradas en cada clase.
    Parámetros: ninguno.
    Salida: matriz donde cada fila contiene las asistencias de una clase.
    """
    matrix = [[] for _ in range(len(classes))]
    for i in range(len(enrollments)):
        class_code = enrollments[i][ENR_CLASS_CODE]
        class_pos = search_class_position(class_code)
        if class_pos != -1:
            matrix[class_pos].append(enrollments[i][ENR_ATTENDANCE])
    return matrix

def total_attendances_by_class():
    """
    Objetivo: calcular y mostrar el total de asistencias de cada clase.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra los totales por pantalla.
    """
    print("TOTAL DE ASISTENCIAS POR CLASE")
    matrix = attendances_by_class_matrix()
    totals = list(map(lambda class_attendances: reduce(lambda accumulated, attendance: accumulated + attendance, class_attendances, 0), matrix))
    for i in range(len(matrix)):
        print(f"Clase: {classes[i][CLASS_NAME]} - Total de asistencias: {totals[i]}")

def enrollment_by_class_level_matrix():
    """
    Objetivo: agrupar las inscripciones según el nivel de la clase correspondiente.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra la cantidad de inscripciones por nivel.
    """
    matrix = [[] for _ in range(3)]
    for i in range(len(enrollments)):
        class_code = enrollments[i][ENR_CLASS_CODE]
        class_pos = search_class_position(class_code)
        if class_pos == -1:
            continue
        level = classes[class_pos][CLASS_LEVEL]
        if 1 <= level <= 3:
            matrix[level - 1].append(enrollments[i][ENR_CODE])
    print("INSCRIPCIONES POR NIVEL DE CLASE")
    for i in range(len(matrix)):
        print(f"Nivel {i + 1}: {len(matrix[i])} inscripciones")

def affiliates_by_type_and_class_matrix():
    """
    Objetivo: agrupar y mostrar los socios según su tipo y la clase en la que están inscriptos.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra las cantidades por tipo y clase.
    """
    matrix = [[[] for _ in range(len(classes))] for _ in range(3)]
    for i in range(len(enrollments)):
        affiliate_code = enrollments[i][ENR_AFFILIATE_CODE]
        class_code = enrollments[i][ENR_CLASS_CODE]
        affiliate_pos = search_affiliate_position(affiliate_code)
        class_pos = search_class_position(class_code)
        if affiliate_pos == -1 or class_pos == -1:
            continue
        affiliate_type = affiliates[affiliate_pos][AFF_TYPE]
        if 1 <= affiliate_type <= 3:
            matrix[affiliate_type - 1][class_pos].append(affiliate_code)
    print("AFILIADOS POR TIPO Y CLASE")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"Socio {get_type_name(i + 1)} - Clase {classes[j][CLASS_NAME]}: {len(matrix[i][j])} afiliados")
