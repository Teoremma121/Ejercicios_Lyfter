# Ejercicios de Diccionarios - Python Básico
# Emmanuel Piedra Esquivel
# Programa 03:
# Cree un programa que use una lista para eliminar keys de un diccionario.
# Ejemplos:
# list_of_keys = [’access_level’, ‘age’]
# employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}
# → {’name’: ‘John’, 'email’: ‘john@ecorp.com’}

product = {'name':'mixer', 'brand':'Ninja','model':'unknown','price':125,'guarantee':'None'}
keys_to_delete = ['model','guarantee']

for key in keys_to_delete:
    product.pop(key)

print(product)