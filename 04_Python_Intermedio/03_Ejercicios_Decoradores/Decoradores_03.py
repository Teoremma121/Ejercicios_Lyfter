# Ejercicios de Decoradores - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 03:

# Cree una clase de User que:
#   - Tenga un atributo de date_of_birth.
#   - Tenga un property de age.
#   - Luego cree un decorador para funciones que acepten un User como parámetro que se 
#       encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.

from datetime import date

def check_age_majority(func):
    def wrapper(user):
        try:
            if user.age < 18:
                raise Exception(f"Usuario -{user.name} no cumple con la mayoría de edad")
            func(user)
        except Exception as e:
            print(f"Error: {e}")
    return wrapper

class User():
    def __init__(self,name,date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - (
            (today.month,today.day) 
            < (self.date_of_birth.month,self.date_of_birth.day))
        return age

@check_age_majority    
def access_permission(user):
    print(f"Usuario -{user.name} tiene permiso de acceso")
    
user_1 = User("Rubeus Hagrid",date(1999,1,12))
user_2 = User("Draco Malfoy",date(2008,8,22))

access_permission(user_1)
access_permission(user_2)