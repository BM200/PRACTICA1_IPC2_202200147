
from registrar_libro_fisico import registrar_libro_fisico


def main():
    #funcion principal que inicia el sistema y muestra el menu
    biblioteca=[]
    
    print("="*50);
    print("Bienvenido al sistema de gestion de biblioteca");
    print("="*50);

    while True:
        print("\n----- MENU PRINCIPAL ---:");
        print("1. Registrar libro Fisico");
        print("2. Registrar libro Digital");
        print("3. Gestionar materiales registrados");
        print("4. Salir");

        opcion = input("Selecciones la gestion que desea realizar. ")
        
        if opcion == "1":
            registrar_libro_fisico(biblioteca)
        elif opcion == "2":
            registrar_libro_digital(biblioteca)
        elif opcion == "3":
            gestionar_materiales(biblioteca)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()
