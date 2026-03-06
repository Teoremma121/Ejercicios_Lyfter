# Ejercicios Extra de Iterables y Listas
# Emmanuel Piedra Esquivel

# Programa 01:
print("Programa 01:")
# Cree un programa que cuente cuántas veces aparece un número específico en una lista.
# Pida al usuario una lista de números y otro número a buscar

user_list = []
counter = 0

while True:
    actual_entry = input(f"""
Digite un número natural para agregar a su lista
o digite FIN para terminar la lista:
>""")
    if actual_entry == "FIN":
        break
    user_list.append(int(actual_entry))

num_to_count = int(input("Digite el número que desea buscar y contar en la lista: "))

for n in user_list:
    if n == num_to_count:
        counter += 1

print(f"""
Esta es la lista que usted digitó:
{user_list}
El número {num_to_count} aparece {counter} veces.""")

# Programa 02:
print("\nPrograma 02:")
# Cree un programa que verifique si todos los elementos de una lista son positivos

list_1 = [45, 62, 77, -3, 88]
messagge = "Todos los números en la lista son positivos"

for n in list_1:
    if n <= 0:
        messagge = "Existe al menos un número negativo o un cero en la lista"
        break

print(messagge)

# Programa 03:
print("\nPrograma 03:")
# Cree un programa que muestre el valor más pequeño de una lista sin usar min().

list_2 = [200, 22, 33, 45, 21, 84, 101]
menor = list_2[0]

for n in list_2:
    if n < menor:
        menor = n

print(f"El número menor de la lista es: {menor}")

# Programa 04:
print("\nPrograma 04:")
# Cree un programa que reciba una lista de números y calcule el promedio de los valores,
# luego cree una nueva lista con solo los valores mayores al promedio

list_3 = [8.5, 14.9, 15.7, 12.2, 14.5, 21.0, 12.5, 13.2, 10.0, 11.5]
sum_total = 0
list_over_avg = []

for number in list_3:
    sum_total += number
avg = round(sum_total/len(list_3),2)

for number in list_3:
    if number > avg:
        list_over_avg.append(number)

print(f"Promedio: {avg}")
print(f"""Lista de valores por encima del promedio:
{list_over_avg}""")

# Programa 05:
print("\nPrograma 05:")
# Cree un programa que le pida al usuario ingresar 5 palabras.
# Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

words = []
long_words = []
ordinals = ["primera","segunda","tercera","cuarta","quinta"]

for i in range(5):
    words.append(input(f"Digite la {ordinals[i]} palabra: "))

for word in words:
    if len(word) > 4:
        long_words.append(word)

print(f"Palabras con más de 4 letras: {long_words}")



