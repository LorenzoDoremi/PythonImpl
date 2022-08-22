from random import random




lista = []

# 1: classico ciclo for per riempire lista. non sempre l'opzione migliore
for x in range(0, 100):
    lista.append(x*10)

# enumerate è la versione più elegante e professionale per scorrere un oggetto iterabile
for index, x in enumerate(lista):
    print(x, end=" - ")


print("")



# list comprehension. ottengo lo stesso risultato ma è più efficiente
lista = [x for x in range(0, 100)]

# list comprehension permette anche di creare ed estrarre valori più interessanti.

oggetti = [ {"x": i, "y": i**2} for i in range(0,10)]

valori_x = [oggetto["x"] for oggetto in oggetti]

print("valori = ")
print(valori_x)




# un oggetto classe. lo vediamo meglio più avanti
class utente:
    def __init__(self, eta):
        self.eta = eta

# 2: lista di oggetti classe
utenti = []
for x in range(0,10):
    utenti.append(utente(int(random()*100)))




# 2.a: ut è una copia finta creata sul momento. questa cosa non funziona!
for ut in utenti:
    ut = utente(50)

# stamperà numeri a caso
for ut in utenti:
    print(ut.eta)


# 2.b: questo funziona. i è solo un indice che permette di puntare alla lista di utenti
for i in range(0,len(utenti)):
    utenti[i] = utente(100)

# stamperà tanti 100
for ut in utenti:
    print(ut.eta)


# si può ottimizzare questo codice? quali sono le possibili problematiche di questo approccio?

