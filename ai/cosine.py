def cosine(v1,v2):
    m1 = 0
    for dim in v1: 
        m1+=(dim**2)
    
    m1 = sqrt(m1)
    
    m2 = 0
    for dim in v2: 
        m2+=(dim**2)
    
    m2 = sqrt(m2)
    
    den = m1*m2
    num = 0 
    for i in range(0,min(len(v1), len(v2))):
        num += v1[i]*v2[i]
    return num/den
