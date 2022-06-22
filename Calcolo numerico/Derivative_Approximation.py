from cmath import sin
from math import radians


def derivative(f, point,  iterations):

    m1 = 0
    m2 = 0
    d = 0
    for i in range(1,iterations):
        m1 = (f(point - 1/i) - f(point)) / (( point - 1/i) - point)
        m2 = (f(point + 1/i) - f(point)) / (( point + 1/i) - point)
        d = (m1+m2)/2
    return d




def square(x):
    return x*x
def m_sin(x):
    return sin(radians(x)) 



p = derivative(m_sin, 0, 100)
print(p)

