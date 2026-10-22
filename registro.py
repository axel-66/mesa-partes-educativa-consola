"""Ingreso y validación de los datos de un expediente."""

from datetime import date

from archivos import guardar_expediente


def pedir_texto(mensaje):
    """Solicita un campo obligatorio que pueda guardarse en una sola línea."""
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("Este campo es obligatorio.")
        elif "|" in texto or "\n" in texto or "\r" in texto:
            print("No se permiten el carácter | ni saltos de línea.")
        else:
            return texto


def pedir_dni():
    """Conserva el DNI como texto, incluidos los ceros iniciales."""
    while True:
        dni = input("DNI (8 dígitos): ").strip()
        if len(dni) == 8 and dni.isascii() and dni.isdigit():
            return dni
        print("El DNI debe contener exactamente 8 dígitos del 0 al 9.")


def registrar_expediente():
    """Solicita los datos y confirma el registro solo después de guardarlo."""
    print("\nREGISTRAR EXPEDIENTE")
    try:
        nombres = pedir_texto("Nombres: ")
        apellidos = pedir_texto("Apellidos: ")
        dni = pedir_dni()
        tipo = pedir_texto("Tipo de solicitud: ")
        asunto = pedir_texto("Asunto: ")
        fecha = date.today().isoformat()
        codigo = guardar_expediente(nombres, apellidos, dni, tipo, asunto, fecha)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"No se pudo completar el registro: {error}")
        return
    except (EOFError, KeyboardInterrupt):
        print("\nRegistro interrumpido.")
        raise SystemExit(0)

    print(f"Expediente registrado correctamente. Código: {codigo}")
    print(f"Fecha de registro: {fecha}")
