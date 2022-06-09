from copy import copy
from random import random
import numpy
from ProfanityFilter import profanityFilter
from primeNumbers import primeNumbers, primeNumbersFix
from pyHash import pyHash
from zeroCalculator import bisection, regulaFalsi

i = 0

def square(x):
    return x*x - 10 
# dichiariamo un array di zeri lungo 20 (metodo non bello)
''' array = [0] * 20; '''

#metodo migliore
''' array = numpy.zeros(10) '''
# matrice 
''' matrix = numpy.zeros((10,10)) '''





# questo permette di modificare l'array
''' for j in range(0,len(array), 1):
  array[j] = int(random()*100) '''
  
#questo no ( a diventa un nuovo oggetto)
''' for a in array:
  a = random()*100


zero = bisection(square,-10,10,100)
'''
zero = regulaFalsi(square,-5,0,10) 
print(zero)
# crivello di eratostene

''' primeNumbersFix(100) '''

# test parolacce con un filtro (esempio di util da programmare per il proprio portfolio)
''' st = "Sedere sedere cACca viga mazzo nerda"
s = profanityFilter(st,"*")
print(s) '''

# semplice implementazione di un hashtable
''' table = pyHash(101)
for i in range(0,50):
  table.insert(i)

print(table.read(40)) '''

# list comprehension
''' numeri = [x for x in range(10)]
quadrati = copy(numeri)
print(quadrati)
numeri[3] = 100
print(quadrati) '''


