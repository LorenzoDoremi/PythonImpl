#Python 3
import urllib.request, json 
import random 
import matplotlib.pyplot as plt
data = []
#sito web della tesi di laurea del professore. quella pagina PHP ritorna un lunghissimo oggetto JSON 
with urllib.request.urlopen("http://klinkart.altervista.org/datajson.php") as url:
    data = json.loads(url.read().decode())


for opera in data: 
    print(opera["autore"]) 





def fibonacci(n):
    if(n == 1):
        return 0 
    if(n == 2):
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)
    
    
for i in range(1,10):
    print(fibonacci(i))
    
    
    
    
class Nodo(): 
    def __init__(self, k ) -> None:
        self.k = k 
        self.next = None 
    def stampaRicorsivo(self):
        print(self.k)
        if(self.next):
            self.next.stampaRicorsivo()
            

n = Nodo(10)
n.next = Nodo(20)
n.stampaRicorsivo()




anni = [ i for i in range(0,10)]
peso = [0.5*anno + random.uniform(-2,2) for anno in anni ]

for i in anni: 
    print(i)

for i in anni: 
    print(i*i)


plt.scatter(anni,peso)
plt.xlabel("anni scoiattolo")
plt.ylabel("peso in kg")
plt.show()