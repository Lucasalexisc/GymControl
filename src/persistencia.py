"""Persistencia de socios, clases e inscripciones en archivo JSON UTF-8."""
import json

from datos import (
    socios,
    clases,
    inscripciones,
    CLASE_HORARIO,
)

RUTA_DATOS_JSON = "datos_gimnasio.json"


def reconstruir_horario(horario):
    """Convierte la estructura leída desde JSON en una tupla inmutable ((dias...), inicio, fin)."""
    if not isinstance(horario, (list, tuple)) or len(horario) != 3:
        raise ValueError("Formato de horario inválido.")
    dias, hora_inicio, hora_fin = horario
    if not isinstance(dias, (list, tuple)) or len(dias) == 0:
        raise ValueError("Lista de días inválida.")
    dias_texto = []
    for dia in dias:
        dias_texto.append(str(dia))
    return (
        tuple(dias_texto),
        str(hora_inicio),
        str(hora_fin),
    )


def guardar_datos(ruta=None):
    """
    Objetivo: guardar las matrices de socios, clases e inscripciones en formato JSON.
    Parámetros: ruta opcional del archivo JSON; por defecto utiliza RUTA_DATOS_JSON.
    Salida: True si se guardó correctamente; False ante un error de escritura.
    """
    destino = RUTA_DATOS_JSON if ruta is None else ruta
    datos = {
        "socios": socios,
        "clases": clases,
        "inscripciones": inscripciones,
    }
    try:
        with open(destino, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
        return True
    except (OSError, TypeError):
        print("Aviso: no se pudieron guardar los datos en datos_gimnasio.json.")
        return False


def cargar_datos(ruta=None):
    """
    Objetivo: recuperar las matrices desde el archivo JSON y reconstruir las tuplas de horarios.
    Parámetros: ruta opcional del archivo JSON; por defecto utiliza RUTA_DATOS_JSON.
    Salida: True si los datos se cargaron o inicializaron correctamente; False ante error.
    """
    origen = RUTA_DATOS_JSON if ruta is None else ruta
    try:
        with open(origen, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
        if not isinstance(contenido, dict):
            raise ValueError("El archivo JSON debe contener un objeto raíz.")

        socios_cargados = contenido["socios"]
        clases_cargadas = contenido["clases"]
        inscripciones_cargadas = contenido["inscripciones"]

        if not (
            isinstance(socios_cargados, list)
            and isinstance(clases_cargadas, list)
            and isinstance(inscripciones_cargadas, list)
        ):
            raise ValueError("Las estructuras principales del JSON deben ser listas.")

        clases_reconstruidas = []
        for fila in clases_cargadas:
            if not isinstance(fila, list) or len(fila) != 5:
                raise ValueError("Fila de clase inválida en JSON.")
            fila_copia = fila[:]
            fila_copia[CLASE_HORARIO] = reconstruir_horario(fila_copia[CLASE_HORARIO])
            clases_reconstruidas.append(fila_copia)

        nuevos_socios = []
        for fila in socios_cargados:
            nuevos_socios.append(list(fila))

        nuevas_inscripciones = []
        for fila in inscripciones_cargadas:
            nuevas_inscripciones.append(list(fila))

        socios[:] = nuevos_socios
        clases[:] = clases_reconstruidas
        inscripciones[:] = nuevas_inscripciones
        return True
    except FileNotFoundError:
        return guardar_datos(origen)
    except (json.JSONDecodeError, KeyError, ValueError, TypeError, OSError, UnicodeError):
        print("Aviso: no se pudo cargar datos_gimnasio.json; se utilizarán los datos en memoria.")
        return False
