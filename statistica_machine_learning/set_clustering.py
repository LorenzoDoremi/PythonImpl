from random import random
from numpy import Infinity, average, insert


animali = [
    {"nome": "Tigre", "peso": 200, "altezza": 120 },
    {"nome": "Leone", "peso": 160, "altezza": 110 },
    {"nome": "Balena", "peso": 15000, "altezza": 3000 },
    {"nome": "Ragno", "peso": 0.15, "altezza": 2 },
    {"nome": "Squalo Tigre", "peso": 1000, "altezza": 12000 },
    {"nome": "Formica", "peso": 0.03, "altezza": 1 },
    {"nome": "Gatto", "peso": 4, "altezza": 40 },
    {"nome": "Pesce Palla", "peso": 1, "altezza": 30 },
    {"nome": "Leone", "peso": 120, "altezza": 110 },
    {"nome": "Capidoglio", "peso": 10000, "altezza": 3000 },
    {"nome": "Ragno", "peso": 0.05, "altezza": 2 },
    {"nome": "Squalo", "peso": 4000, "altezza": 12000 },
    {"nome": "Formica", "peso": 0.03, "altezza": 1 },
    {"nome": "Gatto ciccione", "peso": 8, "altezza": 40 },
    {"nome": "Pesce Palla", "peso": 1, "altezza": 30 },


]
class pivot_set:
    def __init__(self, key, avg):
        self.set = set()
        self.key = key
        self.avg = avg
        self.total = 0
        self.size = 0

    
    def insert(self,data, save_key):
        # salvo il nome
        self.set.add(data[save_key])
        self.size+=1
        self.total += data[self.key]
        self.avg = self.total/self.size
    
    def __str__(self):

        return str(self.set) + " avg = "+str(self.avg)


   




sets = []
clustering_key = "peso"

#creo i set partendo da nessuna informazione (La media)
for i in range(0,4):
    pivot = animali[int(random()*len(animali))]
    new_set = pivot_set(clustering_key, 0)

    #uso il nome per vedere i set in chiarezza, superfluo per i conti
    new_set.insert(pivot, "nome")
    sets.append(new_set)

# inserisco tutti i dati che ho 
def insert_all_data(key):
 for animale in animali: 

    min = Infinity
    i = 0
    #cerco il set più simile all'animale che inserisco
    for i in range(0,len(sets)):
        if(abs(animale[key] - sets[i].avg) < min):
            index = i
            min = abs(sets[i].avg - animale[key] ) 
           
    sets[index].insert(animale, "nome")


insert_all_data(clustering_key)


# ricalcolo ogni volta i pivot dei vari set, ottenendo set più precisi 
def recalculate_pivots(repetitions, key):

    for j in range(repetitions):
      for i in range(0,len(sets)):
         sets[i] = pivot_set("peso", sets[i].avg)
      insert_all_data(key)


recalculate_pivots(10, clustering_key)

for set in sets:
    print(set)


