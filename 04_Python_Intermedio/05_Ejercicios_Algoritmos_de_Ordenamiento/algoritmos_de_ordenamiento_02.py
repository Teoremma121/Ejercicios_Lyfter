# Ejercicios de Algoritmos de Ordenamiento -- Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 02:

# Modifica el bubble_sort para que funcione de derecha a izquierda, 
# ordenando los números menores primero (como en la imagen de abajo).

my_list = [7,4,8,2,6,1,5,3]

def bubble_sort(list_for_sort):
    print(f"Orden inicial: {list_for_sort}")
    for round in range(len(list_for_sort)):
        iterated_element = list_for_sort[len(list_for_sort)-1]
        for iteration in range(len(list_for_sort)-round-1):
            actual_index = len(list_for_sort)-iteration-1
            next_index = len(list_for_sort)-iteration-2
            if iterated_element < list_for_sort[next_index]:
                list_for_sort[actual_index] = list_for_sort[next_index]
                list_for_sort[next_index] = iterated_element
            else:
                iterated_element = list_for_sort[next_index]
            print(f"Recorrido: {round+1}, Iteración: {iteration+1}, {list_for_sort}")
    print(f"Orden final: {list_for_sort}")
    return list_for_sort

bubble_sort(my_list)