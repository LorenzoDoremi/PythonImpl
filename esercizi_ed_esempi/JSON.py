import urllib.request, json 

#Python 3
data = []
with urllib.request.urlopen("http://klinkart.altervista.org/datajson.php") as url:
    data = json.loads(url.read().decode())

autori = []
opere_per_autore = []


#questo algoritmo suddivide le opere per autore
for artwork in data:

    # nuovo autore? creo un nuovo spazio
    if artwork["autore"] not in autori:
        autori.append(artwork["autore"])
        newset = {"autore": artwork["autore"], "lista_opere": []}
        newset["lista_opere"].append(artwork)
        opere_per_autore.append(newset)
    else: 
    # cerco l'elemento che lo ha
     for dict_autore in opere_per_autore:
        if dict_autore["autore"] == artwork["autore"]:
          dict_autore["lista_opere"].append(artwork)
        

#stampa gli autori di nome Lorenzo e quante opere hanno fatto 
for autore in opere_per_autore:
    if "Lorenzo" in autore["autore"]:
        print(autore["autore"])
        print(len(autore["lista_opere"]))




soluzioni_equazione = [];
with urllib.request.urlopen("https://simplechat-doremi.herokuapp.com/2grade?coeff=[1,-2,-2]") as url:
    soluzioni_equazione = json.loads(url.read().decode())
print(soluzioni_equazione)