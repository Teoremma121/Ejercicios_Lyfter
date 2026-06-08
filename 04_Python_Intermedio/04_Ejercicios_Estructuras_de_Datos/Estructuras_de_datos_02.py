# Ejercicios de Estructuras de Datos -- Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 02:

# Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    data: str
    next_node: "Node"

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(f"{current_node.data}")
            current_node = current_node.next_node

class DoubleEndedQueue(LinkedList):
    def __init__(self, head):
        super().__init__(head)
        self.tail = self.head

    def print_structure(self):
        printer = "head"
        current_node = self.head
        while (current_node is not None):
            printer += "--> " + current_node.data
            current_node = current_node.next_node
        printer += "--tail"
        print(printer)
    
    def push_left(self,new_node):
        if self.head:
            new_node.next_node = self.head
            self.head = new_node
            return
        self.head = new_node
        self.tail = self.head
    
    def push_right(self,new_node):
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
            return
        self.head = new_node
        self.tail = new_node

    def pop_left(self):
        if self.head:
            new_head = self.head.next_node  # Lo hago de esta manera para desvincular el nodo
            self.head.next_node = None      # que estoy quitando y luego si consulto su next_node
            self.head = new_head            # se muestre: None

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

node_1 = Node("black")
node_2 = Node("white")
node_3 = Node("red")

print("Creamos la estructura y agregamos el primer nodo")
led_lights = DoubleEndedQueue(node_2)
led_lights.print_structure()
print("Agregamos un nodo a la izquierda")
led_lights.push_left(node_1)
led_lights.print_structure()
print("Agregamos otro nodo a la izquierda")
led_lights.push_left(node_3)
led_lights.print_structure()
print("Retiramos un nodo de la izquierda")
led_lights.pop_left()
led_lights.print_structure()
print("Agregamos un nodo a la derecha")
led_lights.push_right(node_3)
led_lights.print_structure()
print("Retiramos un nodo de la derecha")
led_lights.pop_right()
led_lights.print_structure()
print("Retiramos otro nodo de la derecha")
led_lights.pop_right()
led_lights.print_structure()
print("Retiramos el único nodo desde la derecha")
led_lights.pop_right()
led_lights.print_structure()
print("Agregamos un nodo por la derecha")
led_lights.push_right(node_2)
led_lights.print_structure()
print("Retiramos el único nodo desde la izquierda")
led_lights.pop_right()
led_lights.print_structure()
print("Agregamos un nodo por la izquierda")
led_lights.push_right(node_1)
led_lights.print_structure()
print("Retiramos el único nodo desde la derecha")
led_lights.pop_right()
led_lights.print_structure()

