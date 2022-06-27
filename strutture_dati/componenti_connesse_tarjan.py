from random import random

from numpy import Inf, Infinity
class nodo:
    def __init__(self, v, id):
        self.v = v
        self.id = id
        self.low = id
        self.next : nodo = []

    def print_nodo(self):
        for i in self.next:
            print(str(self.id)+" --> "+str(i.id))

class grafo:
    def __init__(self):
        self.nodi = []

    def crea_nodi(self, n):
        for i in range(0,n):
            self.nodi.append(nodo(v = i, id=int(random()*(1000*n))))
    
    def crea_archi(self, k ):
        for i in range(0,k):
            self.nodi[int(random()*len(self.nodi))].next.append(self.nodi[int(random()*len(self.nodi))])

def recurs(nodo : nodo, v: set, timer):
      nodo.low = timer[0]
      v.add(nodo)
      for i in range(0,len(nodo.next)):
            
         if nodo.next[i] not in v:
            timer[0] +=1
            recurs(nodo.next[i], v, timer)

      min_low = Infinity;
      for i in range(0,len(nodo.next)):
            if nodo.next[i].low < min_low:
                min_low = nodo.next[i].low
      nodo.low = min(nodo.low, min_low)


def tarjan(grafo: grafo):
    v = set()
    timer = [0]
    for nodo in grafo.nodi:
        
        if nodo not in v:
            recurs(nodo, v, timer)
            timer[0]+=1

g = grafo()
g.crea_nodi(4)
g.crea_archi(8)


tarjan(g)



for nodo in g.nodi:
    
    nodo.print_nodo()
    print(nodo.id)
    print(nodo.low)

    print("---")
    





