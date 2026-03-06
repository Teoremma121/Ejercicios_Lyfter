# Ejercicios de Diccionarios - Python Básico
# Emmanuel Piedra Esquivel
# Programa 02:
# Cree un programa que cree un diccionario usando dos listas del mismo tamaño,
# usando una para sus keys, y la otra para sus values.
# Ejemplos:
# list_a = [’first_name’, ‘last_name’, ‘role’]
# list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
# → {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}

keys = ['book_name','author','publish_year']
book_1_values = ["Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997]
book_1 = {}

for index, key in enumerate(keys):
    book_1[key] = book_1_values[index]

print(book_1)