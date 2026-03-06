# Ejercicios Extra de Manejo de CSVs - Python Básico
# Emmanuel Piedra
# Programa 03:
# Cree un programa que abra un archivo .csv con la información de videojuegos (en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada

def count_in_csv(file_path):
    all_genres_found = []
    import csv
    try:
        with open(file_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                all_genres_found.append(row['Género'])
    except FileNotFoundError as e:
        print(f"\nHa ocurrido un error:\n- {e}")
        print("- La dirección es incorrecta o no existe un archivo con ese nombre")
        print("\nEl programa se va a cerrar...")
        exit()
    games_per_genre = count_frequencies_in_list(all_genres_found)
    print("Géneros encontrados:")
    for key, value in games_per_genre.items():
        print(f"{key}: {value}")

def count_frequencies_in_list(full_list):
    frequencies = {}
    for element in full_list:
        frequencies[element] = full_list.count(element)
    return frequencies

count_in_csv("videogames.csv")



