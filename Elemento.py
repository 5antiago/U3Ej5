from zope.interface import implementer
from IElemento import Ielemetos
@implementer(Ielemetos)
class Elementos:
    __Coleccion = list

    def __init__(self):
        self.__Coleccion = []

    def insertarElemento(self, elemento, pos):
        try:
            self.__Coleccion[pos]
            self.__Coleccion.insert(pos, elemento)
        except IndexError:
            print("Posicion no valida")
    def agregarElemeto(self, elemento):
        self.__Coleccion.append(elemento)
    def MostrarElemento(self, pos):
        try:
            print(self.__Coleccion[pos])
        except IndexError:
            print("Posicion no valida")

    def test(self):
        print("Mostando pos")
        self.MostrarElemento(5) #No existe la pocision
        print(self.__Coleccion)
        print("Agregando num 2")
        self.agregarElemeto(2) 
        print(self.__Coleccion)
        print("Insertando num 7 en pos 6")
        self.insertarElemento(7, 6)
        print(self.__Coleccion)
        print("Insertando num 5 en pos 0")
        self.insertarElemento(5, 0)
        print(self.__Coleccion)