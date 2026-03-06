# Ejercicios Extra de Manejo de Archivos - Python Básico
# Emmanuel Piedra Esquivel
# Programa 04:
# Cree un programa que:
# - Pida al usuario una línea de texto
# - Agregue esa línea al final de un archivo existente
# - Si el archivo no existe, lo crea automáticamente

def ask_for_text():
    user_text = input("Escriba una línea de texto para agregar al archivo:\n> ") + "\n"
    return user_text

def write_text(text_to_write, path):
    with open(path,"a", encoding = 'utf-8') as file:
        file.write(text_to_write)

def main():
    write_text(ask_for_text(),"notes.txt")
    with open("notes.txt", encoding = 'utf-8') as file:
        print(f"\nContenido del archivo:\n{file.read()}")
    
main()
