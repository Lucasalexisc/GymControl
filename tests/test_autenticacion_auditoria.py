"""Pruebas funcionales con biblioteca estándar, sin definir clases."""
import contextlib
import copy
import io
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))
sys.path.insert(0, str(RAIZ / "src"))
import auditoria
import datos
import login
import socios
import clases
import inscripciones
import utilidades


def ejecutar_con_entradas(funcion, entradas):
    salida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), contextlib.redirect_stdout(salida):
        resultado = funcion()
    return resultado, salida.getvalue()


def test_reintentos_y_clave_exacta():
    entradas = ["1", "ADMIN", "incorrecta"] * 4 + ["1", "admin", "admin1234"]
    assert ejecutar_con_entradas(login.login, entradas)[0] is True
    eventos = auditoria.leer_auditoria()
    assert auditoria.resumir_auditoria(eventos) == {"ACCESO_FALLIDO": 4, "ACCESO_EXITOSO": 1}
    assert eventos[-1][1] == "admin"
    assert "incorrecta" not in auditoria.RUTA_AUDITORIA.read_text()
    assert "admin1234" not in auditoria.RUTA_AUDITORIA.read_text()


def test_pregunta_y_cambio_metodo():
    entradas = ["2", "no_existe", "2", "admin", "", "2", "admin", "rojo", "1", "admin", "admin1234"]
    assert ejecutar_con_entradas(login.login, entradas)[0] is True
    assert ejecutar_con_entradas(login.login, ["2", " ADMIN ", " AZUL  "])[0] is True
    assert "AZUL" not in auditoria.RUTA_AUDITORIA.read_text()


def test_salida_y_opcion_invalida():
    resultado, salida = ejecutar_con_entradas(login.login, ["x", "3", "0"])
    assert resultado is False and "Opción inválida" in salida
    assert auditoria.usuario_actual == "sin_sesion"


def test_todos_los_usuarios():
    for usuario, clave, pregunta, respuesta in datos.login_users:
        assert ejecutar_con_entradas(login.login, ["1", usuario.upper(), clave])[0]
        assert ejecutar_con_entradas(login.login, ["2", usuario, respuesta.upper()])[0]
    assert utilidades.search_user_position(".*") == -1
    assert login.normalizar_respuesta("  Azul   MARINO ") == "azul marino"


def test_archivo_incremental_y_resumen():
    assert auditoria.leer_auditoria() == []
    auditoria.establecer_usuario("admin")
    assert auditoria.registrar_auditoria("ALTA_SOCIO", "Código=113")
    assert auditoria.registrar_auditoria("ALTA_SOCIO", "Código=114")
    auditoria.cerrar_sesion()
    eventos = auditoria.leer_auditoria()
    assert len(eventos) == 3 and eventos[0][1] == "admin"
    assert auditoria.resumir_auditoria(eventos)["ALTA_SOCIO"] == 2
    assert auditoria.usuario_actual == "sin_sesion"
    assert "ALTA_SOCIO: 2" in ejecutar_con_entradas(auditoria.mostrar_auditoria, [])[1]


def test_campos_y_lineas_invalidas():
    auditoria.registrar_auditoria("ACCESO_FALLIDO", "línea\nextra | evento", usuario="a\rb")
    with auditoria.RUTA_AUDITORIA.open("a", encoding="utf-8") as archivo:
        archivo.write("basura\nfecha | usuario | evento | detalle\n")
    eventos = auditoria.leer_auditoria()
    assert len(eventos) == 1 and eventos[0][1] == "a b"
    assert len(auditoria.RUTA_AUDITORIA.read_text().splitlines()) == 3


def test_errores_archivo():
    with patch.object(Path, "open", side_effect=PermissionError):
        resultado, salida = ejecutar_con_entradas(lambda: auditoria.registrar_auditoria("X", "Y"), [])
        assert resultado is False and "no se pudo guardar" in salida
        assert ejecutar_con_entradas(auditoria.leer_auditoria, [])[0] is None
    auditoria.RUTA_AUDITORIA.write_bytes(b"\xff")
    assert ejecutar_con_entradas(auditoria.leer_auditoria, [])[0] is None


def test_crud_socios():
    ejecutar_con_entradas(socios.sumar_afiliados, ["Prueba", "25", "1", "11-1234-5678"])
    codigo = datos.affiliates[-1][datos.AFF_CODE]
    ejecutar_con_entradas(socios.modify_affiliate, [str(codigo), "si", "26", "si", "si"])
    assert datos.affiliates[-1][datos.AFF_AGE] == 26
    ejecutar_con_entradas(socios.eliminar_afiliados, [str(codigo), "n"])
    assert utilidades.search_affiliate_position(codigo) != -1
    ejecutar_con_entradas(socios.eliminar_afiliados, [str(codigo), "s"])
    assert utilidades.search_affiliate_position(codigo) == -1
    assert [e[2] for e in auditoria.leer_auditoria()] == ["ALTA_SOCIO", "MODIFICACION_SOCIO", "BAJA_SOCIO"]


def test_crud_clases_e_inscripciones():
    ejecutar_con_entradas(clases.sumar_clase, ["Prueba", "1", "3"])
    codigo = datos.classes[-1][datos.CLASS_CODE]
    ejecutar_con_entradas(clases.modify_clase, [str(codigo), "si", "2", "si"])
    ejecutar_con_entradas(inscripciones.alta_inscripcion, [str(codigo), "101"])
    insc = datos.enrollments[-1][datos.ENR_CODE]
    assert datos.classes[-1][datos.CLASS_CAPACITY] == 2
    ejecutar_con_entradas(inscripciones.alta_inscripcion, [str(codigo), "101"])
    assert datos.classes[-1][datos.CLASS_CAPACITY] == 2
    ejecutar_con_entradas(inscripciones.modify_inscripcion, [str(insc), "5", "si"])
    ejecutar_con_entradas(inscripciones.baja_inscripcion, [str(insc), "s"])
    assert datos.classes[-1][datos.CLASS_CAPACITY] == 3
    ejecutar_con_entradas(inscripciones.baja_inscripcion, [str(insc)])
    ejecutar_con_entradas(clases.eliminar_clase, [str(codigo), "s"])
    assert utilidades.search_inscription_position(insc) == -1
    resumen = auditoria.resumir_auditoria(auditoria.leer_auditoria())
    assert resumen == {"ALTA_CLASE": 1, "MODIFICACION_CLASE": 1, "ALTA_INSCRIPCION": 1, "MODIFICACION_INSCRIPCION": 1, "BAJA_INSCRIPCION": 2, "BAJA_CLASE": 1}


def test_sin_cambios_no_audita():
    ejecutar_con_entradas(socios.modify_affiliate, ["101", "si", "si", "si", "si"])
    ejecutar_con_entradas(clases.modify_clase, ["201", "si", "si", "si"])
    ejecutar_con_entradas(inscripciones.modify_inscripcion, ["301", "si", "si"])
    ejecutar_con_entradas(socios.eliminar_afiliados, ["99999"])
    assert auditoria.leer_auditoria() == []


def test_baja_socio_cascada():
    ejecutar_con_entradas(socios.eliminar_afiliados, ["101", "s"])
    assert not any(e[datos.ENR_AFFILIATE_CODE] == 101 for e in datos.enrollments)
    assert auditoria.resumir_auditoria(auditoria.leer_auditoria()) == {"BAJA_INSCRIPCION": 1, "BAJA_SOCIO": 1}


def test_cli_real():
    # El proceso ejecuta el programa real; solo redirige el archivo de auditoría.
    codigo = (
        "import sys, runpy; from pathlib import Path; "
        f"sys.path.insert(0, {str(RAIZ / 'src')!r}); import auditoria; "
        f"auditoria.RUTA_AUDITORIA=Path({str(auditoria.RUTA_AUDITORIA)!r}); "
        f"runpy.run_path({str(RAIZ / 'main.py')!r}, run_name='__main__')"
    )
    datos_entrada = ["1", "admin", "admin1234", "1", "4", "0", "2", "4", "0", "3", "4", "5", "101", "0", "4", "1", "4", "2", "4", "3", "5", "1", "201", "2", "101", "0", "6", "1", "2", "3", "4", "0", "7", "0"]
    proceso = subprocess.run([sys.executable, "-B", "-c", codigo], input="\n".join(datos_entrada)+"\n", text=True, capture_output=True, cwd=auditoria.RUTA_AUDITORIA.parent, timeout=15)
    assert proceso.returncode == 0, proceso.stderr
    assert "Gracias por usar" in proceso.stdout and "RESUMEN POR OPERACIÓN" in proceso.stdout
    assert "Entrada interrumpida" not in proceso.stdout
    assert auditoria.resumir_auditoria(auditoria.leer_auditoria())["CIERRE_SESION"] == 1


def test_interrupcion_cierra_sesion():
    from main import ejecutar
    with patch("builtins.input", side_effect=["1", "admin", "admin1234", EOFError]), contextlib.redirect_stdout(io.StringIO()):
        ejecutar()
    assert auditoria.leer_auditoria()[-1][2] == "CIERRE_SESION"


if __name__ == "__main__":
    pruebas = [funcion for nombre, funcion in list(globals().items()) if nombre.startswith("test_")]
    for prueba in pruebas:
        originales = [copy.deepcopy(matriz) for matriz in (datos.affiliates, datos.classes, datos.enrollments)]
        with tempfile.TemporaryDirectory() as carpeta:
            auditoria.RUTA_AUDITORIA = Path(carpeta) / "auditoria.txt"
            auditoria.establecer_usuario("sin_sesion")
            try:
                prueba()
            finally:
                for matriz, original in zip((datos.affiliates, datos.classes, datos.enrollments), originales):
                    matriz[:] = original
        print(f"OK {prueba.__name__}")
    print(f"{len(pruebas)} pruebas aprobadas.")
