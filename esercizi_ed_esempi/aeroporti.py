import numpy


class hash:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size
    
    def hash_value(self, key):
        
        
        return id(key)*id(key) % self.size
    def insert(self, key):
        
        
       
        self.table[self.hash_value(key)] = key

    def get(self, key):

        return self.table[self.hash_value(key)] != None




aeroporti = [{"id":i, "tabella": hash(255)} for i in range(0,10)] 

print(aeroporti[5])


    

        