import numpy
from random import random, randint


array_di_zeri = numpy.zeros((10))

# media già fatta
media = numpy.average(array_di_zeri)

# varianza... una rottura da scrivere da zero
varianza = numpy.var(array_di_zeri)

# un numero random tra 0 e 100
numero_random = int(random.random()*100);
numero_intero_random = randint(0,100)

print(numero_random)


