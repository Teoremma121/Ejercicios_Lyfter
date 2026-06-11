# Ejercicios Extra de Unit Testing - Python Intermedio
# Emmanuel Piedra Esquivel
# Módulo de funciones, Ejercicio Extra 01:

# 1. Cree una clase de pruebas que contenga al menos 3 funciones que operen con números (como suma, promedio, conversión, etc.) y escriba:
#   - Un caso con números positivos
#   - Un caso con números negativos
#   - Un caso con ceros

def addition(a,b):
    return a + b

def avg(nums_list):
    total_sum = 0
    avg = 0
    for n in nums_list:
        total_sum += n
    if (len(nums_list) != 0) and (total_sum != 0):
        avg = total_sum/len(nums_list)
    return avg

def celsius_to_fahrenheit(celsius_temperature):
    f_temperature = (9/5)*celsius_temperature + 32
    return f_temperature

# 2. Dada la función:

def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2

# Cree un test que:
#   - Valide que dividir(10, 2) retorna 5.0
#   - Verifique que dividir por cero lanza un ValueError
#   - Valide que dividir con un string como parámetro también lanza TypeError

# 3. Suponga la función:

def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()
    
# Cree un test que:
#   - Use unittest.mock para simular el contenido de un archivo
#   - Verifique que retorna las líneas esperadas sin crear archivos reales
#   - Compruebe que lanza FileNotFoundError si el archivo no existe