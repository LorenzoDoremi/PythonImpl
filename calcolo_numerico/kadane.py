import math
def kadane(v):
    inizio = 0 
    fine = 0
    
    curr_sum = 0 
    max_sum = -math.inf
    for i in range(len(v)):
        if v[i] > curr_sum + v[i]:
            curr_sum = v[i]
            inizio = i 
        else: 
            curr_sum += v[i]
            
        if curr_sum > max_sum: 
            max_sum = curr_sum
            fine = i 
    return (inizio,fine,max_sum)


vettore = [5, -7, 3, 4]
print(kadane(vettore))
            
                