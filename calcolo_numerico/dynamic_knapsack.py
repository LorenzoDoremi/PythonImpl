import random




def knap(o,p):
    matrice = [[0 for _ in range(p+1)] for __ in range(len(o)+1)]
    for riga in range(0,len(o)):
        for peso in range(1,len(matrice[riga])):
            
            v_c = o[riga]["v"]
            p_c = o[riga]["w"]
            # elemento massimo che posso aggiungere al peso corrente mancante. 
            v_prec = matrice[riga][max(0,peso - p_c)]
            # non lo posso aggiungere, inserisco la riga precedente. 
            if p_c > peso: 
                 matrice[riga+1][peso] = matrice[riga][peso]
            # vedo se posso aggiungerlo. 
            else: 
                matrice[riga+1][peso] = max(v_c+v_prec,matrice[riga][peso])
    maxa = matrice[-1][-1] 
    print("maximum = ",maxa)      
    return matrice 


oggetti = [
    
    {"v": random.randint(1,10), "w":random.randint(1,4)} for i in range(10)
   
    ]
weight = 10
r = knap(oggetti,weight)
for riga in r: 
    print(riga)