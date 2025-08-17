from material_biblioteca import MaterialBiblioteca

#herencia
class LibroDigital(MaterialBiblioteca):
    #se aplica el concepto de herehncia, ya que se deriva del materialBiblioteca. 

    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self._formato = formato

    #polimorfismo. 
    def prestar(self):
        #comportamiento de prestar un libro digital. 
         print("Nota: El Préstamo de un libro digital es por un máximo de 3 dias.")
         return super().prestar()

    def mostrar_informacion(self):
        super().mostrar_informacion() #Muestra la inf. del mateial base y la inf. especifico del lib. digital. 
        print(f" Tipo de material: Libro Digital")
        print(f"Formato: {self._formato} MB")
        print(f"Duracion de Préstamo: 3 Días")
        print("-"*30   )