import random
import matplotlib.pyplot as plt
# se non funziona questo import, basta fare la versione ad iterazioni 
import time

# semplice programma che cerca linearmente un numero in una lista

l = [ random.randint(0,100) for i in range(0,1000)]
target = random.randint(0,100)

iterazioni = 0 
for i in l: 
    iterazioni+=1
    if(i == target):
        break
print("mi ci sono volute ", iterazioni, "iterazioni per trovare un numero casuale")



# versione con il tempo. questo può essere problematico per problemi molto semplici. (il PC è troppo veloce)
l = [ random.randint(0,100) for i in range(0,1000)]
target = random.randint(0,100)

tempo = time.time_ns()
# calcolo le iterazioni per la ricerca lineare
iterazioni = 0 
for i in l: 
    iterazioni+=1
    if(i == target):
        break
# versione modificata di selection sort 
def order(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)): 
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]


# calcolo il tempo di selection sort per diverse lunghezza di una lista 
x = []
y = []
for i in range(100,1000,100):
    l = [ random.randint(0,100) for k in range(0,i)]
    tempo = time.time_ns()
    order(l)
    temp_finale = time.time_ns() - tempo
    # print("mi ci sono voluti ", temp_finale/1000000, " millisecondi per ordinare una lista") 
    x.append(i)
    y.append(temp_finale/1000000)

plt.plot(x,y)
plt.show()       
