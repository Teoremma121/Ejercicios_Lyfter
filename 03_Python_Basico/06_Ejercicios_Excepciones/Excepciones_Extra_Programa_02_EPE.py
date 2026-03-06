# Ejercicios de Excepciones - Python Básico
# Emmanuel Piedra Esquivel
# Programa 02:
# Cree una función convertir_a_entero(lista) que:
# - Reciba una lista de strings
# - Intente convertir cada elemento a entero usando int()
# - Use try-except para atrapar los errores ValueError
# - Si algún elemento no puede convertirse, mostrar:
#   "No se pudo convertir el elemento: <valor>" y continuar con los demás

def convert_to_integer(strings_list):
    new_list = []
    for element in strings_list:
        try:
            new_list.append(int(element))
            print(f'"{element}" convertido a: {int(element)}')
        except ValueError:
            new_list.append(element)
            print(f"No se pudo convertir el elemento: {element}")
    return new_list

my_list = ['4', 'hola', '10', '5.2', 'Horace', '-7', '0,53']
my_list = convert_to_integer(my_list)


