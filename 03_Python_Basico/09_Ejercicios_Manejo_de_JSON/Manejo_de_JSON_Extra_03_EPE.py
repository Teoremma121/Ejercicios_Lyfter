# Ejercicios Extra de Manejo de JSON - Python Básico
# Emmanuel Piedra Esquivel
# Programa 03:
# Cree un programa que abra un archivo .json con la información de Pokémon
# (en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

def main(path):
    all_151_pokemon = read_json_file(path)
    print_pokemon_stats(all_151_pokemon)

def read_json_file(file_path):
    import json
    with open(file_path,'r',encoding='utf-8') as file:
        list_of_dictionaries = json.load(file)
    return list_of_dictionaries

legible_stats = {
                'HP':"Puntos de Salud",
                'Attack':"Ataque",
                'Defense':"Defensa",
                'Sp. Attack':"Ataque Especial",
                'Sp. Defense':"Defensa Especial",
                'Speed':"Velocidad"
                }

def print_pokemon_stats(list_of_pokemon):    
    stats_for_print = ['Attack','Defense','Speed']
    for index, pokemon in enumerate(list_of_pokemon):
        print(f"\n#{index+1}: {pokemon['name']['english']}")
        for stat in stats_for_print: 
            print(f" - {legible_stats[stat]}: {pokemon['base'][stat]}")

main("pokemon_151_dataset.json")