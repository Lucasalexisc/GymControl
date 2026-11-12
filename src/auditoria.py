"""Auditoría incremental en texto UTF-8, sin almacenar credenciales."""

RUTA_AUDITORIA = "auditoria.txt"
SESION_ACTUAL = {"usuario": "sin_sesion"}


def establecer_usuario(usuario):
    """Asocia las próximas operaciones con el usuario autenticado."""
    SESION_ACTUAL["usuario"] = usuario


def limpiar_campo(valor):
    """Evita que entradas del usuario creen líneas o columnas falsas."""
    return " ".join(str(valor).replace("|", "/").split())


def leer_auditoria(ruta=None):
    """Lee eventos válidos; devuelve None ante errores y [] si aún no existe."""
    origen = RUTA_AUDITORIA if ruta is None else ruta
    eventos = []
    try:
        with open(origen, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                campos = linea.rstrip("\n").split(" | ")
                if len(campos) != 4:
                    continue
                if not campos[0].strip():
                    continue
                eventos.append(campos)
    except FileNotFoundError:
        return []
    except (OSError, UnicodeError):
        print("Aviso: no se pudo leer auditoria.txt.")
        return None
    return eventos


def registrar_auditoria(operacion, detalle, usuario=None, ruta=None):
    """Agrega número de evento, usuario, operación y detalle. Devuelve éxito de escritura."""
    destino = RUTA_AUDITORIA if ruta is None else ruta
    eventos_previos = leer_auditoria(destino)
    numero_evento = 1 if not eventos_previos else len(eventos_previos) + 1
    identificador = f"EV-{numero_evento:04d}"
    usuario_evento = SESION_ACTUAL["usuario"] if usuario is None else usuario
    campos = [identificador, usuario_evento, operacion, detalle]

    campos_limpios = []
    for campo in campos:
        campos_limpios.append(limpiar_campo(campo))

    try:
        with open(destino, "a", encoding="utf-8") as archivo:
            archivo.write(" | ".join(campos_limpios) + "\n")
        return True
    except OSError:
        print("Aviso: no se pudo guardar el evento en auditoria.txt.")
        return False


def resumir_auditoria(eventos):
    """Cuenta los eventos por operación utilizando un diccionario."""
    resumen = {}
    for evento in eventos:
        operacion = evento[2]
        resumen[operacion] = resumen.get(operacion, 0) + 1
    return resumen


def mostrar_auditoria():
    """Muestra el historial persistido y la cantidad de cada operación."""
    eventos = leer_auditoria()
    if eventos is None:
        return
    print("--- HISTORIAL DE AUDITORÍA ---")
    if not eventos:
        print("No hay eventos registrados.")
        return
    for evento in eventos:
        print(" | ".join(evento))
    print("--- RESUMEN POR OPERACIÓN ---")
    resumen = resumir_auditoria(eventos)
    for operacion in sorted(resumen):
        print(f"{operacion}: {resumen[operacion]}")


def cerrar_sesion():
    """Registra el cierre y elimina la identidad de la sesión."""
    if SESION_ACTUAL["usuario"] != "sin_sesion":
        registrar_auditoria("CIERRE_SESION", "Fin de sesión")
    establecer_usuario("sin_sesion")
