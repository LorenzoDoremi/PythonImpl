from random import random




lista = []

# 1: classico ciclo for per riempire lista. scomodo
for x in range(0, 100):
    lista.append(x)

# list comprehension. ottengo lo stesso risultato ma è più efficiente
lista = [x for x in range(0, 100)]




# un oggetto classe. lo vediamo meglio più avanti
class utente:
    def __init__(self, eta):
        self.eta = eta

# 2: lista di oggetti
utenti = []
for x in range(0,10):
    utenti.append(utente(int(random()*100)))

# 2.a: ut è un nuovo oggetto. questa cosa non funziona!
for ut in utenti:
    ut = utente(100)

# 2.b: questo funziona. i è solo un indice che punta alla lista di utenti
for i in range(0,len(utenti)):
    utenti[i] = utente(100)

# stamperà tanti 100
for ut in utenti:
    print(ut.eta)


# si può ottimizzare questo codice? quali sono le possibili problematiche di questo approccio?

