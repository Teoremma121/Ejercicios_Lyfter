# Ejercicios Extra de Algoritmos de Ordenamiento -- Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 01_b:

# Implemente un bubble_sort que funcione para los ejercicios de estructura de datos: 
# https://learning.lyfter.team/dashboard/duad/roadmap/python-intermedio/activity/ejercicios-de-estructuras-de-datos
# La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso

class Node:
    data: int
    next_node: Node

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class DoubleEndedQueue():
    head = Node
    
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def push_left(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next_node = self.head
            self.head = new_node
            return
        self.head = new_node
        self.tail = self.head
    
    def push_right(self,data):
        new_node = Node(data)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
            return
        self.head = new_node
        self.tail = self.head

    def pop_left(self):
        if self.head:
            self.head = self.head.next_node

    def pop_right(self):
        if self.tail:
            current_node = self.head
            while (current_node.next_node is not None):
                if current_node.next_node == self.tail:
                    self.tail = current_node
                    self.tail.next_node = None
                    return
                current_node = current_node.next_node
            self.head = None
            self.tail = self.head

    def print_structure(self):
        printer = "head"
        current_node = self.head
        while (current_node is not None):
            printer += "-> " + str(current_node.data)
            current_node = current_node.next_node
        printer += "-> tail"
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
    
my_queue = DoubleEndedQueue(15)
my_queue.push_left(23)
my_queue.push_left(7)
my_queue.push_right(24)
my_queue.push_right(5)
my_queue.push_left(30)
my_queue.push_right(1)
my_queue.print_structure()
my_queue.bubble_sort()
