from funciones.funcionesLectura import *
from funciones.tranformacionesCsv import *


def mostrar_menu():
    print("1. Leer CSV")
    print("2. Visualizar Ciudades Distintas")
    print("3. Mostrar las columnas del CSV")
    print("4. Distribucion Estado")
    print("5. Distribucion Condado")
    print("6. Rango Electrico")
    print("7. Comparacion Rango Electrico")
    print("8. Normalizacion Rango Electrico")
    print("8. Categorias Rango Electrico")
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
    print("Has seleccionado la Opción 7")
    comparacionRangoElectrico()


def opcion8():
    print("Has seleccionado la Opción 8")
    normalizacionRangoElectrico()


def opcion9():
    print("Has seleccionado la Opción 9")
    categoriasRangoElectrico()