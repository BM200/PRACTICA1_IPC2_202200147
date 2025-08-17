#importamos las funciones especidficas de cada modulo. 
from registrar import registrar_material
from gestionar import gestionar_materiales
from mostrar  import mostrar__todos_los_materiales



def main():
    #funcion principal que inicia el sistema y muestra el menu
    

    print("="*50)
    print("Bienvenido al sistema de gestion de biblioteca")
    print("="*50)

    biblioteca = []  # Lista para almacenar los materiales registrados  
    while True:
        print("\n----- MENU PRINCIPAL ---:")
        print("1. Registrar nuevo material")
        print("2. Gestionar materiales registrados")
        print("3. Mostrar todos los materiales")
        print("4. Salir")
        print("="*50)
        opcion = input("Seleccione la gestión que desea realizar. ")
        
        if opcion == "1":
            registrar_material(biblioteca)
        elif opcion == "2":
            gestionar_materiales(biblioteca)
        elif opcion == "3":
            mostrar__todos_los_materiales(biblioteca)
        elif opcion == "4":
            print("Saliendo del sistema...")

            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        
        input("\n Presione Enter para continuar...")

if __name__ == "__main__":
    main()
