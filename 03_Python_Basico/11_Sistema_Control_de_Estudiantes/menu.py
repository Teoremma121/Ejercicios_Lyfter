# - Agregar, eliminar o editar información de estudiantes
#   - Agregar estudiante
#   - Editar estudiante
#   - Eliminar estudiante
# - Ver la información de los estudiantes
#   - Ver la información de una sección
#       - Mostrar estudiantes por orden alfabético
#       - Mostrar estudiantes por orden de promedio
#       - Mostrar resumen por materia
#   - Ver la información de un nivel (7mo, 8vo, 9no, etc)
#       - BIS
#   - Ver la información de un estudiante 
# - Ver los mejores 3 promedios de estudiante
#       - De una sección
#       - De cada una de las secciones
#       - De un nivel
#       - De cada uno los niveles
# - Ver resumen de estudiantes reprobados
#       - De una sección
#       - De un nivel
#       - De todos los niveles
# - Exportar datos a un archivo CSV
# - Importar datos desde un archivo CSV

def main_test():
    index = ["0"]
    new_index = navigate_menu(index)
    print(new_index)

def navigate_menu(index):
    action = False
    while action == False:
        if ".".join(index) == "0":
            entry = call_main_menu()
            index.append(entry)
        elif ".".join(index) == "0.1":
            entry = call_add_delete_or_mofify_menu()
            if entry == "4":
                index.pop()
            elif entry == "2":
                index.append(entry)
            else:
                index.append(entry)
                action = True
        elif ".".join(index) == "0.1.2":
            entry = call_modify_menu()
            if entry == "3":
                index.append(entry)
            elif entry in ["1","2","5"]:
                index.append(entry)
                action = True
            else:
                index.pop()
        elif ".".join(index) == "0.2":
            entry = call_show_students_info_menu()
            if entry in ["3","5"]:
                index.append(entry)
                action = True
            elif entry in ["1","2"]:
                index.append(entry)
            else:
                index.pop()
        elif ".".join(index) in ["0.2.1","0.2.2"]:
            entry = call_mode_of_students_info_menu()
            if entry in ["1","2"]:
                index.append(entry)
                action = True
            elif entry == "3":
                index.append(entry)
            else:
                index.pop()
        elif ".".join(index) in ["0.2.1.3","0.2.2.3","0.1.2.3"]:
            entry = call_pick_asignature()
            if entry != "6":
                index.append(entry)
                action = True
            else:
                index.pop()
        elif ".".join(index) == "0.3":
            entry = call_best_students_menu()
            if entry != "5":
                index.append(entry)
                action = True
            else:
                index.pop()
        elif ".".join(index) == "0.4":
            entry = call_failed_students_menu()
            if entry != "4":
                index.append(entry)
                action = True
            else:
                index.pop()
        else:
            action = True
    return index

def call_main_menu():
    index = 0
    while index == 0:
        print("\nDigite el número de índice de la acción que desea realizar:")
        print(" 1- Agregar, eliminar o editar información de estudiantes")
        print(" 2- Ver la información de los estudiantes")
        print(" 3- Ver los mejores 3 promedios de estudiante")
        print(" 4- Ver resumen de estudiantes reprobados")
        print(" 5- Exportar datos a un archivo CSV")
        print(" 6- Importar datos desde un archivo CSV")
        print(" 7- SALIR")
        index = input_valid_index(1,8)
    return index

def call_add_delete_or_mofify_menu():
    index = 0
    while index == 0:
        print("\nDigite el número de índice de la acción que desea realizar:")
        print(" 1- Agregar estudiantes")
        print(" 2- Editar la información de un estudiante")
        print(" 3- Eliminar un estudiante")
        print(" 4- Regresar")
        print(" 5- SALIR")
        index = input_valid_index(1,6)
    return index

def call_modify_menu():
    index = 0
    while index == 0:
        print("\nDigite el número de índice de la información que desea editar")
        print(" 1- Nombre")
        print(" 2- Sección")
        print(" 3- Notas")
        print(" 4- Regresar")
        print(" 5- SALIR")
        index = input_valid_index(1,6)
    return index

def call_show_students_info_menu():
    index = 0
    while index == 0:
        print("\nDigite el número de índice de la acción que desea realizar:")
        print(" 1- Mostrar la información de una sección")
        print(" 2- Mostrar la información de un nivel (7mo, 8vo, etc)")
        print(" 3- Mostrar la información de un estudiante")
        print(" 4- Regresar")
        print(" 5- SALIR")
        index = input_valid_index(1,6)
    return index

def call_mode_of_students_info_menu():
    index = 0
    while index == 0:
        print("\nDigite el número de índice de la acción que desea realizar:")
        print(" 1- Mostrar estudiantes por orden alfabético")
        print(" 2- Mostrar estudiantes por orden de promedios")
        print(" 3- Mostrar resumen por materia")
        print(" 4- Regresar")
        print(" 5- SALIR")
        index = input_valid_index(1,6)
    return index

def call_pick_asignature():
    index = 0
    while index == 0:
        print("\nDigite el número de índice de la materia:")
        print(" 1- Español")
        print(" 2- Inglés")
        print(" 3- Estudios Sociales")
        print(" 4- Ciencias")
        print(" 5- Matemáticas")
        print(" 6- Regresar")
        print(" 7- SALIR")
        index = input_valid_index(1,8)
    return index

def call_best_students_menu():
    index = 0
    while index == 0:
        print("\nDigite el número de índice de la acción que desea realizar:")
        print(" 1- Mostrar el top 3 de una sección")
        print(" 2- Mostrar el top 3 para cada una de las secciones")
        print(" 3- Mostrar el top 3 para un nivel (7mo, 8vo, etc)")
        print(" 4- Mostrar el top 3 para cada uno de los niveles")
        print(" 5- Regresar")
        print(" 6- SALIR")
        index = input_valid_index(1,7)
    return index

def call_failed_students_menu():
    index = 0
    while index == 0:
        print("\nDigite el número de índice de la acción que desea realizar:")
        print(" 1- Mostrar los estudiantes reprobados de una sección")
        print(" 2- Mostrar los estudiantes reprobados de un nivel (7mo, 8vo, etc)")
        print(" 3- Mostrar los estudiantes reprobados de todos los niveles")
        print(" 4- Regresar")
        print(" 5- SALIR")
        index = input_valid_index(1,6)
    return index

def call_back_or_exit_menu():
    index = 0
    while index == 0:
        print("\n¿Desea regresar al menú anterior, al menú principal o salir del programa?")
        print(" 1- Regresar")
        print(" 2- HOME")
        print(" 3- SALIR")
        index = input_valid_index(1,4)
    return index

def call_yes_or_not():
    index = 0
    while index == 0:
        print("\n¿Desea confirmar y proceder con esta acción?")
        print(" 1- Sí")
        print(" 2- No")
        index = input_valid_index(1,3)
    return index

def warning_lost_of_data():
    index = 0
    while index == 0:
        print("\nEstá cerrando el programa y la información que no se haya exportado se va perder...")
        print("¿De igual manera desea cerrar el programa?")
        print(" 1- Sí")
        print(" 2- No")
        index = input_valid_index(1,3)
    return index

def input_valid_index(min,max):
    try:
        entry = input(" > ")
        if entry not in list(map(str, range(min,max))):
            print(f"Error: No digitó un número. O el número digitado es menor que {min} o mayor que {max-1}")
            raise ValueError
        return entry
    except ValueError:
        print(f"- Debe digitar únicamente un número de índice válido de las opciones disponibles")
        print(f"- Es decir, alguno de los siguientes números: {list(range(1,max))}")
        return 0

