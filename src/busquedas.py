from datos import (
    classes,
    affiliates,
    CLASS_CODE,
    CLASS_NAME,
    CLASS_LEVEL,
    CLASS_CAPACITY,
    AFF_CODE,
    AFF_NAME,
    AFF_AGE,
    AFF_TYPE,
    get_type_name
)
from validaciones import pedir_entero

def buscar_clase_binaria():
    """
    Objetivo: buscar una clase por su código y mostrar sus datos.
    Parámetros: ninguno; solicita el código por teclado.
    Salida: no devuelve valores; muestra la clase encontrada o un mensaje de error.
    """
    print("BÚSQUEDA BINARIA DE CLASE POR CÓDIGO")
    codigo = pedir_entero("Ingrese el código de la clase a buscar: ", "Código inválido, ingrese un número.")

    codigos = [row[CLASS_CODE] for row in classes]
    nombres = [row[CLASS_NAME] for row in classes]
    niveles = [row[CLASS_LEVEL] for row in classes]
    capacidades = [row[CLASS_CAPACITY] for row in classes]

    n = len(codigos)
    for i in range(1, n):
        clave_codigo = codigos[i]
        clave_nombre = nombres[i]
        clave_nivel = niveles[i]
        clave_capacidad = capacidades[i]
        j = i - 1
        while j >= 0 and codigos[j] > clave_codigo:
            codigos[j + 1] = codigos[j]
            nombres[j + 1] = nombres[j]
            niveles[j + 1] = niveles[j]
            capacidades[j + 1] = capacidades[j]
            j -= 1
        codigos[j + 1] = clave_codigo
        nombres[j + 1] = clave_nombre
        niveles[j + 1] = clave_nivel
        capacidades[j + 1] = clave_capacidad

    inicio = 0
    fin = n - 1
    posicion = -1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if codigos[medio] == codigo:
            posicion = medio
            inicio = fin + 1
        elif codigos[medio] < codigo:
            inicio = medio + 1
        else:
            fin = medio - 1

    if posicion == -1:
        print("Clase no encontrada.")
    else:
        print(f"Clase encontrada:")
        print(f"Código: {codigos[posicion]}, Nombre: {nombres[posicion]}, Nivel: {niveles[posicion]}, Cupos disponibles: {capacidades[posicion]}")

def buscar_socio_secuencial():
    """
    Objetivo: buscar un socio por su código y mostrar sus datos.
    Parámetros: ninguno; solicita el código por teclado.
    Salida: no devuelve valores; muestra el socio encontrado o un mensaje de error.
    """
    print("BÚSQUEDA SECUENCIAL DE SOCIO POR CÓDIGO")
    codigo = pedir_entero("Ingrese el código del socio a buscar: ", "Código inválido, ingrese un número.")

    posicion = -1
    for i in range(len(affiliates)):
        if affiliates[i][AFF_CODE] == codigo:
            posicion = i

    if posicion == -1:
        print("Socio no encontrado.")
    else:
        print(f"Socio encontrado en posición {posicion}:")
        print(f"Código: {affiliates[posicion][AFF_CODE]}, Nombre: {affiliates[posicion][AFF_NAME]}, Edad: {affiliates[posicion][AFF_AGE]}, Tipo: {get_type_name(affiliates[posicion][AFF_TYPE])}")
