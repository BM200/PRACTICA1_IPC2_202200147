def mostrar__todos_los_materiales(biblioteca):
    """
    Muestra la inf. de todos los materiales registrados en la lista.
   
    """
    print("\n--- Listado de Todos los Materiales ---")

    if not biblioteca:
        print("No hay materiales registrados en la biblioteca.")
    else: 
        for material in biblioteca:
            material.mostrar_informacion()
            
