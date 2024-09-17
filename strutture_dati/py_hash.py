import numpy


class pyHash:
    def __init__(self, size):
        self.table = numpy.zeros(size)
        self.size = size
    def insert(self, value):
        
        self.table[self.hashingFunction(value)] = value
    def read(self, value):
        stored = self.table[self.hashingFunction(value)]
        #nell'indirizzo cercato c'è quel valore
        return stored == value 




    def hashingFunction(self, value):
        return (value*value)%self.size