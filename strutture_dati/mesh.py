import random

from numpy import Infinity

'''
si consideri la definizione di una rete Mesh come un insieme interconnesso di dispositivi
ogni dispositivo, rappresentabile completamente o semplicemente come un nodo, sarà collegato a k altri dispositivi
k è variabile per ciascun dispositivo. uno potrebbe essere collegato a 4 altri, come a 10. 

richieste:
1 - si definisca un oggetto Dispositivo/Nodo che contiene almeno un id
2 - si crei una lista di dispositivi di identificativo variabile
3 - si scriva una funzione in grado di determinare se esiste un percorso tra due dispositivi
4 - si modifichi la funzione affinchè si possa calcolare la distanza percorsa tra i due nodi 
5 - si implementino tutte le aggiunte ritenute necessarie (stampa dei nodi intermedi, distanze variabili tra nodi...)

'''

class Nodo():
    def __init__(self,k) -> None:
        self.k = k
        self.adj = []

nodi = [Nodo(i) for i in range(0,10)]

nodi[0].adj.append(nodi[7])
nodi[0].adj.append(nodi[3])
nodi[0].adj.append(nodi[4])
nodi[4].adj.append(nodi[6])
nodi[6].adj.append(nodi[2])
nodi[2].adj.append(nodi[7])
nodi[7].adj.append(nodi[3])

find = 2
'''
#random generator

for i in range(0,len(nodi)):
     for j in range(i+1,len(nodi)):
        r = int(random.random()*10)
        if(r < 8):
            nodi[i].adj.append(nodi[j])

'''


def search(curr: Nodo, k, path_length):
    print(curr.k)
    
    if curr.k == k:
        print("percorso = "+str(path_length))
        return True
    
    for nodo in curr.adj:
      
        if(search(nodo, k, path_length + 1)):
            return True
    return False  
   


print(search(nodi[0], find,0))

     
        