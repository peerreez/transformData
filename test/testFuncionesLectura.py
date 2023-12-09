import io
import unittest
import pandas as pd
from funciones.funcionesLectura import *
from unittest.mock import MagicMock
from variables.variables import ruta_csv

class TestLeerCsv(unittest.TestCase):

    def test_lectura_exitosa(self):
        salida_esperada = "Lectura exitosa:"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            leerCsv()
            self.assertIn(salida_esperada, mock_stdout.getvalue().strip())


    def test_error_inesperado(self):
        ruta_csv = 'archivo_valido.csv'
        # Simula un error inesperado al leer el archivo
        with unittest.mock.patch('pandas.read_csv', side_effect=Exception('Error inesperado')):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                leerCsv()
                self.assertIn("Error inesperado: Error inesperado", mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
