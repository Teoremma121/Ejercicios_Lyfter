# Ejercicios Extra de Funciones - Python Básico
# Emmanuel Piedra Esquivel
# Ejercicio 02:
# Cree una función que reciba una lista de palabras y un número n, y retorne
# una nueva lista con solo las palabras que tengan más de n letras

def ask_list():
    entry_list = input("""Digite una lista de palabras siguiendo el siguiente formato:
> cielo, sol, maravilloso, día
> """)
    return entry_list.split(", ")

def ask_size():
    entry_n = int(input("Ingrese el número mínimo de letras que deben tener las palabras: "))
    return entry_n

def look_words_larger_than_n(full_list = ask_list(), n = ask_size()):
    new_list = []
    for word in full_list:
        if len(word) >= n:
            new_list.append(word)
    return new_list

# Por default usa input para solicitar los datos a la persona usuaria:
print(f"""
Las palabras que tienen la cantidad mínima de letras son:
{look_words_larger_than_n()}""")

# También funciona usando datos predefinidos:
predefined_list = ["Quartz", "Amathyst", "Pearl", "Garnet", "Rubi", "Zaphire"]
predefined_size = 6

print()
print(look_words_larger_than_n(predefined_list,predefined_size))
