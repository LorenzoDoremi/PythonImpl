def metodo_rettangoli(f, min, max, step):
    area = 0
    i = min
    while(i<= max-step ):
        area+= f(i)*step
        i+= step
    return area

def metodo_trapezi(f, min, max, step):
    area = 0
    i = min
    while(i<= max-step ):
        area+= (f(i) + f(i+step))*step/2
        i+= step
    return area




def quadrato(x):
    return x*x

area_parabola = metodo_rettangoli(quadrato, -1, 1, 0.1)
print(area_parabola)
area_parabola = metodo_trapezi(quadrato, -1, 1, 0.1)
print(area_parabola)