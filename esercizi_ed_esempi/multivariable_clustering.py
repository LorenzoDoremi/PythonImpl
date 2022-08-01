from audioop import mul
from random import random

from numpy import Infinity


class multivariable_pivot_set:
    def __init__(self, keys, avg):
        self.s = set()

        # self.key = chiave usata per calcolare la media
        self.keys = keys
        self.avg = avg
        self.total = [0]*len(self.keys)
        self.size = 0

    
    def insert(self,data, save_key):
        # salvo il nome
        self.s.add(data[save_key])
        self.size+=1
        # calcolo la media con la self.key 
        for i in range(0,len(self.keys)):
          self.total[i] += data[self.keys[i]]
        
        
        for i in range(0,len(self.keys)):
            self.avg[i] = self.total[i]/self.size
    
    def __str__(self):

        return str(self.s) + "\navg = "+str(self.avg) + "\nkeys= "+str(self.keys)

    





animali = [{"nome": "gatto","peso": 4, "età": 3,"lunghezza": 55},
{"nome": "leone", "peso": 160, "età": 8,"lunghezza": 250},
{"nome": "tigre","peso": 170,"età": 4, "lunghezza": 270},
{"nome": "ragno", "peso": 0.27, "età": 2, "lunghezza": 14},
{"nome": "cane", "peso": 17, "età": 10, "lunghezza": 120},
{"nome": "squalo", "peso": 5700, "età": 150, "lunghezza": 520},
{"nome": "balena", "peso": 10000, "età": 50, "lunghezza": 1220},
{"nome": "formica", "peso": 0.1, "età": 1, "lunghezza": 5},
{"nome": "caracal","peso": 8, "età": 3,"lunghezza": 105},
{"nome": "lupo", "peso": 100, "età": 8,"lunghezza": 200},
{"nome": "pesce palla","peso": 1,"età": 14, "lunghezza": 70},
{"nome": "elefante", "peso": 5000, "età": 80, "lunghezza": 500},
{"nome": "uomo", "peso": 80, "età": 80, "lunghezza": 180},
{"nome": "mucca", "peso": 1000, "età": 15, "lunghezza": 320},
{"nome": "toro", "peso": 1200, "età": 10, "lunghezza": 350},
{"nome": "farfalla", "peso": 0.05, "età": 1, "lunghezza": 10},

]



keys = ["peso", "età", "lunghezza"]

sets = []

eliminated = []
#creo set randomici
for i in range(0,5):
    new_set = multivariable_pivot_set(keys, [0 for x in keys])
    random_pivot = animali[int(random()*len(animali))]
    new_set.insert(random_pivot,"nome")
    sets.append(new_set)
    #evito duplicati come pivot
    animali.remove(random_pivot)
    eliminated.append(random_pivot)



for el in eliminated:
    animali.append(el)
    


def insert_all_data(sets, data, keys):
    for element in data:
        # calcola la differenza dall'elemento di ciascun set 
        minv = Infinity
        min_set : multivariable_pivot_set = None
        # per ciascun set
        for index in range(0,len(sets)):
            #per ciascuna chiave
            distance = 0
            for key_index in range(0,len(keys)):
                # valore stringa chiave = keys[key_index]
                # element, l'oggetto JSON
                max_value = max(element[keys[key_index]],sets[index].avg[key_index])
                min_value = min(element[keys[key_index]],sets[index].avg[key_index])
                # calcolo la distanza come la somma dei rapporti tra le chiavi. 
                distance += abs(1 - max_value/min_value)
            #se la distanza calcolata dell'attuale set è minore, lo salvo come candidato    
            if distance < minv:
                minv = distance
                min_set = sets[index]
           
        min_set.insert(element, "nome")

            
def multivariable_clustering(sets, data, keys, iterations):
     
     
     for i in range(0,iterations):
            insert_all_data(sets, data, keys)
            for set_index in range(0,len(sets)):
                new_avg = sets[set_index].avg
              
                sets[set_index] = multivariable_pivot_set(keys, new_avg)
     insert_all_data(sets, data, keys)



multivariable_clustering(sets, animali, keys, 100)

for set in sets:
    print("\n ")
   
    print(set)











