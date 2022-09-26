from zooAniamles.animal import Animal

class Ave (Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__ (self, nombre, edad, habitat, genero, colorPlumas):
        super.__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    def getColorPlumas(self):
        return self._colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    @classmethod
    def movimiento(cls):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        x = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls.halcones += 1
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        x = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls.aguilas += 1
    
