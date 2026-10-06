from validaciones import es_entero
from clases import (
    sumar_clase,
    eliminar_clase,
    modify_clase,
    list_clases
)
from socios import (
    sumar_afiliados,
    eliminar_afiliados,
    modify_affiliate,
    list_affiliates
)
from inscripciones import (
    alta_inscripcion,
    baja_inscripcion,
    modify_inscripcion,
    list_inscripciones,
    listar_clases_socio
)
from busquedas import (
    buscar_clase_binaria,
    buscar_socio_secuencial
)
from ordenamientos import (
    ordenar_socios_por_edad,
    ordenar_clases_por_nivel,
    ordenar_inscripciones_por_asistencias
)
from estadisticas import (
    affiliates_by_class,
    enrollment_by_class_level_matrix,
    total_attendances_by_class,
    affiliates_by_type_and_class_matrix
)

# Menús de gestión
def input_clases_option():
    """
    Objetivo: solicitar y validar una opción del menú de gestión de clases.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 4.
    """
    print("--- GESTIÓN DE CLASES ---")
    print("Opcion 1: Sumar clase")
    print("Opcion 2: Eliminar clase")
    print("Opcion 3: Modificar clase")
    print("Opcion 4: Listar clases")
    print("Opcion 0: Volver al menu principal")
    raw_option = input("Ingrese una opción: ")
    while not es_entero(raw_option) or int(raw_option) < 0 or int(raw_option) > 4:
        print("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print("Opcion 1: Sumar clase")
        print("Opcion 2: Eliminar clase")
        print("Opcion 3: Modificar clase")
        print("Opcion 4: Listar clases")
        print("Opcion 0: Volver al menu principal")
        raw_option = input("Ingrese una opción: ")
    option = int(raw_option)
    return option

def clases_menu():
    """
    Objetivo: ejecutar las opciones del menú de clases hasta que el usuario decida volver.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú de clases.
    """
    option = input_clases_option()
    while option != 0:
        if option == 1:
            sumar_clase()
        elif option == 2:
            eliminar_clase()
        elif option == 3:
            modify_clase()
        elif option == 4:
            list_clases()
        option = input_clases_option()

def input_affiliate_option():
    """
    Objetivo: solicitar y validar una opción del menú de gestión de socios.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 4.
    """
    print("--- GESTIÓN DE AFILIADOS ---")
    print("Opcion 1: sumar afiliado")
    print("Opcion 2: eliminar afiliado")
    print("Opcion 3: modificar afiliado")
    print("Opcion 4: listar afiliados")
    print("Opcion 0: Volver al menu principal")

    raw_option = input("Ingrese una opción: ")

    while not es_entero(raw_option) or int(raw_option) < 0 or int(raw_option) > 4:
        print("La opción ingresada es errónea, por favor ingrese una opción válida.")

        print("Opcion 1: sumar afiliado")
        print("Opcion 2: eliminar afiliado")
        print("Opcion 3: modificar afiliado")
        print("Opcion 4: listar afiliados")
        print("Opcion 0: Volver al menu principal")

        raw_option = input("Ingrese una opción: ")
    option = int(raw_option)
    return option

def affiliate_menu():
    """
    Objetivo: ejecutar las opciones del menú de socios hasta que el usuario decida volver.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú de socios.
    """
    option = input_affiliate_option()
    while option != 0:
        if option == 1:
            sumar_afiliados()
        elif option == 2:
            eliminar_afiliados()
        elif option == 3:
            modify_affiliate()
        elif option == 4:
            list_affiliates()
        option = input_affiliate_option()

def input_inscription_option():
    """
    Objetivo: solicitar y validar una opción del menú de gestión de inscripciones.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 5.
    """
    print("--- GESTIÓN DE INSCRIPCIONES ---")
    print("Opcion 1: Alta inscripción")
    print("Opcion 2: Baja inscripción")
    print("Opcion 3: Modificar inscripción")
    print("Opcion 4: Listar inscripciones")
    print("Opcion 5: Listar clases de un socio")
    print("Opcion 0: Volver al menu principal")
    raw_option = input("Ingrese una opción: ")
    while not es_entero(raw_option) or int(raw_option) < 0 or int(raw_option) > 5:
        print("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print("Opcion 1: Alta inscripción")
        print("Opcion 2: Baja inscripción")
        print("Opcion 3: Modificar inscripción")
        print("Opcion 4: Listar inscripciones")
        print("Opcion 5: Listar clases de un socio")
        print("Opcion 0: Volver al menu principal")
        raw_option = input("Ingrese una opción: ")
    option = int(raw_option)
    return option

def inscription_menu():
    """
    Objetivo: ejecutar las opciones del menú de inscripciones hasta que el usuario decida volver.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú de inscripciones.
    """
    option = input_inscription_option()
    while option != 0:
        if option == 1:
            alta_inscripcion()
        elif option == 2:
            baja_inscripcion()
        elif option == 3:
            modify_inscripcion()
        elif option == 4:
            list_inscripciones()
        elif option == 5: 
            listar_clases_socio()
        option = input_inscription_option()

# Menús de búsquedas, ordenamientos y estadísticas
# Las búsquedas requeridas por la consigna se aplican sobre códigos numéricos.
def menu_busqueda():
    """
    Objetivo: solicitar y validar una opción del menú de búsquedas.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 2.
    """
    print("--- MENÚ DE BÚSQUEDA ---")
    print("Opción 1: Buscar clase por código (Binaria)")
    print("Opción 2: Buscar socio por código (Secuencial)")
    print("Opción 0: Volver al menú principal")
    raw_option = input("Ingrese una opción: ")
    while not es_entero(raw_option) or int(raw_option) < 0 or int(raw_option) > 2:
        print("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print("--- MENÚ DE BÚSQUEDA ---")
        print("Opción 1: Buscar clase por código (Binaria)")
        print("Opción 2: Buscar socio por código (Secuencial)")
        print("Opción 0: Volver al menú principal")
        raw_option = input("Ingrese una opción: ")
    return int(raw_option)

def opcion_menu_busqueda():
    """
    Objetivo: ejecutar búsquedas hasta que el usuario decida volver al menú principal.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú de búsquedas.
    """
    option = menu_busqueda()
    while option != 0:
        if option == 1:
            buscar_clase_binaria()
        elif option == 2:
            buscar_socio_secuencial()
        option = menu_busqueda()

def menu_ordenamiento():
    """
    Objetivo: solicitar y validar una opción del menú de ordenamientos.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 3.
    """
    print("--- MENÚ DE ORDENAMIENTO ---")
    print("Opción 1: Ordenar socios por edad (Selección)")
    print("Opción 2: Ordenar clases por nivel (Inserción)")
    print("Opción 3: Ordenar inscripciones por asistencias (Burbujeo)")
    print("Opción 0: Volver al menú principal")
    raw_option = input("Ingrese una opción: ")
    while not es_entero(raw_option) or int(raw_option) < 0 or int(raw_option) > 3:
        print("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print("--- MENÚ DE ORDENAMIENTO ---")
        print("Opción 1: Ordenar socios por edad (Selección)")
        print("Opción 2: Ordenar clases por nivel (Inserción)")
        print("Opción 3: Ordenar inscripciones por asistencias (Burbujeo)")
        print("Opción 0: Volver al menú principal")
        raw_option = input("Ingrese una opción: ")
    return int(raw_option)

def opcion_menu_ordenamiento():
    """
    Objetivo: ejecutar el ordenamiento elegido por el usuario.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra los datos ordenados según la opción elegida.
    """
    option = menu_ordenamiento()
    if option == 1:
        ordenar_socios_por_edad()
    elif option == 2:
        ordenar_clases_por_nivel()
    elif option == 3:
        ordenar_inscripciones_por_asistencias()

def input_matrix_option():
    """
    Objetivo: solicitar y validar una opción del menú de cálculos estadísticos.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 4.
    """
    print("--- MENÚ DE CÁLCULOS ESTADÍSTICOS MATRICIALES ---")
    print("Opción 1: Matriz de cantidad de afiliados por clase")
    print("Opción 2: Matriz de cantidad de inscripciones por nivel de clase")
    print("Opción 3: Total de asistencias por clase")
    print("Opción 4: Matriz de cantidad de afiliados por tipo y clase")
    print("Opción 0: Volver al menú principal")
    rawOption = input("Ingrese una opción: ")
    while not es_entero(rawOption) or int(rawOption) < 0 or int(rawOption) > 4:
        print("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print("--- MENÚ DE CÁLCULOS ESTADÍSTICOS MATRICIALES ---")
        print("Opción 1: Matriz de cantidad de afiliados por clase")
        print("Opción 2: Matriz de cantidad de inscripciones por nivel de clase")
        print("Opción 3: Total de asistencias por clase")
        print("Opción 4: Matriz de cantidad de afiliados por tipo y clase")
        print("Opción 0: Volver al menú principal")
        rawOption = input("Ingrese una opción: ")
    return int(rawOption)

def matrix_menu():
    """
    Objetivo: ejecutar cálculos estadísticos hasta que el usuario decida volver.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú estadístico.
    """
    option = input_matrix_option()
    while option != 0:
        if option == 1:
            affiliates_by_class()
        elif option == 2:
            enrollment_by_class_level_matrix()
        elif option == 3:
            total_attendances_by_class()
        elif option == 4:
            affiliates_by_type_and_class_matrix()
        option = input_matrix_option()

def input_main_option():
    """
    Objetivo: solicitar y validar una opción del menú principal.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 6.
    """
    print("--- MENU PRINCIPAL ---")
    print("Opción 1: Gestión de afiliados")
    print("Opción 2: Gestión de clases")
    print("Opción 3: Gestión de inscripciones")
    print("Opción 4: Ordenamiento")
    print("Opción 5: Búsqueda")
    print("Opción 6: Cálculos estadísticos matriciales")
    print("Opción 0: Salir")
    raw_option = input("Ingrese una opción: ")
    while not es_entero(raw_option) or int(raw_option) < 0 or int(raw_option) > 6:
        print("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print("--- MENU PRINCIPAL ---")
        print("Opción 1: Gestión de afiliados")
        print("Opción 2: Gestión de clases")
        print("Opción 3: Gestión de inscripciones")
        print("Opción 4: Ordenamiento")
        print("Opción 5: Búsqueda")
        print("Opción 6: Cálculos estadísticos matriciales")
        print("Opción 0: Salir")
        raw_option = input("Ingrese una opción: ")
    option = int(raw_option)
    return option

def main_menu():
    """
    Objetivo: ejecutar las opciones principales del sistema hasta que el usuario decida salir.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo general del programa.
    """
    option = input_main_option()
    while option != 0:
        if option == 1:
            affiliate_menu()
        elif option == 2:
            clases_menu()
        elif option == 3:
            inscription_menu()
        elif option == 4:
            opcion_menu_ordenamiento()
        elif option == 5:
            opcion_menu_busqueda()
        elif option == 6:
            matrix_menu()
        option = input_main_option()
