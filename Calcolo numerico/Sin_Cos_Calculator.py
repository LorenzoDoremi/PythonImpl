import math
import time


def factorial(x):
    
    r = x 
    for i in range(1,x):
     r *= x-i  
    return r  


def sin_taylor(a, iterations):

    r = 0
    
    for i in range(0,iterations):

        r += (((-1)**i)/factorial(2*i +1))*((a)**(2*i + 1))
    return r

def cos_taylor(a, iterations):
    
    r = 0
    
    for i in range(0,iterations):

        r += (((-1)**i)/factorial(2*i))*((a)**(2*i))
    return r


k = 0
test = 10000

t = time.time()*1000
for i in range(0,test):
  k = sin_taylor((i%360)*math.pi/180, 5)

print(time.time()*1000 - t)




