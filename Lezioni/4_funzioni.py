#scriviamo un sottoprogramma che possiamo riutilizzare quante volte vogliamo. 

#un sottoprogramma è formato da 4 parti fondamentali:
# 1:il nome
# 2:cosa ritorna
# 3:che parametri riceve
# 4:cosa fa

#fattoriale di 5 = 5*4*3*2*1
def fattoriale(x:int) -> int:
    
 
    for i in range(1,int(x)):
        x*=i
    return x



def fattoriale_generico(x):
    
 
    for i in range(1,int(x)):
        x*=i
    return x


# cosa stamperà? attenzione!
print(fattoriale(5.656))
# e questo?
print(fattoriale_generico(5.656))
