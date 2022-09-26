from gestion.zona import Zona
from mamifero import Mamifero
from ave import Ave
from reptil import Reptil
from pez import Pez
from anfibios import Anfibio

class Animal:
    _totalAnimales = 0
    
    def __init__ (self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    def getHabitat(self):
        return self._habitat

    def setGenero(self, genero):
        self.genero = genero
    def getGenero(self):
        return self._genero
    
    def setZona(self, zona):
        self._zona = zona
    def getZona(self):
        return self._zona

    @classmethod
    def movimiento(cls):
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos: " + Mamifero.cantidadMamiferos + "Aves: " + Ave.cantidadAves + "Reptiles: " + Reptil.cantidadReptiles + "Peces: " + Pez.cantidadPeces + "Anfibios: " + Anfibio.cantidadAnfibios
    
    @classmethod
    def __str__(self):
        if self._zona == None:
            return f"“Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        else:
            return f"“Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona.self._zoo}"