# Ejercicios Extra de Manejo de Archivos - Python Básico
# Emmanuel Piedra Esquivel
# Programa 01:
# Cree un programa que lea un archivo con texto línea por línea,
# quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón
# en un nuevo archivo

def file_to_list(path):
    new_list = []
    with open(path) as file:
        for line in file.readlines():
            new_list.append(line)
    return new_list

def remove_line_breaks(list_to_edit):
    new_list = []
    for element in list_to_edit:
        new_list.append(element.replace("\n",""))
    return new_list

def list_to_file(list_to_write,path):
    text_to_add = " ".join(list_to_write)
    with open(path,"w") as file:
        file.write(text_to_add)


list_to_file(remove_line_breaks(file_to_list("separated_text.txt")),"joined_text.txt")

with open("joined_text.txt") as file:
    print(file.read())