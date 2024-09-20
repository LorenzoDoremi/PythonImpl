# concetto di alias. il ciclo forEach (for x in y) genera alias
a = [i for i in range(0,10)]
for el in a: 
    el = 0
print(a)