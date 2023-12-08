import pandas as pd
from variables.variables import ruta_csv
import matplotlib.pyplot as plt
import seaborn as sns

def visualizarCity():
    # Lee los datos del archivo CSV
    datos = pd.read_csv(ruta_csv)

    # Obtiene ciudades únicas y las imprime
    ciudades_distintas = datos['City'].unique()
    print("Ciudades distintas en el CSV:")
    for ciudad in ciudades_distintas:
        print(ciudad)

def distribucionEstado():
    # Lee los datos del archivo CSV
    df = pd.read_csv(ruta_csv)
    
    # Crea un gráfico de barras horizontales para la distribución de vehículos por estado
    plt.figure(figsize=(12, 6))
    sns.countplot(x='State', data=df, order=df['State'].value_counts().index)
    
    # Configuración del gráfico
    plt.title('Distribución de Vehículos Eléctricos por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Cantidad de Vehículos Eléctricos')
    plt.xticks(rotation=45)
    plt.show()

def distribucionCondado():
    # Lee los datos del archivo CSV
    df = pd.read_csv(ruta_csv)
    
    # Crea un gráfico de barras horizontales para la distribución de vehículos por condado (Top 10)
    plt.figure(figsize=(12, 6))
    sns.countplot(x='County', data=df, order=df['County'].value_counts().head(10).index)
    
    # Configuración del gráfico
    plt.title('Distribución de Vehículos Eléctricos por Condado (Top 10)')
    plt.xlabel('Condado')
    plt.ylabel('Cantidad de Vehículos Eléctricos')
    plt.xticks(rotation=45)
    plt.show()


def rangoElectrico():
    df = pd.read_csv(ruta_csv)
    # Estadísticas resumidas del rango eléctrico
    stats_range = df['Electric Range'].describe()
    print(stats_range)
    # Histograma del rango eléctrico
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Electric Range'], bins=20, kde=True)
    plt.title('Distribución del Rango Eléctrico de Vehículos')
    plt.xlabel('Rango Eléctrico')
    plt.ylabel('Frecuencia')
    plt.show()


def comparacionRangoElectrico():
    df = pd.read_csv(ruta_csv)
    # Comparación de rango eléctrico por año del modelo
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Model Year', y='Electric Range', data=df)
    plt.title('Comparación de Rango Eléctrico por Año del Modelo')
    plt.xlabel('Año del Modelo')
    plt.ylabel('Rango Eléctrico')
    plt.show()