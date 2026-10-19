"""Auditoría incremental en texto UTF-8, sin almacenar credenciales."""
from datetime import datetime
from pathlib import Path

RUTA_AUDITORIA = Path(__file__).resolve().parent.parent / "auditoria.txt"
usuario_actual = "sin_sesion"


def establecer_usuario(usuario):
    """Asocia las próximas operaciones con el usuario autenticado."""
    global usuario_actual
    usuario_actual = usuario


def limpiar_campo(valor):
    """Evita que entradas del usuario creen líneas o columnas falsas."""
    return " ".join(str(valor).replace("|", "/").split())


def registrar_auditoria(operacion, detalle, usuario=None):
    """Agrega fecha, usuario, operación y detalle. Devuelve éxito de escritura."""
    fecha = datetime.now().astimezone().isoformat(timespec="seconds")
    campos = [fecha, usuario_actual if usuario is None else usuario, operacion, detalle]
    try:
        with RUTA_AUDITORIA.open("a", encoding="utf-8") as archivo:
            archivo.write(" | ".join(limpiar_campo(campo) for campo in campos) + "\n")
        return True
    except OSError:
        print("Aviso: no se pudo guardar el evento en auditoria.txt.")
        return False


def leer_auditoria():
    """Lee eventos válidos; devuelve None ante errores y [] si aún no existe."""
    eventos = []
    try:
        with RUTA_AUDITORIA.open(encoding="utf-8") as archivo:
            for linea in archivo:
                campos = linea.rstrip("\n").split(" | ")
                if len(campos) != 4:
                    continue
                try:
                    datetime.fromisoformat(campos[0])
                except ValueError:
                    continue
                eventos.append(campos)
    except FileNotFoundError:
        return []
    except (OSError, UnicodeError):
        print("Aviso: no se pudo leer auditoria.txt.")
        return None
    return eventos


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
    for operacion, cantidad in sorted(resumir_auditoria(eventos).items()):
        print(f"{operacion}: {cantidad}")


def cerrar_sesion():
    """Registra el cierre y elimina la identidad de la sesión."""
    if usuario_actual != "sin_sesion":
        registrar_auditoria("CIERRE_SESION", "Fin de sesión")
    establecer_usuario("sin_sesion")
