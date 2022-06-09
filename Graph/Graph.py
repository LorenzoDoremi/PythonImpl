from asyncio.windows_events import NULL
from distutils import archive_util
from operator import eq
from random import random

from numpy import true_divide
import numpy


class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.archiIn: Nodo = []
        self.archiOut: Arco = []
        self.s = 0

class Arco:
    def __init__(self, nodoA: Nodo, nodoB: Nodo):
        self.a = nodoA
        self.b = nodoB
        self.peso = abs(self.a.valore - self.b.valore)

    def stampa_arco(self) -> str:
        return str(self.a.valore)+" --> "+str(self.b.valore) + " | " + str(self.peso)


class Grafo:
    def __init__(self):
        self.name = "grafo"
        self.nodi: Nodo = []
        self.archi: Arco = []

    def add_nodo(self, valore):
        self.nodi.append(Nodo(valore))

# creo n archi tra nodi casuali


def rand_connect(grafo: Grafo, connects: int):
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

class disjoint_set():
    
    def __init__(self, nodi) -> None:
     
     self.set = []
     for i in range(0, len(nodi)):
        nodi[i].s = i
        self.set.append(i)
     self.rank = numpy.zeros(len(self.set))
    # trovo l'indice numerico nella lista corrispondente
    def find_root(self, nodo):
      
        if self.set[nodo] == nodo:
            return nodo
        else:
            return self.find_root(self.set[nodo])

    def union(self,nodo_a, nodo_b):

        a_root = self.find_root(nodo_a.s)
        b_root = self.find_root(nodo_b.s)
        if a_root != b_root:
            if self.rank[a_root] > self.rank[b_root]:
                self.set[b_root] = a_root
            elif self.rank[a_root] < self.rank[b_root]:
                self.set[a_root] = b_root
            else: 
               self.set[a_root] = b_root
               self.rank[a_root] += 1
            




# dato un grafo, ritorna il set di archi formante il minimum spanning tree
def min_spanning_tree(grafo: Grafo):
    archi_ordinati = [x for x in grafo.archi]
    set_archi = []
   
    # ordino gli archi
    for i in archi_ordinati:
        for j in archi_ordinati:
            if j.peso < i.peso:
                temp = i
                i = j
                j = temp
    
    disjoint_s = disjoint_set(grafo.nodi)
    for arco in archi_ordinati:
     if disjoint_s.find_root(arco.a.s) != disjoint_s.find_root(arco.b.s):
         disjoint_s.union(arco.a, arco.b)
         set_archi.append(arco)


 
       
    return set_archi


grafo = Grafo()
for i in range(0, 20):
    grafo.add_nodo(i)

rand_connect(grafo, 160)

tree:Arco = min_spanning_tree(grafo)
print(len(tree))






