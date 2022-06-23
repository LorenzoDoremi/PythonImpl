# a = angolo espresso in gradi
a = 45
m = a/(90-a)
# x = valore x in cui la lunghezza della retta di coefficiente m è 1 : interseca la circonferenza unitaria)
x = 1 / ((a/(90-a))**2 + 1)**0.5
sin = m*x
cos = x


print(sin)
print(cos)
