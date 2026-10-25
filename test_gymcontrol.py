"""
Suite de Pruebas Unitarias para GymControl (Segunda Parte).
Ejecución independiente: python3 test_gymcontrol.py
Cumple con la restricción §12.1 (sin uso de class / POO).
"""

import os
import sys

ruta_src = os.path.join(os.path.dirname(__file__), "src")
if os.path.exists(ruta_src) and ruta_src not in sys.path:
    sys.path.insert(0, ruta_src)

from validaciones import es_entero, es_nombre_clase_valido, es_telefono_valido
from utilidades import socio_esta_inscripto_en_clase
from auditoria import resumir_auditoria
from clases import es_hora_valida
from socios import liberar_cupos_de_afiliado


def mostrar_resultado_prueba(numero, categoria, funcion, datos, esperado, obtenido):
    """
    Objetivo: mostrar los 5 puntos obligatorios de cada prueba unitaria (§9) y evaluar su aprobación.
    Parámetros: numero (int), categoria (str), funcion (str), datos (str), esperado, obtenido.
    Salida: True si esperado == obtenido; False en caso contrario.
    """
    aprobada = esperado == obtenido
    estado = "APROBADA" if aprobada else "FALLIDA"
    print(f"Prueba #{numero:02d} [{categoria}]")
    print(f"  1. Función probada   : {funcion}")
    print(f"  2. Datos utilizados  : {datos}")
    print(f"  3. Resultado esperado: {esperado}")
    print(f"  4. Resultado obtenido: {obtenido}")
    print(f"  5. Estado de prueba  : {estado}")
    print("-" * 75)
    return aprobada


# --- 4 PRUEBAS DE CASOS VÁLIDOS ---

def prueba_01_telefono_valido():
    dato = "11-2587-8779"
    obtenido = es_telefono_valido(dato)
    return mostrar_resultado_prueba(
        1, "Caso Válido 1/4", "es_telefono_valido(telefono)",
        f"telefono='{dato}'", True, obtenido
    )


def prueba_02_nombre_clase_valido():
    dato = "Funcional Avanzado"
    obtenido = es_nombre_clase_valido(dato) is not None
    return mostrar_resultado_prueba(
        2, "Caso Válido 2/4", "es_nombre_clase_valido(nombre)",
        f"nombre='{dato}'", True, obtenido
    )


def prueba_03_socio_inscripto_activo():
    obtenido = socio_esta_inscripto_en_clase(101, 205)
    return mostrar_resultado_prueba(
        3, "Caso Válido 3/4", "socio_esta_inscripto_en_clase(codigo_socio, codigo_clase)",
        "codigo_socio=101, codigo_clase=205 (inscripción 301 activa)", True, obtenido
    )


def prueba_04_resumen_auditoria_diccionario():
    eventos_prueba = [
        ["2026-10-25T10:00:00-03:00", "admin", "ALTA_SOCIO", "Código=113"],
        ["2026-10-25T10:05:00-03:00", "admin", "ALTA_SOCIO", "Código=114"],
        ["2026-10-25T10:10:00-03:00", "admin", "BAJA_SOCIO", "Código=113"]
    ]
    esperado = {"ALTA_SOCIO": 2, "BAJA_SOCIO": 1}
    obtenido = resumir_auditoria(eventos_prueba)
    return mostrar_resultado_prueba(
        4, "Caso Válido 4/4", "resumir_auditoria(eventos)",
        "3 eventos (2 ALTA_SOCIO, 1 BAJA_SOCIO)", esperado, obtenido
    )


# --- 3 PRUEBAS DE CASOS INVÁLIDOS ---

def prueba_05_telefono_invalido_sin_guiones():
    dato = "1125878779"
    obtenido = es_telefono_valido(dato)
    return mostrar_resultado_prueba(
        5, "Caso Inválido 1/3", "es_telefono_valido(telefono)",
        f"telefono='{dato}' (sin guiones)", False, obtenido
    )


def prueba_06_entero_invalido_texto():
    dato = "abc"
    obtenido = es_entero(dato)
    return mostrar_resultado_prueba(
        6, "Caso Inválido 2/3", "es_entero(valor)",
        f"valor='{dato}' (cadena alfabética)", False, obtenido
    )


def prueba_07_socio_con_inscripcion_inactiva():
    obtenido = socio_esta_inscripto_en_clase(103, 201)
    return mostrar_resultado_prueba(
        7, "Caso Inválido 3/3", "socio_esta_inscripto_en_clase(codigo_socio, codigo_clase)",
        "codigo_socio=103, codigo_clase=201 (inscripción 303 con estado=2 inactiva)", False, obtenido
    )


# --- 2 PRUEBAS DE CASOS LÍMITE ---

def prueba_08_limite_horarios_bordes():
    obtenido = (es_hora_valida("00:00"), es_hora_valida("23:59"), es_hora_valida("24:00"))
    esperado = (True, True, False)
    return mostrar_resultado_prueba(
        8, "Caso Límite 1/2", "es_hora_valida(hora)",
        "horas=('00:00' mínimo válido, '23:59' máximo válido, '24:00' fuera de rango)",
        esperado, obtenido
    )


def prueba_09_limite_baja_socio_sin_inscripciones():
    inscripciones_prueba = [[301, 101, 201, 4, 1]]
    clases_prueba = [[201, "Yoga", 1, 12, (("Lunes",), "08:00", "09:00")]]
    liberados = liberar_cupos_de_afiliado(999, inscripciones_prueba, clases_prueba)
    obtenido = (liberados, clases_prueba[0][3])
    esperado = (0, 12)
    return mostrar_resultado_prueba(
        9, "Caso Límite 2/2", "liberar_cupos_de_afiliado(codigo_afiliado, inscripciones, clases)",
        "codigo_afiliado=999 (sin inscripciones), clase 201 con cupo=12",
        esperado, obtenido
    )


# --- 1 PRUEBA RELEVANTE PARA LA PROBLEMÁTICA DEL SISTEMA ---

def prueba_10_relevante_liberacion_cupos_baja_socio():
    inscripciones_prueba = [
        [312, 112, 201, 0, 1],  # Activa en Yoga (debe devolver 1 cupo)
        [313, 112, 203, 5, 2],  # Inactiva en Boxeo (NO debe devolver cupo)
    ]
    clases_prueba = [
        [201, "Yoga", 1, 14, (("Lunes", "Miércoles"), "08:00", "09:00")],
        [203, "Boxeo", 2, 15, (("Lunes", "Viernes"), "19:00", "20:00")],
    ]
    liberados = liberar_cupos_de_afiliado(112, inscripciones_prueba, clases_prueba)
    obtenido = (liberados, clases_prueba[0][3], clases_prueba[1][3])
    esperado = (1, 15, 15)
    return mostrar_resultado_prueba(
        10, "Caso Relevante del Sistema", "liberar_cupos_de_afiliado(codigo_afiliado, inscripciones, clases)",
        "socio=112 con 1 activa en 201 (cupo 14) y 1 inactiva en 203 (cupo 15)",
        esperado, obtenido
    )


def ejecutar_pruebas():
    print("=" * 75)
    print("EJECUCIÓN DE PRUEBAS UNITARIAS - GYMCONTROL")
    print("=" * 75)
    pruebas = [
        prueba_01_telefono_valido,
        prueba_02_nombre_clase_valido,
        prueba_03_socio_inscripto_activo,
        prueba_04_resumen_auditoria_diccionario,
        prueba_05_telefono_invalido_sin_guiones,
        prueba_06_entero_invalido_texto,
        prueba_07_socio_con_inscripcion_inactiva,
        prueba_08_limite_horarios_bordes,
        prueba_09_limite_baja_socio_sin_inscripciones,
        prueba_10_relevante_liberacion_cupos_baja_socio,
    ]
    aprobadas = 0
    for prueba in pruebas:
        if prueba():
            aprobadas += 1

    total = len(pruebas)
    print(f"RESUMEN FINAL: {aprobadas}/{total} pruebas aprobadas.")
    print("=" * 75)
    return aprobadas == total


if __name__ == "__main__":
    ejecutar_pruebas()
