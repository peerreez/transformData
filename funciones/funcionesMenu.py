from funciones.funcionesLectura import *
from funciones.tranformacionesCsv import *


def mostrar_menu():
    print("1. Leer Csv")
    print("2. Visualizar ciudades distintas")
    print("3. Mostrar las columnas del csv")
    print("4. Distribucion estado")
    print("5. Distribucion condado")
    print("6. Rango electrico")
    print("7. Comparacion Rango electrico")
    print("0. Salir\n")


def opcion1():
    print("Lectura del fichero Electric Vehicle Population Data\n")
    leerCsv()


def opcion2():
    print("Se van a mostrar todas las ciudades distintas")
    visualizarCity()


def opcion3():
    print("Has seleccionado la Opción 3.")
    leerColumnas()


def opcion4():
    print("Has seleccionado la Opción 4.")
    distribucionEstado()


def opcion5():
    print("Has seleccionado la Opción 5")
    distribucionCondado()


def opcion6():
    print("Has seleccionado la Opción 6")
    rangoElectrico()


def opcion7():
    print("Has seleccionado la Opción 6")
    comparacionRangoElectrico()