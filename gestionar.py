from buscar import buscar_material_por_codigo

def gestionar_materiales(biblioteca):
    """
    Permite prestar, devolver o consultar la informacion de un 
    material existente.       
    """
    print("\n--- Gestionar Materiales ---")
    if not biblioteca: 
        print("No hay materiales registrados en la biblioteca. ")
        return
    
    id = input("Ingrese el codigo unico del material: ")
        # Pasamos la lista y el código a la función de búsqueda
    material = buscar_material_por_codigo(biblioteca, id)

    if material:
        print(f"\nMaterial encontrado: '{material.get_titulo()}'")
        opcion = input("¿Qué desea hacer? (1: Prestar, 2: Devolver, 3: Consultar Información): ")

        if opcion == '1':
            material.prestar()
        elif opcion == '2':
            material.devolver()
        elif opcion == '3':
            material.mostrar_informacion()
        else:
            print("Opción no válida.")
    else: 
        print("No se encontró nintun material con ese codigo.")