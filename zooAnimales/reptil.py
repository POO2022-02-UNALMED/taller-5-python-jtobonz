from animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__ (self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super.__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorPlumas(self):
        return self._colorEscamas
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    def getLargoCola(self):
        return self._largoCola

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    @classmethod
    def movimiento(cls):
        return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        x = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas += 1
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        x = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes += 1