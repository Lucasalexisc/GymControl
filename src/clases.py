from datos import (
    classes,
    CLASS_CODE,
    CLASS_NAME,
    CLASS_LEVEL,
    CLASS_CAPACITY,
    get_level_name
)
from validaciones import (
    es_nombre_clase_valido,
    es_entero
)
from utilidades import search_class_position
from socios import remove_enrollments_by_class

def sumar_clase():
    """
    Objetivo: registrar una nueva clase con código generado automáticamente.
    Parámetros: ninguno; solicita el nombre, el nivel y la capacidad por teclado.
    Salida: no devuelve valores; agrega la clase a la matriz de clases.
    """
    print("\nSUMAR CLASE")
    nombre = input("Nombre de la clase: ").strip()
    while not es_nombre_clase_valido(nombre):
        print("ERROR, ingrese una o más palabras formadas solamente por letras")
        nombre = input("Nombre de la clase: ").strip()

    nivel = input("Nivel (1-Principiante, 2-Intermedio, 3-Avanzado): ")
    while not es_entero(nivel) or int(nivel) < 1 or int(nivel) > 3:
        print("ERROR, ingresar nivel entre 1 y 3")
        nivel = input("Nivel (1-Principiante, 2-Intermedio, 3-Avanzado): ")
    nivel = int(nivel)

    capacidad = input("Cupos disponibles: ")
    while not es_entero(capacidad) or int(capacidad) < 1:
        print("ERROR, ingresar un número mayor a 0")
        capacidad = input("Cupos disponibles: ")
    capacidad = int(capacidad)

    codigo = 201 if len(classes) == 0 else classes[-1][CLASS_CODE] + 1
    classes.append([codigo, nombre, nivel, capacidad])

    print(f"Clase '{nombre}' agregada con código {codigo}.")

def eliminar_clase():
    """
    Objetivo: eliminar una clase y sus inscripciones asociadas luego de solicitar confirmación.
    Parámetros: ninguno; solicita el código de la clase por teclado.
    Salida: no devuelve valores; actualiza las matrices de clases e inscripciones.
    """
    print("\nELIMINAR CLASE")
    codigo = input("Ingrese el código de la clase a eliminar: ")
    if not es_entero(codigo):
        print("Código inválido.")
        return
    pos = search_class_position(int(codigo))
    if pos == -1:
        print("Clase no encontrada.")
    else:
        confirm = input(f"¿Seguro que desea eliminar la clase '{classes[pos][CLASS_NAME]}'? (s/n): ")
        if confirm.lower() == "s":
            class_code = classes[pos][CLASS_CODE]
            inscripciones_eliminadas = remove_enrollments_by_class(class_code)
            classes.pop(pos)
            print("Clase eliminada.")
            if inscripciones_eliminadas > 0:
                print(f"Se eliminaron {inscripciones_eliminadas} inscripciones asociadas.")
        else:
            print("Operación cancelada.")

def modify_clase():
    """
    Objetivo: modificar el nombre, el nivel o la capacidad de una clase existente.
    Parámetros: ninguno; solicita el código y los nuevos datos por teclado.
    Salida: no devuelve valores; actualiza la fila correspondiente de clases.
    """
    print("MODIFICAR CLASE")
    codigo = input("Ingrese el código de la clase a modificar: ")
    if not es_entero(codigo):
        print("Código inválido.")
        return
    pos = search_class_position(int(codigo))
    if pos == -1:
        print("Clase no encontrada.")
    else:
        print(f"Clase actual: {classes[pos][CLASS_NAME]}, Nivel: {get_level_name(classes[pos][CLASS_LEVEL])}, Cupos disponibles: {classes[pos][CLASS_CAPACITY]}")
        nombre = input(f"Nuevo nombre (si para mantener '{classes[pos][CLASS_NAME]}'): ").strip()
        if nombre != "si":
            while not es_nombre_clase_valido(nombre):
                print("ERROR, ingrese una o más palabras formadas solamente por letras")
                nombre = input("Nuevo nombre: ").strip()
            classes[pos][CLASS_NAME] = nombre
        nivel = input(f"Nuevo nivel -1-Principiante 2-Intermedio 3-Avanzado- (si para mantener {get_level_name(classes[pos][CLASS_LEVEL])}): ")
        if nivel != "si":
            while not es_entero(nivel) or int(nivel) < 1 or int(nivel) > 3:
                print("ERROR, nivel entre 1 y 3")
                nivel = input("Nuevo nivel: ")
            classes[pos][CLASS_LEVEL] = int(nivel)
        capacidad = input(f"Nuevos cupos disponibles (si para mantener {classes[pos][CLASS_CAPACITY]}): ")
        if capacidad != "si":
            while not es_entero(capacidad) or int(capacidad) < 1:
                print("ERROR, ingresar un número mayor a 0")
                capacidad = input("Nuevos cupos disponibles: ")
            classes[pos][CLASS_CAPACITY] = int(capacidad)
        print(f"Clase modificada: {classes[pos][CLASS_NAME]}, Nivel: {get_level_name(classes[pos][CLASS_LEVEL])}, Cupos disponibles: {classes[pos][CLASS_CAPACITY]}")

def list_clases():
    """
    Objetivo: mostrar los datos de todas las clases registradas.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra la lista de clases por pantalla.
    """
    print("LISTA DE CLASES")
    print(f"{'Código':<10} {'Nombre':<20} {'Nivel':<18} {'Cupos disponibles'}")
    print("-" * 58)
    for i in range(len(classes)):
        print(f"{classes[i][CLASS_CODE]:<10} {classes[i][CLASS_NAME]:<20} {get_level_name(classes[i][CLASS_LEVEL]):<18} {classes[i][CLASS_CAPACITY]}")
