# Ejercicios de Estructuras de Datos -- Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 01:

# Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
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
            print(f"-{current_node.data}")
            current_node = current_node.next_node

class Stack(LinkedList):
    def __init__(self, head):
        super().__init__(head)
    
    def push(self,new_node):
        if self.head:
            new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            new_head = self.head.next_node  # Lo hago de esta manera para desvincular el nodo
            self.head.next_node = None      # que estoy quitando y luego si consulto su next_node
            self.head = new_head            # se muestra: None

print("Agrego el primer ingrediente e imprimo la lista")
hamburguer = Stack(Node("pan"))
hamburguer.print_structure()
print("Agrego el segundo ingrediente, que se coloca arriba del primero")
hamburguer.push(Node("lechuga"))
hamburguer.print_structure()
print("Agrego el tercer ingrediente, que se coloca arriba del stack")
hamburguer.push(Node("torta"))
hamburguer.print_structure()
print("Agrego otro ingrediente, que se coloca arriba del stack")
hamburguer.push(Node("queso"))
hamburguer.print_structure()
print("Agrego otro ingrediente, que se coloca arriba del stack")
hamburguer.push(Node("tomate"))
hamburguer.print_structure()
print("Agrego otro ingrediente, que se coloca arriba del stack")
hamburguer.push(Node("pan"))
hamburguer.print_structure()
print("Elimino un ingrediente, se elimina el pan que está arriba del stack")
hamburguer.pop()
hamburguer.print_structure()
print("Agrego otro ingrediente, que se coloca arriba del stack")
hamburguer.push(Node("cebolla"))
hamburguer.print_structure()
print("Agrego otro ingrediente, que se coloca arriba del stack")
hamburguer.push(Node("pan"))
hamburguer.print_structure()


