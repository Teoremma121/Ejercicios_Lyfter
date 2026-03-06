# Ejercicios de Funciones - Python Básico
# Emmanuel Piedra Esquivel
# Ejercicio 02:
# 2. Experimente con el concepto de scope:
#       2.1 Intente acceder a una variable definida dentro de una función desde afuera.
#       2.2 Intente acceder a una variable global desde una función y cambiar su valor.

def ask_topic ():
    topic = input("Hola,\n¿Sobre qué tema quieres aprender hoy? ") #Variable local
    print(f"Buscando sobre {topic}...")

ask_topic()

# print(topic)
# No se puede acceder a la variable - NameError: name 'topic' is not defined

password = "T0t0r0.Ch1h1r0"  #Variable global

def change_password ():
    password = input("Digite una nueva contraseña: ")

change_password()

print(password)
# La variable no se modifica, sigue siendo la original
