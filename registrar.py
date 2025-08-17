from libro_fisico import LibroFisico
from libro_digital import LibroDigital

def registrar_material(biblioteca):
    """
    # Función para registrar un nuevo material en la biblioteca
    # recibe la lista de la biblioteca como argumento para poder modificarla.
    """
    print("\n --- Registro Nuevo Material ---")
    tipo= input("Elija el tipo de material a registrar: (1: FISICO, 2: DIGITAL): ")

    titulo = input("Ingrese el título: ")
    autor = input("Ingrese el autor: ")

    if tipo == '1':
        while True:
            try:
                ejemplar = int(input("Ingrese el número de ejemplar: "))
                nuevo_libro = LibroFisico(titulo, autor, ejemplar)
                break
            except ValueError:

                print("Error:Porfavor, ingrese un numero entero para el ejemplar.")

        biblioteca.append(nuevo_libro)

        print(f"\n¡Libro Físico '{titulo}' registrado con éxito con el código {nuevo_libro.get_id()}!")
    
    elif tipo =='2':
        while True:
            try:
                tamano = float(input("Ingrese el tamaño del archivo (MB): "))
                nuevo_libro = LibroDigital(titulo, autor, tamano)
                break
            except ValueError:
                print("Error: Por favor, ingrese el tamaño del archivo.")
        
        biblioteca.append(nuevo_libro)
        print(f"\n ¡Libro Digital '{titulo}' registrado en éxito con el código {nuevo_libro.get_id()}!")

    else: 
        print("Opcion no válida. Regresando... al menu principal ")       

                    


