# Ejercicios Extra de Unit Testing - Python Intermedio
# Emmanuel Piedra Esquivel
# Módulo de pruebas, ejercicio 01:

import unittest
from func_extra import (addition, avg, celsius_to_fahrenheit)

# 1. Cree una clase de pruebas que contenga al menos 3 funciones que operen con números (como suma, promedio, conversión, etc.) y escriba:
#   - Un caso con números positivos
#   - Un caso con números negativos
#   - Un caso con ceros

class TestMath(unittest.TestCase):

    def test_addition_with_positives(self):
        a = 5
        b = 2
        result = addition(a,b)
        self.assertEqual(result,7)

    def test_addition_with_negatives(self):
        a = -12
        b = -3
        result = addition(a,b)
        self.assertEqual(result,-15)

    def test_addition_with_zeros(self):
        a = 0
        b = 0
        result = addition(a,b)
        self.assertEqual(result,0)

    def test_avg_with_positives(self):
        input_list = [10,20,40,50]
        result = avg(input_list)
        self.assertEqual(result,30)

    def test_avg_with_negatives(self):
        input_list = [-20,-10,10,20]
        result = avg(input_list)
        self.assertEqual(result,0)

    def test_avg_with_zeros(self):
        input_list = [0,0,0,0]
        result = avg(input_list)
        self.assertEqual(result,0)

    def test_celsius_to_fahrenheit_positive(self):
        input_temp = 25
        result = celsius_to_fahrenheit(input_temp)
        self.assertEqual(result,77)

    def test_celsius_to_fahrenheit_negative(self):
        input_temp = -5
        result = celsius_to_fahrenheit(input_temp)
        self.assertEqual(result,23)

    def test_celsius_to_fahrenheit_zero(self):
        input_temp = 0
        result = celsius_to_fahrenheit(input_temp)
        self.assertEqual(result,32)


if __name__ == '__main__':
    unittest.main()