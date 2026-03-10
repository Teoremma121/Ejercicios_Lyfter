headers = ['name','section','Spanish','English','Socials','Sciences','Math']


def index_to_data_manage(index,current_data):
    if index[1] == "5":
        export_data(current_data)
        return current_data
    else:
        updated_data = import_data()
        return updated_data

def export_data(data):
    import csv
    with open("notas.csv",'w',encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)
    print("La información ha sido exportada al archivo 'notas.csv'")

def import_data():
    import csv
    imported_data = []
    with open("notas.csv",'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            imported_data.append(row)
    print("Ha sido importada la información del archivo 'notas.csv'")
    return imported_data
        