# Ejercicios de Funciones - Python Básico
# Emmanuel Piedra Esquivel
# Ejercicio 04:
# Cree una función que le dé la vuelta a un string y lo retorne.

def reverse_text(original_string):
    reversed_text = ""
    for index in range(len(original_string)-1,-1,-1):
        reversed_text += original_string[index]
    return reversed_text

secret_word = "stnaPerauqS boBegnopS"
secret_word_2 = "amoR y zorrA"

print(reverse_text(secret_word))
print(reverse_text(secret_word_2))
