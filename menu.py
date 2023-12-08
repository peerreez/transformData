"""
Este script ejecuta un menú interactivo que permite al usuario realizar diversas operaciones en un conjunto de datos de vehículos eléctricos.
Importa funciones del módulo 'funcionesMenu' para mostrar el menú y ejecutar las opciones seleccionadas por el usuario.

Cada opción del menú llama a funciones específicas para llevar a cabo operaciones como leer un archivo CSV, visualizar datos, mostrar estadísticas,
realizar transformaciones y más. El bucle continuará ejecutándose hasta que el usuario elija salir.

Nota: Asegúrate de tener el módulo 'funcionesMenu' disponible en el mismo directorio o especifica la ruta correcta.
"""
from funciones.funcionesMenu import *

while True:
    mostrar_menu()
    opcion = input("\nSelecciona una opción: ")
    if opcion == '1':
        opcion1()
    elif opcion == '2':
        opcion2()
    elif opcion == '3':
        opcion3()
    elif opcion == '4':
        opcion4()
    elif opcion == '5':
        opcion5()
    elif opcion == '6':
        opcion6()
    elif opcion == '7':
        opcion7()
    elif opcion == '8':
        opcion8()
    elif opcion == '9':
        opcion9()
    elif opcion == '0':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor")
