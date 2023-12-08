from funciones.funcionesMenu import *

while True:
    mostrar_menu()  
    # Solicitar al usuario que ingrese una opción
    opcion = input("\nSelecciona una opción: ")
    # Evaluar la opción ingresada por el usuario
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
