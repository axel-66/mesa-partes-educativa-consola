"""Búsqueda secuencial de expedientes almacenados en TXT."""

from archivos import leer_expedientes
from registro import pedir_dni, pedir_texto


def mostrar_expediente(expediente):
    """Muestra los siete campos de una fila del archivo."""
    print("\n----------------------------------------")
    print(f"Código: {expediente[0]}")
    print(f"Solicitante: {expediente[1]} {expediente[2]}")
    print(f"DNI: {expediente[3]}")
    print(f"Tipo de solicitud: {expediente[4]}")
    print(f"Asunto: {expediente[5]}")
    print(f"Fecha de registro: {expediente[6]}")


def buscar_expedientes(opcion):
    """Lee el TXT en cada consulta y recorre sus filas buscando coincidencias."""
    try:
        expedientes = leer_expedientes()
    except (OSError, UnicodeError, ValueError) as error:
        print(f"No se pudo consultar el archivo: {error}")
        return

    if not expedientes:
        print("Todavía no hay expedientes registrados.")
        return

    if opcion == "1":
        dato = pedir_texto("Código del expediente (ejemplo EXP-0001): ").upper()
        columna = 0
    else:
        dato = pedir_dni()
        columna = 3

    encontrados = 0
    for expediente in expedientes:
        if expediente[columna] == dato:
            mostrar_expediente(expediente)
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron expedientes para el dato ingresado.")
    else:
        print(f"\nExpedientes encontrados: {encontrados}")


def menu_busqueda():
    """Permite repetir consultas o volver al menú principal."""
    try:
        while True:
            print("\nBUSCAR EXPEDIENTE")
            print("1. Por código de expediente")
            print("2. Por DNI del solicitante")
            print("3. Volver al menú principal")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "3":
                return
            if opcion in ("1", "2"):
                buscar_expedientes(opcion)
            else:
                print("Opción inválida. Ingrese un número del 1 al 3.")
    except (EOFError, KeyboardInterrupt):
        print("\nConsulta interrumpida.")
        raise SystemExit(0)
