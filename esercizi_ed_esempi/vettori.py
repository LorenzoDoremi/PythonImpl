from numpy import Infinity


def massimo(v):
    m = -Infinity # v[0]
    for e in v:
        if e > m : 
            m = e 
    return m 

def minimo(v):
    m = Infinity
    for e in v: 
        if e < v: 
            m = e 
    return m 

def media(v):
     return (minimo(v)+massimo(v))/2
 
def vicino(v):
    m = media(v)
    min_d = Infinity
    for e in v: 
         if abs(e-m) < min_d:
            min_d = abs(e-m)
    return min_d
 
def palindromo(v):
    for i in range(0,int(len(v)/2)):
        if v[i] !=  v[len(v)-1-i]:
            return False
    return True

# versione con array di lunghezza uguale. 
def hamming(v,v2):
    c = 0 
    for i in range(0,len(v)):
        if v[i] != v2[i]:
            c += 1 
    return c 
# versione con array di lunghezze diverse
def hamming2(v,v2):
    # capisco fino a dove posso fare il for
    l = min(len(v),len(v2))
    # se hanno lunghezze diverse, contano come 1*n
    c = max(len(v),len(v2)) - l 
    for i in range(0,l):
        if v[i] != v2[i]:
            c+=1 
    return c 
print(hamming2([1,1,0],[1,1,1,0]))

def coppias(v,k):
    for i in range(0,len(v)):
        for j in range(i+1,len(v)):
            if v[i] + v[j] == k: 
                return True
    return False

def triplas(v,k):
    for i in range(0,len(v)):
        for j in range(i+1,len(v)):
            for z in range(j+1,len(v)):
                if v[i] + v[j] + v[z] == k: 
                    return True
    return False

#questo è DIFFICILISSIMO. infatti non era richiesto. 
# determina se esistono tre numeri in v che sommati sono uguali a k, in tempo O(n^2) 
# esempio: 
lista = [1,6,6,4]
k = 13 
# la risposta è vero (6+6+1)
def triplasN2(v,k):
    # ordino v 
    v.sort()
    # uso tre indici. il primo si sposta a sinistra. gli altri due si alternano in base a quando mi devo avvicinare a k.
    for i in range(0,len(v)):
        j = i+1
        z = len(v)-1
        while j < z: 
            if v[i]+v[j]+v[z] == k: 
                return True
            elif v[i]+v[j]+v[z] < k:
                j+=1 
            else: 
                z-=1 
    return False


