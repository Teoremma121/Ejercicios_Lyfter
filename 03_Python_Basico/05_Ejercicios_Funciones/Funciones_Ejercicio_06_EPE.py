# Ejercicios de Funciones - Python Básico
# Emmanuel Piedra Esquivel
# Ejercicio 06:
# Cree una función que acepte un string con palabras separadas por un guion y
# retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def order_alphabetically(string):
    list = string.split("-")
    ordered_list = sorted(list, key=str.lower)
    ordered_string = "-".join(ordered_list)
    return ordered_string

TI_concepts = "python-variable-funcion-computadora-monitor"
fruits = "pineapple-watermelon-strawberry-banana-papaya-lemon"

print(order_alphabetically(TI_concepts))
print(order_alphabetically(fruits))