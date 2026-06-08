# Ejercicios Extra de Estructuras de Datos -- Python Intermedio
# Emmmanuel Piedra Esquivel
# Programa 03:

# ista doblemente enlazada
#   - Requisitos:
#       - Cada nodo debe tener referencia al siguiente y al anterior
#   - Métodos:
#       - append(data): Agrega al final
#       - prepend(data): Agrega al inicio
#       - delete(data): Elimina el primer nodo con ese valor
#       - print_forward() y print_backward(): Imprime en ambas direcciones

class Node:
    data: str
    next_node: Node
    previous_node: Node

    def __init__(self, data, previous_node=None,next_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

class DoubleLinkedList():
    head: Node

    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def prepend(self,data):
        if self.head:
            new_node = Node(data,next_node=self.head)
            self.head.previous_node = new_node
            self.head = new_node
            return
        self.head = Node(data)
        self.tail = self.head
    
    def append(self,data):
        if self.tail:
            new_node = Node(data,previous_node=self.tail)
            self.tail.next_node = new_node
            self.tail = new_node
            return
        self.head = Node(data)
        self.tail = self.head

    def delete(self,data):
        if self.head == self.tail:
            if self.head.data == data:
                self.head = None
                self.tail = None
                return
            return
        current_node = self.head
        while(current_node.data != data):
            if current_node.next_node is None:
                print("En la lista no existe ningún nodo con el valor indicado")
                return
            current_node = current_node.next_node
        if current_node.previous_node:
            current_node.previous_node.next_node = current_node.next_node
            if current_node == self.tail:
                self.tail = current_node.previous_node
                return
            current_node.next_node.previous_node = current_node.previous_node
            return
        self.head = current_node.next_node
        self.head.previous_node = None

    def print_forward(self):
        printer = "front"
        current_node = self.head
        while (current_node is not None):
            printer += "-> " + str(current_node.data)
            current_node = current_node.next_node
        printer += "-> back"
        print(printer)

    def print_backward(self):
        printer = "back"
        current_node = self.tail
        while (current_node is not None):
            printer += " <-" + str(current_node.data)
            current_node = current_node.previous_node
        printer += " <-front"
        print(printer)

print("Se crea la lista y se agregan los nodos A, B, C")
letters = DoubleLinkedList('A')
letters.append('B')
letters.append('C')
letters.print_forward()
letters.print_backward()
print("Se agrega el nodo X al final")
letters.prepend('X')
letters.print_forward()
letters.print_backward()
print("Se elimina el nodo B")
letters.delete('B')
letters.print_forward()
letters.print_backward()
