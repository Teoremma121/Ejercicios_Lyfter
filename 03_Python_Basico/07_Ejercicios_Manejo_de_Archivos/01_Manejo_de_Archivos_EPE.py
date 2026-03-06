# Ejercicios de Manejo de Archivos - Python Básico
# Emmanuel Piedra Esquivel
# Cree un programa que lea nombres de canciones de un archivo (línea por línea)
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def from_file_to_list(path):
    temp_list = []
    with open(path, encoding = 'utf-8') as file:
        for line in file.readlines():
            temp_list.append(line)
    return temp_list

def order_list(list_to_order):
    new_list = []
    for i in range(len(list_to_order)):
        next_element_in_order = list_to_order[0] 
        for element in list_to_order:
            if element.lower() < next_element_in_order.lower():
                next_element_in_order = element
        new_list.append(next_element_in_order)
        list_to_order.remove(next_element_in_order)
    return new_list

def from_list_to_file(list_to_write,path):
    with open(path, "w", encoding = 'utf-8') as file:
        file.writelines(list_to_write)

from_list_to_file(order_list(from_file_to_list("songs.txt")),"ordered_songs.txt")

# Para revisar:
with open("ordered_songs.txt") as file:
    print(file.read())