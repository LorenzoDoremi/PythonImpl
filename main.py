from random import random
import numpy
from primeNumbers import primeNumbers, primeNumbersFix
from zeroCalculator import bisection, regulaFalsi

i = 0

def square(x):
    return x*x*x - 10 
# dichiariamo un array di zeri lungo 20 (metodo non bello)
array = [0] * 20;

#metodo migliore
array = numpy.zeros(10)
# matrice 
matrix = numpy.zeros((10,10))



m = [2,2,4,432,23545]


m.append(2)


# questo permette di modificare l'array
for j in range(0,len(array), 1):
  array[j] = int(random()*100)
  
#questo no ( a diventa un nuovo oggetto)
for a in array:
  a = random()*100


zero = bisection(square,-10,10,100)
zero = regulaFalsi(square,-10,10,100)

# crivello di eratostene

primeNumbersFix(100)


