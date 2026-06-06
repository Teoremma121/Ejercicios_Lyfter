# Ejercicios Extra de Decoradores - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 3:

# Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
# A esta función se le debe combinar dos decoradores:
#   - @log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
#   - @validate_numbers: revisa que todos los argumentos sean numéricos

from datetime import date

def log_call(func):
    def wrapper(*args):
        print(f"Función: {func.__name__}")
        print(f"Argumento a: {args[0]}")
        print(f"Argumento b: {args[1]}")
        print(f"Fecha: {date.today()}")
        print(f"Resultado: {func(*args)}")
    return wrapper

def validate_numbers(func):
    def wrapper(*args):
        try:
            for value in args:
                if not isinstance(value, (int, float)):
                    raise ValueError(f"Uno de los argumentos no es un número")
            return func(*args)
        except ValueError as e:
            print(f"Error: {e}")
            print("-Ambos argumentos deben ser números")
    return wrapper

@validate_numbers
@log_call
def multiply(number_a,number_b):
    product = number_a*number_b
    return product

multiply(2,3)
print("")
multiply(-2.5,-3.6)
print("")
multiply(15,"tres")