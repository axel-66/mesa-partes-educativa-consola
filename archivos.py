"""Lectura y guardado de expedientes en un archivo de texto."""

from pathlib import Path


ARCHIVO = Path(__file__).resolve().parent / "datos" / "expedientes.txt"


def leer_expedientes():
    """Lee las filas y comprueba su estructura antes de añadir registros."""
    if not ARCHIVO.exists():
        return []

    expedientes = []
    codigos = []
    with ARCHIVO.open("r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            campos = linea.rstrip("\r\n").split("|")
            if len(campos) != 7 or any(not campo.strip() for campo in campos):
                raise ValueError(f"Registro inválido en la línea {numero_linea} del TXT.")
            codigo = campos[0]
            numero = codigo[4:]
            if (not codigo.startswith("EXP-") or not numero.isascii()
                    or not numero.isdigit() or int(numero) < 1):
                raise ValueError(f"Código inválido en la línea {numero_linea} del TXT.")
            if int(numero) in codigos:
                raise ValueError(f"Código repetido en la línea {numero_linea} del TXT.")
            codigos.append(int(numero))
            expedientes.append(campos)
    return expedientes


def guardar_expediente(nombres, apellidos, dni, tipo, asunto, fecha):
    """Genera el siguiente código y añade una fila sin borrar las anteriores."""
    expedientes = leer_expedientes()
    ultimo_numero = 0
    for expediente in expedientes:
        numero = int(expediente[0][4:])
        if numero > ultimo_numero:
            ultimo_numero = numero
    codigo = f"EXP-{ultimo_numero + 1:04d}"
    campos = [codigo, nombres, apellidos, dni, tipo, asunto, fecha]

    ARCHIVO.parent.mkdir(parents=True, exist_ok=True)
    with ARCHIVO.open("a+", encoding="utf-8") as archivo:
        archivo.seek(0)
        contenido = archivo.read()
        if contenido and not contenido.endswith("\n"):
            archivo.write("\n")
        archivo.write("|".join(campos) + "\n")
    return codigo
