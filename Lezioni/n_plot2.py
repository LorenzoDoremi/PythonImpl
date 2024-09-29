import matplotlib.pyplot as plt 

figure, plots = plt.subplots(2,2)
x = [i  for i in range(0,10)]
y = [xi**2 for xi in x]
z = [xi**3 - 4*xi**2 for xi in x]
plots[0][0].plot(x,y,label="linear")
plots[0][1].plot(x,z)
plt.show()