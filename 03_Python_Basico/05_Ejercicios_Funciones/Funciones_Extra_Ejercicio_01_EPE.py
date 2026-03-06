# Ejercicios Extra de Funciones - Python Básico
# Emmanuel Piedra Esquivel
# Ejercicio 01:
# Cree una función que reciba un texto y un carácter, y retorne cuántas veces
# aparece ese carácter en el texto

def ask_text():
    text = input("Escriba el texto a revisar: ")
    return text

def ask_character():
    character = input("Digite el caracter que desea buscar y contar: ")
    return character

def count_char_in_text(full_text = ask_text(), char_to_look = ask_character()):
    count = 0
    for char in full_text:
        if char == char_to_look:
            count += 1
    return count

# Por default usa input para solicitar los datos a la persona usuaria:
print(f"El caracter aparece {count_char_in_text()} veces en el texto.")


# Pero también funciona usando datos predefinidos:
tongue_twister = "A flea and a fly flew up in a flue"
letter = "f"

print("")
print(count_char_in_text(tongue_twister, letter))
