#Ejercicios de Python Intermedio - Emmanuel Piedra
#Ejercicio #01
# Cree una clase de Circle con:
#   - Un atributo de radius (radio).
#   - Un método de get_area que retorne su área.

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        import math
        area = math.pi*(self.radius**2)
        return round(area,2)
    
my_circle = Circle(15)
print(f"El área de my_circle es de: {my_circle.get_area()}")