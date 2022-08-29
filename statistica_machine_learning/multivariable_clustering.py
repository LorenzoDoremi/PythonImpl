from audioop import mul
from random import random

from numpy import Infinity


class multivariable_pivot_set:
    def __init__(self, keys, avg):
        self.s = set()

        
        self.keys = keys
        #avg is a list of averages for each key used
        self.avg = avg
        # the sum value of the i-th key. used for the average calc.
        self.total = [0]*len(self.keys)

        # num of elements in the set
        self.size = 0

    
    def insert(self,data, save_key):
        # in the set i just put the chosen save key for visualization. 
        self.s.add(data[save_key])
        self.size+=1
        # sum on total
        for i in range(0,len(self.keys)):
          self.total[i] += data[self.keys[i]]
        
        # calc average
        for i in range(0,len(self.keys)):
            self.avg[i] = self.total[i]/self.size
    
    def __str__(self):

        return str(self.s) + "\navg = "+str(self.avg) + "\nkeys= "+str(self.keys)

    



# this function inserts a dictionary data into a particular set who keeps track of the average of keys
def insert_all_data(sets, data, keys):
    for element in data:
        # calculate the distance of the dictionary from each given set. find the minimum
        minv = Infinity
        min_set : multivariable_pivot_set = None
        # per ciascun set
        for index in range(0,len(sets)):
            # for each key, calculate the abs difference between dict.key and the set average key
            # sum the differences on distance, and then check. 
            distance = 0
            for key_index in range(0,len(keys)):
                
                max_value = max(element[keys[key_index]],sets[index].avg[key_index])
                min_value = min(element[keys[key_index]],sets[index].avg[key_index])
                distance += abs(1 - max_value/min_value)
            # if distance is lower, save the current set candidate.
            if distance < minv:
                minv = distance
                min_set = sets[index]
        #assign the current dictionary to the candidate set   
        min_set.insert(element, "nome")

# data = a list of dictionaries
# save_key = the name used for indexing and visualization
# keys = a list of keys used to cluster
# iterations = a precision indicator 
# num_sets = how many sets you want            
def multivariable_clustering(data, save_key, keys, iterations, num_sets):
     
     sets = []
     eliminated = []
    
     d = data.copy()
     #creates randomic sets by using the initial data
     for i in range(0,num_sets):
      new_set = multivariable_pivot_set(keys, [0 for x in keys])
      random_pivot = d[int(random()*len(d))]
      new_set.insert(random_pivot,save_key)
      sets.append(new_set)
      #i temporarily remove already visited random pivots
      d.remove(random_pivot)
      eliminated.append(random_pivot)

     
     for el in eliminated:
       d.append(el)

     #for each iteration, insert the data into sets, then get the average a recreate new starting sets.
     for i in range(0,iterations):
            insert_all_data(sets, data, keys)
            for set_index in range(0,len(sets)):
                new_avg = sets[set_index].avg
              
                sets[set_index] = multivariable_pivot_set(keys, new_avg)

     
     # at the end, do a final insert.
     insert_all_data(sets, data, keys)
     return sets






# example dataset
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

# example keys used
''' keys = ["peso", "età", "lunghezza"]
save_key = "nome"


sets = multivariable_clustering(animali, save_key, keys, 100, 5)

for set in sets:
    print("\n ")
   
    print(set)

 '''









