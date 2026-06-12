# Ejercicios de Unit Testing - Python Intermedio
# Emmanuel Piedra Esquivel
# Módulo de funciones:

# 1. Cree los siguientes unit tests para el algoritmo bubble_sort:
#   - Funciona con una lista pequeña.
#   - Funciona con una lista grande (de más de 100 elementos.)
#   - Funciona con una lista vacía.
#   - No funciona con parámetros que no sean una lista.

def bubble_sort(list_for_sort):
    print(f"Orden inicial: {list_for_sort}")
    for round in range(len(list_for_sort)):
        iterated_element = list_for_sort[0]
        for iteration in range(len(list_for_sort)-round-1):
            if iterated_element > list_for_sort[iteration+1]:
                list_for_sort[iteration] = list_for_sort[iteration+1]
                list_for_sort[iteration+1] = iterated_element
            else:
                iterated_element = list_for_sort[iteration+1]
            print(f"Recorrido: {round+1}, Iteración: {iteration+1}, {list_for_sort}")
    print(f"Orden final: {list_for_sort}")
    return list_for_sort


# 2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de funciones (exceptuando el 1 y 2). Enlace:
# https://learning.lyfter.team/dashboard/duad/roadmap/python-bsico/activity/ejercicios-de-funciones

def sum_all_numbers(nums_list):
    sum = 0
    for number in nums_list:
        sum += number
    return sum

def reverse_text(original_string):
    reversed_text = ""
    for index in range(len(original_string)-1,-1,-1):
        reversed_text += original_string[index]
    return reversed_text

def count_capital_or_lower(text):
    capital_letters = 0
    lower_case = 0
    for char in text:
        if char.isupper():
            capital_letters += 1
        elif char.islower():
            lower_case += 1
    print(f"""En el texto hay:
        - {capital_letters} mayúsculas
        - {lower_case} minúsculas""")
    return capital_letters, lower_case

def order_alphabetically(string):
    list = string.split("-")
    ordered_list = sorted(list, key=str.lower)
    ordered_string = "-".join(ordered_list)
    return ordered_string

def check_list_for_primes(list):
    primes = []
    for n in list:
        if check_prime(n):
            primes.append(n)
    return primes

def check_prime(number):
    if number == 1:
        is_prime = False
    else:
        is_prime = True
        for n in range(2,int(number**0.5)+1):
            if number%n == 0:
                is_prime = False
                break
    return is_prime
