from random import random
import numpy
items = [
    {"nome": "Marco", "peso": 80},
    {"nome": "Luisa", "peso": 60},
    {"nome": "Angela", "peso": 50},
    {"nome": "Toby", "peso": 20},
    {"nome": "Marky", "peso": 30},
    {"nome": "Armando", "peso": 90},
    {"nome": "Lorenzo", "peso": 110},
    {"nome": "Elisa", "peso": 55},
]

def clustering(items, clusters_num, iterations, key):
    clusters = []
    # creo i cluster iniziali random
    for i in range(0,clusters_num):
        cluster = {"el": [], "total":0, "mean": 0}
        # appendo il primo oggetto del cluster
        randomel = items[(int)(random()*len(items))]
        cluster["el"].append(randomel)
        # inserisco i dati del primo, e aggiungo ai cluster
        cluster["total"] = randomel[key]
        cluster["mean"] = randomel[key]
        clusters.append(cluster)
    # rieseguo n-volte il processo aggiornando
    for i in range(0, iterations):
        # per ogni elemento da abbinare
        for el in items: 
            min = float("inf")
            mindex = 0
            # per ogni cluster cerco quello più simile
            for index,cluster in enumerate(clusters):
                # calcolo quanto gli elementi di un cluster assomigliano all'oggetto
                dist = abs(cluster["mean"]- el[key])
                
                if(dist < min):
                    min = dist 
                    mindex = index
                   
            # inserisco un nuovo elemento nel cluster più simile e aggiorno le informazioni
            clusters[mindex]["el"].append(el)
            clusters[mindex]["total"] += el[key]
            clusters[mindex]["mean"] =  clusters[mindex]["total"]/len(clusters[mindex]["el"])
      
        # calcolo la media di ogni cluster        
        for c in clusters:
                 # resetto i cluster mantenendo la media. 
                 if(i < iterations-1):
                    c["el"] = []
                 c["total"] = 0
                 
       
            
            
    
    return clusters
         
   
myclusters = clustering(items, 3, 50, "peso")
for m in myclusters: 
    print(m,end="\n")
   
