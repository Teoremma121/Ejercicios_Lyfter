# Ejercicios Extra de Algoritmos de Ordenamiento -- Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 03:

# Validación de entrada antes de ordenar
# Cree una función que reciba una lista y valide:
#   - Que todos los elementos sean números
#   - Que no esté vacía
#   - Luego aplique bubble_sort si pasa las validaciones
#   - Si hay error, debe lanzar un mensaje apropiado

my_list = [7,4,8,2,"seis",1,5,3]
my_list_2 = []
my_list_3 = [7,4,8,2,6,1,5,3]

def validate_numbers(list_for_validate):
    if list_for_validate == []:
        raise Exception("La lista se encuentra vacía")
    for item in list_for_validate:
        if not isinstance(item, (int, float)):
            raise Exception("La lista contiene elementos no numéricos")


def bubble_sort(list_for_sort):
    print(f"Orden inicial: {list_for_sort}")
    effective_rounds = 0
    total_exchanges = 0
    for round in range(len(list_for_sort)):
        this_round_exchanges = 0
        iterated_element = list_for_sort[0]
        for iteration in range(len(list_for_sort)-round-1):
            if iterated_element > list_for_sort[iteration+1]:
                list_for_sort[iteration] = list_for_sort[iteration+1]
                list_for_sort[iteration+1] = iterated_element
                this_round_exchanges += 1
            else:
                iterated_element = list_for_sort[iteration+1]
            print(f"Recorrido: {round+1}, Iteración: {iteration+1}, {list_for_sort}")
        if this_round_exchanges > 0:
            effective_rounds += 1
            total_exchanges += this_round_exchanges
    print(f"Orden final: {list_for_sort}")
    print(f"Recorridos: {effective_rounds}")
    print(f"Intercambios: {total_exchanges}")
    return list_for_sort

def validate_bubble_sort(list_for_sort):
    try:
        validate_numbers(list_for_sort)
        bubble_sort(list_for_sort)
    except Exception as e:
        print(f"Error: {e}")

validate_bubble_sort(my_list)
validate_bubble_sort(my_list_2)
validate_bubble_sort(my_list_3)


