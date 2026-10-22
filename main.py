"""Menú del prototipo de mesa de partes educativa."""

from registro import registrar_expediente
from consultas import menu_busqueda


def mostrar_menu():
    """Muestra las operaciones previstas para el prototipo."""
    print("\nMESA DE PARTES - INSTITUCIÓN EDUCATIVA")
    print("1. Registrar expediente")
    print("2. Buscar expediente")
    print("3. Listar expedientes ordenados por código")
    print("4. Salir")


def main():
    """Repite el menú hasta que el usuario decida salir."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "4":
            print("Programa finalizado.")
            break
        elif opcion == "1":
            registrar_expediente()
        elif opcion == "2":
            menu_busqueda()
        elif opcion == "3":
            print("Esta función está pendiente de implementación.")
        else:
            print("Opción inválida. Ingrese un número del 1 al 4.")


if __name__ == "__main__":
    main()
