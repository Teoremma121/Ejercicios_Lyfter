# Ejercicios Extra de OOP - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 02

# Cree una clase base Animal y dos clases hijas Dog y Cat:
#   - Animal debe tener nombre y método speak() que retorne "Hace un sonido"
#   - Dog debe sobrescribir speak() para decir "Guau"
#   - Cat debe sobrescribir speak() para decir "Miau"

class Animal():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return "Hace un sonido"

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"
    
my_dog = Dog("Pluto")
print(my_dog.speak())
my_cat = Cat("Salem")
print(my_cat.speak())