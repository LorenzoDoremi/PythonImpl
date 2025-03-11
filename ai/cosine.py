from math import sqrt
# calcola il coseno dell'angolo tra due vettori. 
# https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5_q29OPOH_BF8cuWWzYpwISyt92FDXioSEA&s
def cosine(v1,v2):
    
    # calcolo il denominatore della frazione
    m1 = 0
    # dim = dimensione. valore nel vettore...
    for dim in v1: 
        m1+=(dim**2)
    # (1+2+1+...)^2
    m1 = sqrt(m1)
    
    m2 = 0
    for dim in v2: 
        m2+=(dim**2)
    # (1+2+1+...)^2
    m2 = sqrt(m2)
    
    den = m1*m2
    # calcolo il numeratore. 
    num = 0 
    for i in range(0,min(len(v1), len(v2))):
        num += v1[i]*v2[i]
    return num/den
