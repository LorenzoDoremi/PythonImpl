from random import random


dati = [random()*10000  for x in range(0,1000)]

#calcolo la media di una serie di dati
# step = 1, uso tutti i dati
# step = 10, uso un dato ogni 10. 
def media(dati, step):
    media = 0
    for i in range(0,len(dati), step):
      media += dati[i]
    return media/(len(dati)/step)

def precisione(dato_reale, dato_errato):
    precisione = 1 - abs(dato_reale-dato_errato)/dato_reale;
    return precisione



m = media(dati, 1)
print(m)

m_errore = media(dati, 30)
print(m_errore)

precisione = precisione(m, m_errore)
print(str(int(precisione*100))+"%")

