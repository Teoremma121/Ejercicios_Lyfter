# Ejercicios de Los 4 Pilares de OOP - Python Intermedio
# Programa 01:
# Cree una clase de BankAccount que:
#   - Tenga un atributo de balance.
#   - Tenga un método para ingresar dinero.
#   - Tengo un método para retirar dinero.
# Cree otra clase que herede de esta llamada SavingsAccount que:
#   - Tenga un atributo de min_balance que se pueda asignar al crearla.
#   - Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. 
#   - Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.

class MinimumBalanceError(Exception):
    pass

class BankAccount():
    balance = 0

    def deposit_money(self, amount):
        self.balance += amount
        print(f"Se depositó una canditad de ${amount} en la cuenta")

    def withdraw_money(self, amount):
        self.balance -= amount
        print(f"Se retiró una cantidad de ${amount} de la cuenta")


class SavingAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance
        print(f"Se creó una cuenta de ahorros con un balance mínimo de ${min_balance}")
        self.deposit_money(min_balance)
        print(f"... requisito para la creación de la cuenta")
    
    def withdraw_money(self, amount):
        try:
            if (self.balance - amount) < self.min_balance:
                raise MinimumBalanceError("El saldo no puede quedar por debajo del balance mínimo establecido")
            super().withdraw_money(amount)
        except Exception as e:
            print(f"Error: {e}")
            print(f"La cantidad máxima que puede retirar actualmente es de: {self.balance - self.min_balance}")

my_personal_account = SavingAccount(300)
my_personal_account.deposit_money(200)
print(f"El saldo actual de la cuenta es: ${my_personal_account.balance}")
my_personal_account.withdraw_money(300)
print(f"El saldo actual de la cuenta es: ${my_personal_account.balance}")
my_personal_account.withdraw_money(125)
print(f"El saldo actual de la cuenta es: ${my_personal_account.balance}")
