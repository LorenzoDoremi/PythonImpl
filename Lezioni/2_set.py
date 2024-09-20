lista = [1,2,3,65,3,56,2]
set1 = set(lista)
lista2 = [1,2,7,8,89,8]
set2 = set(lista2)

# questo codice calcola la similarità di Jaccard di due liste
unione = set1 | set2 
intersezione = set1 & set2 
jaccard = len(intersezione)/len(unione)

print(jaccard) 