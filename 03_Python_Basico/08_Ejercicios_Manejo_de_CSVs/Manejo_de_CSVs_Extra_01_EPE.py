# Ejercicios Extra de Manejo de CSVs - Python Básico
# Emmanuel Piedra
# Programa 01:
# Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea

def print_from_csv(file_path):
    import csv
    with open(file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key, value in row.items():
                print(f"{key}: {value}")
            print()

print_from_csv("videogames.csv")



