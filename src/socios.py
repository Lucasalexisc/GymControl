from datos import (
socios ,
inscripciones ,
SOCIO_NOMBRE ,
SOCIO_CODIGO ,
SOCIO_EDAD ,
SOCIO_TIPO ,
SOCIO_TELEFONO ,
INSCRIPCION_CODIGO_SOCIO ,
INSCRIPCION_CODIGO_CLASE ,
INSCRIPCION_ESTADO ,
CLASE_CODIGO ,
CLASE_CUPOS ,
clases ,
obtener_nombre_tipo
)
from validaciones import (
es_entero ,
pedir_entero ,
es_telefono_valido
)
from utilidades import buscar_posicion_socio ,buscar_posicion

# Gestión de socios ==> Este codigo habria que eliminarlo ya que no lo llaman en ninguna parte LC 2/9
def pedir_opcion ():
    """
    Objetivo: solicitar y validar una opción del menú de gestión de socios.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 4.
    """
    print ("Opcion 1: sumar afiliado")
    print ("Opcion 2: eliminar afiliado")
    print ("Opcion 3: modificar afiliado")
    print ("Opcion 4: listar afiliados")
    print ("Opcion 0: salir")

    opcion =pedir_entero ("Ingrese una opcion: ","El dato ingresado es erroneo, por favor ingrese una opcion valida.",0 ,4 )

    while opcion <0 or opcion >4 :
        print ("El dato ingresado es erroneo, por favor ingrese una opcion valida.")

        print ("Opcion 1: sumar afiliado")
        print ("Opcion 2: eliminar afiliado")
        print ("Opcion 3: modificar afiliado")
        print ("Opcion 4: listar afiliados")
        print ("Opcion 0: salir")

        opcion =pedir_entero ("Ingrese una opcion: ","El dato ingresado es erroneo, por favor ingrese una opcion valida.",0 ,4 )

    return opcion

def sumar_afiliados ():
    """
    Objetivo: registrar un nuevo socio con código generado automáticamente.
    Parámetros: ninguno; solicita los datos del socio por teclado.
    Salida: no devuelve valores; agrega el socio a la matriz de afiliados.
    """
    print ("SUMAR AFILIADO")
    nombre =input ("Nombre completo: ")

    edad =input ("Ingrese su edad: ")
    while not es_entero (edad )or int (edad )<0 or int (edad )>100 :
        print ("ERROR, se debe ingresar una edad entre 0 y 100")
        edad =input ("Vuelva a ingresar su edad: ")

    tipo_socio =input ("Ingrese su tipo (1-Mensual, 2-Libre, 3-Premium): ")
    while not es_entero (tipo_socio )or int (tipo_socio )<1 or int (tipo_socio )>3 :
        print ("ERROR, se debe ingresar un codigo entre 1 y 3")
        tipo_socio =input ("Vuelva a ingresar su tipo (1-Mensual, 2-Libre, 3-Premium): ")

    telefono =input ("Ingrese el teléfono (formato XX-XXXX-XXXX): ")
    while not es_telefono_valido (telefono ):
        print ("ERROR, el teléfono debe tener el formato XX-XXXX-XXXX")
        telefono =input ("Vuelva a ingresar el teléfono: ")

    codigo =101
    if len (socios )>0 :
        codigo =socios [-1 ][SOCIO_CODIGO ]+1

    socios .append ([nombre ,codigo ,int (edad ),int (tipo_socio ),telefono ])

    print (f"Socio '{nombre}' agregado con código {codigo}.")

def eliminar_afiliados ():
    """
    Objetivo: eliminar un socio y sus inscripciones asociadas, liberando el cupo de las clases con inscripción activa, luego de solicitar confirmación.
    Parámetros: ninguno; solicita el código del socio por teclado.
    Salida: no devuelve valores; actualiza las matrices de afiliados, inscripciones y clases.
    """
    print ("BAJAR AFILIADO")
    codigo =pedir_entero ("Ingrese el código del socio a eliminar: ","Código inválido, ingrese un número.")
    posicion =buscar_posicion_socio (codigo )
    if posicion ==-1 :
        print ("Socio no encontrado.")
    else :
        print (f"¿Seguro que desea eliminar a '{socios[posicion][SOCIO_NOMBRE]}' (teléfono: {socios[posicion][SOCIO_TELEFONO]})? (s/cantidad)")
        confirmacion =input ()
        if confirmacion .lower ()=="s":
            cupos_liberados =liberar_cupos_de_afiliado (codigo ,inscripciones ,clases )
            inscripciones_eliminadas =eliminar_inscripciones_por_socio (codigo )
            socios .pop (posicion )
            print ("Socio eliminado.")
            if inscripciones_eliminadas >0 :
                print (f"Se eliminaron {inscripciones_eliminadas} inscripciones asociadas.")
            if cupos_liberados >0 :
                print (f"Se liberaron {cupos_liberados} cupos en las clases correspondientes.")
        else :
            print ("Operación cancelada.")

def eliminar_inscripcion_en_posicion (posicion ):
    """
    Objetivo: eliminar una inscripción ubicada en una posición determinada.
    Parámetros: posicion, posición de la inscripción que se desea eliminar.
    Salida: no devuelve valores; elimina una fila de la matriz de inscripciones.
    """
    inscripciones .pop (posicion )

def eliminar_inscripciones_por_socio (codigo_socio ):
    """
    Objetivo: eliminar todas las inscripciones pertenecientes a un socio.
    Parámetros: codigo_socio, código del socio.
    Salida: cantidad de inscripciones eliminadas.
    """
    cantidad_eliminada =0
    for indice in range (len (inscripciones )-1 ,-1 ,-1 ):
        if inscripciones [indice ][INSCRIPCION_CODIGO_SOCIO ]==codigo_socio :
            eliminar_inscripcion_en_posicion (indice )
            cantidad_eliminada +=1
    return cantidad_eliminada

def liberar_cupos_de_afiliado (codigo_afiliado ,inscripciones ,clases ):
    """
    Objetivo: devolver un cupo a cada clase en la que el socio tiene una inscripción activa.
    Parámetros: codigo_afiliado, código del socio; inscripciones, matriz de inscripciones; clases, matriz de clases.
    Salida: cantidad de cupos liberados.
    """
    cupos_liberados =0
    for inscripcion in inscripciones :
        if inscripcion [INSCRIPCION_CODIGO_SOCIO ]==codigo_afiliado and inscripcion [INSCRIPCION_ESTADO ]==1 :
            codigo_clase =inscripcion [INSCRIPCION_CODIGO_CLASE ]
            posicion_clase =buscar_posicion (clases ,lambda fila :fila [CLASE_CODIGO ]==codigo_clase )
            if posicion_clase !=-1 :
                clases [posicion_clase ][CLASE_CUPOS ]+=1
                cupos_liberados +=1
    return cupos_liberados

def eliminar_inscripciones_por_clase (codigo_clase ):
    """
    Objetivo: eliminar todas las inscripciones pertenecientes a una clase.
    Parámetros: codigo_clase, código de la clase.
    Salida: cantidad de inscripciones eliminadas.
    """
    cantidad_eliminada =0
    for indice in range (len (inscripciones )-1 ,-1 ,-1 ):
        if inscripciones [indice ][INSCRIPCION_CODIGO_CLASE ]==codigo_clase :
            eliminar_inscripcion_en_posicion (indice )
            cantidad_eliminada +=1
    return cantidad_eliminada

def modificar_socio ():
    """
    Objetivo: modificar afiliados, validando que el código exista y permitiendo
    modificar nombre, edad, tipo y teléfono.
    Parámetros: ninguno; solicita el código y los nuevos datos por teclado.
    Salida: no devuelve valores; actualiza la fila correspondiente de afiliados.
    """
    print ("MODIFICAR AFILIADO")
    codigo =pedir_entero ("Ingrese el código del socio a modificar: ","Código inválido, ingrese un número.")
    posicion =buscar_posicion_socio (codigo )
    if posicion ==-1 :
        print ("Socio no encontrado.")
    else :
        print (f"Socio actual: {socios[posicion][SOCIO_NOMBRE]}, {socios[posicion][SOCIO_EDAD]} años, {obtener_nombre_tipo(socios[posicion][SOCIO_TIPO])}, teléfono: {socios[posicion][SOCIO_TELEFONO]}")
        nombre =input (f"Nuevo nombre (si para mantener '{socios[posicion][SOCIO_NOMBRE]}'): ")
        if nombre !="si":
            socios [posicion ][SOCIO_NOMBRE ]=nombre
        edad =input (f"Nueva edad (si para mantener {socios[posicion][SOCIO_EDAD]}): ")
        if edad !="si":
            while not es_entero (edad )or int (edad )<0 or int (edad )>100 :
                print ("ERROR, se debe ingresar una edad entre 0 y 100")
                edad =input ("Nueva edad: ")
            socios [posicion ][SOCIO_EDAD ]=int (edad )
        print ("Tipos: 1-Mensual  2-Libre  3-Premium")
        codigo_tipo =input (f"Nuevo tipo (si para mantener {socios[posicion][SOCIO_TIPO]}): ")
        if codigo_tipo !="si":
            while not es_entero (codigo_tipo )or int (codigo_tipo )<1 or int (codigo_tipo )>3 :
                print ("ERROR, se debe ingresar un codigo entre 1 y 3")
                codigo_tipo =input ("Nuevo tipo: ")
            socios [posicion ][SOCIO_TIPO ]=int (codigo_tipo )
        telefono =input (f"Nuevo teléfono (si para mantener '{socios[posicion][SOCIO_TELEFONO]}', formato XX-XXXX-XXXX): ")
        if telefono !="si":
            while not es_telefono_valido (telefono ):
                print ("ERROR, el teléfono debe tener el formato XX-XXXX-XXXX")
                telefono =input ("Nuevo teléfono: ")
            socios [posicion ][SOCIO_TELEFONO ]=telefono
        print (f"Socio modificado: {socios[posicion][SOCIO_NOMBRE]}, {socios[posicion][SOCIO_EDAD]} años, {obtener_nombre_tipo(socios[posicion][SOCIO_TIPO])}, teléfono: {socios[posicion][SOCIO_TELEFONO]}")

def listar_socios ():
    """
    Objetivo: mostrar los datos de todos los socios registrados.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra la lista de socios por pantalla.
    """
    print ("LISTA DE AFILIADOS")
    for indice in range (len (socios )):
        print (f"Código: {socios[indice][SOCIO_CODIGO]}, Nombre: {socios[indice][SOCIO_NOMBRE]}, Edad: {socios[indice][SOCIO_EDAD]}, Tipo: {obtener_nombre_tipo(socios[indice][SOCIO_TIPO])}, Teléfono: {socios[indice][SOCIO_TELEFONO]}")
