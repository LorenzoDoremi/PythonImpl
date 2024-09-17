import matplotlib.pyplot as plt
from random import random

import numpy


y = [3*i + (random()-0.5)*10 for i in range(0,10)]
x = [i for i in range(0,10)]

sNum = 0 
sDen = 0

mean_x = numpy.mean(x)
mean_y = numpy.mean(y)
for (i,xi) in enumerate(x):
    sNum += (xi - mean_x)*(y[i]- mean_y)
    sDen += (xi-mean_x)**2

pendenza = sNum/sDen
intercetta = mean_y - pendenza*mean_x

regr = [pendenza*i + intercetta for i in range(0,10)]


# Create a simple line plot

plt.scatter(x,y)
plt.plot(x,regr)

# Add labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Simple Line Plot")

# Show plot with legend
plt.legend()
plt.grid(True)
plt.show()
