from cmath import sin
from math import radians


def derivative(f, point, iterations):
    # coefficiente angolare della retta passante per il punto noto e uno alla sua sinistra vicino
    m1 = 0
    # stessa cosa ma a destra
    m2 = 0
    d = 0
    
    i = 1/iterations
    
    m1 = (f(point - 1/i) - f(point)) / (( point - 1/i) - point)
    m2 = (f(point + 1/i) - f(point)) / (( point + 1/i) - point)
    d = (m1+m2)/2
    return d




def square(x):
    return x*x
def m_sin(x):
    return sin(radians(x)) 



p = derivative(square, 0, 100)
print(p)

