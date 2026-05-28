
def call_main_menu():
    index = "0"
    while index == "0":
        print("\nDigite el número de índice de la acción que desea realizar:")
        print("1. Agregar información de estudiantes")
        print("2. Ver la información de todos los estudiantes")
        print("3. Ver el top 3 de los estudiantes según nota promedio")
        print("4. Ver la nota promedio entre todos los estudiantes")
        print("5. Ver estudiantes reprobados")
        print("6. Eliminar un estudiante")
        print("7. Exportar los datos actuales a un archivo CSV")
        print("8. Importar los datos desde un archivo CSV")
        print("9. Salir")
        index = input_valid_index(10)
    return index

def input_valid_index(top):
    try:
        entry = input(" > ")
        if entry not in list(map(str, range(1,top))):
            raise ValueError("Error: No digitó un número válido")
        return entry
    except ValueError as e:
        print(f"\n{e}")
        print(f"- Debe digitar únicamente un número de índice de las opciones disponibles")
        print(f"- Es decir, alguno de los siguientes números: {list(range(1,top))}")
        return "0"