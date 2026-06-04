# Ejercicios de Los 4 Pilares de OOP - Python Intermedio
# Programa 02:
# Cree una clase abstracta de Shape que:
#   - Tenga los métodos abstractos de calculate_perimeter y calculate_area.
#   - Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
#   - Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        perimeter = 2*pi*self.radius
        return perimeter
    
    def calculate_area(self):
        area = pi*self.radius**2
        return area
    
class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def calculate_perimeter(self):
        perimeter = 4*self.side
        return perimeter
    
    def calculate_area(self):
        area = self.side**2
        return area

class Rectangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        perimeter = 2*(self.base + self.height)
        return perimeter
    
    def calculate_area(self):
        area = self.base*self.height
        return area
    
my_circle = Circle(15)
my_square = Square(15)
my_rectangle = Rectangle(2,5)

print(f"El perímetro del círculo es de: {my_circle.calculate_perimeter()}")
print(f"El área del círculo es de: {my_circle.calculate_area()}")
print(f"El perímetro del cuadrado es de: {my_square.calculate_perimeter()}")
print(f"El área del cuadrado es de: {my_square.calculate_area()}")
print(f"El perímetro del rectangulo es de: {my_rectangle.calculate_perimeter()}")
print(f"El área del rectangulo es de: {my_rectangle.calculate_area()}")