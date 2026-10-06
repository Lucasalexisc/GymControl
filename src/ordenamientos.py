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
    afiliados_ordenados = [fila[:] for fila in affiliates]
    n = len(afiliados_ordenados)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if afiliados_ordenados[j][AFF_AGE] < afiliados_ordenados[pos_min][AFF_AGE]:
                pos_min = j
        afiliados_ordenados[i], afiliados_ordenados[pos_min] = afiliados_ordenados[pos_min], afiliados_ordenados[i]

    print("SOCIOS ORDENADOS POR EDAD (Selección)")
    for row in afiliados_ordenados:
        print(f"Código: {row[AFF_CODE]}, Nombre: {row[AFF_NAME]}, Edad: {row[AFF_AGE]}, Tipo: {get_type_name(row[AFF_TYPE])}")

def ordenar_clases_por_nivel():
    """
    Objetivo: mostrar las clases ordenadas de menor a mayor nivel.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de las clases.
    """
    clases_ordenadas = [fila[:] for fila in classes]
    n = len(clases_ordenadas)
    for i in range(1, n):
        clave_nivel = clases_ordenadas[i][CLASS_LEVEL]
        clave_fila = clases_ordenadas[i][:]
        j = i - 1
        while j >= 0 and clases_ordenadas[j][CLASS_LEVEL] > clave_nivel:
            clases_ordenadas[j + 1] = clases_ordenadas[j][:]
            j -= 1
        clases_ordenadas[j + 1] = clave_fila

    print("CLASES ORDENADAS POR NIVEL (Inserción)")
    for row in clases_ordenadas:
        print(f"Código: {row[CLASS_CODE]}, Nombre: {row[CLASS_NAME]}, Nivel: {row[CLASS_LEVEL]}, Cupos disponibles: {row[CLASS_CAPACITY]}")

def ordenar_inscripciones_por_asistencias():
    """
    Objetivo: mostrar las inscripciones ordenadas de menor a mayor cantidad de asistencias.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra una copia ordenada de las inscripciones.
    """
    inscripciones_ordenadas = [fila[:] for fila in enrollments]
    n = len(inscripciones_ordenadas)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if inscripciones_ordenadas[j][ENR_ATTENDANCE] > inscripciones_ordenadas[j + 1][ENR_ATTENDANCE]:
                inscripciones_ordenadas[j], inscripciones_ordenadas[j + 1] = inscripciones_ordenadas[j + 1], inscripciones_ordenadas[j]

    print("INSCRIPCIONES ORDENADAS POR ASISTENCIAS (Burbujeo)")
    for row in inscripciones_ordenadas:
        print(f"Código: {row[ENR_CODE]}, Socio: {row[ENR_AFFILIATE_CODE]}, Clase: {row[ENR_CLASS_CODE]}, Asistencias: {row[ENR_ATTENDANCE]}, Estado: {row[ENR_STATUS]}")
