from random import random

from requests import head

class Nodo:
    def __init__(self, v): 
        self.v = v
        self.next = None
  

class List:
    def __init__(self):
        self.head = None
        self.l = 0
    def print(self):
        curr = self.head
        while curr:
            print(curr.v)
            curr = curr.next
            

    def push(self, v):
         
        curr = self.head
        if self.head:
            while curr.next:
                curr = curr.next
            curr.next = Nodo(v)
        else:
         self.head = Nodo(v)  
        self.l +=1

    def shift(self, k):
        
  
            
        curr = self.head
        new_head = None
        
        # se k è un numero negativo, vado indietro (trovando k = lunghezza + k)
        if k < 0:
            m = 0
            l = self.head
            while l:
                l=l.next
                m+=1
            k = m+k
            
           
        index = 0
        #cerco la nuova head
        while curr:
            
            # bene, ho trovato la nuova testa
            if index == k:
                new_head = curr
            # se posso andare avanti, continuo
            if curr.next:
                curr = curr.next
            # altrimenti, se ho già trovato la nuova testa mi fermo (sono al termine della lista)
            elif new_head:
                break
            # vuol dire che k è maggiore della lunghezza totale lista. ritorno da capo e continuo
            else:
                curr = self.head
            index+=1
        #creo un loop tra la fine e l'inizio della lista
        curr.next = self.head
        # riparto dalla testa originale e stacco la nuova testa, creando una nuova fine
        curr = curr.next
        self.head = new_head
        #cerco il nodo il cui successivo è la nuova testa
        while curr.next != new_head:
            curr = curr.next
        curr.next = None

    def invert(self):

        prec = None
        curr = self.head
        n = curr.next
        while curr:
           
            #salvo il successivo
            n = curr.next
            # inverto il puntatore
            curr.next = prec
            #sposto il precedente in avanti
            prec = curr
            # sposto il corrente in avanti
            curr = n

         # se il nuovo nodo non esiste, allora il precedente è la fine, e quindi la nuova testa   
            if not curr:
                self.head = prec
                break


        # versione senza break. come cambia il while?
        # self.head = curr
        # self.head.next = prec

            


        
        





lista = List()
for i in range(0,10):
    #lista.push(int(random()*i))
    lista.push(i)
# lista.shift(12)
lista.invert()
lista.print()




 

