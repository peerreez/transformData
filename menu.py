from funciones.funcionesMenu import *

while True:
    mostrar_menu()  
    # Solicitar al usuario que ingrese una opción
    opcion = input("\nSelecciona una opción (1-4): ")
    # Evaluar la opción ingresada por el usuario
    if opcion == '1':
        opcion1()
    elif opcion == '2':
        opcion2()
    elif opcion == '3':
        opcion3()
    elif opcion == '4':
        opcion4()
    elif opcion == '0':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingresa un número del 1 al 4.")
