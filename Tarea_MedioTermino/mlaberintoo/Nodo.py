class Nodo:

    def __init__(self, nombre,r,c,camino):
        self.nombre=nombre
        self.ady = []
        self.color = "blanco"
        self.p = None
        self.d = 0
        self.f = 0
        self.usado = False
        self.id = None
        self.r = r
        self.c = c
        self.camino = camino
        self.borrar = False
    def addAdyacente(self,ady):
        if ady not in self.ady:
            self.ady.append(ady)
    def __str__(self):
        #cadena = f"{self.nombre} ({self.d}/{self.f}) p({self.p.nombre if self.p!=None else '' }): "
        #for a in self.ady:
        #    cadena+= a.nombre + ","
        cadena = str(self.r)+" "+str(self.c)
        return cadena