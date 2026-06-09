# Ejercicios Extra de Unit Testing - Python Intermedio
# Emmanuel Piedra Esquivel
# Módulo de pruebas, Ejercicio Extra 02:

# Cree un test que:
#   - Valide que dividir(10, 2) retorna 5.0
#   - Verifique que dividir por cero lanza un ValueError
#   - Valide que dividir con un string como parámetro también lanza TypeError

import unittest
from func_extra import (divide)

class TestDivide(unittest.TestCase):
    def test_divide(self):
        pass