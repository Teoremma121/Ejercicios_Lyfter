# Ejercicios Extra de Diccionarios - Python Básico
# Emmanuel Piedra Esquivel
# Programa 01:
# Dada una lista de ventas con la siguiente información:
# - date
# - customer_email
# - items
# Y cada item teniendo la siguiente información:
# - name
# - upc
# - unit_price
# Cree un diccionario que guarde el total de ventas de cada UPC.

sales = [
{
'date':'27/02/23',
'customer_email':'joe@gmail.com',
'items': [
{'name':'Lava Lamp','upc':'ITEM-453','unit_price': 65.76},
{'name':'Iron', 'upc':'ITEM-324','unit_price': 32.45},
{'name':'Basketball','upc':'ITEM-432','unit_price':12.54}
]
},
{		
'date':'27/02/23',
'customer_email':'david@gmail.com',
'items': [
{'name':'Lava Lamp','upc':'ITEM-453','unit_price':65.76},
{'name':'Key Holder','upc':'ITEM-23','unit_price':5.42},
]	
},	
{		
'date':'26/02/23',
'customer_email':'amanda@gmail.com',
'items': [
{'name':'Key Holder','upc':'ITEM-23','unit_price':3.42},
{'name':'Basketball','upc':'ITEM-432','unit_price':17.54},
]	
},
]

total_sales_per_upc = {}

for sale in sales:
    for item in sale['items']:
        if total_sales_per_upc.get(item["upc"]) == None:
            total_sales_per_upc[item["upc"]] = 0
        total_sales_per_upc[item["upc"]] += item["unit_price"]

print(total_sales_per_upc)



