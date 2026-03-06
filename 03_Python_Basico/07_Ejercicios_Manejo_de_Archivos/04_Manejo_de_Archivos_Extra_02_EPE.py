# Ejercicios Extra de Manejo de Archivos - Python Básico
# Emmanuel Piedra Esquivel
# Programa 02:
# Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene
# en total.(Considere que las palabras están separadas por espacios y/o saltos de línea)

def read_file(path):
    with open(path) as file:
        text = file.read()
    return text

def count_words(text_to_count):
    text_to_count.replace("\n"," ")
    words_list = text_to_count.split()
    count = len(words_list)
    return count

def main():
    full_text = read_file("words_to_count.txt")
    total_words = count_words(full_text)
    print(f"Este archivo contiene {total_words} palabras")

main()
