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
        print(curr.v)
        while curr.next:
            curr = curr.next
            print(curr.v)

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
        
        while curr.next:
            switch = curr
            for i in range(0,self.l-k):
                if switch.next:
                    switch = switch.next
                else: 
                    switch = self.head
                    
            curr.v = switch.v
            curr = curr.next





lista = List()
for i in range(0,10):
    #lista.push(int(random()*i))
    lista.push(i)
lista.shift(2)
lista.print()



 

