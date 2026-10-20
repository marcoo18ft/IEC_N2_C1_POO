"""
entrada.py
Funciones para leer datos por consola. Repiten la pregunta hasta que el dato
sea válido. Si se pasa 'actual' (al modificar), ENTER conserva ese valor.
"""
from datos.auxiliar import (ErrorValidacion, convertir_fecha, normalizar_rut, validar_email,
                            validar_entero_positivo, validar_fecha_nacimiento, validar_hora,
                            validar_telefono, validar_texto)


def _convertir(valor, tipo, campo):
    if tipo == "texto":
        return validar_texto(valor, campo, 100)
    if tipo == "texto_largo":
        return validar_texto(valor, campo, 255)
    if tipo == "texto_opcional":
        return validar_texto(valor, campo, 255, obligatorio=False)
    if tipo == "rut":
        return normalizar_rut(valor)
    if tipo == "email":
        return validar_email(valor)
    if tipo == "telefono":
        return validar_telefono(valor)
    if tipo == "id":
        return validar_entero_positivo(valor, campo)
    if tipo == "fecha":
        return convertir_fecha(valor)
    if tipo == "fecha_nacimiento":
        return validar_fecha_nacimiento(valor)
    if tipo == "hora":
        return validar_hora(valor)
    return valor


def pedir_dato(mensaje, tipo="texto", actual=None):
    """tipos: texto, texto_largo, texto_opcional, rut, email, telefono, id,
    fecha, fecha_nacimiento, hora."""
    while True:
        pista = ""
        if actual is not None and str(actual) != "":
            pista = f" [{actual}]"
        valor = input(f"{mensaje}{pista}: ").strip()
        if valor == "" and actual is not None:
            valor = str(actual)
        try:
            return _convertir(valor, tipo, mensaje)
        except ErrorValidacion as error:
            print(f"   ⚠ {error}")


def pedir_si_no(mensaje):
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("   ⚠ Responda 's' o 'n'.")


def pausar():
    input("\nPresione ENTER para continuar...")
