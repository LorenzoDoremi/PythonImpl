# scriviamo un sottoprogramma che possiamo riutilizzare quante volte vogliamo.

# un sottoprogramma è formato da 4 parti fondamentali:
# 1:il nome
# 2:cosa ritorna
# 3:che parametri riceve
# 4:cosa fa

# def significa define = definisci

# fattoriale di 5 = 5*4*3*2*1
def fattoriale(x: int) -> int:

    for i in range(1, int(x)):
        x *= i
    return x


def fattoriale_generico(x):

    for i in range(1, int(x)):
        x *= i
    return x


# cosa stamperà? attenzione!
print(fattoriale(5.656))
# e questo?
print(fattoriale_generico(5.656))


# sommiamo tutti i numeri in un vettore.
def somma_vettore(lista):

    totale = 0
    for numero in lista:
        totale += numero
    return totale


numeri = [1, 2, 3, 4, 5]
print(somma_vettore(numeri))

# utile la funziona somma_vettore? beh in realtà no. Pyhton è bello perchè ci sono le cose già fatte ;)
somma = sum(numeri)
print(somma)


def informazioni_vettore(lista):

    # ritorniamo la lunghezza, la somma dei valori e la loro media. già più interessante!
    return [len(lista), sum(lista), sum(lista)/len(lista)]


print(informazioni_vettore(numeri))
