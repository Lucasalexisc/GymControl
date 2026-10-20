from auditoria import registrar_auditoria
from datos import (
inscripciones ,
clases ,
socios ,
CLASE_CODIGO ,
CLASE_NOMBRE ,
CLASE_CUPOS ,
SOCIO_NOMBRE ,
INSCRIPCION_CODIGO ,
INSCRIPCION_CODIGO_SOCIO ,
INSCRIPCION_CODIGO_CLASE ,
INSCRIPCION_ASISTENCIAS ,
INSCRIPCION_ESTADO
)
from validaciones import pedir_entero ,es_entero
from utilidades import (
buscar_posicion_clase ,
buscar_posicion_socio ,
buscar_posicion_inscripcion ,
existe_codigo_clase ,
existe_codigo_socio ,
socio_esta_inscripto_en_clase
)
from clases import listar_clases
from socios import listar_socios

def alta_inscripcion ():
    """
    Objetivo: registrar una inscripción activa para un socio en una clase con cupo disponible.
    Parámetros: ninguno; solicita los códigos de la clase y del socio por teclado.
    Salida: no devuelve valores; agrega la inscripción y descuenta un cupo de la clase.
    """
    listar_clases ()
    codigo_clase =pedir_entero ("Ingrese el código de la clase a la que desea inscribirse: ","por favor ingrese un código válido.")
    while not existe_codigo_clase (codigo_clase ):
        print ("por favor ingrese un código válido.")
        codigo_clase =pedir_entero ("Ingrese el código de la clase a la que desea inscribirse: ","por favor ingrese un código válido.")
    posicion_clase =buscar_posicion_clase (codigo_clase )
    if clases [posicion_clase ][CLASE_CUPOS ]<=0 :
        print ("No hay cupos disponibles para esa clase.")
        return
    listar_socios ()
    codigo_socio =pedir_entero ("Ingrese su código de afiliado: ","por favor ingrese un código de afiliado válido.")
    while not existe_codigo_socio (codigo_socio ):
        print ("por favor ingrese un código de afiliado válido.")
        codigo_socio =pedir_entero ("Ingrese su código de afiliado: ","por favor ingrese un código de afiliado válido.")
    if socio_esta_inscripto_en_clase (codigo_socio ,codigo_clase ):
        print ("ERROR: El afiliado ya se encuentra inscripto en esta clase.")
        return

    codigo =301 if len (inscripciones )==0 else inscripciones [-1 ][INSCRIPCION_CODIGO ]+1
    inscripciones .append ([codigo ,int (codigo_socio ),int (codigo_clase ),0 ,1 ])
    clases [posicion_clase ][CLASE_CUPOS ]-=1
    registrar_auditoria("ALTA_INSCRIPCION", f"Código={codigo}; socio={codigo_socio}; clase={codigo_clase}")
    print ("Inscripción realizada con éxito.")

def listar_inscripciones ():
    """
    Objetivo: mostrar los datos de todas las inscripciones registradas.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra la lista de inscripciones por pantalla.
    """
    print ("LISTA DE INSCRIPCIONES")
    print (f"{'Código':<10} {'Socio':<20} {'Clase':<20} {'Asistencias':<12} {'Estado'}")
    print ("-"*80 )
    for indice in range (len (inscripciones )):
        posicion_socio =buscar_posicion_socio (inscripciones [indice ][INSCRIPCION_CODIGO_SOCIO ])
        posicion_clase =buscar_posicion_clase (inscripciones [indice ][INSCRIPCION_CODIGO_CLASE ])
        nombre_socio =socios [posicion_socio ][SOCIO_NOMBRE ]if posicion_socio !=-1 else "Socio inexistente"
        nombre_clase =clases [posicion_clase ][CLASE_NOMBRE ]if posicion_clase !=-1 else "Clase inexistente"
        print (f"{inscripciones[indice][INSCRIPCION_CODIGO]:<10} {nombre_socio:<20} {nombre_clase:<20} {inscripciones[indice][INSCRIPCION_ASISTENCIAS]:<12} {'Activa' if inscripciones[indice][INSCRIPCION_ESTADO] == 1 else 'Inactiva'}")

def clases_de_socio (codigo_socio ):
    """
    Objetivo: obtener los nombres de las clases activas de un socio.
    Parámetros: codigo_socio, código del socio.
    Salida: lista con los nombres de las clases activas del socio.
    """
    posiciones =list (filter (
    lambda indice :inscripciones [indice ][INSCRIPCION_CODIGO_SOCIO ]==codigo_socio and inscripciones [indice ][INSCRIPCION_ESTADO ]==1 ,
    range (len (inscripciones ))
    ))
    nombre_clases =list (map (
    lambda indice :clases [buscar_posicion_clase (inscripciones [indice ][INSCRIPCION_CODIGO_CLASE ])][CLASE_NOMBRE ],
    posiciones
    ))
    return nombre_clases

def listar_clases_socio ():
    """
    Objetivo: mostrar las clases activas de un socio específico.
    Parámetros: ninguno; solicita el código del socio por teclado.
    Salida: no devuelve valores; muestra las clases o un mensaje informativo.
    """
    print ("Clases de un socio")
    codigo =pedir_entero ("Ingrese el codigo del socio: ","Codigo invalido, ingresar un numero")
    posicion =buscar_posicion_socio (codigo )
    if posicion ==-1 :
        print ("Error,socio no encontrado")
        return
    clases =clases_de_socio (codigo )
    if not clases :
        print ("El socio no tiene clases activas")
    else :
        print (f"El socio {socios[posicion][SOCIO_NOMBRE]} tiene las clases: {', '.join(clases)}")

def baja_inscripcion ():
    """
    Objetivo: finalizar una inscripción activa luego de solicitar confirmación.
    Parámetros: ninguno; solicita el código de la inscripción por teclado.
    Salida: no devuelve valores; actualiza el estado y libera un cupo de la clase.
    """
    print ("BAJA DE INSCRIPCIÓN")
    codigo =pedir_entero ("Ingrese el código de la inscripción a dar de baja: ","Código inválido, ingrese un número.")
    posicion =buscar_posicion_inscripcion (codigo )
    if posicion ==-1 :
        print ("Inscripción no encontrada.")
    elif inscripciones [posicion ][INSCRIPCION_ESTADO ]==2 :
        print ("La inscripción ya estaba finalizada.")
    else :
        posicion_socio =buscar_posicion_socio (inscripciones [posicion ][INSCRIPCION_CODIGO_SOCIO ])
        posicion_clase =buscar_posicion_clase (inscripciones [posicion ][INSCRIPCION_CODIGO_CLASE ])
        nombre_socio =socios [posicion_socio ][SOCIO_NOMBRE ]if posicion_socio !=-1 else "Socio inexistente"
        nombre_clase =clases [posicion_clase ][CLASE_NOMBRE ]if posicion_clase !=-1 else "Clase inexistente"
        confirmacion =input (f"¿Seguro que desea dar de baja la inscripción del socio '{nombre_socio}' en la clase '{nombre_clase}' ? (s/cantidad): ")
        if confirmacion .lower ()=="s":
            inscripciones [posicion ][INSCRIPCION_ESTADO ]=2
            if posicion_clase !=-1 :
                clases [posicion_clase ][CLASE_CUPOS ]+=1
            registrar_auditoria("BAJA_INSCRIPCION", f"Código={codigo}; finalizada")
            print ("Inscripción dada de baja.")
        else :
            print ("Operación cancelada.")

def modificar_inscripcion ():
    """
    Objetivo: modificar las asistencias o el estado de una inscripción existente.
    Parámetros: ninguno; solicita el código y los nuevos datos por teclado.
    Salida: no devuelve valores; actualiza la inscripción y los cupos de la clase.
    """
    print ("MODIFICAR INSCRIPCIÓN")
    codigo =pedir_entero ("Ingrese el código de la inscripción a modificar: ","Código inválido, ingrese un número.")
    posicion =buscar_posicion_inscripcion (codigo )
    if posicion ==-1 :
        print ("Inscripción no encontrada.")
        return

    posicion_clase =buscar_posicion_clase (inscripciones [posicion ][INSCRIPCION_CODIGO_CLASE ])
    posicion_socio =buscar_posicion_socio (inscripciones [posicion ][INSCRIPCION_CODIGO_SOCIO ])
    nombre_socio =socios [posicion_socio ][SOCIO_NOMBRE ]if posicion_socio !=-1 else "Socio inexistente"
    nombre_clase =clases [posicion_clase ][CLASE_NOMBRE ]if posicion_clase !=-1 else "Clase inexistente"
    print (f"Inscripción actual: Socio '{nombre_socio}', Clase '{nombre_clase}', Asistencias: {inscripciones[posicion][INSCRIPCION_ASISTENCIAS]}, Estado: {'Activa' if inscripciones[posicion][INSCRIPCION_ESTADO] == 1 else 'Inactiva'}")
    print ("1. Modificar solo asistencias")
    print ("2. Modificar solo estado")
    print ("3. Modificar asistencias y estado")
    print ("0. Cancelar")
    opcion =pedir_entero ("Seleccione una opción: ","Opción inválida, ingrese un número entre 0 y 3.",0 ,3 )
    if opcion ==0 :
        print ("Operación cancelada.")
        return

    inscripcion_anterior =inscripciones [posicion ][:]
    estado_anterior =inscripciones [posicion ][INSCRIPCION_ESTADO ]
    asistencias_actuales =inscripciones [posicion ][INSCRIPCION_ASISTENCIAS ]
    nuevo_estado =estado_anterior
    nuevas_asistencias =asistencias_actuales

    if opcion ==1 or opcion ==3 :
        nuevas_asistencias =pedir_entero ("Nuevas asistencias: ","ERROR, las asistencias deben ser un número mayor o igual a 0.",0 )
    if opcion ==2 or opcion ==3 :
        nuevo_estado =pedir_entero ("Nuevo estado (1-Activa, 2-Inactiva): ","ERROR, estado entre 1 y 2.",1 ,2 )

    if estado_anterior ==2 and nuevo_estado ==1 :
        if posicion_clase ==-1 :
            print ("No se puede activar porque la clase no existe.")
            return
        if clases [posicion_clase ][CLASE_CUPOS ]<=0 :
            print ("No hay cupos disponibles para activar esta inscripción.")
            return

    inscripciones [posicion ][INSCRIPCION_ASISTENCIAS ]=nuevas_asistencias
    inscripciones [posicion ][INSCRIPCION_ESTADO ]=nuevo_estado
    if estado_anterior ==1 and nuevo_estado ==2 and posicion_clase !=-1 :
        clases [posicion_clase ][CLASE_CUPOS ]+=1
    elif estado_anterior ==2 and nuevo_estado ==1 :
        clases [posicion_clase ][CLASE_CUPOS ]-=1

    if inscripcion_anterior !=inscripciones [posicion ]:
        registrar_auditoria("MODIFICACION_INSCRIPCION", f"Código={codigo}")
        print (f"Inscripción modificada: Socio '{nombre_socio}', Clase '{nombre_clase}', Asistencias: {nuevas_asistencias}, Estado: {'Activa' if nuevo_estado == 1 else 'Inactiva'}")
    else :
        print ("La inscripción no tuvo cambios.")
