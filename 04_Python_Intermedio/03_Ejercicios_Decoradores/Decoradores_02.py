# Ejercicios de Decoradores - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 02:

# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números,
# y arroje una excepción de no ser así.

def check_if_numbers(func):
    def wrapper(*args):
        try:
            for index, arg in enumerate(args):
                if not isinstance(arg, (int, float)):
                    raise ValueError(f"El argumento {index+1} ({arg}) no es un número")
            func(*args)
        except ValueError as e:
            print(f"Error: {e}")
            print("Todos los argumentos deben ser números")
    return wrapper

@check_if_numbers
def sum_week_tips(*args):
    total = 0
    for tip in args:
        total += tip
    print(f"Las propinas de esta semana fueron: {total}")

sum_week_tips(15,7,21,12,15,14,8)
sum_week_tips(15,7,21,"doce",15,14,8)
