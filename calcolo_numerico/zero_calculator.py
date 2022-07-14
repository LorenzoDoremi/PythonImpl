# approssimazione zeri di una funzione tramite bisezione
from bisect import bisect
from tkinter.tix import X_REGION


def bisection(func, min, max, iteractions):
   
    a = min
    b = max
    mid = (min + max)/2
    if iteractions == 0 or func(mid) == 0:
        return mid
    else:
        if func(a)*func(mid) < 0:
            return bisection(func, a, mid, iteractions - 1)
        else:
            return bisection(func, mid, b, iteractions - 1)


# approssimazione zeri tramite corde (regula falsi)
def regula_falsi(func, min, max, iteractions):
  
    # estremi x presi in considerazione
    a = min
    b = max
    # coefficiente angolare della retta
    m = (func(b) - func(a))/(b - a)
  
    # valore x dello zero della retta
    # spiegazione esempio = una retta con coefficiente m = 3, perderà/guadagnerà 3 y per ogni 1 x. 
    # Se la retta nel punto x vale 12 e ha m = 4, basteranno 12/4 = 3 passi per arrivare a 0. 
    # uso il valore assoluto perchè vado sempre da sinistra a destra (min -> max)
    x = min + abs(func(min)/m)

    if iteractions == 0 or func(x) == 0:
        return x
    else:
        if func(a)*func(x) < 0:
           # print("LEFT")
            return regula_falsi(func, a, x, iteractions - 1)
        else:
           # print("RIGHT")
            return regula_falsi(func, x, b, iteractions - 1)

def secanti(func,first,last,iteractions):
 
 
  x_i = 0
 
  
  for i in range(0,iteractions):
       
        if(abs(first - last) > 0.01):
        
          # principio simile alla regula falsi, ma il punto x_i è al di fuori del range first-last
          x_i = first - (func(first)/ ((func(last) - func(first))/(last-first)))
          first = last
          last = x_i

  return x_i
        
def newton_raphson(func, min, max, iterations):
    ""
    ''' if func(min)*func(max) >= 0:
        return False '''
    
    xi = max
    for i in range(0,iterations):

        
        coeff = (func(xi) - func(xi-0.1))/(xi - (xi-0.1))
        xi -= abs(func(xi)/coeff)
        print(xi)
        if abs(func(xi)) < 0.01:
           break
    
    return xi
        


        
''' print(regula_falsi(lambda x : x**2 - 5, -5,2,100))
print(bisection(lambda x : x**2 - 5, -5,5,100))
print(secanti(lambda x : x**2 - 5, -5,2,100))'''
print(newton_raphson(lambda x : x**2 - 5, -5,5,100)) 



