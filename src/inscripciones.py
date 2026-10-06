from datos import (
    enrollments,
    classes,
    affiliates,
    CLASS_CODE,
    CLASS_NAME,
    CLASS_CAPACITY,
    AFF_NAME,
    ENR_CODE,
    ENR_AFFILIATE_CODE,
    ENR_CLASS_CODE,
    ENR_ATTENDANCE,
    ENR_STATUS
)
from validaciones import pedir_entero, es_entero
from utilidades import (
    search_class_position,
    search_affiliate_position,
    search_inscription_position,
    does_class_code_exist,
    does_affiliate_code_exist,
    is_affiliate_enrolled_in_class
)
from clases import list_clases
from socios import list_affiliates

def alta_inscripcion():
    """
    Objetivo: registrar una inscripción activa para un socio en una clase con cupo disponible.
    Parámetros: ninguno; solicita los códigos de la clase y del socio por teclado.
    Salida: no devuelve valores; agrega la inscripción y descuenta un cupo de la clase.
    """
    list_clases()
    class_code = pedir_entero("Ingrese el código de la clase a la que desea inscribirse: ", "por favor ingrese un código válido.")
    while not does_class_code_exist(class_code):
        print("por favor ingrese un código válido.")
        class_code = pedir_entero("Ingrese el código de la clase a la que desea inscribirse: ", "por favor ingrese un código válido.")
    class_pos = search_class_position(class_code)
    if classes[class_pos][CLASS_CAPACITY] <= 0:
        print("No hay cupos disponibles para esa clase.")
        return
    list_affiliates()
    affiliate_code = pedir_entero("Ingrese su código de afiliado: ", "por favor ingrese un código de afiliado válido.")
    while not does_affiliate_code_exist(affiliate_code):
        print("por favor ingrese un código de afiliado válido.")
        affiliate_code = pedir_entero("Ingrese su código de afiliado: ", "por favor ingrese un código de afiliado válido.")
    if is_affiliate_enrolled_in_class(affiliate_code, class_code):
        print("ERROR: El afiliado ya se encuentra inscripto en esta clase.")
        return
    
    codigo = 301 if len(enrollments) == 0 else enrollments[-1][ENR_CODE] + 1
    enrollments.append([codigo, int(affiliate_code), int(class_code), 0, 1])
    classes[class_pos][CLASS_CAPACITY] -= 1
    print("Inscripción realizada con éxito.")

def list_inscripciones():
    """
    Objetivo: mostrar los datos de todas las inscripciones registradas.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra la lista de inscripciones por pantalla.
    """
    print("LISTA DE INSCRIPCIONES")
    print(f"{'Código':<10} {'Socio':<20} {'Clase':<20} {'Asistencias':<12} {'Estado'}")
    print("-" * 80)
    for i in range(len(enrollments)):
        affiliate_pos = search_affiliate_position(enrollments[i][ENR_AFFILIATE_CODE])
        class_pos = search_class_position(enrollments[i][ENR_CLASS_CODE])
        affiliate_name = affiliates[affiliate_pos][AFF_NAME] if affiliate_pos != -1 else "Socio inexistente"
        class_name = classes[class_pos][CLASS_NAME] if class_pos != -1 else "Clase inexistente"
        print(f"{enrollments[i][ENR_CODE]:<10} {affiliate_name:<20} {class_name:<20} {enrollments[i][ENR_ATTENDANCE]:<12} {'Activa' if enrollments[i][ENR_STATUS] == 1 else 'Inactiva'}")

def clases_de_socio(affiliate_code): 
    """
    Objetivo: obtener los nombres de las clases activas de un socio.
    Parámetros: affiliate_code, código del socio.
    Salida: lista con los nombres de las clases activas del socio.
    """
    posiciones = list(filter(
        lambda i: enrollments[i][ENR_AFFILIATE_CODE] == affiliate_code and enrollments[i][ENR_STATUS] == 1,
        range(len(enrollments))
    ))
    nombre_clases = list(map(
        lambda i: classes[search_class_position(enrollments[i][ENR_CLASS_CODE])][CLASS_NAME],
        posiciones
    ))
    return nombre_clases

def listar_clases_socio():
    """
    Objetivo: mostrar las clases activas de un socio específico.
    Parámetros: ninguno; solicita el código del socio por teclado.
    Salida: no devuelve valores; muestra las clases o un mensaje informativo.
    """
    print("Clases de un socio")
    codigo = pedir_entero("Ingrese el codigo del socio: ","Codigo invalido, ingresar un numero")
    pos = search_affiliate_position(codigo)
    if pos == -1:
        print("Error,socio no encontrado")
        return
    clases = clases_de_socio(codigo)
    if not clases:
        print("El socio no tiene clases activas")
    else:
        print(f"El socio {affiliates[pos][AFF_NAME]} tiene las clases: {', '.join(clases)}")

def baja_inscripcion():
    """
    Objetivo: finalizar una inscripción activa luego de solicitar confirmación.
    Parámetros: ninguno; solicita el código de la inscripción por teclado.
    Salida: no devuelve valores; actualiza el estado y libera un cupo de la clase.
    """
    print("BAJA DE INSCRIPCIÓN")
    codigo = pedir_entero("Ingrese el código de la inscripción a dar de baja: ", "Código inválido, ingrese un número.")
    pos = search_inscription_position(codigo)
    if pos == -1:
        print("Inscripción no encontrada.")
    elif enrollments[pos][ENR_STATUS] == 2:
        print("La inscripción ya estaba finalizada.")
    else:
        affiliate_pos = search_affiliate_position(enrollments[pos][ENR_AFFILIATE_CODE])
        class_pos = search_class_position(enrollments[pos][ENR_CLASS_CODE])
        affiliate_name = affiliates[affiliate_pos][AFF_NAME] if affiliate_pos != -1 else "Socio inexistente"
        class_name = classes[class_pos][CLASS_NAME] if class_pos != -1 else "Clase inexistente"
        confirm = input(f"¿Seguro que desea dar de baja la inscripción del socio '{affiliate_name}' en la clase '{class_name}' ? (s/n): ")
        if confirm.lower() == "s":
            enrollments[pos][ENR_STATUS] = 2
            if class_pos != -1:
                classes[class_pos][CLASS_CAPACITY] += 1
            print("Inscripción dada de baja.")
        else:
            print("Operación cancelada.")

def modify_inscripcion():
    """
    Objetivo: modificar las asistencias o el estado de una inscripción existente.
    Parámetros: ninguno; solicita el código y los nuevos datos por teclado.
    Salida: no devuelve valores; actualiza la inscripción y los cupos de la clase.
    """
    print("MODIFICAR INSCRIPCIÓN")
    codigo = pedir_entero("Ingrese el código de la inscripción a modificar: ", "Código inválido, ingrese un número.")
    pos = search_inscription_position(codigo)
    if pos == -1:
        print("Inscripción no encontrada.")
    else:
        estado_anterior = enrollments[pos][ENR_STATUS]
        class_pos = search_class_position(enrollments[pos][ENR_CLASS_CODE])
        affiliate_pos = search_affiliate_position(enrollments[pos][ENR_AFFILIATE_CODE])
        affiliate_name = affiliates[affiliate_pos][AFF_NAME] if affiliate_pos != -1 else "Socio inexistente"
        class_name = classes[class_pos][CLASS_NAME] if class_pos != -1 else "Clase inexistente"
        print(f"Inscripción actual: Socio '{affiliate_name}', Clase '{class_name}', Asistencias: {enrollments[pos][ENR_ATTENDANCE]}, Estado: {'Activa' if enrollments[pos][ENR_STATUS] == 1 else 'Inactiva'}")
        asistencias = input(f"Nuevas asistencias (si para mantener {enrollments[pos][ENR_ATTENDANCE]}): ")
        if asistencias != "si":
            while not es_entero(asistencias) or int(asistencias) < 0:
                print("ERROR, las asistencias deben ser un número mayor o igual a 0")
                asistencias = input("Nuevas asistencias: ")
            enrollments[pos][ENR_ATTENDANCE] = int(asistencias)
        estado = input(f"Nuevo estado -1-Activa 2-Inactiva- (si para mantener {'Activa' if enrollments[pos][ENR_STATUS] == 1 else 'Inactiva'}): ")
        if estado != "si":
            while not es_entero(estado) or int(estado) < 1 or int(estado) > 2:
                print("ERROR, estado entre 1 y 2")
                estado = input("Nuevo estado: ")
            nuevo_estado = int(estado)
            if estado_anterior == 1 and nuevo_estado == 2:
                enrollments[pos][ENR_STATUS] = nuevo_estado
                if class_pos != -1:
                    classes[class_pos][CLASS_CAPACITY] += 1
            elif estado_anterior == 2 and nuevo_estado == 1:
                if class_pos == -1:
                    print("No se puede activar porque la clase no existe.")
                elif classes[class_pos][CLASS_CAPACITY] <= 0:
                    print("No hay cupos disponibles para activar esta inscripción.")
                else:
                    enrollments[pos][ENR_STATUS] = nuevo_estado
                    classes[class_pos][CLASS_CAPACITY] -= 1
            else:
                enrollments[pos][ENR_STATUS] = nuevo_estado
        affiliate_pos = search_affiliate_position(enrollments[pos][ENR_AFFILIATE_CODE])
        class_pos = search_class_position(enrollments[pos][ENR_CLASS_CODE])
        affiliate_name = affiliates[affiliate_pos][AFF_NAME] if affiliate_pos != -1 else "Socio inexistente"
        class_name = classes[class_pos][CLASS_NAME] if class_pos != -1 else "Clase inexistente"
        print(f"Inscripción modificada: Socio '{affiliate_name}', Clase '{class_name}', Asistencias: {enrollments[pos][ENR_ATTENDANCE]}, Estado: {'Activa' if enrollments[pos][ENR_STATUS] == 1 else 'Inactiva'}")
