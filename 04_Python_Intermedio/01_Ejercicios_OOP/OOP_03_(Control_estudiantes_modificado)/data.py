def index_to_data_manage(index,data):
    if index == "7":
        export_data(data)
        return data
    elif index == "8":
        imported_data = import_data(data)
        return imported_data

def export_data(data):
    import csv
    from actions import Student
    headers = ['name','section','spanish','english','socials','sciences']
    exported_data = []
    for student_object in data:
        student_dict = {}
        for attribute in headers:
            student_dict[attribute] = getattr(student_object, attribute)
        exported_data.append(student_dict)
    with open("notas.csv",'w',encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(exported_data)
    print("\n--La información ha sido exportada al archivo 'notas.csv'--")

def import_data(data):
    import csv
    from actions import Student
    imported_data = []
    try:
        with open("notas.csv",'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            for row in reader:
                student = Student("none","none",0,0,0,0)
                for attribute in headers:
                    setattr(student, attribute, row[attribute])
                imported_data.append(student)
    except FileNotFoundError:
        print("\nError: No existe un archivo con datos previamente exportados")
        return data
    print("--Ha sido importada la información del archivo 'notas.csv'--")
    return imported_data