# creo una semplice hash table che riceve un numero N, lo elabora e lo converte in una posizione K 
import random


class hashTable:
    def __init__(self, dimensione):
        # risolvo il problema delle collisioni: ogni cella è una lista vuota in partenza. (chaining)
        self.tabella = []
        for i in range(dimensione):
            self.tabella.append([])
        self.dimensione = dimensione
        self.contenuto = 0
        
        
        
    # definisco una funzione che converte N in K
    def hashing(self, N):
        # funzione dell'esempio (pessima)
        #return 2*N
        
        # risolvo (almeno parzialmente) il problema della distribuzione uniforme
        # sfrutto i numeri primi = evitano che si formino dei pattern
        # nota: non è una gran funzione. c'è un mondo che studia solo questo campo. 
        return (((N*101)**31)%251) % self.dimensione
    
    # funzione che inserisce nella posizione K il valore N
    def insert(self,N):
        
        # risolvo il problema delle dimensioni: scelgo una soglia (0.9) oltre alla quale raddoppio la tabella
        if(self.contenuto/self.dimensione > 0.9): 
           self.resize()
        K = self.hashing(N)
        self.tabella[K].append(N)
        self.contenuto += 1
        
        
    # funzione che cerca il valore N nella tabella
    def search(self, N):
        # trasformo N in K
        K = self.hashing(N)
        # cerco nella catena corrispondente
        for elemento in self.tabella[K]:
            if(elemento == N):
                return True
        return False
    def printTable(self):
        for catena in self.tabella:
            print(catena)
    # risolvo il problema delle dimensioni      
    def resize(self):
            for i in range(self.dimensione):
                self.tabella.append([])
            # metodo brutto...
            self.dimensione*=2
            # ora bisognerebbe fare il rehashing: reinserire tutti gli elementi nella posizione corretta


# esempio di utilizzo
table = hashTable(10)
# inserisci elementi a caso 
for i in range(0,100):
    table.insert(random.randint(0,100))

table.printTable()
print(table.dimensione)
