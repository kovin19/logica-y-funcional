import math
from queue import Queue

from Arco import Arco
from Nodo import Nodo
import operator

class Grafo:


    def __init__(self,nombre):
        self.nombre = nombre
        self.nodos = {}
        self.arcos = []
        self.time = 0
        self.Gt = None
        self.lineas = None
    def addNodo(self, nodo,r,c,camino):
        nG = str(r)+nodo+str(c)
        #print(nG)
        if nG not in self.nodos:
            n = Nodo(nG,r,c,camino)
            self.nodos[nG]=n
            return n
    def addNodoObj(self, nodo):
        if nodo.nombre not in self.nodos:
            self.nodos[nodo.nombre]=nodo
    def addArco(self, origen,destino0,peso):
        origen = self.nodos[origen.nombre]
        destino = self.nodos[destino0.nombre]
        arco = Arco(origen,destino,peso)
        self.arcos.append(arco)
        origen.addAdyacente(destino)
        destino.addAdyacente(origen)
    def __str__(self):

        cadena = ""

        r = 0
        for nodo in self.nodos.values():
            if nodo.r>r:
                cadena = cadena+'\n'
                r=nodo.r
            if nodo.borrar:
                cadena = cadena+' '
            else:
                if nodo.camino:
                    cadena = cadena+'0'
                else:
                    cadena = cadena+'+'
        return cadena

    def BFS(self, s, fin):
        for nodo in self.nodos.values():
            nodo.d = float("Inf")
            nodo.p = None
            nodo.color = "Blanco"
        s = self.nodos[s.nombre]
        s.color = "Gris"
        s.d = 0
        Q = []
        Q.append(s)
        while (len(Q)>0):
            u = Q.pop(0)
            if u == fin:
                u.borrar=True
                p = u.p
                while p != None:
                    p.borrar = True
                    p = p.p
                continue
            for v in u.ady:
                if (v.color == "Blanco"):
                    v.color = "Gris"
                    v.d = u.d+1
                    v.p = u
                    Q.append(v)
            u.color = "Negro"
