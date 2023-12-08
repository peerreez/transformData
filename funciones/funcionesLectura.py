import pandas as pd
from variables.variables import ruta_csv


def leerCsv():
    try:
        datos = pd.read_csv(ruta_csv)
        print("Lectura exitosa:")
        print(datos)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en la ruta '{ruta_csv}'.")
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo en la ruta '{ruta_csv}' está vacío.")
    except pd.errors.ParserError:
        print(f"Error: No se pudo parsear correctamente el archivo en la ruta '{ruta_csv}'. Verifica el formato del CSV.")
    except Exception as e:
        print(f"Error inesperado: {e}")

