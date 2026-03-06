# Ejercicios Extra de Manejo de CSVs - Python Básico
# Emmanuel Piedra
# Programa 02:
# Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación

def search_in_csv(file_path):
    category = ask_for_esrb()
    filtered_games = []
    import csv
    try:
        with open(file_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Clasificación'] == category:
                    filtered_games.append(row['Título'])
    except FileNotFoundError as e:
        print(f"\nHa ocurrido un error:\n- {e}")
        print("- La dirección es incorrecta o no existe un archivo con ese nombre")
        print("\nEl programa se va a cerrar...")
        exit()
    print_games_if_any(filtered_games,category)

def ask_for_esrb():
    esrb_list = ["E","E10+","T","M","AO"]
    valid_esrb = False
    while valid_esrb == False:
        try:
            esrb_to_find = input("\nDigite una clasificación ESRB para filtrar los juegos:\n> ")
            if esrb_to_find in esrb_list:
                valid_esrb = True
            else:
                raise ValueError("\nEl texto digitado no es una clasificación ESRB válida")
        except ValueError as e:
            print(f"{e}\nPuede digitar únicamente una opción de las siguientes:")
            for i in esrb_list:
                print(f"- {i}")
    return esrb_to_find

def print_games_if_any(list_of_games, category):
    if len(list_of_games) == 0:
        print("\nNo hay ningún juego en la base de datos que cumpla con la categoría")
    else:
        print(f"\nA continuación se muestran todos los juegos que corresponden a la Categoría ESRB = {category}")
        print(f"Total de juegos encontrados: {len(list_of_games)}")
        for game in list_of_games:
            print(f"- {game}")

search_in_csv("videogames.csv")



