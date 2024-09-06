def eq(x):
    return x**2



def integ(f,x0,xn,p):
    s = 0 
  
    while(x0 < xn):
        s+= (f(x0)+f(x0+p))*p/2
        x0+=p

    return s 



print(integ(eq,0,5,0.01))