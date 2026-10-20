"""
auxiliar.py
Clases y funciones de apoyo usadas por todas las capas: excepciones propias,
validaciones y conversiones de fecha/hora. Se centralizan aquí para no
duplicar código.
"""
import re
from datetime import date, datetime, time, timedelta


class ErrorValidacion(Exception):
    """Se lanza cuando un dato no cumple una regla (formato, rango, obligatorio)."""


class ErrorBaseDatos(Exception):
    """Se lanza cuando falla la conexión o una consulta SQL."""


# ---------------------------------------------------------------- Textos
def limpiar_texto(valor):
    """Convierte a texto y quita espacios sobrantes. None pasa a ''."""
    if valor is None:
        return ""
    return str(valor).strip()


def validar_texto(valor, campo, largo_maximo=100, obligatorio=True):
    texto = limpiar_texto(valor)
    if obligatorio and texto == "":
        raise ErrorValidacion(f"El campo '{campo}' es obligatorio.")
    if len(texto) > largo_maximo:
        raise ErrorValidacion(f"El campo '{campo}' no puede superar {largo_maximo} caracteres.")
    return texto


def validar_entero_positivo(valor, campo):
    try:
        numero = int(valor)
    except (TypeError, ValueError):
        raise ErrorValidacion(f"El campo '{campo}' debe ser un número entero.")
    if numero <= 0:
        raise ErrorValidacion(f"El campo '{campo}' debe ser mayor que cero.")
    return numero


# ------------------------------------------------- RUT, correo y teléfono
def normalizar_rut(rut):
    """Valida el RUT chileno (módulo 11) y lo devuelve como '12345678-5'."""
    limpio = limpiar_texto(rut).replace(".", "").replace("-", "").upper()
    if len(limpio) < 2 or len(limpio) > 9:
        raise ErrorValidacion("RUT inválido. Ejemplo: 12.345.678-5")
    cuerpo = limpio[:-1]
    digito = limpio[-1]
    if not cuerpo.isdigit():
        raise ErrorValidacion("RUT inválido. Ejemplo: 12.345.678-5")

    suma = 0
    multiplicador = 2
    for numero in reversed(cuerpo):
        suma += int(numero) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = 11 - (suma % 11)
    if resto == 11:
        esperado = "0"
    elif resto == 10:
        esperado = "K"
    else:
        esperado = str(resto)

    if digito != esperado:
        raise ErrorValidacion("RUT inválido: el dígito verificador no corresponde.")
    return f"{int(cuerpo)}-{digito}"


def validar_email(email):
    texto = limpiar_texto(email).lower()
    if not re.match(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$", texto):
        raise ErrorValidacion("Correo electrónico inválido. Ejemplo: nombre@correo.cl")
    if len(texto) > 100:
        raise ErrorValidacion("El correo no puede superar 100 caracteres.")
    return texto


def validar_telefono(telefono):
    texto = limpiar_texto(telefono).replace(" ", "")
    if not re.match(r"^\+?[0-9]{8,12}$", texto):
        raise ErrorValidacion("Teléfono inválido. Ejemplo: +56912345678")
    return texto


# ---------------------------------------------------------- Fechas y horas
def convertir_fecha(valor):
    """Convierte 'dd-mm-aaaa' (o 'aaaa-mm-dd') a objeto date."""
    if isinstance(valor, datetime):
        return valor.date()
    if isinstance(valor, date):
        return valor
    texto = limpiar_texto(valor)
    for formato in ["%d-%m-%Y", "%Y-%m-%d"]:
        try:
            return datetime.strptime(texto, formato).date()
        except ValueError:
            pass
    raise ErrorValidacion("Fecha inválida. Use el formato dd-mm-aaaa (ej: 25-10-2026).")


def validar_fecha_nacimiento(valor):
    fecha = convertir_fecha(valor)
    if fecha > date.today():
        raise ErrorValidacion("La fecha de nacimiento no puede ser futura.")
    if fecha.year < 1900:
        raise ErrorValidacion("La fecha de nacimiento no es válida.")
    return fecha


def formatear_fecha(fecha):
    if fecha is None:
        return ""
    return fecha.strftime("%d-%m-%Y")


def formatear_fecha_hora(fecha_hora):
    if fecha_hora is None:
        return ""
    return fecha_hora.strftime("%d-%m-%Y %H:%M")


def formatear_hora(valor):
    """Devuelve 'HH:MM'. MySQL entrega las horas (TIME) como timedelta."""
    if valor is None:
        return ""
    if isinstance(valor, timedelta):
        total = int(valor.total_seconds())
        horas = total // 3600
        minutos = (total % 3600) // 60
        return f"{horas:02d}:{minutos:02d}"
    if isinstance(valor, time):
        return valor.strftime("%H:%M")
    return limpiar_texto(valor)[:5]


def validar_hora(valor):
    texto = formatear_hora(valor)
    try:
        return datetime.strptime(texto, "%H:%M").strftime("%H:%M")
    except ValueError:
        raise ErrorValidacion("Hora inválida. Use el formato HH:MM (ej: 09:30).")


def hora_a_minutos(hora):
    """'09:30' -> 570. Sirve para comparar y calcular rangos horarios."""
    partes = validar_hora(hora).split(":")
    return int(partes[0]) * 60 + int(partes[1])
