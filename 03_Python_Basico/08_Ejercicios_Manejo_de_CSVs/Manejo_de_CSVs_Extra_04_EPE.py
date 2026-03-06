# Ejercicios Extra de Manejo de CSVs - Python Básico
# Emmanuel Piedra
# Programa 04:
# Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
# Muestre todos los videojuegos desarrollados por esa empresa en formato legible:

def search_in_csv(file_path):
    developer = input("Digite el nombre de un desarrollador para filtrar los videojuegos:\n> ") 
    filtered_games = []
    import csv
    try:
        with open(file_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Desarrollador'] in developer or developer in row['Desarrollador']:
                    game = f"{row['Título']} (Clasificación: {row['Clasificación']}, Género: {row['Género']})"
                    filtered_games.append(game)
    except FileNotFoundError as e:
        print(f"\nHa ocurrido un error:\n- {e}")
        print("- La dirección es incorrecta o no existe un archivo con ese nombre")
        print("\nEl programa se va a cerrar...")
        exit()
    print_games_if_any(filtered_games,developer)

def print_games_if_any(list_of_games, category):
    if len(list_of_games) == 0:
        print(f"\nNo existe ningún juego en la base de datos que pertenezca al desarrollador: {category}")
    else:
        print(f"\nA continuación se muestran todos los juegos desarrollados por {category}")
        print(f"Total de juegos encontrados: {len(list_of_games)}")
        for game in list_of_games:
            print(f"- {game}")

search_in_csv("videogames.csv")



