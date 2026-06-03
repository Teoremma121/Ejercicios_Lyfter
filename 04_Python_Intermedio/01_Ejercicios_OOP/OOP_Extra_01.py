# Ejercicios Extra de OOP - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 01

# Cree una clase Rectangle que:
#   - Tenga atributos width y height
#   - Tenga un método get_area() que retorne el área
#   - Tenga un método get_perimeter() que retorne el perímetro
#   - Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

class Rectangle():
    def __init__(self):
        width = input("Ingrese el ancho: ")
        height = input("Ingrese la altura: ")
        if (int(width) < 0) or (int(height) < 0):
            raise ValueError("Existe un valor negativo, los valores deben ser positivos")
        self.width = int(width)
        self.height = int(height)

    def get_area(self):
        area = self.width*self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter
    
try:
    my_rectangle = Rectangle()
    print(f"El área del rectangulo es de: {my_rectangle.get_area()}")
    print(f"El perímetro del rectangulo es de: {my_rectangle.get_perimeter()}")
except ValueError as e:
    print(f"Error: {e}")
