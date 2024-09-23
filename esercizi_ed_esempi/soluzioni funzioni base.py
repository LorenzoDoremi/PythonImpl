from math import sqrt 
#4
def cuboabs(a):
    cubo = a**3
    if(cubo<0):
        return cubo*-1
    else:
        return cubo

#5
def is_floating(a):
    b = int(a)
    if a==b:
        return False
    else:
        return True
#6 
def media_intera(a,b):
      return int((a+b)/2)
#7
def decina_maggiore(a):
     #se ad esempio a = 67, b = 6
     b = int(a/10) 
     return b*10 + 10 
#8 
def check(n1,n2,n3):
    return n1 > n2 and n1 > n3
#9
def continuer(a):
    if(a < 0 ):
        return a-1
    else: 
        return a+1
#10 
def distanza_punti(x,y,x2,y2):
    ''' per avere sqrt
    bisogna, all'inizio del programma, include 
    o  from numpy import sqrt 
    oppure from math import sqrt '''
    distanza = sqrt((x-x2)**2 + (y-y2)**2)
    return distanza  
#11 
def somma(a,b,c):
    if(a+b == c):
        return True
    else: 
        return False
     