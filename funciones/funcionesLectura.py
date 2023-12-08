import pandas as pd
from variables.variables import ruta_csv


def leerCsv():
    """
    Esta función intenta leer un archivo CSV en la ruta especificada utilizando Pandas.
    Muestra los datos leídos si la operación es exitosa.
    
    Excepciones manejadas:
    - FileNotFoundError: El archivo no se encuentra en la ruta especificada.
    - pd.errors.EmptyDataError: El archivo en la ruta especificada está vacío.
    - pd.errors.ParserError: No se pudo parsear correctamente el archivo CSV. Verifica el formato.
    - Exception: Cualquier otro error inesperado.

    Nota: Asegúrate de tener la biblioteca Pandas instalada antes de usar esta función.
    """
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


def mostrarTiposDeDatosCsv():
    """
    Intenta leer un archivo CSV en la ruta especificada utilizando Pandas.
    Muestra los tipos de datos de cada columna si la operación es exitosa.

    Excepciones manejadas:
    - FileNotFoundError: El archivo no se encuentra en la ruta especificada.
    - pd.errors.EmptyDataError: El archivo en la ruta especificada está vacío.
    - pd.errors.ParserError: No se pudo leer correctamente el archivo CSV. Verifica el formato.

    Nota: Asegúrate de tener la biblioteca Pandas instalada antes de usar esta función.
    """
    try:
        datos = pd.read_csv(ruta_csv)
        columnas_y_tipos = datos.dtypes
        print("Tipos de datos de cada columna:")
        print(columnas_y_tipos)
    except FileNotFoundError:
        print(f"No se encontró el archivo en la ruta: {ruta_csv}")
    except pd.errors.EmptyDataError:
        print(f"El archivo en la ruta {ruta_csv} está vacío.")
    except pd.errors.ParserError:
        print(f"No se pudo leer el archivo en la ruta {ruta_csv}. Verifica el formato CSV.")