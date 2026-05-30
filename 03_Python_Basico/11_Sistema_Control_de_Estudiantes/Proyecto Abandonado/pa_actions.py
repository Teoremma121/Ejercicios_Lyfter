class DuplicadosError(Exception):
    pass

indexed_asignatures =   [
                        {'index':1,'esp':"Español",'eng':"Spanish"},
                        {'index':2,'esp':"Inglés",'eng':"English"},
                        {'index':3,'esp':"Estudios Sociales",'eng':"Socials"},
                        {'index':4,'esp':"Ciencias",'eng':"Sciences"},
                        {'index':5,'esp':"Matemáticas",'eng':"Math"}
                        ]

def index_to_action(index,actual_data):
    import copy
    data_copy = copy.deepcopy(actual_data)
    joined_index = ".".join(index)
    if joined_index == "exit":
        exit()
    elif index[1] == "1":
        if index[2] == "1":
            add_n_students(actual_data)
        elif index[2] == "2":
            modify(actual_data,index)
        elif index[2] == "3":
            delete_student(actual_data)
    elif index[1] == "2":
        if index[2] == "1":
            show_a_section(data_copy,index)
        elif index[2] == "2":
            show_a_level(data_copy,index)
        elif index[2] == "3":
            show_a_student(data_copy)
    elif index[1] == "3":
        show_best_students(index,data_copy)
    elif index[1] == "4":
        show_failed(index,data_copy)

def add_n_students(data):
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
        for asignature in indexed_asignatures:
            student_info[asignature['eng']]= input_valid_grade(asignature['esp'])
        data.append(student_info)
    print("Se ha agregado correctamente la información de los estudiantes")

def delete_student(data):
    import menu
    index = search_for_a_student(data,"eliminar")
    if index != None:
        print(f"Va a eliminar el estudiante {data[index]['name']} de la sección {data[index]['section']}")
        confirmation = menu.call_yes_or_not()
        if confirmation == "1":
            data.pop(index)
            print("Se ha eliminado el estudiante")
        else:
            print("No se ha eliminado el estudiante")

def show_a_section(data,index):
    section = search_for_a_section(data)
    data = filter_by_section(data,section)
    calculate_avg(data)
    asignature_esp = None
    if index[3] == "3":
        for asignature in indexed_asignatures:
            if asignature['index'] == int(index[4]):
                asignature_key = asignature['eng']
                asignature_esp = asignature['esp']
                break
    data, message = index_to_order(index,data,asignature_esp)
    if section != None:
        print(f"Mostrando la sección {section}{message}")
        if index[3] != "3":
            for student_index, student in enumerate(data):
                print(f"\n#{student_index+1}: {student['name']}")
                for asignature in indexed_asignatures:
                    print(f"{asignature['esp']}: {student[asignature['eng']]}")
                print(f" -Promedio: {student['avg']}")
        else:
            for student_index, student in enumerate(data):
                print(f"#{student_index+1} {student['name']}: {student[asignature_key]}")
            summary = summary_by_asignature(data,asignature_key)
            print(f"\nPromedio de la sección en {asignature_esp}: {summary['avg']}")
            print(f"Nota más alta de la sección en {asignature_esp}: {summary['max']}")
            print(f"Nota más baja de la sección en {asignature_esp}: {summary['min']}")
            print(f"Reprobados en {asignature_esp}: {summary['failed']}")
            
def show_a_level(data,index):
    level = search_for_a_level(data)
    data = filter_by_level(data,level)
    calculate_avg(data)
    asignature_esp = None
    if index[3] == "3":
        for asignature in indexed_asignatures:
            if asignature['index'] == int(index[4]):
                asignature_key = asignature['eng']
                asignature_esp = asignature['esp']
                break
    data, message = index_to_order(index,data,asignature_esp)
    if level != None:
        print(f"Mostrando el nivel {level}{message}")
        if index[3] != "3":
            for student_index, student in enumerate(data):
                print(f"\n#{student_index+1}: {student['name']}, sección {student['section']}")
                for asignature in indexed_asignatures:
                    print(f"{asignature['esp']}: {student[asignature['eng']]}")
                print(f" -Promedio: {student['avg']}")
        else:
            for student_index, student in enumerate(data):
                print(f"#{student_index+1} {student['name']}, sección {student['section']}: {student[asignature_key]}")
            summary = summary_by_asignature(data,asignature_key)
            print(f"\nPromedio del nivel en {asignature_esp}: {summary['avg']}")
            print(f"Nota más alta del nivel en {asignature_esp}: {summary['max']}")
            print(f"Nota más baja del nivel en {asignature_esp}: {summary['min']}")
            print(f"Reprobados en {asignature_esp}: {summary['failed']}")

def show_a_student(data):
    student_to_show_index = search_for_a_student(data)
    if student_to_show_index != None:
        student_info = data[student_to_show_index]
        print(f"\nNombre: {student_info['name']}, Sección: {student_info['section']}")
        print("Notas:")
        total = 0
        for asignature in indexed_asignatures:
            print(f"  -{asignature['esp']}: {student_info[asignature['eng']]}")
            total += float(student_info[asignature['eng']])
        print(f"Promedio: {round(total/5,2)}")

def show_best_students(index,data):
    if index[2] == "1":
        section = search_for_a_section(data)
        message = f" la sección {section}"
        data = filter_by_section(data,section)
        data = calculate_avg(data)
        data = order_by_avg(data)
    elif index[2] == "2":
        message = " cada sección"
        sections = []
        for student in data:
            if student['section'] not in sections:
                sections.append(student['section'])
        agrouped_data = {}
        for section in sections:
            section_data = []
            for student in data:
                if student['section'] == section:
                    section_data.append(student)
            section_data = calculate_avg(section_data)
            section_data = order_by_avg(section_data)
            agrouped_data[section] = section_data
    elif index[2] == "3":
        level = search_for_a_level(data)
        message = f"l nivel {level}"
        data = filter_by_level(data,level)
        data = calculate_avg(data)
        data = order_by_avg(data)
    elif index[2] == "4":
        message = "cada nivel"
        levels = []
        for student in data:
            if student['section'][:-1] not in levels:
                levels.append(student['section'][:-1])
        agrouped_data = {}
        for level in levels:
            level_data = []
            for student in data:
                if student['section'][:-1] == level:
                    level_data.append(student)
            level_data = calculate_avg(level_data)
            level_data = order_by_avg(level_data)
            agrouped_data[level] = level_data
    print(f"Mejores promedios de{message}")
    if index[2] == "1":
        for i in range(3):
            print(f"#{i+1}: {data[i]['name']} - {data[i]['avg']}")
    elif index[2] == "2":
        for section in sections:
            print(f"\nSección {section}")
            for i in range(3):
                print(f"#{i+1}: {agrouped_data[section][i]['name']} - {agrouped_data[section][i]['avg']}")
    elif index[2] == "3":
        for i in range(3):
            print(f"#{i+1}: {data[i]['name']}, Sección {data[i]['section']} - {data[i]['avg']}")
    elif index[2] == "4":
        for level in levels:
            print(f"\nNivel {level}")
            for i in range(3):
                print(f"#{i+1}: {agrouped_data[level][i]['name']}, Sección {agrouped_data[level][i]['section']} - {agrouped_data[level][i]['avg']}")

def show_failed(index,data):
    if index[2] == "1":
        section = search_for_a_section(data)
        data = filter_by_section(data,section)
        message = f"estudiantes reprobados de la sección {section}"
        section_info = ""
    elif index[2] == "2":
        level = search_for_a_level(data)
        data = filter_by_level(data,level)
        message = f"estudiantes reprobados del nivel {level}"
    elif index[2] == "3":
        message = f"todos los estudiantes reprobados"
    total = len(data)
    data = filter_failed_students(data)
    data = sorted(data, key=lambda x: (x['section'], x['name'].lower()))
    failed_percentage = round(100*len(data)/total,2)
    print("Mostrando",message)
    print(f"Porcentaje de reprobados: {failed_percentage} %")
    for student in data:
        if index[2] != "1":
            section_info = f", Sección {student['section']}"
        print(f"\n -{student['name']}{section_info}")
        for asignature in indexed_asignatures:
            if float(student[asignature['eng']]) < 60:
                print(f"  {asignature['esp']}: {student[asignature['eng']]}")

def index_to_order(index,data,asignature):
    if index[3] == "1":
        data = order_alphabetically(data)
        message = " en orden alfabético"
    elif index[3] == "2":
        data = order_by_avg(data)
        message = " en orden de promedios"
    elif index[3] == "3":
        sub_index = int(index[4])
        data = filter_and_order_by_asignature(data,sub_index)
        message = f", resumen de {asignature}"
    return data, message

def filter_by_section(data,section):
    filtered_data = []
    for student in data:
        if student['section'] == section:
            filtered_data.append(student)
    return filtered_data

def filter_by_level(data,level):
    filtered_data = []
    for student in data:
        if level == student['section'][:-1]:
            filtered_data.append(student)
    return filtered_data

def calculate_avg(data):
    for index, student in enumerate(data):
        total = 0
        for asignature in indexed_asignatures:
            total += float(student[asignature['eng']])
        data[index]['avg'] = round((total/5),2)
    return data

def filter_failed_students(data):
    failed_students = []
    for student in data:
        for asignature in indexed_asignatures:
            if float(student[asignature['eng']]) < 60:
                failed_students.append(student)
                break
    return failed_students

def order_by_avg(data):
    data = sorted(data,key=lambda x: x["avg"], reverse=True)
    return data

def order_alphabetically(data):
    data = sorted(data,key=lambda x: x["name"].lower())
    return data

def filter_and_order_by_asignature(data,asignature_index):
    filtered_data = []
    for asignature in indexed_asignatures:
        if asignature['index'] == asignature_index:
            asignature_key = asignature['eng']
    for student in data:
        temp_student = {}
        temp_student['name'] = student['name']
        temp_student['section'] = student['section']
        temp_student[asignature_key] = student[asignature_key]
        filtered_data.append(temp_student)
    ordered_data = sorted(filtered_data,key=lambda x: x[asignature_key], reverse=True)
    return ordered_data

def summary_by_asignature(data,asignature):
    summary = {'max':0,'min':0,'avg':0,'failed':0}
    summary['max'] = max(data, key=lambda x: x[asignature])[asignature]
    summary['min'] = min(data, key=lambda x: x[asignature])[asignature]
    total = 0
    for student in data:
        total += float(student[asignature])
        if float(student[asignature]) < 60:
            summary['failed'] += 1
    summary['avg'] = round(total/len(data),2)
    return summary

def modify(data,menu_index):
    student_index = search_for_a_student(data,"editar")
    if student_index != None:
        if menu_index[3] == "1":
            data[student_index] = edit_name(data,student_index)
        elif menu_index[3] == "2":
            data[student_index] = edit_section(data,student_index)
        elif menu_index[3] == "3":
            data[student_index] = edit_grade(data,student_index,menu_index)

def edit_name(data,index):
    student_info = data[index]
    not_duplicates_found = False
    while not_duplicates_found == False:
        try:
            new_name = input_valid_name("nuevo ")
            check_for_duplicates(student_info['section'],new_name,data)
            student_info['name'] = new_name
            print("Se modificó el nombre del estudiante")
            not_duplicates_found = True
        except DuplicadosError as e:
            print(e)
            print("No pueden haber estudiantes con el mismo nombre y la misma sección")
    return student_info

def edit_section(data,index):
    student_info = data[index]
    not_duplicates_found = False
    while not_duplicates_found == False:
        try:
            new_section = input_valid_section("nueva ")
            check_for_duplicates(new_section,student_info['name'],data)
            student_info['section'] = new_section
            print("Se modificó la sección del estudiante")
            not_duplicates_found = True
        except DuplicadosError as e:
            print(e)
            print("No pueden haber estudiantes con el mismo nombre y la misma sección")
    return student_info

def edit_grade(data,student_index,menu_index):
    student_info = data[student_index]
    for asignature in indexed_asignatures:
        if asignature['index'] == int(menu_index[4]):
            esp_asignature = asignature['esp']
            eng_asignature = asignature['eng']
    student_info[eng_asignature] = input_valid_grade(esp_asignature,"nueva ")
    print(f"Se ha modificado la nota de {esp_asignature}")
    return student_info

def search_for_a_student(data,message="buscar"):
    print(f"Digite el nombre del estudiante que desea {message}:")
    student_to_find = input(" > ")
    print(f"Digite la sección del estudiante que desea {message}:")
    section_to_find = input(" > ")
    for i,student in enumerate(data):
        if (student['name'] == student_to_find) & (student['section'] == section_to_find):
            return i
    print(f"Estudiante con el nombre {student_to_find} de la sección {section_to_find} no se ha encontrado en la base de datos")
    return None
        
def input_quantity_of_students():
    import menu
    valid_quantity = False
    while valid_quantity == False:
        print("¿Cuántos estudiantes desea agregar?")
        try:
            n = int(input(" > "))
            if n < 0:
                raise ValueError
            valid_quantity = True
            if n > 100:
                print(f"Va a agregar de forma continua la información de {n} estudiantes")
                confirmation = menu.call_yes_or_not()
                if confirmation == "2":
                    valid_quantity = False
        except ValueError:
            print("No digitó un número válido")
            print("Debe digitar un número mayor a 0 que corresponda a la cantidad de estudiantes que desea agregar")
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

def search_for_a_section(data):
    valid_section = False
    while valid_section == False:
        print(f"Digite la sección que desea mostrar")
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
    section_exists = False
    for student in data:
        if section == student['section']:
            section_exists = True
    if section_exists == False:
        print("No existe ningún estudiante que pertenezca a esa sección")
        section = None
    return section

def search_for_a_level(data):
    valid_level = False
    while valid_level == False:
        levels = []
        for student in data:
            if student['section'][:-1] not in levels:
                levels.append(student['section'][:-1])
        print(f"Niveles existentes en la base de datos:")
        print(levels)
        print(f"Digite el nivel que desea mostrar")
        try:
            level = input(" > ")
            if (level.isdigit()) & (level in levels):
                valid_level = True
            else:
                raise ValueError("El nivel ingresado no es un número válido")
        except ValueError as e:
            print(e)
            print("Debe digitar un número natural válido que corresponda a alguno de los existentes:")
    return level

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




        

