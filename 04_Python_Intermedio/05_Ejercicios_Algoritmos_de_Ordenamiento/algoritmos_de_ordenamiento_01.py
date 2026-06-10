# Ejercicios de Algoritmos de Ordenamiento -- Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 01:

# Crea un bubble_sort por tu cuenta sin revisar el código de la lección.

my_list = [7,4,8,2,6,1,5,3]

def bubble_sort(list_for_sort):
    print(f"Orden inicial: {list_for_sort}")
    for round in range(len(list_for_sort)):
        iterated_element = list_for_sort[0]
        for iteration in range(len(list_for_sort)-round-1):
            if iterated_element > list_for_sort[iteration+1]:
                list_for_sort[iteration] = list_for_sort[iteration+1]
                list_for_sort[iteration+1] = iterated_element
            else:
                iterated_element = list_for_sort[iteration+1]
            print(f"Recorrido: {round+1}, Iteración: {iteration+1}, {list_for_sort}")
    print(f"Orden final: {list_for_sort}")
    return list_for_sort

bubble_sort(my_list)

