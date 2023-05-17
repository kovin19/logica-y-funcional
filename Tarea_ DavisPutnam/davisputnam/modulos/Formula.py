import copy

from modulos.Clausula import Clausula

class Formula:
    def __init__(self):
        self.clausulas = []
        self.certificado = {}
        self.B = 0
        self.aB = None
        self.clausulasFB = []
        self.resG = []
    def addClausula(self,clausula):
        self.clausulas.append(clausula)

    def addClausulaFB(self,clausula):
        self.clausulasFB.append(clausula)

    def __str__(self):
        cadena = '['
        for c in self.clausulas:
            cadena += str(c)+' '
        if len(cadena)>1:
            cadena = cadena[:-1]
        cadena+=']'
        return cadena
    def orFormula(self, formula):
        f = Formula()
        for c in formula.clausulas:
            self.orFormulaC(c,f)
        return f

    def orFormulaC(self, clausula,f):
        for c in self.clausulas:
            cClon = c.getClon()
            for a in clausula.atomos:
                cClon.addAtomo(a)
            f.addClausula(cClon)

    def notFormula(self,formula):
        f = Formula()
        fClon = Formula()
        if len(formula.clausulas)==1:
            cl = Clausula()
            for a in formula.clausulas[0].atomos:
                cl.addAtomo(a)
            for a in cl.atomos:
                a.negar()
                clN = Clausula()
                clN.addAtomo(a)
                f.addClausula(clN)
            return f
        for c in formula.clausulas:
            fClon.addClausula(c.getClon())
        for c in fClon.clausulas:
            for a in c.atomos:
                a.negar()
        while (len(fClon.clausulas)>0):
            c = fClon.clausulas.pop()
            for a in c.atomos:
                for c2 in fClon.clausulas:
                    for a2 in c2.atomos:
                        c3 = Clausula()
                        c3.addAtomo(a)
                        c3.addAtomo(a2)
                        f.addClausula(c3)
        return f

    def andFormula(self, formula):
        f = Formula()
        for c in self.clausulas:
            f.addClausula(c.getClon())
        for c in formula.clausulas:
            f.addClausula(c.getClon())
        return f

    def clausulaVacia(self):
        for c in self.clausulas:
            if len(c.atomos) == 0:
                return True
        return False

    def calusulaUnitaria(self):
        atomosU = []
        for c in self.clausulas:
            if len(c.atomos) == 1:
                atomosU.append(c.atomos[0].getClon())
        #for au in atomosU:
            #print(au)
        if len(atomosU)>0:
            clausulasEl = []
            for c2 in self.clausulas:
                for a in c2.atomos:
                    if a.nombre == atomosU[0].nombre and a.estado == atomosU[0].estado:
                        clausulasEl.append(c2)
            for cE in clausulasEl:
                self.clausulas.remove(cE)
            for c in self.clausulas:
                aEl = []
                for a2 in c.atomos:
                    if atomosU[0].nombre == a2.nombre:
                        aEl.append(a2)
                for ae in aEl:
                    c.atomos.remove(ae)
            #for a in self.clausulas:
                #print(a)
            #print("CU",atomosU[0],"=",self)
            return atomosU[0]
        return None

    def literalPura(self):
        atomos = []
        for c in self.clausulas:
            for a in c.atomos:
                guardar = True
                for a2 in atomos:
                    if a.nombre == a2.nombre:
                        guardar = False
                if guardar:
                    atomos.append(a)
        atomosEl = []
        for a in atomos:
            for c in self.clausulas:
                for a2 in c.atomos:
                    if a2.nombre == a.nombre and a2.estado != a.estado:
                        if a not in atomosEl:
                            atomosEl.append(a)
        #for a in atomos:
            #print(a)
        for a in atomosEl:
            #print(a)
            atomos.remove(a)
        if len(atomos)>0:
            clausulasEl = []
            for c in self.clausulas:
                for a2 in c.atomos:
                    if a2.nombre == atomos[0].nombre:
                        clausulasEl.append(c)

            for cE in clausulasEl:
                self.clausulas.remove(cE)
            #print('LP',atomos[0],'=',self)
            return atomos[0]
        return None

    def bifurcacion(self, B, resG):
        if B == 2:
            self.clausulas=self.clausulasFB
        atC = self.clausulas[0].atomos[0].getClon()
        if B == 2:
            atC.negar()
        f = Formula()
        f.aB = atC
        f.B = B
        for c in self.clausulas:
            f.addClausula(c.getClon())
        if B == 1:
            self.resG = copy.copy(resG)
            for c in self.clausulas:
                f.addClausulaFB(c.getClon())
        clausulasEl = []
        for c in f.clausulas:
            for a in c.atomos:
                if a.nombre == atC.nombre and a.estado == atC.estado:
                    clausulasEl.append(c)
        for cE in clausulasEl:
            f.clausulas.remove(cE)

        for c in f.clausulas:
            aEl = []
            for a2 in c.atomos:
                if atC.nombre == a2.nombre:
                    aEl.append(a2)
            for ae in aEl:
                c.atomos.remove(ae)
        #print("B"+str(B),atC,'=',f)
        return f