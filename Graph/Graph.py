from random import random


class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.archiIn: Nodo = []
        self.archiOut: Arco = []


class Arco:
    def __init__(self, nodoA: Nodo, nodoB: Nodo):
        self.a: Nodo = nodoA
        self.b: Nodo = nodoB
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


# dato un grafo, ritorna il set di archi formante il minimum spanning tree        
def minSpanningTree(grafo: Grafo) -> set:
    archi_ordinati = [x for x in grafo.archi]
    for i in archi_ordinati:
     for j in archi_ordinati:
        if j.peso < i.peso:
            temp = j
            j = i
            i = j
    set_nodi = set()
    set_archi = set()
    for arco in archi_ordinati:
     if(arco.a not in set_nodi or arco.b not in set_nodi):
        set_nodi.add(arco.a)
        set_nodi.add(arco.b)
        set_archi.add(arco)
    return set_archi


grafo = Grafo()
for i in range(0, 140):
    grafo.addNodo(int(random()*100))

randConnect(grafo, 450)

tree = minSpanningTree(grafo)

print(len(tree))
print()
for i in tree:
  print(i.peso, end=" | ")

