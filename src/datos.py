# Índices fijos para cada fila de la matriz
LOGIN_USERNAME, LOGIN_PASSWORD = 0, 1
AFF_NAME, AFF_CODE, AFF_AGE, AFF_TYPE, AFF_PHONE = 0, 1, 2, 3, 4
CLASS_CODE, CLASS_NAME, CLASS_LEVEL, CLASS_CAPACITY = 0, 1, 2, 3
ENR_CODE, ENR_AFFILIATE_CODE, ENR_CLASS_CODE, ENR_ATTENDANCE, ENR_STATUS = 0, 1, 2, 3, 4

# Estructuras matriciales
login_users = [
    ["admin", "admin1234"],
    ["recepcion1", "recep123"],
    ["recepcion2", "recep456"],
    ["profeyoga", "yoga2026"],
    ["profebox", "boxeo2026"],
    ["profezumba", "zumba2026"],
    ["coordinador", "coord123"],
    ["ventas1", "ventas123"],
    ["ventas2", "ventas456"],
    ["consulta", "consulta123"]
]

affiliates = [
    ["Juan Perez", 101, 28, 1, "11-2587-8779"],
    ["Maria Juana", 102, 32, 3, "11-3456-1028"],
    ["Rodriguez Pol", 103, 69, 2, "11-4678-2193"],
    ["Tambussi Fer", 104, 18, 1, "11-5789-3046"],
    ["Alejandro Esteban", 105, 65, 2, "11-6890-4175"],
    ["Sofia Diaz", 106, 22, 1, "11-7123-5684"],
    ["Camila Torres", 107, 45, 1, "11-8234-6795"],
    ["Joaquin parros", 108, 37, 1, "11-9345-7806"],
    ["Maria Anjoli", 109, 27, 3, "11-1467-8920"],
    ["Mateo retil", 110, 22, 3, "11-2578-9031"],
    ["Lucas Gomez", 111, 19, 2, "11-3689-0142"],
    ["julio", 112, 32, 3, "11-4790-1253"]
]

classes = [
    [201, "Yoga", 1, 15],
    [202, "Crossfit", 3, 10],
    [203, "Boxeo", 2, 15],
    [204, "Pilates", 1, 15],
    [205, "Musculacion", 2, 10],
    [206, "Spinning", 2, 12],
    [207, "Funcional", 3, 14],
    [208, "Zumba", 1, 20],
    [209, "Natacion", 2, 16],
    [210, "Stretching", 1, 18]
]

enrollments = [
    [301, 101, 205, 8, 1],
    [302, 102, 204, 3, 1],
    [303, 103, 201, 10, 2],
    [304, 104, 201, 2, 1],
    [305, 105, 201, 7, 1],
    [306, 106, 203, 10, 2],
    [307, 107, 203, 10, 2],
    [308, 108, 203, 10, 2],
    [309, 109, 205, 8, 1],
    [310, 110, 204, 5, 1],
    [311, 111, 201, 9, 1]
]

def get_level_name(level_code):
    """
    Objetivo: obtener el nombre correspondiente a un código de nivel de clase.
    Parámetros: level_code, código numérico del nivel.
    Salida: nombre del nivel o "Desconocido" si el código no es válido.
    """
    if level_code == 1:
        return "Principiante"
    elif level_code == 2:
        return "Intermedio"
    elif level_code == 3:
        return "Avanzado"
    else:
        return "Desconocido"

def get_type_name(type_code):
    """
    Objetivo: obtener el nombre correspondiente a un código de tipo de socio.
    Parámetros: type_code, código numérico del tipo de socio.
    Salida: nombre del tipo o "Desconocido" si el código no es válido.
    """
    if type_code == 1:
        return "Mensual"
    elif type_code == 2:
        return "Libre"
    elif type_code == 3:
        return "Premium"
    else:
        return "Desconocido"
