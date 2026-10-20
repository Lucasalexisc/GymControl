from auditoria import mostrar_auditoria
from validaciones import es_entero
from clases import (
sumar_clase ,
eliminar_clase ,
modificar_clase ,
listar_clases
)
from socios import (
sumar_afiliados ,
eliminar_afiliados ,
modificar_socio ,
listar_socios
)
from inscripciones import (
alta_inscripcion ,
baja_inscripcion ,
modificar_inscripcion ,
listar_inscripciones ,
listar_clases_socio
)
from busquedas import (
buscar_clase_binaria ,
buscar_socio_secuencial
)
from ordenamientos import (
ordenar_socios_por_edad ,
ordenar_clases_por_nivel ,
ordenar_inscripciones_por_asistencias
)
from estadisticas import (
socios_por_clase ,
matriz_inscripciones_por_nivel_clase ,
total_asistencias_por_clase ,
matriz_socios_por_tipo_y_clase
)

# Menús de gestión
def pedir_opcion_clases ():
    """
    Objetivo: solicitar y validar una opción del menú de gestión de clases.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 4.
    """
    print ("--- GESTIÓN DE CLASES ---")
    print ("Opcion 1: Sumar clase")
    print ("Opcion 2: Eliminar clase")
    print ("Opcion 3: Modificar clase")
    print ("Opcion 4: Listar clases")
    print ("Opcion 0: Volver al menu principal")
    opcion_ingresada =input ("Ingrese una opción: ")
    while not es_entero (opcion_ingresada )or int (opcion_ingresada )<0 or int (opcion_ingresada )>4 :
        print ("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print ("Opcion 1: Sumar clase")
        print ("Opcion 2: Eliminar clase")
        print ("Opcion 3: Modificar clase")
        print ("Opcion 4: Listar clases")
        print ("Opcion 0: Volver al menu principal")
        opcion_ingresada =input ("Ingrese una opción: ")
    opcion =int (opcion_ingresada )
    return opcion

def menu_clases ():
    """
    Objetivo: ejecutar las opciones del menú de clases hasta que el usuario decida volver.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú de clases.
    """
    opcion =pedir_opcion_clases ()
    while opcion !=0 :
        if opcion ==1 :
            sumar_clase ()
        elif opcion ==2 :
            eliminar_clase ()
        elif opcion ==3 :
            modificar_clase ()
        elif opcion ==4 :
            listar_clases ()
        opcion =pedir_opcion_clases ()

def pedir_opcion_socios ():
    """
    Objetivo: solicitar y validar una opción del menú de gestión de socios.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 4.
    """
    print ("--- GESTIÓN DE AFILIADOS ---")
    print ("Opcion 1: sumar afiliado")
    print ("Opcion 2: eliminar afiliado")
    print ("Opcion 3: modificar afiliado")
    print ("Opcion 4: listar afiliados")
    print ("Opcion 0: Volver al menu principal")

    opcion_ingresada =input ("Ingrese una opción: ")

    while not es_entero (opcion_ingresada )or int (opcion_ingresada )<0 or int (opcion_ingresada )>4 :
        print ("La opción ingresada es errónea, por favor ingrese una opción válida.")

        print ("Opcion 1: sumar afiliado")
        print ("Opcion 2: eliminar afiliado")
        print ("Opcion 3: modificar afiliado")
        print ("Opcion 4: listar afiliados")
        print ("Opcion 0: Volver al menu principal")

        opcion_ingresada =input ("Ingrese una opción: ")
    opcion =int (opcion_ingresada )
    return opcion

def menu_socios ():
    """
    Objetivo: ejecutar las opciones del menú de socios hasta que el usuario decida volver.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú de socios.
    """
    opcion =pedir_opcion_socios ()
    while opcion !=0 :
        if opcion ==1 :
            sumar_afiliados ()
        elif opcion ==2 :
            eliminar_afiliados ()
        elif opcion ==3 :
            modificar_socio ()
        elif opcion ==4 :
            listar_socios ()
        opcion =pedir_opcion_socios ()

def pedir_opcion_inscripciones ():
    """
    Objetivo: solicitar y validar una opción del menú de gestión de inscripciones.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 5.
    """
    print ("--- GESTIÓN DE INSCRIPCIONES ---")
    print ("Opcion 1: Alta inscripción")
    print ("Opcion 2: Baja inscripción")
    print ("Opcion 3: Modificar inscripción")
    print ("Opcion 4: Listar inscripciones")
    print ("Opcion 5: Listar clases de un socio")
    print ("Opcion 0: Volver al menu principal")
    opcion_ingresada =input ("Ingrese una opción: ")
    while not es_entero (opcion_ingresada )or int (opcion_ingresada )<0 or int (opcion_ingresada )>5 :
        print ("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print ("Opcion 1: Alta inscripción")
        print ("Opcion 2: Baja inscripción")
        print ("Opcion 3: Modificar inscripción")
        print ("Opcion 4: Listar inscripciones")
        print ("Opcion 5: Listar clases de un socio")
        print ("Opcion 0: Volver al menu principal")
        opcion_ingresada =input ("Ingrese una opción: ")
    opcion =int (opcion_ingresada )
    return opcion

def menu_inscripciones ():
    """
    Objetivo: ejecutar las opciones del menú de inscripciones hasta que el usuario decida volver.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú de inscripciones.
    """
    opcion =pedir_opcion_inscripciones ()
    while opcion !=0 :
        if opcion ==1 :
            alta_inscripcion ()
        elif opcion ==2 :
            baja_inscripcion ()
        elif opcion ==3 :
            modificar_inscripcion ()
        elif opcion ==4 :
            listar_inscripciones ()
        elif opcion ==5 :
            listar_clases_socio ()
        opcion =pedir_opcion_inscripciones ()

        # Menús de búsquedas, ordenamientos y estadísticas
        # Las búsquedas requeridas por la consigna se aplican sobre códigos numéricos.
def menu_busqueda ():
    """
    Objetivo: solicitar y validar una opción del menú de búsquedas.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 2.
    """
    print ("--- MENÚ DE BÚSQUEDA ---")
    print ("Opción 1: Buscar clase por código (Binaria)")
    print ("Opción 2: Buscar socio por código (Secuencial)")
    print ("Opción 0: Volver al menú principal")
    opcion_ingresada =input ("Ingrese una opción: ")
    while not es_entero (opcion_ingresada )or int (opcion_ingresada )<0 or int (opcion_ingresada )>2 :
        print ("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print ("--- MENÚ DE BÚSQUEDA ---")
        print ("Opción 1: Buscar clase por código (Binaria)")
        print ("Opción 2: Buscar socio por código (Secuencial)")
        print ("Opción 0: Volver al menú principal")
        opcion_ingresada =input ("Ingrese una opción: ")
    return int (opcion_ingresada )

def opcion_menu_busqueda ():
    """
    Objetivo: ejecutar búsquedas hasta que el usuario decida volver al menú principal.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú de búsquedas.
    """
    opcion =menu_busqueda ()
    while opcion !=0 :
        if opcion ==1 :
            buscar_clase_binaria ()
        elif opcion ==2 :
            buscar_socio_secuencial ()
        opcion =menu_busqueda ()

def menu_ordenamiento ():
    """
    Objetivo: solicitar y validar una opción del menú de ordenamientos.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 3.
    """
    print ("--- MENÚ DE ORDENAMIENTO ---")
    print ("Opción 1: Ordenar socios por edad (Selección)")
    print ("Opción 2: Ordenar clases por nivel (Inserción)")
    print ("Opción 3: Ordenar inscripciones por asistencias (Burbujeo)")
    print ("Opción 0: Volver al menú principal")
    opcion_ingresada =input ("Ingrese una opción: ")
    while not es_entero (opcion_ingresada )or int (opcion_ingresada )<0 or int (opcion_ingresada )>3 :
        print ("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print ("--- MENÚ DE ORDENAMIENTO ---")
        print ("Opción 1: Ordenar socios por edad (Selección)")
        print ("Opción 2: Ordenar clases por nivel (Inserción)")
        print ("Opción 3: Ordenar inscripciones por asistencias (Burbujeo)")
        print ("Opción 0: Volver al menú principal")
        opcion_ingresada =input ("Ingrese una opción: ")
    return int (opcion_ingresada )

def opcion_menu_ordenamiento ():
    """
    Objetivo: ejecutar el ordenamiento elegido por el usuario.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra los datos ordenados según la opción elegida.
    """
    opcion =menu_ordenamiento ()
    if opcion ==1 :
        ordenar_socios_por_edad ()
    elif opcion ==2 :
        ordenar_clases_por_nivel ()
    elif opcion ==3 :
        ordenar_inscripciones_por_asistencias ()

def pedir_opcion_matriz ():
    """
    Objetivo: solicitar y validar una opción del menú de cálculos estadísticos.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 4.
    """
    print ("--- MENÚ DE CÁLCULOS ESTADÍSTICOS MATRICIALES ---")
    print ("Opción 1: Matriz de cantidad de afiliados por clase")
    print ("Opción 2: Matriz de cantidad de inscripciones por nivel de clase")
    print ("Opción 3: Total de asistencias por clase")
    print ("Opción 4: Matriz de cantidad de afiliados por tipo y clase")
    print ("Opción 0: Volver al menú principal")
    opcion_ingresada =input ("Ingrese una opción: ")
    while not es_entero (opcion_ingresada )or int (opcion_ingresada )<0 or int (opcion_ingresada )>4 :
        print ("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print ("--- MENÚ DE CÁLCULOS ESTADÍSTICOS MATRICIALES ---")
        print ("Opción 1: Matriz de cantidad de afiliados por clase")
        print ("Opción 2: Matriz de cantidad de inscripciones por nivel de clase")
        print ("Opción 3: Total de asistencias por clase")
        print ("Opción 4: Matriz de cantidad de afiliados por tipo y clase")
        print ("Opción 0: Volver al menú principal")
        opcion_ingresada =input ("Ingrese una opción: ")
    return int (opcion_ingresada )

def menu_matriz ():
    """
    Objetivo: ejecutar cálculos estadísticos hasta que el usuario decida volver.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo del menú estadístico.
    """
    opcion =pedir_opcion_matriz ()
    while opcion !=0 :
        if opcion ==1 :
            socios_por_clase ()
        elif opcion ==2 :
            matriz_inscripciones_por_nivel_clase ()
        elif opcion ==3 :
            total_asistencias_por_clase ()
        elif opcion ==4 :
            matriz_socios_por_tipo_y_clase ()
        opcion =pedir_opcion_matriz ()

def pedir_opcion_principal ():
    """
    Objetivo: solicitar y validar una opción del menú principal.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 7.
    """
    print ("--- MENU PRINCIPAL ---")
    print ("Opción 1: Gestión de afiliados")
    print ("Opción 2: Gestión de clases")
    print ("Opción 3: Gestión de inscripciones")
    print ("Opción 4: Ordenamiento")
    print ("Opción 5: Búsqueda")
    print ("Opción 6: Cálculos estadísticos matriciales")
    print ("Opción 7: Historial de auditoría")
    print ("Opción 0: Salir")
    opcion_ingresada =input ("Ingrese una opción: ")
    while not es_entero (opcion_ingresada )or int (opcion_ingresada )<0 or int (opcion_ingresada )>7 :
        print ("La opción ingresada es errónea, por favor ingrese una opción válida.")
        print ("--- MENU PRINCIPAL ---")
        print ("Opción 1: Gestión de afiliados")
        print ("Opción 2: Gestión de clases")
        print ("Opción 3: Gestión de inscripciones")
        print ("Opción 4: Ordenamiento")
        print ("Opción 5: Búsqueda")
        print ("Opción 6: Cálculos estadísticos matriciales")
        print ("Opción 7: Historial de auditoría")
        print ("Opción 0: Salir")
        opcion_ingresada =input ("Ingrese una opción: ")
    opcion =int (opcion_ingresada )
    return opcion

def menu_principal ():
    """
    Objetivo: ejecutar las opciones principales del sistema hasta que el usuario decida salir.
    Parámetros: ninguno.
    Salida: no devuelve valores; administra el flujo general del programa.
    """
    opcion =pedir_opcion_principal ()
    while opcion !=0 :
        if opcion ==1 :
            menu_socios ()
        elif opcion ==2 :
            menu_clases ()
        elif opcion ==3 :
            menu_inscripciones ()
        elif opcion ==4 :
            opcion_menu_ordenamiento ()
        elif opcion ==5 :
            opcion_menu_busqueda ()
        elif opcion ==6 :
            menu_matriz ()
        elif opcion ==7 :
            mostrar_auditoria ()
        opcion =pedir_opcion_principal ()
