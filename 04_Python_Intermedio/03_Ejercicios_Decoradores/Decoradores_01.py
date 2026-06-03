# Ejercicios de Decoradores - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 01:

# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def print_and_return(func):
    def wrapper(*args):
        for i in range(len(args)):
            print(f"-Arg {i+1}: {args[i]}")
        return func(*args)
    return wrapper

@print_and_return
def calculate_total_points(singles,doubles,triples):
    total = 20*(singles + 2*doubles + 3*triples)
    return total

value = calculate_total_points(7,4,1)
print(value)

@print_and_return
def add_words(*args):
    sentence = ""
    for word in args:
        sentence += word + " "
    return sentence

result = add_words("Esto","es","un","ejemplo")
print(result)
