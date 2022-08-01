from random import random

from numpy import sqrt


def montecarlo_pi(iterations):

   
    inside = 0
   
    for i in range(0,iterations):
        # valori da -1 a 1. quadrato che iscrive il cerchio
        x = (random()-0.5)*2
        y = (random()-0.5)*2
        dist = sqrt(x**2 + y**2)
        if dist <= 1:
            inside +=1

    # perchè 4? pensa...quattro quadrati di area 1....    
    return (inside/iterations) * 4



    
    



a = montecarlo_pi(100000)
print(a)




