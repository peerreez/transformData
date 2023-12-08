import pandas as pd
from variables.variables import ruta_csv

def visualizarCity():
    # Leer el archivo CSV
    datos = pd.read_csv(ruta_csv)

    # Obtener ciudades distintas
    ciudades_distintas = datos['City'].unique()

    # Mostrar las ciudades distintas
    print("Ciudades distintas en el CSV:")
    for ciudad in ciudades_distintas:
        print(ciudad)