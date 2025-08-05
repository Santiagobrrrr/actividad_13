students = {}
courses = {}

def add_student(id_student, name_student, carrer_student): # Función para añadir del case 1, los datos al diccionario principal
    students[id_student] = {
        "name": name_student,
        "carrer": carrer_student,
        "course": {}
    }
    print(f"\nEstudiante registrado en el sistema.")
    print(students)

def request_id_student(): # Función que solicita el ID del usuario
    while True:
        try:
            id_user = int(input("Ingresa el ID del usuario: ")) # Solicitud de ID
        # Posibles errores si no ingresa un entero
        except ValueError:
            print(f"Error: valor inválido. Intente de nuevo.")
        except TypeError:
            print(f"Error: tipo inválido. Intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        else:
            if id_user in students:
                print(f"Nombre del usuario: {students[id_user]['name']}.") # Si el ID existe en el diccionario de estudiantes, se muestra su información
                print(f"Carrera: {students[id_user]['carrer']}.")
                return id_user # Retorna el ID del estudiante encontrado
            else:
                print(f"El ID {id_user} no existe. Redirigiendo al menú.") # Si el ID no existe se informa que se regresa al menú principal
                return None # Se retorna None por si no se encuentra, para poder manejarlo después

def add_course(id_student): # Función que agrega curso
    while True:
        course_user = input(f"Ingrese el nombre del curso a agregar: ").strip().lower() # Función para no tener campo vacíos, y se pone en minuscula para no tener inconvenientes
        if course_user == "": # Verificación si ingresa el campo vacío
            print(f"No puede ingresar una curso vacío, intente nuevamente.")
        else:
            break

    if course_user not in courses: # Se verifica si el curso que desea agregar ya existe en el subdiccionario del estudiante
        while True:
            try:
                grade_user = float(input(f"Ingrese la nota del curso: "))
            # Posibles errores si no ingresa un entero
            except ValueError:
                print(f"Error: ingreso mal un valor, intente de nuevo.")
            except TypeError:
                print(f"Error: tipo de valor inválido, intente de nuevo.")
            except Exception as e:
                print(f"Error inesperado: {e}")

            else:
                if grade_user >= 0 and grade_user <= 100: # Solo se guardan las notas de 0 a 100
                    courses[course_user] = { # Se creo un diccionario para guardar las notas de cada curso
                        "grade_user": grade_user
                    }
                    students[id_student]["course"][course_user] = courses[course_user] # Se guarda el curso y la nota en el ID del estudiante ingresado
                    print(f"Nota registrada en el sistema.")
                    print(courses)
                    print(students)
                    break

                else:
                    print(f"Debe de ingresar una nota entre 0 y 100.")
    else:
        print(f"El curso ya esta registrado en el sistema. Intente de nuevo. Redirigiendo al menú.")

def consult_student():  # Función para consultar un estudiante y mostrar sus datos, cursos, promedio y si aprueba
    id_selected = request_id_student()  # Se solicita el ID del estudiante, reutilizando la función existente

    if id_selected is not None:  # Si se ingresó un ID válido (es decir, está en el sistema)
        student = students[id_selected]
        print(f"\n--- Información del estudiante ---")
        print(f"Nombre: {student['name']}")
        print(f"Carrera: {student['carrer']}")

        if student["course"]:  # Verificación si el estudiante tiene cursos registrados
            print(f"\nCursos y notas:")
            total = 0
            passed_all = True  # Se asume que ha aprobado todos los cursos

            for course_name, course_info in student["course"].items():  # Se recorre el diccionario de cursos
                grade = course_info["grade_user"]  # Se obtiene la nota del curso
                print(f"- {course_name.upper()}: {grade} puntos")
                total += grade
                if grade < 61:  # Se verifica si alguna nota es menor a 61
                    passed_all = False  # Si una nota es menor, no aprueba todos

            average = total / len(student["course"])  # Se calcula el promedio de notas
            print(f"\nPromedio de notas: {average}")

            if passed_all:
                print(f"El estudiante aprueba todos los cursos.")  # Si todas las notas son >= 61
            else:
                print(f"El estudiante no aprueba todos los cursos.")  # Si alguna nota es < 61
        else:
            print(f"\nEste estudiante no tiene cursos registrados.")  # Si no tiene cursos en su registro

def view_students():  # Función que muestra todos los estudiantes registrados con sus cursos y notas
    while True:
        if not students:  # Si el diccionario de estudiantes está vacío
            print("\nNo hay estudiantes registrados aún.")
            break

        print(f"\n-- Lista de todos los estudiantes registrados --")

        for id_student, data in students.items():
            print(f"\nID único: {id_student}")
            print(f"Nombre: {data['name']}")
            print(f"Carrera: {data['carrer']}")

            if data["course"]:  # Si tiene cursos registrados
                print(f"Cursos registrados:")
                for course_name, course_data in data["course"].items(): # Accede a subdiccionario de los cursos
                    print(f"  - {course_name.upper()}: {course_data['grade_user']} puntos")
            else:
                print("No tiene cursos registrados.")
        break

while True:
    print(f"\n-- MENÚ PARA ADMINISTRACIÓN DE ESTUDIANTES --") # Menú principal
    print(f"1. Agregar estudiantes")
    print(f"2. Agregar curso con nota")
    print(f"3. Consultar estudiante")
    print(f"4. Mostrar estudiantes")
    print(f"5. Salir")

    option_user = input(f"Ingrese la opción a la que desea ir: ")

    match option_user:
        case "1":
            print(f"\nAgregar estudiantes")
            while True: # No se creo una función 'def' para poder manejar variables globales
                try:
                    id_student = int(input(f"\nIngrese el ID del estudiante: "))

                except ValueError:
                    print(f"Error: Valor no valido")
                except TypeError:
                    print(f"Error: Tipo no válido")
                except Exception as e:
                    print(f"Se produjo un error inesperado: {e}")
                else:
                    if id_student in students: # Hace la verificación si el ID ya existe, si existe lo dirige al menú principal
                        print(f"El estudiante con id: '{id_student}' ya existe, intente nuevamente. Redirigiendo al menú...")
                        break
                    else:
                        while True:
                            name_student = input(f"Ingrese el nombre del estudiante: ").strip() # Función para no poder tener campos vacíos
                            if name_student == "":
                                print(f"No puede ingresar un valor vacío, intente nuevamente.")
                            else:
                                break

                        while True:
                            carrer_student = input(f"Ingrese el carrera del estudiante: ").strip() # Función para no poder tener campos vacíos
                            if carrer_student == "":
                                print(f"No puede ingresar una carrera vacía, intente nuevamente.")
                            else:
                                break
                        add_student(id_student, name_student, carrer_student) # Se llama a la función de añadir estudiantes con las variables globales tomadas
                    break

        case "2":
            print("\nAgregar curso con nota")
            id_selected = request_id_student() # Llamamos a la función y verificamos el id del valor retornado
            if id_selected is not None:
                add_course(id_selected) # Si el ID del valor retornado es válido entonces se agrega el curso

        case "3":
            print(f"\nConsultar estudiante")
            consult_student()

        case "4":
            print(f"\nMostrar estudiantes")
            view_students()

        case "5":
            print(f"\nSaliendo del programa...")
            break

        case _:
            print(f"\nOpción invalida, intente de nuevo")