
def funzione(x):
    return x**3 - 3*x**2 + 5


def zero_bisection(f,init,fin,it):
    middle = (fin+init)/2
    if f(middle) == 0 or it == 0: 
        return middle
    elif f(middle)*f(init) < 0:
        return zero_bisection(f,init,middle,it-1)
    else: 
        return zero_bisection(f,middle,fin,it-1)  
    

def corde(f,init,fin,it):
    m = (f(fin)-f(init))/(fin-init)
    n_p = init+abs(f(init)/m) 
    if f(n_p) == 0 or it == 0: 
        return n_p 
    else: 
        return corde(f,n_p,fin,it-1)




print(zero_bisection(funzione,-10,10,30))
print(corde(funzione,-10,10,30))