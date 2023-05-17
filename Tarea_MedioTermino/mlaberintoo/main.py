from Grafo import Grafo

G = Grafo("grafo")
archivo = open("data/laberinto.txt")
lineas = archivo.readlines()
lineas[2] = lineas[2].strip('\n')
inicio = lineas[2].split(',')
lineas[3] = lineas[3].strip('\n')
fin = lineas[3].split(',')
#print (inicio)
#print (fin)
for r in range(4,len(lineas)):
    linea = lineas[r]
    linea = linea.strip('\n')
    r = r - 4

    for c in range(0,len(linea)):
        if linea[c] == '0':
            n = G.addNodo('0',r,c,True)
            for n2 in G.nodos.values():
                if ((n2.camino and n.camino)and(n2.r == n.r)and(n2.c == n.c-1 or n2.c == n.c+1)) or ((n2.camino and n.camino)and(n2.c == n.c)and(n2.r == n.r-1 or n2.r == n.r+1)):

                    G.addArco(n2,n,1)
        else:
            G.addNodo('+',r,c,False)
for nodo in G.nodos.values():
    if str(nodo.r) == inicio[0] and str(nodo.c) == inicio[1]:
        ini = nodo
    if str(nodo.r) == fin[0] and str(nodo.c) == fin[1]:
        fi = nodo
G.BFS(ini,fi)
print(G)