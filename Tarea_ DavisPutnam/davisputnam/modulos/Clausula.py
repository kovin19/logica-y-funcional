from modulos.Atomo import Atomo
import copy
class Clausula:
    def __init__(self):
        self.atomos=[]

    def addAtomo(self, atomo):
        crear = True
        for a in self.atomos:
            if (atomo.nombre == a.nombre and atomo.estado == a.estado):
                crear = False
        if crear:
            self.atomos.append(copy.copy(atomo))

    def __str__(self):
        cadena = '('
        for a in self.atomos:
            cadena += str(a)+','
        if len(cadena)>1:
            cadena = cadena[:-1]
        cadena+=')'
        return cadena

    def getClon(self):
        c = Clausula()
        for a in self.atomos:
            c.addAtomo(a.getClon())
        return c

    def isTautología(self):
        nombres = []
        for a in self.atomos:
            nombres.append(a.nombre)
        for a in self.atomos:
            r = nombres.count(a.nombre)
            if r > 1:
                return True
        return False