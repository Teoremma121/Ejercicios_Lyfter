# Ejercicios Extra de Unit Testing - Python Intermedio
# Emmanuel Piedra Esquivel
# Módulo de pruebas, Ejercicio Extra 03:

# Cree un test que:
#   - Use unittest.mock para simular el contenido de un archivo
#   - Verifique que retorna las líneas esperadas sin crear archivos reales
#   - Compruebe que lanza FileNotFoundError si el archivo no existe

import unittest
from func_extra import (read_lines)

class TestReading(unittest.TestCase):
    pass