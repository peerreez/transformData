import pandas as pd
from variables.variables import ruta_csv
import matplotlib.pyplot as plt
import seaborn as sns


def visualizarCity():
    """
    Esta función lee un archivo CSV en la ruta especificada y muestra las ciudades únicas presentes en la columna 'City'.
    
    Paso 1: Lee los datos del archivo CSV utilizando Pandas.
    Paso 2: Obtiene ciudades únicas de la columna 'City'.
    Paso 3: Imprime las ciudades distintas presentes en el CSV.

    Nota: Asegúrate de tener la biblioteca Pandas instalada antes de usar esta función.
    """
    datos = pd.read_csv(ruta_csv)
    ciudades_distintas = datos['City'].unique()
    print("Ciudades distintas en el CSV:")
    for ciudad in ciudades_distintas:
        print(ciudad)
    return ciudades_distintas


def distribucionEstado():
    """
    Esta función genera y muestra un gráfico de barras que representa la distribución de vehículos eléctricos por estado.
    
    Paso 1: Lee los datos del archivo CSV en la ruta especificada utilizando Pandas.
    Paso 2: Crea un gráfico de barras utilizando Seaborn para visualizar la distribución por estado.
    Paso 3: Personaliza el gráfico con títulos, etiquetas y rotación del eje x.
    Paso 4: Muestra el gráfico.

    Nota: Asegúrate de tener las bibliotecas Pandas, Matplotlib y Seaborn instaladas antes de usar esta función.
    """
    df = pd.read_csv(ruta_csv)
    plt.figure(figsize=(12, 6))
    sns.countplot(x='State', data=df, order=df['State'].value_counts().index)
    plt.title('Distribución de Vehículos Eléctricos por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Cantidad de Vehículos Eléctricos')
    plt.xticks(rotation=45)
    plt.show()
    


def distribucionCondado():
    """
    Esta función genera y muestra un gráfico de barras que representa la distribución de vehículos eléctricos por condado, mostrando los 10 primeros.
    
    Paso 1: Lee los datos del archivo CSV en la ruta especificada utilizando Pandas.
    Paso 2: Crea un gráfico de barras utilizando Seaborn para visualizar la distribución por condado (Top 10).
    Paso 3: Personaliza el gráfico con títulos, etiquetas y rotación del eje x.
    Paso 4: Muestra el gráfico.

    Nota: Asegúrate de tener las bibliotecas Pandas, Matplotlib y Seaborn instaladas antes de usar esta función.
    """
    df = pd.read_csv(ruta_csv)
    plt.figure(figsize=(12, 6))
    sns.countplot(x='County', data=df, order=df['County'].value_counts().head(10).index)
    plt.title('Distribución de Vehículos Eléctricos por Condado (Top 10)')
    plt.xlabel('Condado')
    plt.ylabel('Cantidad de Vehículos Eléctricos')
    plt.xticks(rotation=45)
    plt.show()


def rangoElectrico():
    """
    Esta función calcula y muestra la distribución del rango eléctrico de los vehículos eléctricos presentes en el conjunto de datos.
    
    Paso 1: Lee los datos del archivo CSV en la ruta especificada utilizando Pandas.
    Paso 2: Calcula estadísticas descriptivas del rango eléctrico.
    Paso 3: Imprime las estadísticas descriptivas.
    Paso 4: Crea un histograma utilizando Seaborn para visualizar la distribución del rango eléctrico.
    Paso 5: Personaliza el gráfico con títulos, etiquetas y leyenda.
    Paso 6: Muestra el histograma.

    Nota: Asegúrate de tener las bibliotecas Pandas, Matplotlib y Seaborn instaladas antes de usar esta función.
    """
    df = pd.read_csv(ruta_csv)
    stats_range = df['Electric Range'].describe()
    print(stats_range)
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Electric Range'], bins=20, kde=True)
    plt.title('Distribución del Rango Eléctrico de Vehículos')
    plt.xlabel('Rango Eléctrico')
    plt.ylabel('Frecuencia')
    plt.show()


def comparacionRangoElectrico():
    """
    Esta función compara el rango eléctrico de vehículos a lo largo de los años del modelo utilizando un gráfico de caja.
    
    Paso 1: Lee los datos del archivo CSV en la ruta especificada utilizando Pandas.
    Paso 2: Crea un gráfico de caja utilizando Seaborn para comparar el rango eléctrico por año del modelo.
    Paso 3: Personaliza el gráfico con títulos, etiquetas y leyenda.
    Paso 4: Muestra el gráfico.

    Nota: Asegúrate de tener las bibliotecas Pandas, Matplotlib y Seaborn instaladas antes de usar esta función.
    """
    df = pd.read_csv(ruta_csv)
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Model Year', y='Electric Range', data=df)
    plt.title('Comparación de Rango Eléctrico por Año del Modelo')
    plt.xlabel('Año del Modelo')
    plt.ylabel('Rango Eléctrico')
    plt.show()


def normalizacionRangoElectrico():
    """
    Esta función realiza la normalización del rango eléctrico de los vehículos y muestra los valores normalizados.
    
    Paso 1: Lee los datos del archivo CSV en la ruta especificada utilizando Pandas.
    Paso 2: Calcula la normalización del rango eléctrico utilizando la fórmula estándar.
    Paso 3: Imprime los valores normalizados.

    Nota: Asegúrate de tener la biblioteca Pandas instalada antes de usar esta función.
    """
    df = pd.read_csv(ruta_csv)
    df['Electric Range Normalized'] = ((df['Electric Range'] - df['Electric Range'].mean()) / df['Electric Range'].std()).round(5)
    print(df['Electric Range Normalized'].to_string(index=False))


def categoriasRangoElectrico():
    """
    Esta función asigna categorías al rango eléctrico de los vehículos (Bajo, Medio, Alto) y muestra las categorías resultantes.
    
    Paso 1: Lee los datos del archivo CSV en la ruta especificada utilizando Pandas.
    Paso 2: Define los límites y etiquetas de las categorías de rango eléctrico.
    Paso 3: Utiliza pd.cut() para asignar categorías al rango eléctrico.
    Paso 4: Imprime las categorías resultantes.

    Nota: Asegúrate de tener la biblioteca Pandas instalada antes de usar esta función.
    """
    df = pd.read_csv(ruta_csv)
    bins = [0, 100, 200, float('inf')]
    labels = ['Bajo', 'Medio', 'Alto']
    df['Range Category'] = pd.cut(df['Electric Range'], bins=bins, labels=labels, right=False)
    print(df['Range Category'])
