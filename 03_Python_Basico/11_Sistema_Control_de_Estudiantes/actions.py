import menu

class DuplicatesError(Exception):
    pass

indexed_asignatures =   [
                        {'index':1,'esp':"Español",'eng':"Spanish"},
                        {'index':2,'esp':"Inglés",'eng':"English"},
                        {'index':3,'esp':"Estudios Sociales",'eng':"Socials"},
                        {'index':4,'esp':"Ciencias",'eng':"Sciences"},
                        ]

def index_to_action(index,data):
    if index == "1":
        add_n_students(data)
    elif index == "2":
        show_info(data)
    elif index == "3":
        show_top_students(data)
    elif index == "4":
        show_total_avg(data)
    elif index == "5":
        show_failed_students(data)
    elif index == "6":
        delete_student(data)
    elif index == "9":
        exit()

def add_n_students(data):
    n = input_quantity_of_students()
    for i in range(n):
        student_info = {}
        not_duplicates_found = False
        while not_duplicates_found == False:
            try:
                print(f"\nIngresando estudiante {i+1} de {n}")
                student_info['name'] = input_valid_name("agregar")
                student_info['section'] = input_valid_section("agregar")
                if find_student(student_info['name'],student_info['section'],data)[1] == False:
                    not_duplicates_found = True
                else:
                    raise DuplicatesError("Error: Ya existe un estudiante con el mismo nombre y la misma sección")
            except DuplicatesError as e:
                print(f"\n{e}")
                print(" -No pueden haber dos estudiantes con el mismo nombre y la misma sección")
        print("\n--Proceda a ingresar las notas del estudiante--")
        for asignature in indexed_asignatures:
            student_info[asignature['eng']] = input_valid_grade(asignature['esp'])
        data.append(student_info)
    print(f"Se ha agregado correctamente la información de {n} estudiantes")

def show_info(data):
    for student in data:
        print(f"\nNombre: {student['name']}, Sección: {student['section']}")
        for asignature in indexed_asignatures:
            print(f" -{asignature['esp']}: {student[asignature['eng']]}")

def show_top_students(data):
    from copy import deepcopy
    temporal_data = deepcopy(data)
    calculate_avg(temporal_data)
    temporal_data = order_by_avg(temporal_data)
    print("\n--Mostrando estudiantes con las mejores notas promedio:--\n")
    for i in range(3):
        student_info = temporal_data[i]
        print(f"#{i+1}. {student_info['name']}, Sección: {student_info['section']}, Nota Promedio: {student_info['avg']}")

def show_total_avg(data):
    from copy import deepcopy
    temporal_data = deepcopy(data)
    calculate_avg(temporal_data)
    total_sum = 0
    for student in temporal_data:
        total_sum += student['avg']
    total_avg = round(total_sum/len(temporal_data),2)
    print(f"\n--El promedio de las notas de todos los estudiantes es de: {total_avg}--")

def delete_student(data):
    print("\n--Proceda a digitar los datos del estudiante que desea eliminar--")
    name = input_valid_name("eliminar")
    section = input_valid_section("eliminar")
    student_index, student_exists = find_student(name,section,data)
    if student_exists == True:
        choice = "0"
        while choice == "0":
            print(f"\nSe va a eliminar la información del estudiante {name} de la sección {section}")
            print("Digite el número de índice correspondiente para confirmar o cancelar")
            print(" 1. Eliminar el estudiante")
            print(" 2. Cancelar")
            choice = menu.input_valid_index(3)
        if choice == "1":
            data.pop(student_index)
            print("--Se eliminó el estudiante de la base de datos")
        else:
            print("No se ha eliminado el estudiante")
    else:
        print("\n--En la base de datos no existe un estudiante con el nombre y la sección digitados--")

def show_failed_students(data):
    print("\n--Mostrando los estudiantes rebrobados--")
    for student in data:
        for asignature in indexed_asignatures:
            if float(student[asignature['eng']]) < 60:
                print(f"\n-{student['name']}, Sección {student['section']}")
                for asign in indexed_asignatures:
                    if float(student[asign['eng']]) < 60:
                        print(f"---> {asign['esp']}: {student[asign['eng']]}")
                break

def input_quantity_of_students():
    valid_quantity = False
    while valid_quantity == False:
        print("\n¿Cuantos estudiantes desea agregar?")
        try:
            n = input(" > ")
            if n.isdigit():
                if int(n) > 0:
                    n = int(n)
                    valid_quantity = True
            else:
                raise ValueError("Error: No digitó un número, el número es negativo o es cero")
        except ValueError as e:
            print(f"\n{e}")
            print(" - Debe digitar un número válido")
            print(" - Debe digitar un número mayor a 0 que corresponda a la cantidad de estudiantes que desea agregar")
    return n

def input_valid_name(message):
    valid_name = False
    while valid_name == False:
        print(f"\nDigite el nombre del estudiante que desea {message}")
        try:
            name = input(" > ")
            for char in name:
                if char.isdigit() == True:
                    raise ValueError("Error: El nombre no puede contener números")
            if name == "":
                raise ValueError("Error: No digitó un nombre")
            valid_name = True
        except ValueError as e:
            print(f"\n{e}")
            print("Digite un nombre correcto que cumpla las condiciones:")
            print(" - El nombre no puede estar vacío")
            print(" - El nombre no puede contener números")
    return name

def input_valid_section(message):
    valid_section = False
    while valid_section == False:
        print(f"\nDigite la sección del estudiante que desea {message}")
        try:
            section = input(" > ")
            if section[:-1].isdigit() & section[-1].isupper():
                if int(section[:-1]) >= 0:
                    valid_section = True
            else:
                raise ValueError("La sección digitada no cumple con el formato requerido")
        except ValueError as e:
            print(f"\n{e}")
            print("Debe digitar un sección válida siguiendo el formato 'NS'. Donde:")
            print(" - N debe ser un número entero mayor de cero que represente el nivel")
            print(" - S debe ser una letra del alfabeto en mayúscula que represente la sección")
            print("Por ejemplo: 7A, 7B, 8A, 9C, 10A, etc")
    return section

def input_valid_grade(asignature):
    valid_grade = False
    while valid_grade == False:
        print(f"Digite la nota de {asignature}")
        try:
            grade = round(float(input(" > ")),2)
            if grade < 0 or grade > 100:
                raise ValueError("Error: No digitó una nota válida")
            valid_grade = True
        except ValueError as e:
            print(f"\n{e}")
            print("- La nota debe ser un número entre 0 y 100")
            print("- Si lo requiere el número puede tener decimales")
    return grade

def calculate_avg(data):
    for index, student in enumerate(data):
        total_sum = 0
        for asignature in indexed_asignatures:
            total_sum += float(student[asignature['eng']])
        data[index]['avg'] = round((total_sum/4),2)
    return data

def order_by_avg(data):
    return sorted(data, key = lambda x: x["avg"], reverse = True)

def find_student(name, section, data):
    for i, student in enumerate(data):
        if student['name'] == name:
            if student['section'] == section:
                return i, True
    return None, False


