# Ejercicios Extra de OOP - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 03

# Cree una clase Product con:
#   - Nombre, precio y cantidad
#   - Cree una clase Inventory que:
#   - Guarde productos en una lista
#   - Tenga métodos para:
#       - Agregar un producto
#       - Mostrar todos los productos
#       - Calcular el valor total del inventario

class Product():
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class Inventory():
    def __init__(self):
        self.stock = []
    
    def add_product(self,product):
        self.stock.append(product)
        print(f"--Se agregó el producto {product.name} al inventario--")
    
    def show_stock(self):
        for p in self.stock: 
            print(f"\n--Nombre: {p.name}")
            print(f"Precio: ${p.price}")
            print(f"Cantidad: {p.quantity}")

    def calculate_stock_value(self):
        total = 0
        for p in self.stock:
            total += p.price*p.quantity
        print(f"\nEl valor total del inventario es de: ${total}")


product1 = Product("Black Forest Cake",30,3)
product2 = Product("Lemon Drizzle Cake",20,5)
product3 = Product("Coffe Cake",15,7)
product4 = Product("Pound Cake",25,4)
product5 = Product("Angel Food Cake",50,1)

my_inventory = Inventory()
my_inventory.add_product(product1)
my_inventory.add_product(product2)
my_inventory.add_product(product3)
my_inventory.add_product(product4)
my_inventory.add_product(product5)
my_inventory.show_stock()
my_inventory.calculate_stock_value()
