from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__ (self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    def getCantidadAletas(self):
        return self._cantidadAletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    @classmethod
    def movimiento(cls):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        x = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        x = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1

    