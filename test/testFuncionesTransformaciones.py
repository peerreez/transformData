import unittest
import sys
import numpy as np
from io import StringIO
from funciones.transformacionesCsv import *
from unittest.mock import patch

class TestVisualizarCity(unittest.TestCase):
    def test_lectura_de_datos(self):
        # Supongamos que tienes un archivo CSV llamado 'test_data.csv' con algunas ciudades
        ruta_csv = 'test_data.csv'
        
        # Captura la salida estándar para verificarla
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Llama a la función y recupera la salida estándar
        result = visualizarCity()
        sys.stdout = sys.__stdout__
        
        # Verifica que la función devuelva algo y que la salida contenga ciudades
        self.assertIsNotNone(result)
        self.assertTrue(any(result))
        # Verifica que el resultado sea un array de Numpy
        self.assertIsInstance(result, np.ndarray)

if __name__ == '__main__':
    unittest.main()

