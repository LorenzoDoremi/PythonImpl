def bullseye(m): 
   
    j = 0 
    while j < len(m)/2:
        for k in range(j,len(m)-j):
            m[j][k] = "X"
            m[k][j] = "X" 
            m[len(m)-1-j][k] = "X"  
            m[k][len(m)-1-j] = "X"
        j+=2  
         
m = [[" " for i in range(3)] for j in range(3)]
bullseye(m)
for riga in m: 
    print(riga)   