# Ejercicios de Excepciones - Python Básico
# Emmanuel Piedra Esquivel
# Programa 01:
# Cree un programa que:
# Pida al usuario su nombre
# Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
# Luego pida su edad
# Si no es un número válido, capture el ValueError y muestre un mensaje
# Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"

def ask_name():
    valid_name = False
    while valid_name == False:
        try:
            name = input("Digite su nombre: ")
            if name.isdigit():
                raise ValueError("El nombre no puede ser un número")
            valid_name = True
        except ValueError as e:
            print(f"Ha ocurrido un error: {e}")  
    return name
    
def ask_age():
    valid_age = False
    while valid_age == False:
        try:
            age = int(input("Digite su edad: "))
            valid_age = True
        except ValueError:
            print("Error: Debe digitar un número válido")
    return age
    
def main():    
    try:
        name = ask_name()
        age = ask_age()
    except Exception as e:
        print(f"Ha ocurrido un error: {e}\nEl programa se va a cerrar")
        exit()
    print(f"¡Hola {name}, su edad es {age}!")

main()