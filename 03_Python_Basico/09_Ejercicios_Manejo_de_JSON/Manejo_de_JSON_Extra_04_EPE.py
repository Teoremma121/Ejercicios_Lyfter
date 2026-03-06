# Ejercicios Extra de Manejo de JSON - Python Básico
# Emmanuel Piedra Esquivel
# Programa 03:
# ree un programa que abra un archivo .json con la información de Pokémon 
# (en base al JSON que fue generado en el ejercicio 1) y:
# - Lea el archivo JSON
# - Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# - Calcule y muestre el promedio de nivel para cada tipo:

def main(path):
    all_151_pokemon = read_json_file(path)
    avg_level_per_type = calculate_avg_level_by_pokemon_type(all_151_pokemon)
    print("A continuación se muestra el promedio de nivel para cada tipo")
    for pokemon_type, avg_level in avg_level_per_type.items():
        print(f"Tipo {pokemon_types_dict[pokemon_type]} → Promedio de nivel: {avg_level}")

def read_json_file(file_path):
    import json
    with open(file_path,'r',encoding='utf-8') as file:
        list_of_dictionaries = json.load(file)
    return list_of_dictionaries

pokemon_types_dict = {
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

def calculate_avg_level_by_pokemon_type(pokemon_list):
    avg_level_per_type = {}
    for pokemon_type in pokemon_types_dict:
        total_level_sum = 0
        count_pokemon = 0
        for pokemon in pokemon_list:
            if pokemon_type in pokemon['type']:
                count_pokemon += 1
                total_level_sum += pokemon['level']
        if count_pokemon == 0:
            avg_level_per_type[pokemon_type] = "-- (No hay pokemon de este tipo)"
        else:
            avg_level_per_type[pokemon_type] = round(total_level_sum/count_pokemon,1)
    return avg_level_per_type

main("pokemon_151_dataset.json")