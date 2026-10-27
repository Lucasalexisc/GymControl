"""Pruebas funcionales sin clases propias. No modifican la auditoría del gimnasio."""
import builtins
import contextlib
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))
import auditoria
import login


def ejecutar_login(respuestas):
    entradas = iter(respuestas)
    entrada_original = builtins.input
    builtins.input = lambda mensaje="": next(entradas)
    try:
        return login.iniciar_sesion()
    finally:
        builtins.input = entrada_original


def prueba_archivo_inexistente():
    assert auditoria.leer_auditoria() == []


def prueba_escritura_acumulativa():
    auditoria.establecer_usuario("admin")
    assert auditoria.registrar_auditoria("ALTA_SOCIO", "Código=113")
    assert auditoria.registrar_auditoria("BAJA_SOCIO", "Código=113")
    eventos = auditoria.leer_auditoria()
    assert len(eventos) == 2
    assert eventos[0][1:] == ["admin", "ALTA_SOCIO", "Código=113"]
    assert eventos[1][2] == "BAJA_SOCIO"
    assert auditoria.resumir_auditoria(eventos) == {"ALTA_SOCIO": 1, "BAJA_SOCIO": 1}


def prueba_separadores_y_saltos():
    assert auditoria.registrar_auditoria("ALTA|SOCIO", "uno\ndos\rtres", usuario=" a | b ")
    eventos = auditoria.leer_auditoria()
    assert len(eventos) == 1
    assert eventos[0][1:] == ["a / b", "ALTA/SOCIO", "uno dos tres"]


def prueba_lineas_invalidas():
    with open(auditoria.RUTA_AUDITORIA, "w", encoding="utf-8") as archivo:
        archivo.write("incompleta\nfecha inválida | admin | ALTA | dato\n")
    assert auditoria.registrar_auditoria("ALTA_SOCIO", "Código=113")
    assert len(auditoria.leer_auditoria()) == 1


def prueba_utf8_invalido():
    with open(auditoria.RUTA_AUDITORIA, "wb") as archivo:
        archivo.write(b"\xff")
    assert auditoria.leer_auditoria() is None


def prueba_errores_archivo():
    # Abrir un directorio como archivo falla también cuando el proceso tiene permisos elevados.
    auditoria.RUTA_AUDITORIA = os.path.dirname(auditoria.RUTA_AUDITORIA)
    assert auditoria.registrar_auditoria("ALTA_SOCIO", "Código=113") is False
    assert auditoria.leer_auditoria() is None


def prueba_contrasena_y_secreto():
    assert ejecutar_login(["1", " ADMIN ", "admin1234"]) is True
    assert auditoria.usuario_actual == "admin"
    eventos = auditoria.leer_auditoria()
    assert eventos[0][2] == "ACCESO_EXITOSO"
    with open(auditoria.RUTA_AUDITORIA, encoding="utf-8") as archivo:
        assert "admin1234" not in archivo.read()


def prueba_pregunta_y_secreto():
    assert ejecutar_login(["2", "admin", "  AZUL  "]) is True
    with open(auditoria.RUTA_AUDITORIA, encoding="utf-8") as archivo:
        assert "azul" not in archivo.read().casefold()


def prueba_reintentos_y_cambio_metodo():
    respuestas = ["1", "admin", "incorrecta"] * 4 + ["2", "admin", "azul"]
    assert ejecutar_login(respuestas) is True
    assert auditoria.resumir_auditoria(auditoria.leer_auditoria()) == {
        "ACCESO_FALLIDO": 4, "ACCESO_EXITOSO": 1,
    }


def prueba_usuario_inexistente_y_cancelacion():
    assert ejecutar_login(["opcion inválida", "2", "inexistente", "0"]) is False
    assert auditoria.usuario_actual == "sin_sesion"
    assert auditoria.resumir_auditoria(auditoria.leer_auditoria()) == {
        "ACCESO_FALLIDO": 1, "ACCESO_CANCELADO": 1,
    }


def prueba_cierre_unico():
    auditoria.establecer_usuario("admin")
    auditoria.cerrar_sesion()
    auditoria.cerrar_sesion()
    assert auditoria.usuario_actual == "sin_sesion"
    eventos = auditoria.leer_auditoria()
    assert len(eventos) == 1 and eventos[0][1:3] == ["admin", "CIERRE_SESION"]


def prueba_ruta_desde_otro_directorio():
    # El hijo importa desde otra carpeta: la ruta debe seguir apuntando a la raíz del proyecto.
    codigo = "import sys; sys.path.insert(0, sys.argv[1]); import auditoria; print(auditoria.RUTA_AUDITORIA)"
    resultado = subprocess.run(
        [sys.executable, "-B", "-c", codigo, os.path.join(RAIZ, "src")],
        cwd=os.path.dirname(auditoria.RUTA_AUDITORIA), capture_output=True, text=True, check=True,
    )
    assert resultado.stdout.strip() == os.path.join(os.path.realpath(RAIZ), "auditoria.txt")


def ejecutar_pruebas():
    pruebas = [
        prueba_archivo_inexistente, prueba_escritura_acumulativa,
        prueba_separadores_y_saltos, prueba_lineas_invalidas,
        prueba_utf8_invalido, prueba_errores_archivo,
        prueba_contrasena_y_secreto, prueba_pregunta_y_secreto,
        prueba_reintentos_y_cambio_metodo, prueba_usuario_inexistente_y_cancelacion,
        prueba_cierre_unico, prueba_ruta_desde_otro_directorio,
    ]
    aprobadas = 0
    for prueba in pruebas:
        ruta_original = auditoria.RUTA_AUDITORIA
        usuario_original = auditoria.usuario_actual
        salida = io.StringIO()
        try:
            with tempfile.TemporaryDirectory() as carpeta:
                auditoria.RUTA_AUDITORIA = os.path.join(carpeta, "auditoria.txt")
                auditoria.establecer_usuario("sin_sesion")
                with contextlib.redirect_stdout(salida):
                    prueba()
            aprobadas += 1
            print("APROBADA:", prueba.__name__)
        except Exception as error:
            print("FALLIDA:", prueba.__name__, repr(error))
            print(salida.getvalue())
        finally:
            auditoria.RUTA_AUDITORIA = ruta_original
            auditoria.establecer_usuario(usuario_original)
    print(f"Resultado: {aprobadas}/{len(pruebas)} pruebas aprobadas.")
    return aprobadas == len(pruebas)


if __name__ == "__main__":
    sys.exit(0 if ejecutar_pruebas() else 1)
