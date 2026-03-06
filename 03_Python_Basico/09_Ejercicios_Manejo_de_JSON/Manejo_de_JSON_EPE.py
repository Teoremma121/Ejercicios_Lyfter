# Ejercicios de Manejo de JSON - Python Básico
# Emmanuel Piedra Esquivel
# Programa 01:
# Investigue cómo leer y escribir archivos JSON en Python aquí.
# Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON (https://learning.lyfter.team/dashboard/roadmap/fffab4f1-5c3f-480a-9671-ae1a235c3b6a/dac6b243-2cab-496f-96de-5debb9ce613e)
# Debe leer el archivo para importar los Pokémones existentes.
# Luego debe pedir la información del Pokémon a agregar.
# Finalmente debe guardar el nuevo Pokémon en el archivo.

def main(path):
    list_of_pokemon = read_json_file(path)
    list_of_pokemon.append(ask_for_pokemon_info())
    write_json_file(path,list_of_pokemon)

def read_json_file(file_path):
    import json
    with open(file_path,'r',encoding='utf-8') as file:
        list_of_dictionaries = json.load(file)
    return list_of_dictionaries

def write_json_file(file_path,new_object):
    import json
    with open(file_path,'w',encoding='utf-8') as file:
        json.dump(new_object,file,indent=3)
    print("\nSe ha reescrito el archivo json")

def ask_for_pokemon_info():
    new_pokemon = {}
    new_pokemon['name'] = ask_for_name()
    new_pokemon['level'] = ask_for_level()
    new_pokemon['type'] = ask_for_type()
    new_pokemon['base'] = ask_for_base_stats()
    print(f"\nFue almacenada la información del pokemon {new_pokemon['name']['english']}")
    print(new_pokemon)
    return new_pokemon

def ask_for_name():
    names = {}
    names['english'] = input("Digite el nombre del pokemon:\n> ")
    other_language = True
    while other_language == True:
        print("\n¿Desea agregar el nombre en otro idioma?")
        valid_answer = False
        while valid_answer == False:
            try:
                answer = input('Digite "SI" o "NO"\n> ')
                if answer == "SI":
                    valid_answer = True
                    languages = [0,'japanese','french','german']
                    languages_spanish = [0, 'japonés', 'francés', 'alemán']
                    language_index = ask_for_language_index()
                    names[languages[language_index]] = input(f"\nDigite el nombre del pokemon en idioma {languages_spanish[language_index]}:> ")
                elif answer == "NO":
                    valid_answer = True
                    other_language = False
                else:
                    raise ValueError("Debe digitar únicamente 'SI' o 'NO'")
            except ValueError as e:
                print(f"{e}")
    return names

def ask_for_language_index():
    valid_index = False
    while valid_index == False:
        try:
            print("\nDigite el número de índice para elegir un idioma:")
            print("1 - japonés\n2 - francés\n3 - alemán")
            language_index = int(input("> "))
            if language_index in range(1,4):
                valid_index = True
            else:
                raise ValueError("El número digitado es menor que 1 o mayor que 3")
        except ValueError as e:
            print(f"\nHa ocurrido un error!\nDetalles: {e}")
            print(f"Debe digitar un número válido que sea 1, 2 o 3")
    return language_index

def ask_for_level():
    level = 0
    valid_level = False
    while valid_level == False:
        try:
            level = int(input("\nDigite el nivel del pokemon:\n> "))
            if level in range(1,100):
                valid_level = True
            else:
                raise ValueError("Un pokemon no puede tener un nivel menor a 1 o mayor a 100")
        except ValueError as e:
            print(f"\nHa ocurrido un error!\nDetalles: {e}")
            print("Debe digitar un número entre 1 y 100.")
    return level

def ask_for_type():
    valid_types = ['Water','Steel','Bug','Dragon','Electric','Ghost','Fire','Fairy','Ice','Fighting','Normal','Grass','Psychic','Rock','Dark','Ground','Poison','Flying']
    types = []
    valid_type_01 = False
    while valid_type_01 == False:
        try:
            type_1 = input("\nDigite en inglés el primer tipo del pokemon:\n> ")
            if type_1 in valid_types:
                valid_type_01 = True
                types.append(type_1)
            else:
                raise ValueError("Debe ingresar un tipo de pokemon válido")
        except ValueError as e:
            print(f"\nHa ocurrido un error!\nDetalles: {e}")
            print(f"Debe ingresar un tipo de los 18 disponibles:\n{valid_types}")
    valid_type_02 = False
    while valid_type_02 == False:
        try:
            type_2 = input("\nDigite en inglés un segundo tipo para el pokemon o presione\nENTER si el pokemon no tiene segundo tipo:\n> ")
            if type_2 in valid_types:
                valid_type_02 = True
                types.append(type_2)
            elif type_2 == "":
                valid_type_02 = True
            else:
                raise ValueError("Debe ingresar un tipo de pokemon válido\no presionar ENTER para ningún tipo")
        except ValueError as e:
            print(f"\nHa ocurrido un error.\nDetalles: {e}")
            print(f"Debe ingresar un tipo de los 18 disponibles:\n{valid_types}")
    return types

def ask_for_base_stats ():
    stats_names = {'HP':"Puntos de Salud",'Attack':"Ataque",'Defense':"Defensa",'Sp. Attack':"Ataque Especial",'Sp. Defense':"Defensa Especial",'Speed':"Velocidad"}
    base_stats = {}
    for key in stats_names.keys():
        base_stats[key] = ask_for_valid_number(stats_names[key])
    return base_stats

def ask_for_valid_number(stat_type):
    valid_stat = False
    while valid_stat == False:
        try:
            stat = int(input(f"\nDigite {stat_type} base:\n> "))
            valid_stat = True
        except ValueError as e:
            print(f"\nHa ocurrido un error!\nDetalles: {e}")
            print("Debe digitar un número natural válido para cada estadística.")
    return stat

main("pokemon.json")

# English: Froslass
# Japanese: Yukimenoko
# French: Momartik
# German: Frosdedje
# Tipos: Hielo/Fantasma
# HP: 70
# Ataque: 80
# Defensa: 70
# At. esp: 80
# Def. esp: 70
# Velocidad: 110

    