# Ejercicios Extra de Manejo de JSON - Python Básico
# Emmanuel Piedra Esquivel
# Programa 02:
# Cree un programa que abra un archivo .json con la información de Pokémon
# (en base al JSON que fue generado en el ejercicio 1) y:
# - Lea el archivo JSON de Pokémon
# - Pida al usuario un tipo de Pokémon
# - Muestre todos los Pokémon que sean de ese tipo

def main(path):
    all_151_pokemon = read_json_file(path)
    filtered_pokemon = filter_by_pokemon_type(ask_for_pokemon_type(), all_151_pokemon)
    if len(filtered_pokemon) == 0:
        print("\nNo se encontraron pokemon de este tipo")
    else:
        print("\nLos pokemon que tienen este tipo son:")
        for pokemon in filtered_pokemon:
            print(f"- {pokemon}")

def read_json_file(file_path):
    import json
    with open(file_path,'r',encoding='utf-8') as file:
        list_of_dictionaries = json.load(file)
    return list_of_dictionaries

spanish_types = {
                'Water':"Agua",
                'Steel':"Acero",
                'Bug':"Bicho",
                'Dragon':"Dragón",
                'Electric':"Eléctrico",
                'Ghost':"Fantasma",
                'Fire':"Fuego",
                'Fairy':"Hada",
                'Ice':"Hielo",
                'Fighting':"Lucha",
                'Normal':"Normal",
                'Grass':"Planta",
                'Psychic':"Psíquico",
                'Rock':"Roca",
                'Dark':"Siniestro",
                'Ground':"Tierra",
                'Poison':"Veneno",
                'Flying':"Volador"
                }

def ask_for_pokemon_type():
    valid_pokemon_type = False
    while valid_pokemon_type == False:
        try:
            pokemon_type_to_found = input("\nDigite el tipo de pokemon para filtrar:\n> ")
            if pokemon_type_to_found in spanish_types.values():
                valid_pokemon_type = True
            else:
                raise ValueError("Debe ingresar un tipo de pokemon válido")
        except ValueError as e:
            print(f"\nHa ocurrido un error!\nDetalles: {e}")
            print(f"Debe ingresar un tipo de los 18 disponibles:")
            for value in spanish_types.values():
                print(f" - {value}")
    for english, spanish in spanish_types.items():
        if spanish == pokemon_type_to_found:
            pokemon_type_to_found = english
            break
    return pokemon_type_to_found

def filter_by_pokemon_type(pokemon_type,pokemon_list):
    filtered_pokemon = []
    for pokemon in pokemon_list:
        if pokemon_type in pokemon['type']:
            filtered_pokemon.append(pokemon['name']['english'])
    return filtered_pokemon

main("pokemon_151_dataset.json")

