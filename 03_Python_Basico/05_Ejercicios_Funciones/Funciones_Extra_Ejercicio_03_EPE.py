# Ejercicios Extra de Funciones - Python Básico
# Emmanuel Piedra Esquivel
# Ejercicio 03:
# Cree una función que reciba un string y retorne cuántas vocales contiene

def count_vowels(full_string):
    count = 0
    for char in full_string.lower():
        if char in "aáeéiíoóuúü":
            count += 1
    return count

text = "La Iguana Ana toma café de Orosi"

print(f"La cantidad de vocales en el texto es: {count_vowels(text)}")