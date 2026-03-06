# Ejercicios Extra de Manejo de Archivos - Python Básico
# Emmanuel Piedra Esquivel
# Programa 03:
# Cree un programa que:
# - Lea un archivo línea por línea
# - Convierta cada línea a mayúsculas
# - Escriba el contenido en un nuevo archivo

def read_file_per_line(path):
    new_list = []
    with open(path, encoding = 'utf-8') as file:
        for line in file.readlines():
            new_list.append(line)
    return new_list

def convert_to_capitals(list_of_strings):
    new_list = []
    for line in list_of_strings:
        new_list.append(line.upper())
    return new_list

def write_list_to_file(list_to_write, path):
    with open(path,"w", encoding = 'utf-8') as file:
        file.writelines(list_to_write)

def main():
    list_of_lines = read_file_per_line("lower_case.txt")
    capital_lines = convert_to_capitals(list_of_lines)
    write_list_to_file(capital_lines, "capital_letters.txt")
    with open("capital_letters.txt", encoding = 'utf-8') as file:
        print(file.read())
    
main()
