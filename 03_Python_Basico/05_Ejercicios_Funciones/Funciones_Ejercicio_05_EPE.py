# Ejercicios de Funciones - Python Básico
# Emmanuel Piedra Esquivel
# Ejercicio 05:
# Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.

def count_capital_or_lower(string):
    print(f"""En el texto hay:
        - {count_capital_letters(string)} mayúsculas
        - {count_lower_case(string)} minúsculas""")
    
def count_capital_letters(string):
    capital_letters = 0
    for char in string:
        if char.isupper() == True:
            capital_letters += 1
    return capital_letters

def count_lower_case(string):
    lower_case = 0
    for char in string:
        if char.islower() == True:
            lower_case += 1
    return lower_case


password = "T0T0r0.C4lc1f3r"
sentence = "Comí 5 manzanas"

count_capital_or_lower(password)
count_capital_or_lower(sentence)


