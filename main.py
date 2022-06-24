from copy import copy
from random import random
import numpy
from esercizi_ed_esempi.profanity_filter import profanityFilter
from calcolo_numerico.prime_numbers import primeNumbers, primeNumbersFix
from strutture_dati.py_hash import pyHash
from calcolo_numerico.zero_calculator import bisection, regula_falsi
from calcolo_numerico.integral_calculator import metodo_rettangoli
i = 0

def square(x):
    return x*x - 10 
# dichiariamo un array di zeri lungo 20 (metodo non bello)
''' array = [0] * 20; '''

#metodo migliore
''' array = numpy.zeros(10) '''
# matrice 
''' matrix = numpy.zeros((10,10)) '''

''' 
class user:
      def __init__(self, age):
           self.age = age


def editUser(l,k):
      m = user(50)
      l.age = m.age

a = user(10)
b = user(50)
editUser(a,b)
print(a.age) '''






           


# questo permette di modificare l'array
''' for j in range(0,len(array), 1):
  array[j] = int(random()*100) '''
  
#questo no ( a diventa un nuovo oggetto)
''' for a in array:
  a = random()*100


zero = bisection(square,-10,10,100)
'''
''' zero = regula_falsi(square,-5,0,10) 
print(zero) '''
# crivello di eratostene

primeNumbersFix(100) 

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




