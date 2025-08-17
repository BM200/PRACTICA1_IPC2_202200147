import random
import string


def generar_id():
     caracteres = string.ascii_uppercase + string.digits
     id = ''.join(random.choice(caracteres) for _ in range(8))
     return id


#CLASE BASE : MaterialBiblioteca
class MaterialBiblioteca:
    """
    Clase Padre 
    """
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._id = generar_id()
        self._estado = "disponible"
#acceder a los atributos encapsulados(Getters)


    def get_titulo(self):
         return self._titulo


    def get_autor(self):
         return self._autor
    
    def get_id(self):
         return self._id

    def get_estado(self):
         return self._estado

    def prestar(self): 
        #devuelve true si el prestamo fue exitoso y false en caso contrario. 
        if self._estado == "disponible":
           self._estado = "prestado"
           print(f"El Libro '{self._titulo}' prestado con éxito")
           return True
        else:
             print(f"El Libro '{self._titulo}' ya esta prestado")
             return False 
        
    def devolver(self):

        if self._estado == "prestado":
            self._estado = "disponible"
            print(f"El Libro '{self._titulo}' devuelto con éxito")
            return True
        else:
            print(f"El Libro '{self._titulo}' no se encuentra disponible.")
            return False
        
    def mostrar_informacion(self):
         print("---** Informacion del Material **---")
         print(f" ID: {self._id}")
         print(f" Titulo: {self._titulo}")
         print(f" Autor: {self._autor}")
         print(f" Estado: {self._estado}")
