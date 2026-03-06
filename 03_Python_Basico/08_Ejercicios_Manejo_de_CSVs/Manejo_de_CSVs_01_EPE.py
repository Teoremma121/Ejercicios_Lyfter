# Ejercicios de Manejo de CSVs - Python Básico
# Emmanuel Piedra
# Programa 01:
# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# Debe incluir:
# - Nombre
# - Género
# - Desarrollador
# - Clasificación ESRB

def main():
    videogames = ask_for_n_games()
    write_csv(videogames, videogames[0].keys(), "videogames01.csv")
    print("\nInformación digitada en el archivo CSV:")
    check_csv("videogames01.csv")

def ask_for_n_games():
    all_games = []
    n = int(input("¿Cuántos videojuegos desea ingresar en la base de datos?\n> "))
    for index in range(1,n+1):
        print(f"\nEstá digitando la información del juego número: {index}")
        all_games.append(ask_info_per_game())
    return all_games

def ask_info_per_game():
    videogame_dict = {}
    videogame_dict['Título'] = input(" - Digite el nombre del videojuego: ")
    videogame_dict['Género'] = input(" - Digite el género al que pertenece el videojuego: ")
    videogame_dict['Desarrollador'] = input(" - Digite el desarrollador del videojuego: ")
    videogame_dict['Clasificación_ESRB'] = input(" - Digite la clasificación ESRB del videojuego: ")
    return videogame_dict

def write_csv(list_of_dictionaries, headers, file_path):
    import csv
    with open(file_path, "w", encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(list_of_dictionaries)

def check_csv(file_path):
    import csv
    with open(file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

main()



