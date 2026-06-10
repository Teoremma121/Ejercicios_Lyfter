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
        a = 10
        b = 2
        result = divide(a,b)
        self.assertEqual(result,5.0)

    def test_divide_by_zero(self):
        a = 10
        b = 0
        with self.assertRaises(ValueError):
            divide(a,b)
    
    def test_divide_by_string(self):
        a = 10
        b = "string"
        with self.assertRaises(TypeError):
            divide(a,b)

if __name__ == '__main__':
    unittest.main()