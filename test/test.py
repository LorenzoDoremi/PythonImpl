'''
Es 5
'''

def brb(n,e):
    if(e<0):
        return 1/n**-e
    else:
        return n**e
    
def brb(n,e):
    sol = n**e 
    if(e < 0 ):
        return 1/sol
    return sol 

iwd = brb(4,2)
print(iwd)