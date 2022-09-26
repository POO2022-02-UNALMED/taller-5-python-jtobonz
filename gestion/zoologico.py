from zona import Zona

class Zoologico:
    _zonas = []

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    def getUbicacion(self):
        return self._ubicacion

    @classmethod
    def setZonas(cls, zonas):
        cls._zonas = zonas
    @classmethod
    def getZonas(cls):
        return cls._zonas
    @classmethod
    def agregarZonas(cls, zona):
        cls._zonas.append(zona)

    def cantidadTotalAnimales(cls):
        cantidadTotalAnimales = 0
        for i in range (len(cls._zonas)):
            cantidadTotalAnimales += cls._zonas[i].cantidadAnimales
        return cantidadTotalAnimales