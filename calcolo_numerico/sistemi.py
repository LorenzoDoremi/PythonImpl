




import numpy


# 2x - 1 = 4
# x - 3  = 9

#metodo delle matrici
sistema = [
    [2,-1],
    [1,3],
]
b =  [4,9]
sol  = numpy.linalg.inv(sistema).dot(b)

print(sol)
#metodo di Cramer

det = numpy.linalg.det(sistema)
det_x = 0
det_y = 0

print(det)

# sostituisco la x ([0]) con il valore di B [0]
sistx = numpy.copy(sistema)
for i in range(0, len(sistema)):
    sistx[i][0] = b[i]

# sostituisco la y ([1]) con il valore di B [1]
sisty = numpy.copy(sistema)
for i in range(0, len(sistema)):
    sisty[i][1]= b[i]

det_x = numpy.linalg.det(sistx)
det_y = numpy.linalg.det(sisty)

print(det_x)
print(det_y)
print([numpy.ceil(det_x/det),numpy.ceil(det_y/det)])    


# metodo di gauss 

sist = [
    [4,-2,1],
    [-2,4,-2],
    [1,-2,4]
]
sol_gauss = [11,-16,17]


def gauss(sist,sol): 


    ""


