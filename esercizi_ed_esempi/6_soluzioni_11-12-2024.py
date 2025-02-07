# 1
'''
x = [i for i in range(-30,31)]
y = [i**2 -3 for i in x]
'''
#2 
x = [i for i in range(-30,31)]
def xy(v):
    
    y = [i**2 -3 for i in v]
    return y 

y = xy(x)
#3 estrarre i pari 
p = []
for i in y: 
    if i % 2 == 0:
        p.append(i)
#4 matplotlib.
'''
la difficoltà sta nel capire che 
servono delle ascisse per i dati di P'''

'''
import matplotlib.pyplot as plt 
xp = [i for i in range(0,len(p))]
plt.xlabel("X")
plt.ylabel("Numeri Pari")
plt.plot(xp,p)
plt.show()
# 5
plt.xlabel("X")
plt.ylabel("Numeri Pari")
plt.plot(xp,p,color="green")
plt.show()
'''
#6 matrice 8x8 di zeri 
matrice = [[0 for i in range(0,8)] for i in range(0,8)]
#6 versione con cicli e append
matrice = [] 
for i in range(0,8):
    v = []
    for j in range(0,8):
        v.append(0)
    matrice.append(v)

#7 scacchiera 
def scacchiera(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if (i+j) % 2 == 0:
                matrix[i][j] = "O"
            else:
                matrix[i][j] = "X"
scacchiera(matrice)
# stampo bene la matrice 
for riga in matrice: 
    for cella in riga: 
        print(cella,end=" ")
    print("")
#8 somma v 
def f_soglia(vettore, soglia):
    totale = 0
    i = 0  
    while i < len(vettore) and totale < soglia: 
        totale += vettore[i]
        i+=1
    return totale 
# dimostrazione 
v = [1,4,7,7,10,12,0,5,5]
print(f_soglia(v,14))

# 9 somma coppia con vettore ordinato. 
def somma_ord(v, k):
    i = 0 
    j = len(v)-1
    # muovo due indici. se la somma è più bassa, alzo il minore. se è troppo alta, abbasso il maggiore.
    while i < j: 
        if v[i]+v[j] == k:
            return True
        elif v[i]+v[j] < k:
            i+=1
        else:
            j-=1
    return False 
print(somma_ord(v,17))

# 10 
# la difficoltà sta nel fatto che ogni volta che faccio pop(), 
# riduco la lunghezza del vettore (rischiando di andare oltre) e sposto il prossimo elemento sulla posizione
# attuale, rischiando di perderlo. 
def pop_dinamico(vettore):
        i = 0 
        while i < len(vettore):
            # devo ricordarmi di non andare avanti se tolgo un elemento
            if vettore[i] % 2 == 0: 
                vettore.pop(i)
            else: 
                i+=1
pop_dinamico(v)
print(v)