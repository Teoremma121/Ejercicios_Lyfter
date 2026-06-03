# Ejercicios Extra de Decoradores - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 2:

# Cree un decorador @requires_login que:
#   - Verifique si la variable global user_logged_in es True
#   - Si no lo es, debe lanzar una excepción "Usuario no autenticado"
#   - Si lo es, la función decorada se ejecuta normalmente

users_list = []
user_logged_in = False

def requires_login(func):
    def wrapper(*args):
        if user_logged_in:
            return func(*args)
        print("Usuario no autenticado")
    return wrapper

class User():
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
    
    @classmethod
    def register(cls,name,email,password):
        users_list.append({'name':name,'email':email,'password':password})
        print(f"Se registró el usuario: {name}")
        return User(name,email,password)
    
    @classmethod
    def login(cls,email,password):
        for user in users_list:
            if email == user['email']:
                if password == user['password']:
                    print(f"Ha iniciado sesión con el usuario: {user['name']}")
                    return True
                else:
                    print("La contraseña digitada es incorrecta")
                    return False
        print("No se encuentra registrado un usuario con el correo electrónico digitado")

@requires_login    
def add_item_to_car(item):
    print(f"Se añadió el item: {item} al carrito")

def logout():
    print("Cerró la sesión")
    return False

User.register('Teoremma121','novatogames121@gmail.com',"54321")
user_logged_in = User.login("novatogames121@gmail.com","54321")
add_item_to_car("pink_mousepad")
user_logged_in = logout()
print("\n")
User.register('InfernalToad','peach.and.toad@gmail.com','Mario.is.dumb')
user_logged_in = User.login('peach.and.toad@gmail.com','DumbMario')
add_item_to_car("love_poisson")

