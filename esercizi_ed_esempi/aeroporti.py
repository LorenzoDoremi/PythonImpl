from random import random
import numpy


class hash:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size
     
    # funzione di hashing
    def hash_value(self, key):
        seed = pow(2,7) -1
        
        return (id(key)*seed) % self.size
    #inserisci nella hash l'oggetto in base alla chiave data
    def insert(self, new_object):

        self.table[self.hash_value(new_object)] = new_object

    def get(self, key):

        return self.table[self.hash_value(key)] != None

    def __str__(self):

        string = ""
        for aereo in self.table:
            if aereo:
                string+= "nome volo = "+str(aereo)+"\n"
        return string


class aereo:
    def __init__(self, nome_volo, id_aeroporto):
        self.id_aeroporto = id_aeroporto
        self.nome_volo = nome_volo
    def __str__(self):
        return "aeroporto di riferimento = "+str(self.id_aeroporto)+" nome volo = "+str(self.nome_volo)


def insert_plane(aereo: aereo, aeroporti):

    for aeroporto in aeroporti:

        if aeroporto["id"] == aereo.id_aeroporto:

            aeroporto["tabella"].insert(aereo)


aeroporti = [{"id": i, "tabella": hash(255)} for i in range(0, 10)]


for i in range(0, 100):
    new_aereo = aereo(int(random()*99999), int(random()*10))
    insert_plane(new_aereo, aeroporti)


print(aeroporti[5]["tabella"])
