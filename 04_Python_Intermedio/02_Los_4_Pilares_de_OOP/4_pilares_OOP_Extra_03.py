# Ejercicios Extra de Los 4 de OOP - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 03:

# - Cree una clase base Vehicle con los atributos:
#   - _brand
#   - _year
# - Agregue un método get_info() que devuelva una descripción del vehículo.
# - Luego cree dos clases hijas:
#   - Car
#   - Motorcycle
#   - Cada una debe agregar su propio atributo (por ejemplo, doors o type) y 
#       sobrescribir el método get_info() para incluir esta información adicional.

class Vehicle():
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    
    def get_info(self):
        print(f"El vehículo es de la marca {self.brand}, año {self.year}")
    
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    
    def get_info(self):
        print(f"El vehículo es un automóvil {self.doors} puertas, de la marca {self.brand}, año {self.year}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, bike_type):
        super().__init__(brand, year)
        self.type = bike_type
    
    def get_info(self):
        print(f"El vehículo es una motocicleta tipo {self.type}, de la marca {self.brand}, año {self.year}")

vehicle_01 = Car("Toyota",2011,4)
vehicle_02 = Motorcycle("Suzuki",2015,"Chopper")

vehicle_01.get_info()
vehicle_02.get_info()