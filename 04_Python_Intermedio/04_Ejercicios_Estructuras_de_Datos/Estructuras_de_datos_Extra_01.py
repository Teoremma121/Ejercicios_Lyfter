# Ejercicios Extra de Estructuras de Datos -- Python Intermedio
# Emmmanuel Piedra Esquivel
# Programa 01:

# Cree una estructura que represente una cola básica (Queue) con objetos enlazados
#   - Restricción:
#       - no usar list, dict, tuple, collections
#   - Métodos requeridos:
#       - enqueue(data): agrega un nodo al final
#       - dequeue(): elimina y retorna el nodo del inicio
#       - print_all(): imprime todos los elementos de la cola en 

class Node:
    data: str
    next_node: "Node"

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:
    head: Node

    def __init__(self, data):
        self.head = Node(data)
    
    def enqueue(self,data):
        current_node = self.head
        while(current_node.next_node is not None):
            current_node = current_node.next_node
        current_node.next_node = Node(data)

    def dequeue(self):
        if self.head:
            old_head = self.head
            self.head = self.head.next_node
            print(old_head.data)
            return old_head
        
    def print_all(self):
        printer = "No hay nodos en la cola"
        if self.head:
            printer = self.head.data
            current_node = self.head.next_node
            while (current_node is not None):
                printer += " -> " + current_node.data
                current_node = current_node.next_node
        print(printer)

print("Se agregan A, B y C a la cola")
q = Queue('A')
q.enqueue('B')
q.enqueue('C')
q.print_all()
print("Se quita A de la cola")
q.dequeue()
print("Cola actualizada:")
q.print_all()
print("Se agrega A a la cola")
q.enqueue('A')
q.print_all()