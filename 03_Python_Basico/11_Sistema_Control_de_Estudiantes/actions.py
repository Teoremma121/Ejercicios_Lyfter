class DuplicadosError(Exception):
    pass

index_descriptions = {
                    "0.1.1":"Agregar estudiantes",
                    "0.1.2":"Editar un estudiante",
                    "0.1.3":"Eliminar un estudiante",
                    "0.2.1.1":"Mostrar estudiantes de una sección/alfabético",
                    "0.2.1.2":"Mostrar estudiantes de una sección/por promedio",
                    "0.2.1.3":"Mostrar estudiantes de una sección/resumen materia",
                    "0.2.2.1":"Mostrar estudiantes de una nivel/alfabético",
                    "0.2.2.2":"Mostrar estudiantes de una nivel/por promedio",
                    "0.2.2.3":"Mostrar estudiantes de una nivel/resumen materia",
                    "0.2.3":"Mostrar la información de un estudiante",
                    "0.3.1":"Top 3 de una sección",
                    "0.3.2":"Top 3 de todas las secciones",
                    "0.3.3":"Top 3 de un nivel",
                    "0.3.4":"Top 3 de todos los niveles",
                    "0.4.1":"Reprobados de una sección",
                    "0.4.2":"Reprobados de un nivel",
                    "0.4.3":"Reprobados de todos los niveles",
                    "0.5":"Exportar datos",
                    "0.6":"Importar datos",}

functions = [{
            'exit':["0.7","0.1.5","0.2.5","0.2.1.5","0.2.1.3.7","0.2.2.5","0.2.2.3.7","0.3.6","0.4.5"],
            'add-modify-delete':["0.1.1","0.1.2","0.1.3"]
            }]

asignatures = {
                'Spanish':'Español',
                'English':'Inglés',
                'Socials':'Estudios Sociales',
                'Sciences':'Ciencias',
                'Math':'Matemáticas'
                }

def index_to_action(index,actual_data):
    data = actual_data
    joined_index = ".".join(index)
    if joined_index in functions[0]['exit']:
        exit()
    if index[1] == "1":
        if index[2] == "1":
            data = add_n_students(data)
        elif index[2] == "2":
            data = modify(data,index)
        elif index[2] == "3":
            data = delete_student(data)
    else:
        print(index_descriptions[joined_index])
    return data

def add_n_students(actual_data):
    data = actual_data
    n = input_quantity_of_students()
    for i in range(n):
        student_info = {}
        not_duplicates_found = False
        while not_duplicates_found == False:
            try:
                print(f"\nIngresando estudiante {i+1} de {n}")
                student_info['name'] = input_valid_name()
                student_info['section'] = input_valid_section()
                check_for_duplicates(student_info['section'],student_info['name'],data)
                not_duplicates_found = True
            except DuplicadosError as e:
                print(e)
                print("No pueden haber estudiantes con el mismo nombre y la misma sección")
        student_info['grades'] = {}
        for eng, esp in asignatures.items():
            student_info["grades"][eng]= input_valid_grade(esp)
        data.append(student_info)
    print("Se ha agregado correctamente la información de los estudiantes")
    return data

def modify(actual_data,index):
    data = actual_data
    indexed_asignatures = ['0','Español','Inglés','Estudios Sociales','Ciencias','Matemáticas']
    print("Digite el nombre del estudiante que desea buscar para editar:")
    student_to_modify = input(" > ")
    print("Digite la sección del estudiante que desea buscar para editar:")
    student_to_modify_section = input(" > ")
    student_found = False
    for i,student in enumerate(data):
        if (student['name'] == student_to_modify) & (student['section'] == student_to_modify_section):
            student_found = True
            if index[3] == "1":
                not_duplicates_found = False
                while not_duplicates_found == False:
                    try:
                        new_name = input_valid_name("nuevo ")
                        check_for_duplicates(data[i]['section'],new_name,data)
                        data[i]['name'] = new_name
                        print("Se modificó el nombre del estudiante")
                        not_duplicates_found = True
                    except DuplicadosError as e:
                        print(e)
                        print("No pueden haber estudiantes con el mismo nombre y la misma sección")
            elif index[3] == "2":
                not_duplicates_found = False
                while not_duplicates_found == False:
                    try:
                        new_section = input_valid_section("nueva ")
                        check_for_duplicates(new_section,data[i]['name'],data)
                        data[i]['section'] = new_section
                        print("Se modificó la sección del estudiante")
                        not_duplicates_found = True
                    except DuplicadosError as e:
                        print(e)
                        print("No pueden haber estudiantes con el mismo nombre y la misma sección")
            elif index[3] == "3":
                new_grade = input_valid_grade(indexed_asignatures[int(index[4])],"nueva ")
                for eng, esp in asignatures.items():
                    if esp == indexed_asignatures[int(index[4])]:
                        student['grades'][eng] = new_grade
                        print(f"Se ha modificado la nota de {esp}")
    if student_found == False:
        print(f"El estudiante con el nombre {student_to_modify} de la sección {student_to_modify_section} no se ha encontrado en la base de datos")
    return data

def delete_student(actual_data):
    data = actual_data
    print("Digite el nombre del estudiante que desea eliminar")
    student_to_delete = input(" > ")
    print("Digite la sección del estudiante que desea eliminar:")
    student_to_delete_section = input(" > ")
    student_found = False
    for i,student in enumerate(data):
            if (student['name'] == student_to_delete) & (student['section'] == student_to_delete_section):
                data.pop(i)
                print("Se ha eliminado el estudiante")
                student_found = True
    if student_found == False:
        print(f"El estudiante con el nombre: {student_to_delete} de la sección {student_to_delete_section} no se ha encontrado en la base de datos")
    return data
        
def input_quantity_of_students():
    valid_quantity = False
    while valid_quantity == False:
        print("¿Cuántos estudiantes desea agregar?")
        try:
            n = int(input(" > "))
            valid_quantity = True
        except ValueError:
            print("No digitó un número válido")
            print("Debe digitar un número natural que corresponda a la cantidad de estudiantes que desea agregar")
    return n

def input_valid_name(message=""):
    valid_name = False
    while valid_name == False:
        print(f"Digite el {message}nombre del estudiante")
        try:
            name = input(" > ")
            for char in name:
                if char.isdigit() == True:
                    raise ValueError("El nombre no puede contener números")
            if name == "":
                raise ValueError("No digitó un nombre")
            valid_name = True
        except ValueError as e:
            print(e)
            print("Digite un nombre correcto que cumpla las condiciones")
            print("El nombre no puede estar vacío y no puede contener números")
    return name

def check_for_duplicates(section,name,data):
    for i, student in enumerate(data):
        if student['name'] == name:
            if data[i]['section'] == section:
                raise DuplicadosError("Ya existe un estudiante con el mismo nombre y la misma sección")

def input_valid_section(message=""):
    valid_section = False
    while valid_section == False:
        print(f"Digite la {message}sección del estudiante (Ejemplo: 11B)")
        try:
            section = input(" > ")
            if section[:-1].isdigit() & section[-1].isupper():
                valid_section = True
            else:
                raise ValueError("La sección ingresada no cumple con el formato")
        except ValueError as e:
            print(e)
            print("Debe digitar una sección válida siguiendo el formato 'nivel-sección'")
            print("Por ejemplo: 7A, 7B, 8A, 9C, 10A, etc")
    return section

def input_valid_grade(asignature,message=""):
    valid_note = False
    while valid_note == False:
        print(f"Digite la {message}nota de {asignature}")
        try:
            grade = round(float(input(" > ")),2)
            if grade < 0 or grade > 100:
                raise ValueError
            valid_note = True
        except ValueError:
            print("- No digitó una nota válida")
            print("- La nota debe ser un número entre 0 y 100")
            print("- Si lo requiere el número puede tener decimales")
    return grade




        

