from isolation_generator import dataset

class isolation_tree: 
    def __init__(self,data):
        self.data = data 
        self.insiemi = [data]
    def split(self,key,value = None):
        sub_insiemi = []
        for insieme in self.insiemi: 
            # limito gli split a 4 elementi. 
            if len(insieme) > 4:
                i1 = [] 
                i2 = []
                # controllo se ho a che fare con numeri
                avg = 0 
                if isinstance(insieme[0][key],(int,float,complex)): 
                    for elemento in insieme: 
                        
                        avg += elemento[key]
                    avg /= len(insieme)
              
                # inizio a controllare ogni elemento dell'insieme
                for elemento in insieme: 
                    # splitto i numeri 
                    if isinstance(elemento[key],(int,float,complex)):
                        
                        if elemento[key] < avg: 
                            i1.append(elemento)
                        else: 
                            i2.append(elemento)
                    # splitto stringhe 
                    else: 
                        if elemento[key] != value: 
                            i1.append(elemento)
                        else: 
                            i2.append(elemento)
                # non considero vettori vuoti. 
                if len(i1) > 0:        
                    sub_insiemi.append(i1)
                if len(i2) > 0:
                    sub_insiemi.append(i2)
        self.insiemi = sub_insiemi


# dataset viene generato dal documento python che crea persone casuali e alcuni outlier.
tree = isolation_tree(dataset)
tree.split("altezza")
tree.split("peso")
tree.split("altezza")
tree.split("peso")


avlen = max(len(a) for a in tree.insiemi)
for sub in tree.insiemi: 
    if len(sub) <= avlen/3: 
        print(sub)


    
           
        
        
        
