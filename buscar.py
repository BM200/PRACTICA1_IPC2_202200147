
def buscar_material_por_codigo(biblioteca, id):
    ##BUSCA UN  LIBRO EN LA LISTA DE LA BIBLIOTECA POR SU ID, DEVUELVE EL OBJETO DEL LIBRO O None SI NO. 
    for material in biblioteca: 
        if material.get_id() == id:
            return material
        
    return None