#funzione che rimappa un numero 
# da un intervallo all'altro (come in classe)
def remap(num,in1,fin1,in2,fin2):
    r = num-in1 
    #rapporto di dimensione tra gli intervalli
    rapporto = (fin2-in2)/(fin1-in1)
    nuovo_numero = in2+r*rapporto
    return nuovo_numero



print(remap(10,0,100,50,100))