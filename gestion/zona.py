

class Zona:
    _animales = []
    def __init__ (self, nombre, zoo):
        self._nombre = nombre
        self._zoo = zoo

    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

    def setZoo(self, zoo):
        self._zoo = zoo
    def getZoo(self):
        return self._zoo

    @classmethod
    def agregarAnimales(cls, animales):
        cls._animales.append(animales)
    @classmethod
    def cantidadAnimales(cls):
        return len(cls._animales)

