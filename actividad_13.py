from logging import exception

students = {}

def add_student(id_student, name_student, carrer_student):
    students[id_student] = {
        "name": name_student,
        "carrer": carrer_student,
    }
    print(f"\nEstudiante registrado en el sistema.")
    print(students)

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
            print(f"\nAgregar estudiantes")
            while True:
                try:
                    id_student = int(input(f"\nIngrese el ID del estudiante: "))

                except ValueError:
                    print(f"Error: Valor no valido")
                except TypeError:
                    print(f"Error: Tipo no válido")
                except Exception as e:
                    print(f"Se produjo un error inesperado: {e}")
                else:
                    break

            while True:
                if id_student in students:
                    print(f"El estudiante con id: '{id_student}' ya existe, intente nuevamente.")
                else:
                    break

            while True:
                name_student = input(f"\nIngrese el nombre del estudiante: ").strip()
                if name_student == "":
                    print(f"No puede ingresar un valor vacío, intente nuevamente.")
                else:
                    break

            while True:
                carrer_student = input(f"\nIngrese el carrera del estudiante: ")
                if carrer_student == "":
                    print(f"No puede ingresar una carrera vacía, intente nuevamente.")
                else:
                    break

            add_student(id_student, name_student, carrer_student)


        case "2":
            print(f"\nAgregar curso con nota")

        case "3":
            print(f"\nConsultar estudiante")

        case "4":
            print(f"\nMostrar estudiantes")

        case "5":
            print(f"\nSaliendo del programa...")
            break

        case _:
            print(f"\nOpción invalida, intente de nuevo")