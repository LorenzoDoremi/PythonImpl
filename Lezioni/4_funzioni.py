# scriviamo un sottoprogramma che possiamo riutilizzare quante volte vogliamo.

# un sottoprogramma è formato da 4 parti fondamentali:
# 1:il nome
# 2:cosa ritorna
# 3:che parametri riceve
# 4:cosa fa

# def significa define = definisci



def area_triangolo(b,h):
    a = b*h/2
    return a


base = 12
altezza = 8
area = area_triangolo(base,altezza)






#funzione che determina se qualcuno è maggiorenne. 
def maggiorenne(anni):
    if(anni >= 18):
        return True
    else: 
        return False
#funzione che rimappa un numero da un intervallo all'altro (come in classe)
def remap(num,in1,fin1,in2,fin2):
    r = num-in1 
    #rapporto di dimensione tra gli intervalli
    rapporto = (fin2-in2)/(fin1-in1)
    nuovo_numero = in2+r*rapporto
    return nuovo_numero

def valore_assoluto(n):
    if(n<0):
        return n*-1
    return n

def volume_cilindro(raggio,altezza):
    return raggio**2*3.1415*altezza


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


# perchè non è cambiato un bel niente?

# sommiamo tutti i numeri in un vettore.
def somma_vettore(lista):

    totale = 0
    for numero in lista:
        totale += numero
    return totale


numeri = [1, 2, 3, 4, 5]
print(somma_vettore(numeri))

# utile la funziona somma_vettore? beh in realtà no. Python è bello perchè ci sono le cose già fatte ;)
somma = sum(numeri)
print(somma)


def informazioni_vettore(lista):

    # ritorniamo la lunghezza, la somma dei valori e la loro media. già più interessante!
    return [len(lista), sum(lista), sum(lista)/len(lista)]


print(informazioni_vettore(numeri))
