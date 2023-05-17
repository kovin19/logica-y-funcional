from modulos.Atomo import Atomo
from modulos.Clausula import Clausula
from modulos.Formula import Formula

def prioridad(c):
    if (c == '|'):
        return 1
    if (c == '&'):
        return 2
    if (c == '>'):
        return 3
    if (c == '='):
        return 4
    if (c == '-' or c =='˜') :
        return 5
    if (c == '('):
        return -1
    if (c == ')'):
        return -2
    return 0

def infijo2postfijo(infijo):
    postfijo = []
    pila = []
    for ch in infijo:
        p=prioridad(ch)
        if p==-1:
            pila.append(ch)
        elif p==-2:
            while (len(pila)>0):
                tope = pila.pop()
                if (tope != '('):
                    postfijo.append(tope)
                else:
                    break
        elif p>0:
            if len(pila) == 0 or p>prioridad(pila[-1]):
                pila.append(ch)
            else:
                while len(pila)>0 and p < prioridad((pila[-1])):
                    tope = pila.pop()
                    postfijo.append(tope)
                pila.append(ch)
        else:
            postfijo.append(ch)
    while len(pila) > 0:
        postfijo.append(pila.pop())
    return postfijo

def evaluarPostfijo(postfijo):
    pila = []
    for ch in postfijo:
        p=prioridad(ch)
        if p == 0:
            a = Atomo(ch)
            c = Clausula()
            f = Formula()
            c.addAtomo(a)
            f.addClausula(c)
            pila.append(f)
        elif p == 1:
            b = pila.pop()
            a = pila.pop()
            c = a.orFormula(b)
            pila.append(c)
        elif p == 2:
            b = pila.pop()
            a = pila.pop()
            c = a.andFormula(b)
            pila.append(c)
        elif p == 3: #so
            b = pila.pop()
            a = pila.pop()
            a = a.notFormula(a)
            c = a.orFormula(b)
            pila.append(c)
        elif p == 4: #si y sólo sí
            b = pila.pop()
            a = pila.pop()
            aN = a.notFormula(a)
            c = aN.orFormula(b)

            bN = b.notFormula(b)
            c2 = bN.orFormula(a)

            c3 = c.andFormula(c2)

            pila.append(c3)
        elif p == 5:
            a = pila.pop()
            b = a.notFormula(a)
            pila.append(b)
    return pila.pop()

def alDavidAndPutnam(formula):

    resA = []
    claDel = []
    for c in formula.clausulas:
        if c.isTautología():
            claDel.append(c)
    for c in claDel:
        formula.clausulas.remove(c)
    res = None
    if len(formula.clausulas)==0:
        res = True

    while res==None:
        if formula.clausulaVacia():
            if formula.B>0:
                if formula.B==2:
                    res = False
                else:
                    Bf2 = formula.bifurcacion(2,formula.resG)
                    resA = formula.resG
                    if alDavidAndPutnam(Bf2):
                        resA.append(Bf2.aB)
                        formula.B = 2
                        res = True
                    else:
                        res = False
            else:
                res=False
        else:
            if len(formula.clausulas)==0:
                res=True
            else:
                at = formula.calusulaUnitaria()
                if at != None:
                    resA.append(at)
                at2 = formula.literalPura()
                if at2 != None:
                    resA.append(at2)
                if at != None or at2 != None:
                    pass
                else:
                    Bf1 = formula.bifurcacion(1,resA)
                    if alDavidAndPutnam(Bf1):
                        if Bf1.B!=2:
                            resA.append(Bf1.aB)
                        res = True
                    else:
                        res = False
    if res:
        for a in resA:
            print(a.nombre,'=',a.estado)
    elif formula.B == 0:
        print('La fórmula es insatisfactible.')
    return res


archivo = open("data/ejemplo15.txt")
lineas = archivo.readlines()
agregar = True
for linea in lineas:
    cadena = ''
    formula = []
    for caracter in linea:
        if caracter == '|' or caracter == '&' or caracter == '>' or caracter == '=' or caracter == '-'or caracter == '˜' or caracter == '(' or caracter == ')':
            if len(cadena) > 0:
                formula.append(cadena)
                cadena = ''
            formula.append(caracter)
        else:
            if caracter != ' ':
                cadena+=caracter
    if len(cadena) > 0 and cadena != '\n':
        formula.append(cadena)
    print(evaluarPostfijo(infijo2postfijo(formula)))
    alDavidAndPutnam(evaluarPostfijo(infijo2postfijo(formula)))



