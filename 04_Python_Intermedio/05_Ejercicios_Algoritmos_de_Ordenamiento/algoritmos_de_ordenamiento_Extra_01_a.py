# Ejercicios Extra de Algoritmos de Ordenamiento -- Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 01_a:

# Implemente un bubble_sort que funcione para los ejercicios de estructura de datos:
# https://learning.lyfter.team/dashboard/duad/roadmap/python-intermedio/activity/ejercicios-de-estructuras-de-datos
# La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso

class Node:
    data: int
    next_node: Node

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    head: Node

    def __init__(self, data):
        self.head = Node(data)
    
    def push(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            self.head = self.head.next_node

    def print_structure(self):
        printer = "head"
        current_node = self.head
        while (current_node is not None):
            printer += "-> " + str(current_node.data)
            current_node = current_node.next_node
        print(printer)

    def bubble_sort(self):
        current_node = self.head
        structure_length = 0
        while current_node is not None:
            structure_length += 1
            current_node = current_node.next_node

        print(f"Orden inicial:")
        self.print_structure()
        for round in range(structure_length):
            iterated_node = self.head
            previous_node = None
            iteration = 1
            while iteration <= (structure_length-round-1):
                comparative_node = iterated_node.next_node
                if iterated_node.data > comparative_node.data:
                    if iterated_node == self.head:
                        self.head = comparative_node
                    iterated_node.next_node = comparative_node.next_node
                    comparative_node.next_node = iterated_node
                    if previous_node:
                        previous_node.next_node = comparative_node
                    previous_node = comparative_node
                else:
                    previous_node = iterated_node
                    iterated_node = comparative_node
                print(f"Recorrido: {round+1}, Iteración: {iteration}")
                self.print_structure()
                iteration += 1
        print(f"Orden final:")
        self.print_structure()
        return self
    
my_stack = Stack(3)
my_stack.push(4)
my_stack.push(2)
my_stack.push(5)
my_stack.push(1)
my_stack.push(6)
my_stack.push(7)
my_stack.print_structure()
my_stack.bubble_sort()
