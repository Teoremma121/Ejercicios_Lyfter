# Ejercicios de Excepciones - Python Básico
# Emmanuel Piedra Esquivel
# Cree una calculadora por linea de comando. Esta debe de tener un número actual,
# y un menú para decidir qué operación hacer con otro número:
#  -1. Suma
#  -2. Resta
#  -3. Multiplicación
#  -4. División
#  -5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar,
# multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si
# ingresa un número invalido a la hora de hacer la operación.

def calculator():
    storage = "erased"
    while True:
        try:
            storage = cycle_per_operation(storage)
        except Exception as ex:
            print(f"Ha habido un error y el programa se va a cerrar...\Detalles: {ex}")
            exit()

def cycle_per_operation(storage):
    first_number = check_or_fill_storage(storage)
    selected_function = select_from_menu()
    if selected_function in range(1,5):
        result = guide_trough_operation(first_number,selected_function)
    elif selected_function == 5:
        result = "erased"
        print("\nEl número almacenado ha sido borrado")
    else:
        print("El programa se va a cerrar...")
        exit()
    return result

def check_or_fill_storage(storage):
    if storage == "erased":
        new_first_number = digit_number("\nDigite el primer número: ")
        return new_first_number
    else:
        print(f"\nEl número actual almacenado es: {storage}")
        return storage
    
def digit_number(message):
    valid_number = False
    while valid_number == False:
        try:
            number = float(input(message))
            valid_number = True
        except ValueError as e:
            print(f"\nError: no digitó un número válido.\nDetalles: {e}")
    return number

def select_from_menu():
    valid_index = False
    while valid_index == False:
        try:
            index = int(input("\nDigite el índice de la operación que desea realizar:"
            "\n1. Suma"
            "\n2. Resta"
            "\n3. Multiplicación"
            "\n4. División"
            "\n5. Borrar Resultado"
            "\n6. Salir"
            "\n> "))
            if index > 6 or index < 1:
                raise ValueError("El número de índice que digitó es menor que 1 o mayor que 5")
            valid_index = True
        except ValueError as e:
            print(f"\nError: no digitó un número de índice válido.\nDetalles: {e}")
    return index

def guide_trough_operation(first_number,index):
    result = first_number
    valid_operation = False
    while valid_operation == False:
        try:
            second_number = digit_number(second_number_message(index))
            result = run_operation(first_number,second_number,index)
            valid_operation = True
        except ZeroDivisionError as e:
            print(f"\nError: El divisor no puede ser cero.\nDetalles: {e}")
    print(f"\nEl resultado es: {result}")
    return result

def second_number_message(index):
    operations = [0,"a sumar","a restar","multiplicador","divisor"]
    message = f"\nDigite el número {operations[index]}: "
    return message

def run_operation(a,b,index):
    result = a
    if index == 1:
        result = a + b
    elif index == 2:
        result = a - b
    elif index == 3:
        result = a * b
    else:
        try:
            result = a / b
        except ZeroDivisionError as e:
            raise ZeroDivisionError(e)
    return result

calculator()





