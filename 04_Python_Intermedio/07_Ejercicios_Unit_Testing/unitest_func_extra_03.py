# Ejercicios Extra de Unit Testing - Python Intermedio
# Emmanuel Piedra Esquivel
# Módulo de pruebas, Ejercicio Extra 03:

# Cree un test que:
#   - Use unittest.mock para simular el contenido de un archivo
#   - Verifique que retorna las líneas esperadas sin crear archivos reales
#   - Compruebe que lanza FileNotFoundError si el archivo no existe

import unittest
from func_extra import (read_lines)
from unittest.mock import (mock_open, patch)

class TestReading(unittest.TestCase):
    def test_read_lines(self):
        mocked_file = mock_open(read_data="línea 1\nlínea 2\nlínea 3")

        with patch("builtins.open", mocked_file):
            content = read_lines("mocked.txt")

        self.assertEqual(content,["línea 1\n", "línea 2\n", "línea 3"])

    def test_read_lines_with_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_lines("mocked.txt")

if __name__ == '__main__':
    unittest.main()