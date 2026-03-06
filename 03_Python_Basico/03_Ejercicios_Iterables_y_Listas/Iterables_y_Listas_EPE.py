# Ejercicios de Iterables y Listas - Python Básico
# Emmanuel Piedra Esquivel

# Programa 01:
print("Programa 01:")
# Cree un programa que itere e imprima los valores de dos listas
# del mismo tamaño al mismo tiempo.

list_1 = ["Happiness", "be", "even", "the", "of", "if", "only", "to", "on", "light"]
list_2 = ["can", "found", "in", "darkest", "times,", "one", "remembers", "turn", "the","."]

for index in range(list_1):
    print(f"{list_1[index]} {list_2[index]}")

# Programa 02:
print("\nPrograma 02:")
# Cree un programa que itere e imprima un string 
# letra por letra de derecha a izquierda.

secret_word = "stnaP erauqS boB"

for char in range(len(secret_word)-1,-1,-1):
    print(secret_word[char])

# Programa 03:
print("\nPrograma 03:")
# Cree un programa que intercambie el primer y ultimo elemento de una lista.
# Debe funcionar con listas de cualquier tamaño.

list_3 = ["Si","Re","Mi","Fa","Sol","La","Do"]

list_3.append(list_3.pop(0))
list_3.insert(0,list_3.pop(len(list_3)-2))

print(list_3)

# Programa 04:
print("\nPrograma 04:")
# Cree un programa que elimine todos los números impares de una lista.

numbers = [15,20,17,33,44,86,95,13,20,51,26,34]
pairs = []

for number in numbers:
    if number%2 == 0:
        pairs.append(number)
numbers = pairs

print(numbers)

# Programa 05:
print("\nPrograma 05:")
# Cree un programa que le pida al usuario 10 números, y al final le muestre
# los números que ingresó y el número más alto

user_list = []
ordinals = ["primer","segundo","tercer","cuarto","quinto","sexto","sétimo","octavo","noveno","décimo"]

for ordinal in ordinals:
    user_list.append(int(input(f"Digite el {ordinal} número de su lista: ")))

mayor = user_list[0]

for n in user_list:
    if n > mayor:
        mayor = n

print(f"""
Esta es su lista de números completa:
{user_list}
El número más alto fue:
{mayor}""")
