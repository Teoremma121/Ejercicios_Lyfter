def index_to_data_manage(index,data):
    if index == "7":
        export_data(data)
        return data
    elif index == "8":
        imported_data = import_data(data)
        return imported_data

def export_data(data):
    headers = ['name','section','Spanish','English','Socials','Sciences']
    import csv
    with open("notas.csv",'w',encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)
    print("\n--La información ha sido exportada al archivo 'notas.csv'--")

def import_data(data):
    import csv
    imported_data = []
    try:
        with open("notas.csv",'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                imported_data.append(row)
    except FileNotFoundError:
        print("\nError: No existe un archivo con datos previamente exportados")
        return data
    print("--Ha sido importada la información del archivo 'notas.csv'--")
    return imported_data