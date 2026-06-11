#  Ejercicios Extra de Análisis de Algoritmos -- Python Intermedio
#  Emmanuel Piedra Esquivel

# * Ejercicio 01: 
# Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros n números naturales

# Versión 1
def manual_add(n):
    result = 0 # O(1)
    for i in range(1, n + 1): # O(n)
        result += i # O(n)
    return result # O(1)

# Versión 2
def add_formula(n):
    return n * (n + 1) // 2 # O(1)

# Preguntas:
# ¿Cuál es la complejidad de cada versión?
# * Versión 1: O(n), Versión 2: O(1)
# ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
# * Versión 2, tiene menor complejidad, se ejecuta más rápido, la instrucción se ejecuta una única vez

# * Ejercicio 02: 
# Considere los siguientes dos algoritmos:

def linear_search(my_list, target):
    for item in my_list: # O(n)
        if item == target: # O(n)
            return True # O(1)
    return False # O(1)

def binary_search(my_list, target):
    low = 0 # O(1)
    high = len(my_list) - 1 # O(1)
    while low <= high: # O(n)
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Preguntas:
# ¿Cuál es la complejidad de cada algoritmo?
# * Ambos tiene complejidad O(n)
# ¿En qué condiciones conviene usar cada uno?
# * El método linear_search resulta más ágil para un target que probablemente se encuentre en las primeras posiciones de una lista ordenada, 
# * El método binary_search puede resultar mucho más rápido en listas de gran tamaño, reduciendo el rango a la mitad con cada iteración
# ¿Qué pasa si la lista no está ordenada?
# * El método binary_search solo funciona en listas ordenadas de menor a mayor
# * Si la lista está desordenada solo se puede usar linear_search y es impredecible la duración efectiva que vaya a tener

# * Ejercicio 03:
# Analice la siguiente función:

def print_all_pairs(my_dict):
    for key1 in my_dict: # O(n)
        for key2 in my_dict: # O(n^2)
            print(f"{key1}-{key2}")

# Preguntas:
# ¿Cuál es la complejidad temporal?
# * La complejidad es O(n^2)
# ¿Cuanto dura si hay 1 millón de claves?
# * La duración sería: O(1.000.000^2) = 1.000.000.000.000