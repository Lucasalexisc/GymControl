import re

def es_entero(valor):
    """
    Objetivo: determinar si un valor puede convertirse en un número entero.
    Parámetros: valor, dato que se desea validar.
    Salida: True si el valor es convertible a entero; False en caso contrario.
    """
    try:
        valor = int(valor)
        res = True
    except:
        res = False
    return res

def es_flotante(valor):
    """
    Objetivo: determinar si un valor puede convertirse en un número decimal.
    Parámetros: valor, dato que se desea validar.
    Salida: True si el valor es convertible a decimal; False en caso contrario.
    """
    try:
        valor = float(valor)
        res = True
    except:
        res = False
    return res

def es_string(valor):
    """
    Objetivo: determinar si un valor puede convertirse en una cadena de caracteres.
    Parámetros: valor, dato que se desea validar.
    Salida: True si el valor es convertible a cadena; False en caso contrario.
    """
    try:
        valor = str(valor)
        res = True
    except:
        res = False
    return res

def es_nombre_clase_valido(nombre):
    """
    Objetivo: validar que un nombre de clase contenga únicamente letras sin espacios.
    Parámetros: nombre, cadena que se desea validar.
    Salida: coincidencia encontrada si el nombre es válido; None en caso contrario.
    """
    return re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", nombre) ## Agrego tildes y espacios 

def pedir_entero(mensaje, mensaje_error="El dato ingresado debe ser numérico.", minimo=None, maximo=None):
    """
    Objetivo: solicitar un número entero hasta que cumpla las condiciones indicadas.
    Parámetros: mensaje, texto de solicitud; mensaje_error, aviso de error; minimo y maximo, límites opcionales.
    Salida: número entero validado.
    """
    valor = input(mensaje)
    while not es_entero(valor) or (minimo is not None and int(valor) < minimo) or (maximo is not None and int(valor) > maximo):
        print(mensaje_error)
        valor = input(mensaje)
    return int(valor)

def es_telefono_valido(telefono):
    """
    Objetivo: Valida teléfonos en formato XX-XXXX-XXXX, por ejemplo 11-2587-8779.
    Parámetros: teléfono a validar.
    Salida: flag booleana indicando si el teléfono es válido.
    """
    return re.fullmatch(r"\d{2}-\d{4}-\d{4}", telefono) is not None
