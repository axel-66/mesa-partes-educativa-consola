"""Menú inicial del prototipo de mesa de partes educativa."""


def mostrar_menu():
    """Muestra las operaciones previstas para el prototipo."""
    print("\nMESA DE PARTES - INSTITUCIÓN EDUCATIVA")
    print("1. Registrar expediente")
    print("2. Buscar expediente por código")
    print("3. Buscar expedientes por DNI")
    print("4. Listar expedientes ordenados por código")
    print("5. Salir")


def main():
    """Repite el menú hasta que el usuario decida salir."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "5":
            print("Programa finalizado.")
            break
        elif opcion in ("1", "2", "3", "4"):
            print("Esta función está pendiente de implementación.")
        else:
            print("Opción inválida. Ingrese un número del 1 al 5.")


if __name__ == "__main__":
    main()
