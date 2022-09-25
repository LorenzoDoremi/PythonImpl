from random import random
from re import M



lista_piena = [1,2,3]
lista = []

# un dizionario. oggetto UTILISSIMO!
dizionario = {"nome": "Lorenzo", "eta": 28}


# 1: classico ciclo for per riempire lista. non sempre l'opzione migliore
for x in range(0, 10):
    lista.append(x*10)

# enumerate è la versione più elegante e professionale per scorrere un oggetto iterabile
for index, x in enumerate(lista):
    print(x, end=" - ")


print("")


# list comprehension. ottengo lo stesso risultato ma è ancora più elegante e leggibile
lista = [x for x in range(0, 100)]

# list comprehension permette anche di creare o estrarre valori più interessanti. ad esempio dizionari

oggetti = [ {"x": i, "y": i**2} for i in range(0,10)]

valori_x = [oggetto["x"] for oggetto in oggetti]

print("valori di x = ", end= " ")
print(valori_x)


l = [1,2,3,4]
m = [5,6,7,8]
conc = l+m  # [1,2,3,4,5,6,7,8]
sum = [l[i] + m[i] for i in range(0,len(l))] #[6,8,10,12]
#diff = m - l #questo non esiste

#i primi 3 elementi di una lista
parte = l[:3]
#gli ultimi n-2 elementi (ovvero quanti ne salto)
k = l[2:]
print(k)
