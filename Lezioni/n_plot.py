import matplotlib.pyplot as plt
from random import random
data = []
figure, axis = plt.subplots(2, 2)
# creo una lista di dizionari contenenti una transazione economica (come oggetti JSON!)
# id = id transazione
# a = primo committente
# b = secondo committente
# sum = quantità di denaro
for i in range(0, 10):
    data.append(
        {
            "id": int(random()*1000),
            "mittente": int(random()*10),
            "destinatario": int(random()*10),
            "sum": int(random()*10000)
        }
    )

# conta il numero di occorrenze di oggetti con una chiave numerica in una lista di dizionari  
#  
# O(N) temporale ma O(k) spaziale
def min_max_counter(max,data,target):
      occs = [0 for x in range(0,max)]
      for el in data:
          occs[el[target]] +=1
      return occs


#valori primo plot. guardo le quantità di denaro di ciascuna transazione
ids = [x["id"] for x in data]
sums = [x["sum"] for x in data]
axis[0][0].bar(ids, sums, width=10)


#valori secondo plot (guardo la relazione tra i vari utenti)
aas = [x["mittente"] for x in data]
bs = [x["destinatario"] for x in data]
axis[1][0].scatter(aas, bs)


# calcolo il numero di transazioni fatte dai vari ID di tipo destinatario
b_occs = min_max_counter(10,data,"destinatario")

print(b_occs)

axis[0][1].plot(b_occs)

# python già riconosce categorie uguali se hanno stringe uguali (come il nome)
soldi = [100,100,20,50,200]
persone = ["Gianni", "Franco", "Gianni", "Luca", "Andrea"]
axis[1][1].plot(persone,soldi)


# metto label, titoli e altro
axis[0][0].set(xlabel="ID", xticks=ids,  ylabel="TRANSAZ")
axis[1][0].set(xlabel="Mittente", ylabel="Destinatario", xticks=bs)
axis[0][1].set(xlabel="Destinatario", ylabel="occorrenze", xticks=[x for x in range(0,10)])

plt.show()
