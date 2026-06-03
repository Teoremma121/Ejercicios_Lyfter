# Ejercicios Extra de Decoradores - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 01:

# Cree una función que imprima “Hola, [nombre]” dos veces:
# Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas,
# con los mismos argumentos

def repeat_twice(func):
    def wrapper(name):
        func(name)
        func(name)
    return wrapper

@repeat_twice
def print_hello(name):
    print("Hola",name)

print_hello("Emmanuel")