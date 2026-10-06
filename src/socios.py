from datos import (
    affiliates,
    enrollments,
    AFF_NAME,
    AFF_CODE,
    AFF_AGE,
    AFF_TYPE,
    AFF_PHONE,
    ENR_AFFILIATE_CODE,
    ENR_CLASS_CODE,
    get_type_name
)
from validaciones import (
    es_entero,
    pedir_entero,
    es_telefono_valido
)
from utilidades import search_affiliate_position

# Gestión de socios ==> Este codigo habria que eliminarlo ya que no lo llaman en ninguna parte LC 2/9
def input_option():
    """
    Objetivo: solicitar y validar una opción del menú de gestión de socios.
    Parámetros: ninguno.
    Salida: opción elegida como número entero entre 0 y 4.
    """
    print("Opcion 1: sumar afiliado")
    print("Opcion 2: eliminar afiliado")
    print("Opcion 3: modificar afiliado")
    print("Opcion 4: listar afiliados")
    print("Opcion 0: salir")

    option = pedir_entero("Ingrese una opcion: ", "El dato ingresado es erroneo, por favor ingrese una opcion valida.", 0, 4)

    while option < 0 or option > 4:
        print("El dato ingresado es erroneo, por favor ingrese una opcion valida.")

        print("Opcion 1: sumar afiliado")
        print("Opcion 2: eliminar afiliado")
        print("Opcion 3: modificar afiliado")
        print("Opcion 4: listar afiliados")
        print("Opcion 0: salir")

        option = pedir_entero("Ingrese una opcion: ", "El dato ingresado es erroneo, por favor ingrese una opcion valida.", 0, 4)

    return option

def sumar_afiliados():
    """
    Objetivo: registrar un nuevo socio con código generado automáticamente.
    Parámetros: ninguno; solicita los datos del socio por teclado.
    Salida: no devuelve valores; agrega el socio a la matriz de afiliados.
    """
    print("SUMAR AFILIADO")
    nombre = input("Nombre completo: ")

    edad = input("Ingrese su edad: ")
    while not es_entero(edad) or int(edad) < 0 or int(edad) > 100:
        print("ERROR, se debe ingresar una edad entre 0 y 100")
        edad = input("Vuelva a ingresar su edad: ")

    affiliate_type = input("Ingrese su tipo (1-Mensual, 2-Libre, 3-Premium): ")
    while not es_entero(affiliate_type) or int(affiliate_type) < 1 or int(affiliate_type) > 3:
        print("ERROR, se debe ingresar un codigo entre 1 y 3")
        affiliate_type = input("Vuelva a ingresar su tipo (1-Mensual, 2-Libre, 3-Premium): ")

    telefono = input("Ingrese el teléfono (formato XX-XXXX-XXXX): ")
    while not es_telefono_valido(telefono):
        print("ERROR, el teléfono debe tener el formato XX-XXXX-XXXX")
        telefono = input("Vuelva a ingresar el teléfono: ")

    codigo = 101
    if len(affiliates) > 0:
        codigo = affiliates[-1][AFF_CODE] + 1

    affiliates.append([nombre, codigo, int(edad), int(affiliate_type), telefono])

    print(f"Socio '{nombre}' agregado con código {codigo}.")

def eliminar_afiliados():
    """
    Objetivo: eliminar un socio y sus inscripciones asociadas luego de solicitar confirmación.
    Parámetros: ninguno; solicita el código del socio por teclado.
    Salida: no devuelve valores; actualiza las matrices de afiliados e inscripciones.
    """
    print("BAJAR AFILIADO")
    codigo = pedir_entero("Ingrese el código del socio a eliminar: ", "Código inválido, ingrese un número.")
    pos = search_affiliate_position(codigo)
    if pos == -1:
        print("Socio no encontrado.")
    else:
        print(f"¿Seguro que desea eliminar a '{affiliates[pos][AFF_NAME]}' (teléfono: {affiliates[pos][AFF_PHONE]})? (s/n)")
        confirm = input()
        if confirm.lower() == "s":
            inscripciones_eliminadas = remove_enrollments_by_affiliate(codigo)
            affiliates.pop(pos)
            print("Socio eliminado.")
            if inscripciones_eliminadas > 0:
                print(f"Se eliminaron {inscripciones_eliminadas} inscripciones asociadas.")
        else:
            print("Operación cancelada.")

def remove_enrollment_at(position):
    """
    Objetivo: eliminar una inscripción ubicada en una posición determinada.
    Parámetros: position, posición de la inscripción que se desea eliminar.
    Salida: no devuelve valores; elimina una fila de la matriz de inscripciones.
    """
    enrollments.pop(position)

def remove_enrollments_by_affiliate(affiliate_code):
    """
    Objetivo: eliminar todas las inscripciones pertenecientes a un socio.
    Parámetros: affiliate_code, código del socio.
    Salida: cantidad de inscripciones eliminadas.
    """
    deleted_count = 0
    for i in range(len(enrollments) - 1, -1, -1):
        if enrollments[i][ENR_AFFILIATE_CODE] == affiliate_code:
            remove_enrollment_at(i)
            deleted_count += 1
    return deleted_count

def remove_enrollments_by_class(class_code):
    """
    Objetivo: eliminar todas las inscripciones pertenecientes a una clase.
    Parámetros: class_code, código de la clase.
    Salida: cantidad de inscripciones eliminadas.
    """
    deleted_count = 0
    for i in range(len(enrollments) - 1, -1, -1):
        if enrollments[i][ENR_CLASS_CODE] == class_code:
            remove_enrollment_at(i)
            deleted_count += 1
    return deleted_count

def modify_affiliate():
    """
    Objetivo: modificar afiliados, validando que el código exista y permitiendo
    modificar nombre, edad, tipo y teléfono.
    Parámetros: ninguno; solicita el código y los nuevos datos por teclado.
    Salida: no devuelve valores; actualiza la fila correspondiente de afiliados.
    """
    print("MODIFICAR AFILIADO")
    codigo = pedir_entero("Ingrese el código del socio a modificar: ", "Código inválido, ingrese un número.")
    pos = search_affiliate_position(codigo)
    if pos == -1:
        print("Socio no encontrado.")
    else:
        print(f"Socio actual: {affiliates[pos][AFF_NAME]}, {affiliates[pos][AFF_AGE]} años, {get_type_name(affiliates[pos][AFF_TYPE])}, teléfono: {affiliates[pos][AFF_PHONE]}")
        nombre = input(f"Nuevo nombre (si para mantener '{affiliates[pos][AFF_NAME]}'): ")
        if nombre != "si":
            affiliates[pos][AFF_NAME] = nombre
        edad = input(f"Nueva edad (si para mantener {affiliates[pos][AFF_AGE]}): ")
        if edad != "si":
            while not es_entero(edad) or int(edad) < 0 or int(edad) > 100:
                print("ERROR, se debe ingresar una edad entre 0 y 100")
                edad = input("Nueva edad: ")
            affiliates[pos][AFF_AGE] = int(edad)
        print("Tipos: 1-Mensual  2-Libre  3-Premium")
        type_code = input(f"Nuevo tipo (si para mantener {affiliates[pos][AFF_TYPE]}): ")
        if type_code != "si":
            while not es_entero(type_code) or int(type_code) < 1 or int(type_code) > 3:
                print("ERROR, se debe ingresar un codigo entre 1 y 3")
                type_code = input("Nuevo tipo: ")
            affiliates[pos][AFF_TYPE] = int(type_code)
        telefono = input(f"Nuevo teléfono (si para mantener '{affiliates[pos][AFF_PHONE]}', formato XX-XXXX-XXXX): ")
        if telefono != "si":
            while not es_telefono_valido(telefono):
                print("ERROR, el teléfono debe tener el formato XX-XXXX-XXXX")
                telefono = input("Nuevo teléfono: ")
            affiliates[pos][AFF_PHONE] = telefono
        print(f"Socio modificado: {affiliates[pos][AFF_NAME]}, {affiliates[pos][AFF_AGE]} años, {get_type_name(affiliates[pos][AFF_TYPE])}, teléfono: {affiliates[pos][AFF_PHONE]}")

def list_affiliates():
    """
    Objetivo: mostrar los datos de todos los socios registrados.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra la lista de socios por pantalla.
    """
    print("LISTA DE AFILIADOS")
    for i in range(len(affiliates)):
        print(f"Código: {affiliates[i][AFF_CODE]}, Nombre: {affiliates[i][AFF_NAME]}, Edad: {affiliates[i][AFF_AGE]}, Tipo: {get_type_name(affiliates[i][AFF_TYPE])}, Teléfono: {affiliates[i][AFF_PHONE]}")
