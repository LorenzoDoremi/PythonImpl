'''
ABC
DEF
DE


'''
# genero un CDC
class Classe():
    def __init__(self,id,docenti) -> None:
        self.id = id
        self.docenti = docenti
# genero un gruppo di CDC scrutinio paralleli
class Gruppo():
    def __init__(self, classe : Classe ) -> None:
        # Inizializza classi e docenti come liste vuote
        self.classi = []
        self.docenti = []
        
        if classe: 
            self.addClasse(classe)
    def addClasse(self,classe : Classe):
         self.classi.append(classe.id)
         for docente in classe.docenti:
             self.docenti.append(docente)

c1 = Classe(1,['a','b','c'])            
c2 = Classe(2,['c','d','e'])   
c3 = Classe(3,['f','a','t'])   
c4 = Classe(4,['f','d','x'])

gruppi = [
    Gruppo(c1), 
    Gruppo(c2),
    Gruppo(c3),
    Gruppo(c4)
]

for gruppo in gruppi: 
    for gruppo2 in gruppi: 
        disjoint = True
        for docente in gruppo2.docenti:
            if(docente in gruppo.docenti):
                disjoint = False
                break
        if(disjoint):
            for classe in gruppo2.classi:
                gruppo.classi.append(classe)
                gruppo2.classi.remove(classe)
            for docente in gruppo.docenti: 
                gruppo2.docenti.append(docente)


for gruppo in gruppi: 
    print(gruppo.classi)
            
                
    
         





