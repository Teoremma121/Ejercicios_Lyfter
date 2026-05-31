#Ejercicios de Python Intermedio - Emmanuel Piedra
#Ejercicio #02
# Cree una clase de Bus con:
#   - Un atributo de max_passengers.
#   - Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). 
#       Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
#   - Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Bus():
    passengers = []
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
    
    def passenger_gets_on(self,person):
        if len(self.passengers) == self.max_passengers:
            print(f"--El autobus está lleno. {person.name} no pudo subir al autobus--")
            return
        self.passengers.append(person)
        print(f"--{person.name} subió al autobus--")

    def passenger_gets_off(self,name):
        for index, passenger in enumerate(self.passengers):
            if passenger.name == name:
                self.passengers.pop(index)
                print(f"--{passenger.name} bajó del autobus--")
                return
        print(f"--{name} no se encuentra a bordo del autobus")

    def show_passengers_list(self):
        if self.passengers == []:
            print("--El autobus se encuentra vacío--")
            return
        print("--Mostrando lista de pasajeros:--")
        for passenger in self.passengers:
            print(f"   >{passenger.name}, Edad: {passenger.age}")

my_bus = Bus(3)
my_bus.passenger_gets_on(Person("Ana",35))
my_bus.passenger_gets_on(Person("Luis",45))
my_bus.passenger_gets_on(Person("Juan",27))
my_bus.passenger_gets_on(Person("Roberto",63))
my_bus.show_passengers_list()
my_bus.passenger_gets_off("Roberto")
my_bus.passenger_gets_off("Luis")
my_bus.show_passengers_list()
my_bus.passenger_gets_off("Juan")
my_bus.passenger_gets_off("Ana")
my_bus.show_passengers_list()





