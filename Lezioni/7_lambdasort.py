items = [
    {"id":9, "n":8},
    {"id":4, "n":18},
    {"id":3, "n":0},
    {"id":1, "n":12},
    {"id":2, "n":100},
    
]
def getk(a):
    return a["id"] 
items.sort(key= getk)
#versione lambda
items.sort(key = lambda d: d["id"])
print(items)
#sort modifica la lista, #sorted ritorna una nuova lista