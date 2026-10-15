from datos import (
clases ,
CLASE_CODIGO ,
CLASE_NOMBRE ,
CLASE_NIVEL ,
CLASE_CUPOS ,
obtener_nombre_nivel
)
from validaciones import (
es_nombre_clase_valido ,
es_entero
)
from utilidades import buscar_posicion_clase
from socios import eliminar_inscripciones_por_clase

def sumar_clase ():
    """
    Objetivo: registrar una nueva clase con código generado automáticamente.
    Parámetros: ninguno; solicita el nombre, el nivel y la capacidad por teclado.
    Salida: no devuelve valores; agrega la clase a la matriz de clases.
    """
    print ("\nSUMAR CLASE")
    nombre =input ("Nombre de la clase: ").strip ()
    while not es_nombre_clase_valido (nombre ):
        print ("ERROR, ingrese una o más palabras formadas solamente por letras")
        nombre =input ("Nombre de la clase: ").strip ()

    nivel =input ("Nivel (1-Principiante, 2-Intermedio, 3-Avanzado): ")
    while not es_entero (nivel )or int (nivel )<1 or int (nivel )>3 :
        print ("ERROR, ingresar nivel entre 1 y 3")
        nivel =input ("Nivel (1-Principiante, 2-Intermedio, 3-Avanzado): ")
    nivel =int (nivel )

    capacidad =input ("Cupos disponibles: ")
    while not es_entero (capacidad )or int (capacidad )<1 :
        print ("ERROR, ingresar un número mayor a 0")
        capacidad =input ("Cupos disponibles: ")
    capacidad =int (capacidad )

    codigo =201 if len (clases )==0 else clases [-1 ][CLASE_CODIGO ]+1
    clases .append ([codigo ,nombre ,nivel ,capacidad ])

    print (f"Clase '{nombre}' agregada con código {codigo}.")

def eliminar_clase ():
    """
    Objetivo: eliminar una clase y sus inscripciones asociadas luego de solicitar confirmación.
    Parámetros: ninguno; solicita el código de la clase por teclado.
    Salida: no devuelve valores; actualiza las matrices de clases e inscripciones.
    """
    print ("\nELIMINAR CLASE")
    codigo =input ("Ingrese el código de la clase a eliminar: ")
    if not es_entero (codigo ):
        print ("Código inválido.")
        return
    posicion =buscar_posicion_clase (int (codigo ))
    if posicion ==-1 :
        print ("Clase no encontrada.")
    else :
        confirmacion =input (f"¿Seguro que desea eliminar la clase '{clases[posicion][CLASE_NOMBRE]}'? (s/cantidad): ")
        if confirmacion .lower ()=="s":
            codigo_clase =clases [posicion ][CLASE_CODIGO ]
            inscripciones_eliminadas =eliminar_inscripciones_por_clase (codigo_clase )
            clases .pop (posicion )
            print ("Clase eliminada.")
            if inscripciones_eliminadas >0 :
                print (f"Se eliminaron {inscripciones_eliminadas} inscripciones asociadas.")
        else :
            print ("Operación cancelada.")

def modificar_clase ():
    """
    Objetivo: modificar el nombre, el nivel o la capacidad de una clase existente.
    Parámetros: ninguno; solicita el código y los nuevos datos por teclado.
    Salida: no devuelve valores; actualiza la fila correspondiente de clases.
    """
    print ("MODIFICAR CLASE")
    codigo =input ("Ingrese el código de la clase a modificar: ")
    if not es_entero (codigo ):
        print ("Código inválido.")
        return
    posicion =buscar_posicion_clase (int (codigo ))
    if posicion ==-1 :
        print ("Clase no encontrada.")
    else :
        print (f"Clase actual: {clases[posicion][CLASE_NOMBRE]}, Nivel: {obtener_nombre_nivel(clases[posicion][CLASE_NIVEL])}, Cupos disponibles: {clases[posicion][CLASE_CUPOS]}")
        nombre =input (f"Nuevo nombre (si para mantener '{clases[posicion][CLASE_NOMBRE]}'): ").strip ()
        if nombre !="si":
            while not es_nombre_clase_valido (nombre ):
                print ("ERROR, ingrese una o más palabras formadas solamente por letras")
                nombre =input ("Nuevo nombre: ").strip ()
            clases [posicion ][CLASE_NOMBRE ]=nombre
        nivel =input (f"Nuevo nivel -1-Principiante 2-Intermedio 3-Avanzado- (si para mantener {obtener_nombre_nivel(clases[posicion][CLASE_NIVEL])}): ")
        if nivel !="si":
            while not es_entero (nivel )or int (nivel )<1 or int (nivel )>3 :
                print ("ERROR, nivel entre 1 y 3")
                nivel =input ("Nuevo nivel: ")
            clases [posicion ][CLASE_NIVEL ]=int (nivel )
        capacidad =input (f"Nuevos cupos disponibles (si para mantener {clases[posicion][CLASE_CUPOS]}): ")
        if capacidad !="si":
            while not es_entero (capacidad )or int (capacidad )<1 :
                print ("ERROR, ingresar un número mayor a 0")
                capacidad =input ("Nuevos cupos disponibles: ")
            clases [posicion ][CLASE_CUPOS ]=int (capacidad )
        print (f"Clase modificada: {clases[posicion][CLASE_NOMBRE]}, Nivel: {obtener_nombre_nivel(clases[posicion][CLASE_NIVEL])}, Cupos disponibles: {clases[posicion][CLASE_CUPOS]}")

def listar_clases ():
    """
    Objetivo: mostrar los datos de todas las clases registradas.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra la lista de clases por pantalla.
    """
    print ("LISTA DE CLASES")
    print (f"{'Código':<10} {'Nombre':<20} {'Nivel':<18} {'Cupos disponibles'}")
    print ("-"*58 )
    for indice in range (len (clases )):
        print (f"{clases[indice][CLASE_CODIGO]:<10} {clases[indice][CLASE_NOMBRE]:<20} {obtener_nombre_nivel(clases[indice][CLASE_NIVEL]):<18} {clases[indice][CLASE_CUPOS]}")
