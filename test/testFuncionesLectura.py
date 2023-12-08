
import unittest
import pandas as pd
from funciones.funcionesLectura import *


class TestLeerCsv(unittest.TestCase):

    def test_lectura_exitosa(self):
        ruta_csv = 'ruta_valida.csv'
        salida_esperada = "Lectura exitosa:"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            leerCsv(ruta_csv)
            self.assertIn(salida_esperada, mock_stdout.getvalue().strip())

    def test_archivo_no_encontrado(self):
        ruta_csv = 'ruta_invalida.csv'
        salida_esperada = f"Error: Archivo no encontrado en la ruta '{ruta_csv}'."
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            leerCsv(ruta_csv)
            self.assertIn(salida_esperada, mock_stdout.getvalue().strip())

    def test_archivo_vacio(self):
        ruta_csv = 'archivo_vacio.csv'
        salida_esperada = f"Error: El archivo en la ruta '{ruta_csv}' está vacío."
        # Simula un archivo vacío
        with open(ruta_csv, 'w') as f:
            pass
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            leerCsv(ruta_csv)
            self.assertIn(salida_esperada, mock_stdout.getvalue().strip())

    def test_formato_csv_invalido(self):
        ruta_csv = 'formato_invalido.csv'
        salida_esperada = f"Error: No se pudo parsear correctamente el archivo en la ruta '{ruta_csv}'. Verifica el formato del CSV."
        # Simula un archivo con formato incorrecto
        with open(ruta_csv, 'w') as f:
            f.write('a,b,c\n1,2,3,4')  # Número incorrecto de columnas
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            leerCsv(ruta_csv)
            self.assertIn(salida_esperada, mock_stdout.getvalue().strip())

    def test_error_inesperado(self):
        ruta_csv = 'archivo_valido.csv'
        # Simula un error inesperado al leer el archivo
        with unittest.mock.patch('pandas.read_csv', side_effect=Exception('Error inesperado')):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                leerCsv(ruta_csv)
                self.assertIn("Error inesperado: Error inesperado", mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
