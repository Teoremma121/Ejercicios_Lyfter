#  Ejercicios de Análisis de Algoritmos -- Python Intermedio
#  Emmanuel Piedra Esquivel
#  Ejercicio 01:

#  Analice el algoritmo de bubble_sort usando la Big O Notation:

def bubble_sort(list_for_sort):
    print(f"Orden inicial: {list_for_sort}") #O(1)
    for round in range(len(list_for_sort)): #O(n)
        iterated_element = list_for_sort[0] #O(n)
        for iteration in range(len(list_for_sort)-round-1): #O(n^2) 
            if iterated_element > list_for_sort[iteration+1]: #O(n^2)
                list_for_sort[iteration] = list_for_sort[iteration+1] #O(n^2)
                list_for_sort[iteration+1] = iterated_element #O(n^2)
            else:
                iterated_element = list_for_sort[iteration+1] #O(n^2)
            print(f"Recorrido: {round+1}, Iteración: {iteration+1}, {list_for_sort}") #O(n^2)
    print(f"Orden final: {list_for_sort}") #O(1)
    return list_for_sort #O(1)


# * Complejidad del algoritmo: O(n^2)



