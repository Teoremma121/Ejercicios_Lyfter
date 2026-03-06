# Ejercicios de Sintaxis - Python Básico -- Emmanuel Piedra Esquivel

# Ejercicio 01:
# Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

#print("Pura" + " " + "Vida")
# Resultado: Pura Vida
# >print("Edad" + 8)
# Resultado: TypeError: can only concatenate str (not "int") to str
# >print(8 + "botellas")
# Resultado: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >print([2,3,5] + [3,2,0])
# Resultado: [2, 3, 5, 3, 2, 0]
# >print("animals:" + ["cat","dog"])
# Resultado: TypeError: can only concatenate str (not "list") to str
# >print(8.16 + 7)
# Resultado:15.16
# >print(True + True)
# Resultado: 2

# Ejercicio 02:
print("Ejercicio 02:")
# Cree un programa que le pida al usuario su nombre, apellido, y edad,
# y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven,
# adulto, o adulto mayor.

first_name = input("Digite su primer nombre: ")
last_name = input("Digite su apellido: ")
age = int(input("Digite su edad: "))

if age <= 5:
    category = "bebé"
elif age <= 11:
    category = "niño(a)"
elif age <= 15:
    category = "preadolescente"
elif age <= 21:
    category = "adolescente"
elif age <= 40:
    category = "adulto(a) joven"
elif age < 65:
    category = "adulto(a)"
else:
    category = "adulto(a) mayor"

print(f"Su nombre completo es {first_name} {last_name}")
print(f"Usted es un(a) {category}")

# Ejercicio 03:
print("Ejercicio 03:")
# Cree un programa con un numero secreto del 1 al 10. 
# El programa no debe cerrarse hasta que el usuario adivine el numero.

import random
secret_number = random.randint(1, 10)
number = int(input("Adivine un número del 1 al 10: "))
while number != secret_number:
    print("Su número no es el correcto")
    number = int(input("Pruebe con un nuevo número: "))
print("¡Felicidades! Adivinó")
print(f"El número secreto era {secret_number}")

# Ejercicio 04:
print("Ejercicio 04:")
# Cree un programa que le pida tres números al usuario y muestre el mayor.

print("Debe digitar tres números para verificar cual es el mayor")
counter = ["primer","segundo","tercer"]
mayor = 0
for count in counter:
    number = int(input(f"Digite el {count} número: "))
    if number > mayor:
        mayor = number
print(f"El número mayor es: {mayor}")

#Ejercicio 05:
print("Ejercicio 05:")
# Dada n cantidad de notas de un estudiante, calcular:
# -Cuantas notas tiene aprobadas (mayor a 70).
# -Cuantas notas tiene desaprobadas (menor a 70).
# -El promedio de todas.
# -El promedio de las aprobadas.
# -El promedio de las desaprobadas.

number_of_grades = int(input("¿Cuántas notas desea ingresar?: "))
counter_grade = 1
approved_grades = 0
failed_grades = 0
sum_approved = 0
sum_failed = 0
sum_total = 0
approved_avg = 0
failed_avg = 0
while counter_grade <= number_of_grades:
    grade = float(input(f"Digite la nota número {counter_grade}): "))
    sum_total = sum_total + grade
    if grade >= 70:
        approved_grades = approved_grades + 1
        sum_approved = sum_approved + grade
    else:
        failed_grades = failed_grades + 1
        sum_failed = sum_failed + grade
    counter_grade = counter_grade + 1
total_avg = round(sum_total/number_of_grades,2)
if approved_grades >= 1:
    approved_avg = round(sum_approved/approved_grades,2)
if failed_grades >= 1:
    failed_avg = round(sum_failed/failed_grades,2)
print(f"""
{approved_grades} notas aprobadas
{failed_grades} notas desaprobadas
Promedio total: {total_avg}
Promedio de notas aprobadas: {approved_avg}
Promedio de notas desaprobadas: {failed_avg}
""")

