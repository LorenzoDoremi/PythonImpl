


from math import sqrt
from random import random


items = []

## genero delle "connessioni"
for i in  range(0,100):
    rand = random()
    # un Denial of Service
    if rand > 0.2:
        items.append({"classe": "DOS","payload": random()*20000, "ping": random()*30})
    else: 
        items.append({"classe": "CONN","payload": random()*1500, "ping": random()*120})
    


test =  { "payload": 200, "ping": 90}

# questa funzione ha un grosso problema. (quale?)
def distance(item1, item2, keys):
    dist = 0
    for key in keys: 
       dist += sqrt(item1[key]**2 + item2[key]**2)
      
    return dist

# versione migliorata. (coseno di similarità)
def distance2(item1, item2, keys):
    magn1 = 0
    magn2 = 0
    scalar = 0
    for key in keys: 
       magn1 += item1[key]**2 
       magn2 += item2[key]**2
       scalar += item1[key]*item2[key]
    magn1 = sqrt(magn1)
    magn2 = sqrt(magn2)
   
    return scalar/(magn1*magn2)

# k-nearest neighbours
def classify(items, test, k):
    for i in range(0,len(items)):
        for j in range(i+1,len(items)):
            #metto in ordine tutti gli elementi in base alla distanza dall'elemento test
            if(distance2(items[i], test, ["payload", "ping"]) > distance2(items[j],test, ["payload", "ping"])):
                
                items[i],items[j] = items[j], items[i]
    #prendo i k membri più vicini 
    k_neighs = items[:k] 
    classes = {}
    for neigh in k_neighs:
        if neigh["classe"] in classes:
            classes[neigh["classe"]] +=1
        else: 
           classes[neigh["classe"]] = 1 
    print(classes) 
           
                

classify(items,test, 20)

