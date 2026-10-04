import re
from datos import (
    classes,
    affiliates,
    enrollments,
    login_users,
    CLASS_CODE,
    AFF_CODE,
    LOGIN_USERNAME,
    ENR_CODE,
    ENR_AFFILIATE_CODE,
    ENR_CLASS_CODE,
    ENR_STATUS
)

def search_position(rows, condition):
    """
    Objetivo: encontrar la posición de la primera fila que cumpla una condición.
    Parámetros: rows, matriz donde buscar; condition, función que evalúa cada fila.
    Salida: posición de la fila o -1 si ninguna cumple la condición.
    """
    positions = list(filter(lambda i: condition(rows[i]), range(len(rows))))
    if len(positions) > 0:
        return positions[0]
    return -1

def search_class_position(code):
    """
    Objetivo: encontrar la posición de una clase a partir de su código.
    Parámetros: code, código de la clase buscada.
    Salida: posición de la clase o -1 si no existe.
    """
    return search_position(classes, lambda row: row[CLASS_CODE] == code)

def search_affiliate_position(code):
    """
    Objetivo: encontrar la posición de un socio a partir de su código.
    Parámetros: code, código del socio buscado.
    Salida: posición del socio o -1 si no existe.
    """
    return search_position(affiliates, lambda row: row[AFF_CODE] == code)

def search_user_position(username):
    """
    Objetivo: encontrar la posición de un usuario sin distinguir mayúsculas de minúsculas.
    Parámetros: username, nombre de usuario buscado.
    Salida: posición del usuario o -1 si no existe.
    """
    position = -1
    for i in range(len(login_users)):
        if re.fullmatch(login_users[i][LOGIN_USERNAME], username, re.IGNORECASE):
            position = i
    return position

def does_class_code_exist(code):
    """
    Objetivo: determinar si existe una clase con un código específico.
    Parámetros: code, código de la clase buscada.
    Salida: True si la clase existe; False en caso contrario.
    """
    for row in classes:
        if row[CLASS_CODE] == code:
            return True
    return False

def does_affiliate_code_exist(code):
    """
    Objetivo: determinar si existe un socio con un código específico.
    Parámetros: code, código del socio buscado.
    Salida: True si el socio existe; False en caso contrario.
    """
    for row in affiliates:
        if row[AFF_CODE] == code:
            return True
    return False

def is_affiliate_enrolled_in_class(affiliate_code, class_code):
    """
    Objetivo: determinar si un socio ya posee una inscripción activa en una clase utilizando lambda y filter.
    Parámetros: affiliate_code (int), class_code (int).
    Salida: True si el afiliado ya está inscripto activamente; False en caso contrario.
    """
    inscripciones_previas = list(filter(
        lambda enr: enr[ENR_AFFILIATE_CODE] == affiliate_code and enr[ENR_CLASS_CODE] == class_code and enr[ENR_STATUS] == 1,
        enrollments
    ))
    return len(inscripciones_previas) > 0

def search_inscription_position(code):
    """
    Objetivo: encontrar la posición de una inscripción a partir de su código.
    Parámetros: code, código de la inscripción buscada.
    Salida: posición de la inscripción o -1 si no existe.
    """
    position = -1
    for i in range(len(enrollments)):
        if enrollments[i][ENR_CODE] == code:
            position = i
    return position
