# Ejercicios Extra de Estructuras de Datos -- Python Intermedio
# Emmmanuel Piedra Esquivel
# Programa 02:

# Cree una clase LinkedList con los métodos:
#   - insert_front(data): Inserta al inicio
#   - insert_back(data): Inserta al final
#   - delete(data): Elimina el primer nodo con el valor dado
#   - print_all(): Imprime todos los valores

class Node:
    data: int
    next_node: Node

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList():
    head: Node

    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def insert_front(self,data):
        if self.head:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
            return
        self.head = Node(data)
        self.tail = self.head
    
    def insert_back(self,data):
        if self.tail:
            new_node = Node(data)
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
        previous_node = None
        current_node = self.head
        next_node = current_node.next_node
        while(current_node.data != data):
            if not next_node:
                print("En la lista no existe ningún nodo con el valor indicado")
                return
            previous_node = current_node
            current_node = next_node
            next_node = current_node.next_node
        if previous_node:
            previous_node.next_node = next_node
            if current_node == self.tail:
                self.tail = previous_node
            return
        self.head = next_node

    def print_all(self):
        printer = "front"
        current_node = self.head
        while (current_node is not None):
            printer += "-> " + str(current_node.data)
            current_node = current_node.next_node
        printer += "-> back"
        print(printer)

print("Se crea la lista")
ll = LinkedList(10)
ll.print_all()
print("Se inserta 20 al frente")
ll.insert_front(20)
ll.print_all()
print("Se inserta 30 atrás")
ll.insert_back(30)
ll.print_all()
print("Se elimina el primer 10 en el orden")
ll.delete(10)
ll.print_all()
print("Se insertan varios datos")
ll.insert_back(15)
ll.insert_back(5)
ll.insert_back(15)
ll.print_all()
print("Se elimna el primer 15 en el orden")
ll.delete(15)
ll.print_all()
print("Se elimna el primer 15 en el orden")
ll.delete(15)
ll.print_all()
print("Se eliminan todos los datos")
ll.delete(30)
ll.delete(5)
ll.print_all()
ll.delete(20)
ll.print_all()
print("Se agrega un dato por atrás")
ll.insert_back(40)
ll.print_all()
print("Se elimina el dato")
ll.delete(40)
ll.print_all()
print("Se agrega un dato por el frente")
ll.insert_front(20)
ll.print_all()