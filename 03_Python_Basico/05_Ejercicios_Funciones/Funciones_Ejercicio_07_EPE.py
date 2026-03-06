# Ejercicios de Funciones - Python Básico
# Emmanuel Piedra Esquivel
# Ejercicio 07:
# Cree una función que acepte una lista de números y retorne una lista con los números
# primos de la misma.
# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# - Tip 1: Investigue la lógica matemática para averiguar si un número es primo,
#  y conviértala a código. No busque el código, eso no ayudaría.
# - Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero
# es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para
# revisar si el numero es primo o no.

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
    
    
    