# Cree una estructura de objetos que asemeje una Queue.
#   - Debe incluir los métodos de enqueue (para agregar nodos) y dequeue (para quitar nodos).
#   - Debe incluir un método para hacer print de toda la estructura.
#   - No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

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
            print(current_node.data)
            current_node = current_node.next_node

class Queue(LinkedList):
    def __init__(self, head):
        super().__init__(head)
    
    def enqueue(self,new_node):
        current_node = self.head
        while(current_node.next_node is not None):
            current_node = current_node.next_node
        current_node.next_node = new_node

    def dequeue(self):
        if self.head:
            new_head = self.head.next_node
            self.head.next_node = None
            self.head = new_head

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")

print("\nSe crea la instancia queue y se agrega el nodo head (A)")
my_queue = Queue(node_a)
my_queue.print_structure()
print("Se agrega al final el nodo B")
my_queue.enqueue(node_b)
my_queue.print_structure()
print("Se agrega al final el nodo C")
my_queue.enqueue(node_c)
my_queue.print_structure()
print("Se comprueba que el atributo next de los nodos si se modifica con el método")
print(f"Siguiente nodo de B --> {node_b.nextnode.data}")
print("Se agrega al final el nodo D")
my_queue.enqueue(node_d)
my_queue.print_structure()
print("Se elimina el primer nodo (First In, First Out)")
my_queue.dequeue()
my_queue.print_structure()
print("Se verifica que el nodo A que ya no está en cola no tiene un next asignado")
print(f"Siguiente nodo de A --> {node_a.nextnode}")
print("Se agrega el nodo A al final de la cola")
my_queue.enqueue(node_a)
my_queue.print_structure()