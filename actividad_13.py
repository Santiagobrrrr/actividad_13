while True:
    print(f"-- MENÚ PARA ADMINISTRACIÓN DE ESTUDIANTES --")
    print(f"1. Agregar estudiantes")
    print(f"2. Agregar curso con nota")
    print(f"3. Consultar estudiante")
    print(f"4. Mostrar estudiantes")
    print(f"5. Salir")

    option_user = input(f"Ingrese la opción a la que desea ir: ")

    match option_user:
        case "1":
            print("\nAgregar estudiantes")

        case "2":
            print("\nAgregar curso con nota")

        case "3":
            print("\nConsultar estudiante")

        case "4":
            print("\nMostrar estudiantes")

        case "5":
            print("\nSaliendo del programa...")
            break

        case _:
            print(f"\nOpción invalida, intente de nuevo")