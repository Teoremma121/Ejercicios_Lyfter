# Ejercicios de Diccionarios - Python Básico
# Emmanuel Piedra Esquivel
# Programa 01:
# Cree un diccionario que guarde la siguiente información sobre un hotel:
# -nombre
# -numero_de_estrellas
# -habitaciones
# El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
# -numero
# -piso
# -precio_por_noche

hotel = {
    "name":"Sandy Bay",
    "stars_number": 3,
    "rooms":[
        {"number": 207,"floor": 2,"price_per_night": 150},
        {"number": 303,"floor": 3,"price_per_night": 200},
        {"number": 701,"floor": 7,"price_per_night": 500}
    ]
}

price = hotel["rooms"][2]["price_per_night"]
print(f"El precio por noche de la habitación 701 en el Sandy Bay es de: ${price}")