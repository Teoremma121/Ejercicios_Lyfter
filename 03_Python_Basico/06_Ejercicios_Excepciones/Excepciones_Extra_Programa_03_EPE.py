# Ejercicios de Excepciones - Python Básico
# Emmanuel Piedra Esquivel
# Programa 03:
# Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total

def add_values(values_list):
    total = 0
    for element in values_list:
        try:    
            total += float(element)
            print(f"- {element} sumado correctamente")
        except ValueError:
            print(f"- Elemento inválido: {element}")
    print(f"Total de la suma: {total}")

my_list = ['10', 'manzana', '5.5', '3', 'n/a']
add_values(my_list)

