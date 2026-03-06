# Ejercicios Extra de Diccionarios - Python Básico
# Emmanuel Piedra Esquivel
# Programa 03:
# Dada una lista de productos vendidos, donde cada uno tiene categoría y precio,
# cree un diccionario que acumule el total por categoría.

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

sales_per_category = {}

for sale in products:
    if sales_per_category.get(sale["category"]) == None:
        sales_per_category[sale["category"]] = 0
    sales_per_category[sale["category"]] += sale["price"]

print(sales_per_category)