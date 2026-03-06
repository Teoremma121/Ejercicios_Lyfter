# Ejercicios Extras de Sintaxis - Python Básico -- Emmanuel Piedra Esquivel

#Ejercicio 1.1:
print("Ejercicio 1.1:")

# Cree un pseudocódigo que le pida un precio de producto al usuario,
# calcule su descuento y muestre el precio final tomando en cuenta que:
# Si el precio es menor a 100, el descuento es del 2%.
# Si el precio es mayor o igual a 100, el descuento es del 10%.

price = int(input("Digite el precio del producto: "))
if price < 100:
    discount = 0.02
else:
    discount = 0.1
price = round(price*(1-discount),2)
print(f"El precio con descuento es: {price}")

#Ejercicio 1.2:
print("Ejercicio 1.2:")
# Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule
# si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos
# faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. 
# Si es exactamente igual, muestre “Igual”.

time = int(input("Digite el tiempo en segundos: "))
if time > 600:
    message = "Mayor"
elif time == 600:
    message = "Igual"
else:
    message = "Faltan " + str(600 - time) + " segundos"
print(message)

#Ejercicio 1.3:
print("Ejercicio 1.3:")
# Cree un algoritmo que le pida un numero al usuario, y realice una suma
# de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado
# de la suma.

number = int(input("Digite un número natural: "))
counter = 1
total = 0
while counter <= number:
    total = total + counter
    counter = counter + 1
print(f"El resultado de la suma es: {total}")

# Ejercicio 2.1:
print("Ejercicio 2.1:")
# Cree un diagrama de flujo que tenga un numero secreto del 1 al 10,
# y le pida al usuario adivinar ese número. El algoritmo no debe terminar
# hasta que el usuario adivine el numero.

import random
secret_number = random.randint(1, 10)
number = int(input("Adivine un número del 1 al 10: "))
while number != secret_number:
    print("Su número no es el correcto")
    number = int(input("Pruebe con un nuevo número: "))
print("¡Felicidades! Adivinó")
print(f"El número secreto era {secret_number}")

# Ejercicio 2.2:
print("Ejercicio 2.2:")
# Cree un diagrama de flujo que pida 3 números al usuario. 
# Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”.
# Sino, mostrar “incorrecto”.

print("Debe digitar tres números:")
counter_2 = ["primer", "segundo", "tercer"]
message_2 = ["Incorrecto","Correcto"]
total_2 = 0
condition = False

for count in counter_2:
    number_2 = int(input(f"Digite el {count} número: "))
    if number_2 == 30:
        condition = True
    total_2 = total_2 + number_2
if total_2 == 30:
    condition = True

print(message_2[condition])

# Ejercicio 3:
print("Ejercicio 3:")
# Convertidor de unidades de temperatura
# Pida al usuario ingresar una temperatura en Celsius
# Conviértala a Fahrenheit y Kelvin
# Muestre los tres valores

temp_celsius = float(input("Ingrese la temperatura en Celsius: "))
temp_farenheit = round(1.8*temp_celsius + 32, 2)
temp_kelvin = round(temp_celsius + 273.15, 2)

print(f"""
Celsius: {temp_celsius}
Farenheit: {temp_farenheit}
Kelvin: {temp_kelvin}
""")

# Ejercicio 4:
print("Ejercicio 4:")
# Tabla de multiplicar personalizada
# Pida al usuario un número del 1 al 10
# Muestre su tabla de multiplicar del 1 al 12

number_3 = int(input("Ingrese un número: "))
counter_3 = 1

while counter_3 <= 12:
    product = counter_3*number_3
    print(f"{number_3} X {counter_3} = {product}")
    counter_3 = counter_3 + 1



