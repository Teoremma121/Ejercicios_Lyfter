# Ejercicios Extra de Algoritmos de Ordenamiento -- Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 02:

# Conteo de pasos (bubble_sort_steps)
# Modifique su implementación de bubble_sort para que:
#   - Cuente cuántas iteraciones (pasadas) realiza el algoritmo
#   - Cuente cuántos intercambios se hicieron en total

my_list = [7,4,8,2,6,1,5,3]

def bubble_sort_steps(list_for_sort):
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

bubble_sort_steps(my_list)