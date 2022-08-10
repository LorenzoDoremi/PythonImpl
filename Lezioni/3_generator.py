# i generatori: un caso molto particolare di creazione di dati

# 1: creo un generatore tramite list comprehension
numeri = (x for x in range(0, 10))

# primo loop. stampa.
for n in numeri:
    print(n, end=" ")
# secondo loop. non più utilizzabile!!!!!
for n in numeri:
    print(n*n, end=" ")

quadrati = (x*x for x in numeri)

# non posso nemmeno estrarre da quel generatore
for n in quadrati:
    print(n*n, end=" ")


# 2: creo un generatore tramite yield

def numeroni():
    for i in range(0, 10):
        yield i

# assegno
nuovi_numeroni = numeroni()

# stampo. funziona!
for i in nuovi_numeroni:
    print(i)

# non posso stampare un'altra volta. 
for i in nuovi_numeroni:
    print(i)


# quanto utilizzare un generatore e quando utilizzare una lista?
