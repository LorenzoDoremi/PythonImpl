from random import random
import matplotlib.pyplot as plt
from numpy import average

figure, axis = plt.subplots(2)

#funzione che ritorna valori leggermente errati intorno ad una retta del tipo y = k   (m = 1, q = 0)
def population(k):
    return k+(random()-0.5)*10

#popolo una serie di valori continui (per evitare un inutile sort )
curr = 0
x = []
for i in range(0,10):
  curr = curr + random()*10
  x.append(curr)

# calcolo dei valori "errati" attorno  ai valori di x
y = [population(i) for i in x]





# coefficienti della retta
m = 0
q = 0


# metodo 1 per calcolare il coefficiente angolare. 
# 1: Cosa sto facendo?
# 2: Quando non funziona? 
# 3: Perché?
for i in range(1, len(x)):
    m += (y[i] - y[i-1])/(x[i]- x[i-1])
  

m = m/len(x)


# metodo 2 per calcolare il coefficiente angolare (minimi quadrati)   m = sum2/sum1
avgy = average(y)
avgx = average(x)
sum1, sum2 = 0, 0
for i in range(0,len(x)):
    sum2 += (y[i] - avgy)*(x[i] - avgx)
    sum1 += (x[i] - avgx)**2

m = sum2/sum1


# calcolo q.   y = mx + q   ->  q = y - mx   (calcolo sempre la media, avendo tanti valori)
for i in range(0,len(x)):
    q+= y[i] - m*x[i]

q = q/len(x)



# calcolo l'errore dalla retta di coefficiente m se mi interessa
def error(coeff, qq):
 err = 0   
 for i in range(0,len(x)):
      err+= (y[i] - (coeff*i + qq))**2
 return err



line = [k*m + q for k in x]
print(m)
print(q)
axis[0].plot(x,y)
axis[0].plot(x,line)
axis[1].plot(y,x)



plt.show()



# https://medium.com/swlh/ols-method-of-linear-regression-using-c-6cdc1fd74918
# https://it. .org/wiki/Metodo_dei_minimi_quadrati#Stimatori_OLS