# Ejercicios de Funciones - Python Básico
# Emmanuel Piedra Esquivel
# Ejercicio 03:
# Cree una función que retorne la suma de todos los números de una lista.
# La función va a tener un parámetro (la lista) y retornar un número (la suma 
# de todos sus elementos).

def sum_all_numbers (list):
    sum = 0
    for number in list:
        sum += number
    return sum

list_01 = [15, 85, 26, 74, 51, 13, 12]
list_02 = [4, 6, 2, 29]

print(sum_all_numbers(list_01))
print(sum_all_numbers(list_02))
