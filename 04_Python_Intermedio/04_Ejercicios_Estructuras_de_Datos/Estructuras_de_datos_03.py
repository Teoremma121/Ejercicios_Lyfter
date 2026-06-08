# Ejercicios de Estructuras de Datos -- Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 03:

# Cree una estructura de objetos que asemeje un Binary Tree.
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    data: str
    child_a: Node
    child_b: Node
    parent: Node
    level: int

    def __init__(self, data):
        self.data = data
        self.child_a = None
        self.child_b = None
        self.parent = None
        self.level = None

    def print_node(self):
        parent = "-root-"
        if self.parent:
            parent = self.parent.data
        print(f"-{self.data}, Nivel: {self.level}, Padre: {parent}")
        if self.child_a:
            self.child_a.print_node()
        if self.child_b:
            self.child_b.print_node()


class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root
        self.root.level = 0

    def add_node(self,new_node,parent):
        if parent.child_a:
            if parent.child_b:
                print("Ya el nodo padre tiene 2 hijos, no hay espacio para agregar el nuevo nodo")
                return
            parent.child_b = new_node
        else:
            parent.child_a = new_node
        new_node.parent = parent
        new_node.level = parent.level + 1

    def print_structure(self):
        self.root.print_node()

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")
node_h = Node("H") 
my_tree = BinaryTree(node_a)
my_tree.add_node(node_b,node_a)
my_tree.add_node(node_c,node_a)
my_tree.print_structure()
my_tree.add_node(node_d,node_c)
print("")
my_tree.print_structure()
my_tree.add_node(node_e,node_b)
my_tree.add_node(node_f,node_c)
my_tree.add_node(node_g,node_b)
print("")
my_tree.add_node(node_h,node_c)
my_tree.add_node(node_h,node_g)
print("")
my_tree.print_structure()
