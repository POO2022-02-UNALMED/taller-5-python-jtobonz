from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__ (self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenosos(self, venenoso):
        self._venenoso = venenoso
    def getVenenosos(self):
        return self._venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    @classmethod
    def movimiento(cls):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        x = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        x = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1