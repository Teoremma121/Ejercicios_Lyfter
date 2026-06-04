# Ejercicios Extra de Los 4 de OOP - Python Intermedio
# Emmanuel Piedra Esquivel
# Programa 02:

# Cree una clase abstracta User con los siguientes métodos abstractos:
#   - get_role()
#   - has_permission(permission)
#   - Luego cree dos clases que hereden de ella:
#       - AdminUser
#       - RegularUser
#       - Cada una debe implementar los métodos

from abc import (ABC, abstractmethod)

class User(ABC):
    def __init__(self, name):
        self.name = name
        self.permissions = {'create':False,'delete':False,'edit':False,'read':False}

    @abstractmethod
    def get_role(self):
        return None
    
    @abstractmethod
    def has_permission(self,permission):
        return self.permissions[permission]

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.permissions['create'] = True
        self.permissions['delete'] = True
        self.permissions['edit'] = True
        self.permissions['read'] = True
    
    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return super().has_permission(permission)
    
class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.permissions['create'] = False
        self.permissions['delete'] = False
        self.permissions['edit'] = False
        self.permissions['read'] = True
    
    def get_role(self):
        return "Regular"

    def has_permission(self,permission):
        return super().has_permission(permission)

user1 = RegularUser("Ana")
print(f"Nombre: {user1.name}")
print(f"Rol: {user1.get_role()}")
print(f"Permiso para crear: {user1.has_permission('create')}")
print(f"Permiso para borrar: {user1.has_permission('delete')}")
print(f"Permiso para editar: {user1.has_permission('edit')}")
print(f"Permiso para leer: {user1.has_permission('read')}")

user2 = AdminUser("Luis")
print(f"Nombre: {user2.name}")
print(f"Rol: {user2.get_role()}")
print(f"Permiso para crear: {user2.has_permission('create')}")
print(f"Permiso para borrar: {user2.has_permission('delete')}")
print(f"Permiso para editar: {user2.has_permission('edit')}")
print(f"Permiso para leer: {user2.has_permission('read')}")

