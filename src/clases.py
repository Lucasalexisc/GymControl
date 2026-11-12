from auditoria import registrar_auditoria
from persistencia import guardar_datos

from datos import (
    clases,
    CLASE_CODIGO,
    CLASE_NOMBRE,
    CLASE_NIVEL,
    CLASE_CUPOS,
    CLASE_HORARIO,
    obtener_nombre_nivel,
)
from validaciones import (
    es_nombre_clase_valido,
    pedir_entero,
)
from utilidades import buscar_posicion_clase
from socios import eliminar_inscripciones_por_clase

DIAS_SEMANA = {
    "lunes": "Lunes",
    "martes": "Martes",
    "miercoles": "Miércoles",
    "jueves": "Jueves",
    "viernes": "Viernes",
    "sabado": "Sábado",
    "domingo": "Domingo",
}


def normalizar_dia(dia):
    dia_normalizado = dia.strip().casefold()
    return (
        dia_normalizado
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
    )


def son_dias_validos(dias_ingresados):
    if not dias_ingresados:
        return False
    partes = dias_ingresados.split(",")
    for dia in partes:
        if normalizar_dia(dia) not in DIAS_SEMANA:
            return False
    return True


def es_hora_valida(hora):
    partes = hora.split(":")
    if len(partes) != 2:
        return False
    if not partes[0].isdigit() or not partes[1].isdigit():
        return False
    horas = int(partes[0])
    minutos = int(partes[1])
    return 0 <= horas <= 23 and 0 <= minutos <= 59


def hora_a_minutos(hora):
    partes = hora.split(":")
    horas = int(partes[0])
    minutos = int(partes[1])
    return horas * 60 + minutos


def pedir_horario():
    """Solicita un bloque horario y devuelve una tupla inmutable."""
    dias_ingresados = input("Días de cursada separados por coma: ").strip()
    while not son_dias_validos(dias_ingresados):
        print("ERROR, ingrese uno o más días de la semana válidos, separados por coma.")
        dias_ingresados = input("Días de cursada separados por coma: ").strip()

    lista_dias = []
    for dia in dias_ingresados.split(","):
        lista_dias.append(DIAS_SEMANA[normalizar_dia(dia)])
    dias = tuple(lista_dias)

    hora_inicio = input("Hora de inicio (HH:MM): ").strip()
    while not es_hora_valida(hora_inicio):
        print("ERROR, ingrese una hora válida en formato HH:MM.")
        hora_inicio = input("Hora de inicio (HH:MM): ").strip()

    hora_fin = input("Hora de fin (HH:MM): ").strip()
    while not es_hora_valida(hora_fin) or hora_a_minutos(hora_fin) <= hora_a_minutos(hora_inicio):
        print("ERROR, ingrese una hora posterior a la de inicio en formato HH:MM.")
        hora_fin = input("Hora de fin (HH:MM): ").strip()

    return (dias, hora_inicio, hora_fin)


def formatear_horario(horario):
    """Convierte el bloque horario en un texto apto para mostrar."""
    dias, hora_inicio, hora_fin = horario
    return f"{', '.join(dias)} | {hora_inicio} a {hora_fin}"


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

    nivel = pedir_entero("Nivel (1-Principiante, 2-Intermedio, 3-Avanzado): ", "ERROR, ingresar nivel entre 1 y 3", 1, 3)
    capacidad = pedir_entero("Cupos disponibles: ", "ERROR, ingresar un número mayor a 0", 1)
    horario = pedir_horario()

    codigo = 201 if len(clases) == 0 else clases[-1][CLASE_CODIGO] + 1
    clases.append([codigo, nombre, nivel, capacidad, horario])

    guardar_datos()
    registrar_auditoria("ALTA_CLASE", f"Código={codigo}")
    print(f"Clase '{nombre}' agregada con código {codigo}.")


def eliminar_clase():
    """
    Objetivo: eliminar una clase y sus inscripciones asociadas luego de solicitar confirmación.
    Parámetros: ninguno; solicita el código de la clase por teclado.
    Salida: no devuelve valores; actualiza las matrices de clases e inscripciones.
    """
    print("\nELIMINAR CLASE")
    codigo = pedir_entero("Ingrese el código de la clase a eliminar: ", "Código inválido, ingrese un número.")
    posicion = buscar_posicion_clase(codigo)
    if posicion == -1:
        print("Clase no encontrada.")
    else:
        confirmacion = input(f"¿Seguro que desea eliminar la clase '{clases[posicion][CLASE_NOMBRE]}'? (s/n): ")
        if confirmacion.lower() == "s":
            codigo_clase = clases[posicion][CLASE_CODIGO]
            inscripciones_eliminadas = eliminar_inscripciones_por_clase(codigo_clase)
            clases.pop(posicion)
            guardar_datos()
            registrar_auditoria("BAJA_CLASE", f"Código={codigo_clase}; inscripciones eliminadas={inscripciones_eliminadas}")
            print("Clase eliminada.")
            if inscripciones_eliminadas > 0:
                print(f"Se eliminaron {inscripciones_eliminadas} inscripciones asociadas.")
        else:
            print("Operación cancelada.")


def modificar_clase():
    """
    Objetivo: modificar un atributo de una clase por vez mediante un submenú.
    Parámetros: ninguno; solicita el código de la clase y la opción a modificar.
    Salida: no devuelve valores; actualiza el atributo elegido de la clase.
    """
    print("MODIFICAR CLASE")
    codigo = pedir_entero("Ingrese el código de la clase a modificar: ", "Código inválido, ingrese un número.")
    posicion = buscar_posicion_clase(codigo)
    if posicion == -1:
        print("Clase no encontrada.")
    else:
        clase_anterior = clases[posicion][:]
        opcion = -1
        while opcion != 0:
            print(f"\nClase: {clases[posicion][CLASE_NOMBRE]} | Nivel: {obtener_nombre_nivel(clases[posicion][CLASE_NIVEL])} | Cupos: {clases[posicion][CLASE_CUPOS]} | Horario: {formatear_horario(clases[posicion][CLASE_HORARIO])}")
            print("1. Modificar nombre")
            print("2. Modificar nivel")
            print("3. Modificar cupos")
            print("4. Modificar horario")
            print("0. Salir")
            opcion = pedir_entero("Seleccione el atributo a modificar: ", "Opción inválida.", 0, 4)

            if opcion == 1:
                nombre = input("Nuevo nombre: ").strip()
                while not es_nombre_clase_valido(nombre):
                    print("ERROR, ingrese una o más palabras formadas solamente por letras")
                    nombre = input("Nuevo nombre: ").strip()
                clases[posicion][CLASE_NOMBRE] = nombre
            elif opcion == 2:
                nivel = pedir_entero("Nuevo nivel (1-Principiante, 2-Intermedio, 3-Avanzado): ", "ERROR, nivel entre 1 y 3", 1, 3)
                clases[posicion][CLASE_NIVEL] = nivel
            elif opcion == 3:
                capacidad = pedir_entero("Nuevos cupos disponibles: ", "ERROR, ingrese un número mayor a 0", 1)
                clases[posicion][CLASE_CUPOS] = capacidad
            elif opcion == 4:
                clases[posicion][CLASE_HORARIO] = pedir_horario()

            if opcion != 0:
                print("Atributo modificado correctamente.")
        if clase_anterior != clases[posicion]:
            guardar_datos()
            registrar_auditoria("MODIFICACION_CLASE", f"Código={codigo}")


def listar_clases():
    """
    Objetivo: mostrar los datos de todas las clases registradas.
    Parámetros: ninguno.
    Salida: no devuelve valores; muestra la lista de clases por pantalla.
    """
    print("LISTA DE CLASES")
    print(f"{'Código':<10} {'Nombre':<20} {'Nivel':<18} {'Cupos':<8} {'Horario'}")
    print("-" * 90)
    for indice in range(len(clases)):
        print(f"{clases[indice][CLASE_CODIGO]:<10} {clases[indice][CLASE_NOMBRE]:<20} {obtener_nombre_nivel(clases[indice][CLASE_NIVEL]):<18} {clases[indice][CLASE_CUPOS]:<8} {formatear_horario(clases[indice][CLASE_HORARIO])}")
