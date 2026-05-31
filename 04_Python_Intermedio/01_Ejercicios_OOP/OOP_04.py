#Ejercicios de Python Intermedio - Emmanuel Piedra
#Ejercicio #04
# Cree las siguientes clases:
#   Head
#   Torso
#   Arm
#   Hand
#   Leg
#   Feet
# Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.

class Hand:
    def __init__(self):
        pass

class Foot:
    def __init__(self):
        pass

class Head:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Leg:
    def __init__(self, foot):
        self.feet = foot

class Torso:
    def __init__(self, head, right_arm, left_arm):
        self.head = head
        self.rightarm = right_arm
        self.lefarm = left_arm

class Human:
    def __init__(self, torso, right_leg, left_leg):
        self.torso = torso
        self.right_leg = right_leg
        self.left_leg = left_leg

right_hand = Hand()
left_hand = Hand()
righ_foot = Foot()
lef_foot = Foot()
head = Head()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
right_leg = Leg(righ_foot)
left_leg = Leg(lef_foot)
torso = Torso(head, right_arm, left_arm)
Human = Human(torso, right_leg, left_leg)

