from asyncio.windows_events import NULL
from distutils import archive_util
from random import random

from numpy import true_divide


class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.archiIn: Nodo = []
        self.archiOut: Arco = []
        self.parentSet: set


class Arco:
    def __init__(self, nodoA: Nodo, nodoB: Nodo):
        self.a = nodoA
        self.b = nodoB
        self.peso = abs(self.a.valore - self.b.valore)

    def stampaArco(self) -> str:
        return str(self.a.valore)+" --> "+str(self.b.valore) + " | " + str(self.peso)


class Grafo:
    def __init__(self):
        self.name = "grafo"
        self.nodi: Nodo = []
        self.archi: Arco = []

    def addNodo(self, valore):
        self.nodi.append(Nodo(valore))

# creo n archi tra nodi casuali


def randConnect(grafo: Grafo, connects: int):
    for i in range(0, connects):
        randA = grafo.nodi[int((random()*100) % len(grafo.nodi))]
        randB = grafo.nodi[int((random()*100) % len(grafo.nodi))]
        a = Arco(randA, randB)
        grafo.archi.append(a)
        randA.archiIn.append(a)
        randB.archiOut.append(a)

def f_diff(set1, set2):
    diff = False
    for item in set1:
        if item not in set2:
            diff = True
    for item2 in set2:
        if item2 not in set1:
            diff = True
    return diff


# dato un grafo, ritorna il set di archi formante il minimum spanning tree (senza utilizzare disjoint sets)
def minSpanningTree(grafo: Grafo):
    archi_ordinati = [x for x in grafo.archi]
    set_archi = set()
    set_nodi = []
    # ordino gli archi
    for i in archi_ordinati:
        for j in archi_ordinati:
            if j.peso < i.peso:
                temp = i
                i = j
                j = temp

    for nodo in grafo.nodi:
        nset = set()
        nset.add(nodo)
        nodo.parentSet = nset

    for arco in archi_ordinati:
        if(f_diff(arco.a.parentSet, arco.b.parentSet) ):
            
          
            
            arco.a.parentSet = arco.a.parentSet.union(arco.b.parentSet)
            for node in arco.a.parentSet:
                node.parentSet = arco.a.parentSet


            set_archi.add(arco)
            '''  print(list(x.valore for x in arco.a.parentSet), end="  ")
            print("") '''
    return set_archi


grafo = Grafo()
for i in range(0, 10):
    grafo.addNodo(i)

randConnect(grafo, 10)

tree = minSpanningTree(grafo)

for nodo in grafo.nodi:
    for set in nodo.parentSet:
        print(set.valore, end=" - ")
    print("") 




