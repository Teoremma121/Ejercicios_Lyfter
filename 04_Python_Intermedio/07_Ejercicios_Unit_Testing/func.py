# Ejercicios de Unit Testing - Python Intermedio
# Emmanuel Piedra Esquivel
# Módulo de funciones:

# 1. Cree los siguientes unit tests para el algoritmo bubble_sort:
#   - Funciona con una lista pequeña.
#   - Funciona con una lista grande (de más de 100 elementos.)
#   - Funciona con una lista vacía.
#   - No funciona con parámetros que no sean una lista.
# 
# 2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de funciones (exceptuando el 1 y 2). Enlace:
# https://learning.lyfter.team/dashboard/duad/roadmap/python-bsico/activity/ejercicios-de-funciones

def sum_all_numbers (list):
    sum = 0
    for number in list:
        sum += number
    return sum

list_01 = [15, 85, 26, 74, 51, 13, 12]
list_02 = [4, 6, 2, 29]

print(sum_all_numbers(list_01))
print(sum_all_numbers(list_02))

def reverse_text(original_string):
    reversed_text = ""
    for index in range(len(original_string)-1,-1,-1):
        reversed_text += original_string[index]
    return reversed_text

secret_word = "stnaPerauqS boBegnopS"
secret_word_2 = "amoR y zorrA"

print(reverse_text(secret_word))
print(reverse_text(secret_word_2))

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

def order_alphabetically(string):
    list = string.split("-")
    ordered_list = sorted(list, key=str.lower)
    ordered_string = "-".join(ordered_list)
    return ordered_string

TI_concepts = "python-variable-funcion-computadora-monitor"
fruits = "pineapple-watermelon-strawberry-banana-papaya-lemon"

print(order_alphabetically(TI_concepts))
print(order_alphabetically(fruits))

def check_list_for_primes(list):
    primes = []
    for n in list:
        if check_prime(n) == True:
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


numbers_list = [1, 4, 6, 7, 13, 9, 67]

print(check_list_for_primes(numbers_list))
