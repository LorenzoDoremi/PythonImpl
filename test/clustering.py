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

def clustering(list, clusters_num, iterations):
    clusters = []
    # creo i cluster iniziali random
    for i in range(0,clusters_num):
        cluster = {"el": [], "total":0, "mean": 0}
        randomel = list[(int)(random()*len(list))]
        cluster["el"].append(randomel)
        # inserisco il primo elemento
        cluster["total"] = randomel["peso"]
        cluster["mean"] = randomel["peso"]
        clusters.append(cluster)
    # rieseguo n-volte il processo aggiornando
    for i in range(0, iterations):
        # per ogni elemento
        for el in list: 
            min = float("inf")
            mindex = 0
            # per ogni cluster cerco quello più simile
            for c in range(0,len(clusters)):
                # calcolo quanto gli elementi di un cluster assomigliano all'oggetto
                dist = abs(clusters[c]["mean"]- el["peso"])
                
                if(dist < min):
                    min = dist 
                    mindex = c
                   
            # inserisco un nuovo elemento e aggiorno le informazioni
            clusters[mindex]["el"].append(el)
            clusters[mindex]["total"] += el["peso"]
            clusters[mindex]["mean"] =  clusters[mindex]["total"]/len(clusters[mindex]["el"])
      
        # calcolo la media di ogni cluster        
        for c in clusters:
                 # resetto i cluster mantenendo la media. 
                 if(i < iterations-1):
                    c["el"] = []
                 c["total"] = 0
                 
       
            
            
    
    return clusters
         
   
myclusters = clustering(items, 3, 20)
for m in myclusters: 
    print(m,end="\n")
   
