
from material_biblioteca import MaterialBiblioteca

#herencia
class LibroFisico(MaterialBiblioteca):
    #se aplica el concepto de herehncia, ya que se eriva del materialBiblioteca. 

    def __init__(self, titulo, autor, ejemplar):
        super().__init__(titulo, autor)
        self._ejemplar = ejemplar

    #polimorfismo. 
    def prestar(self):
        #comportamiento de prestar un libro fisico. 
         print("Nota: El Préstamo de un libro fisico es por un máximo de 7 dias.")
         return super().prestar()
    
    def mostrar_informacion(self):
        super().mostrar_informacion() #Muestra la inf. del mateial base y la inf. especifico del lib. fisico. 
        print(f" Tipo de material: Libro Físico")
        print(f"Número de Ejemplar: {self._ejemplar}")
        print(f"Duracion de Préstamo: 7 Días")
        print("-"*30   )
        

    
        
    