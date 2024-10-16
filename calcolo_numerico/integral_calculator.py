def metodo_rettangoli(f, min, max, step):
    area = 0
    i = min
    while(i<= max-step ):
        area+= f(i)*step
        i+= step
    return area

def metodo_punto_medio(f,min,max,step):
    area = 0
    i = min
    while(i<= max-step ):
        area+= ((f(i)+f(i+step))/2)*step
        i+= step
    return area

def metodo_trapezi(f, min, max, step):
    area = 0
    i = min
    while(i<= max-step ):
        area+= (f(i) + f(i+step))*step/2
        i+= step
    return area

def metodo_simspon(f, min,max,step):
    sum = 0 
    i = 0
    while(i<= (max-min)/step ):
        coeff = 0
        if(i == 0 or i == (max-min)/step ):
             coeff = 1
        elif( i%2 == 0):
            coeff = 2
        elif(i%2 == 1 ):
            coeff = 4
        sum += coeff*f(min + i*step)
        i+= 1
    return sum*step/3
        




def quadrato(x):
    return x*x

area_parabola = metodo_rettangoli(quadrato, -1, 1, 0.1)
print(area_parabola)
area_parabola = metodo_trapezi(quadrato, -1, 1, 0.1)
print(area_parabola)
area_parabola = metodo_punto_medio(quadrato, -1, 1, 0.1)
print(area_parabola)
area_parabola = metodo_simspon(quadrato, -1, 1, 0.1)
print(area_parabola)