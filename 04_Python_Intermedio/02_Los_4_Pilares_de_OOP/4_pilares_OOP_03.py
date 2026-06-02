# Ejercicios de Los 4 Pilares de OOP - Python Intermedio
# Programa 03:
# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

# Los usos más comunes son:
# 01. Combinar comportamientos independientes o compartir funcionalidades transversales
#       - Permite combinar las capacidades/métodos de las clases padre sin duplicar código
# 02. Interfaces o comportamientos especializados
#       - Combinando las capacidades de dos clases padres distintas puedo dar a lugar a una clase hija con capacidades más específicas/complejas

class Flying_Creature():
    lightning_debility = True
    name = "Criatura voladora" 
    def fly(self):
        print(f"--{self.name} se eleva en el aire--")

class Fire_Creature():
    name = "Criatura ígnea"
    fire_resistance = True
    water_debility = True
    def cast_fire(self):
        print(f"--{self.name} lanza bolas de fuego--")

class Any_Creature():
    name = "Cualquier criatura"
    def die(self):
        print(f"--{self.name} llega a 0 HP y muere--")

class Phoenix(Any_Creature,Flying_Creature,Fire_Creature):
    def __init__(self):
        self.name = "El ave Fénix"
    # Esta criatura es más compleja que las otras, tiene las capacidades combinadas de una criatura de fuego y una criatura voladora
    # Es decir, puede volar y lanzar fuego
    # Además, es especialmente resistente al fuego, pero muy vulnerable al agua y los relámpagos

class Alquemist():
    name = "Alquimista"
    def drink_potion(self):
        print(f"--{self.name} toma una poción y restaura 2 HP--")

class Sky_Elven():
    name = "Elfo del cielo"
    def cast_lightning(self):
        print(f"--{self.name} lanza un relámpago--")

class Water_Mage():
    fire_resistance = True
    name = "Mago elemental del agua" 
    def cast_water(self):
        print(f"--{self.name} lanza un ataque de agua--")

class Player(Alquemist,Sky_Elven,Water_Mage):
    def __init__(self,name):
        self.name = name
    # Este es un personaje más especialiazado, que tiene las copacidades combinadas de otras 3 clases de personaje

enemy = Phoenix()
avatar = Player("Stormie la aprendiz de magia")

enemy.fly()
enemy.cast_fire()
if avatar.fire_resistance:
    print("El ataque hace solo la mitad del daño normal")
avatar.drink_potion()
avatar.cast_lightning()
if enemy.lightning_debility:
    print("El ataque hace el doble del daño normal")
    avatar.cast_water()
if enemy.water_debility:
    print("El ataque hace el doble del daño normal")
enemy.die()
