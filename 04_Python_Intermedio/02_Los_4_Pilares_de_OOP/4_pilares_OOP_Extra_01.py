# Ejercicios Extra de Los 4 de OOP - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 01:

# Cree una clase Employee con los siguientes requisitos:
#   - Atributos privados: _name, _salary
#   - Use @property y @<atributo>.setter para:
#   - Mostrar el nombre y el salario
#   - Validar que el salario nunca sea negativo
#   - Cree un método promote que aumente el salario un porcentaje definido

class Employee():
    def __init__(self,name,salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = value
        
    def promote(self, percentage):
        self.salary = self._salary*(1+percentage)


try:
    employee_1 = Employee("Horace",600)
    print(f"-Nombre del empleado: {employee_1.name}")
    print(f"Salario: {employee_1.salary}")
    print(f"Se va a hacer un incremento del 20% en el salario")
    employee_1.promote(0.2)
    print(f"Nuevo salario: {employee_1.salary}")
except ValueError as e:
    print(f"Error: {e}")

try:
    print("\nSe va a intentar crear una instancia de la clase Employee usando un salario negativo")
    employee_2 = Employee("Nimphadora",-200)
except ValueError as e:
    print(f"Error: {e}")
try:
    print(f"-Nombre del empleado: {employee_2.name}")
    print(f"Salario: {employee_2.salary}")
except NameError as e:
    print(f"Error: {e}")
    print("No se creó employee_2 porque la validación detectó el salario negativo")

employee_3 = Employee("Remus",300)
print(f"\n-Nombre del empleado: {employee_3.name}")
print(f"Salario: {employee_3.salary}")
try:
    print('Se va a intentar "settear" el salario a un valor negativo')
    employee_3.salary = -100
except ValueError as e:
    print(f"Error: {e}")
print(f"El salario sigue siendo: {employee_3.salary}")
