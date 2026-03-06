# Ejercicios Extra de Manejo de JSON - Python Básico
# Emmanuel Piedra Esquivel
# Programa 01:
# Cree un programa que abra un archivo .json con la información de Pokémon 
# (en base al JSON que fue generado en el ejercicio 1) y:
# - Lea el archivo JSON de Pokémon
# - Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel
# (o cualquier otro atributo definido)

def main(path):
    all_151_pokemon = read_json_file(path)
    print_pokemon_info(all_151_pokemon)

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

legible_stats = {
                'HP':"Puntos de Salud",
                'Attack':"Ataque",
                'Defense':"Defensa",
                'Sp. Attack':"Ataque Especial",
                'Sp. Defense':"Defensa Especial",
                'Speed':"Velocidad"
                }

def print_pokemon_info(list_of_pokemon):    
    for index, pokemon in enumerate(list_of_pokemon):
        print(f"\n#{index+1}: {pokemon['name']['english']}")
        translated_types = []
        for pokemon_type in pokemon['type']:
            translated_types.append(spanish_types[pokemon_type])
        print(f"Tipo: {" / ".join(translated_types)}")
        print(f"Nivel: {pokemon['level']}")
        print("Estadísticas base:")
        for stat, value in pokemon['base'].items():
            print(f" - {legible_stats[stat]}: {value}")

main("pokemon_151_dataset.json")