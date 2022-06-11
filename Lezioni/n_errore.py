from random import random


dati = [random()*10000  for x in range(0,1000)]


def media(dati, step):
    media = 0
    for i in range(0,len(dati), step):
      media += dati[i]
    return media/(len(dati)/step)

m = media(dati, 1)
print(m)

m_errore = media(dati, 30)
print(m_errore)

precisione = 1 - abs(m-m_errore)/m;
print(str(int(precisione*100))+"%")

