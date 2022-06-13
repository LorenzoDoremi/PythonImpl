import matplotlib.pyplot as plt
from random import random
data = []
figure, axis = plt.subplots(3, 1)
# creo una lista di dizionari (come oggetti JSON!)
for i in range(0, 10):
    data.append(
        {
            "id": int(random()*1000),
            "a": int(random()*10),
            "b": int(random()*10),
            "sum": int(random()*10000)
        }
    )

# conta il numero di occorrenze di una chiave numerica in una lista di dizionari  
# (ad esempio quanti esami sostenuti dallo studente con un id target) 
# O(N) temporale ma O(k) spaziale
def min_max_counter(max,data,target):
      occs = [0 for x in range(0,max)]
      for el in data:
          occs[el[target]] +=1
      return occs


#valori primo plot
ids = [x["id"] for x in data]
sums = [x["sum"] for x in data]
axis[0].bar(ids, sums, width=10)


#valori secondo plot
aas = [x["a"] for x in data]
bs = [x["b"] for x in data]
axis[1].scatter(aas, bs)



b_occs = min_max_counter(0,10,data,"b")

print(b_occs)

axis[2].plot(b_occs)


# metto label, titoli e altro
axis[0].set(xlabel="ID", ylabel="TRANSAZ")
axis[1].set(xlabel="A", ylabel="B", xticks=bs)
axis[2].set(xlabel="B", ylabel="occorrenze")
plt.show()
