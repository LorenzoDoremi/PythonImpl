# utilizziamo i set per sviluppare un software in grado di consigliarci canzoni.
# partiamo dal definire una canzone come un dizionario/JSON
canzone_test = {
    "titolo": "Them Bones",
    "artista": "Alice in Chains",
    "generi": ["grunge","rock","alternative rock", "heavy metal"]
}
# creiamo un semplice dataset. 
canzoni = [
    {"titolo": "Blinding Lights", "artista": "The Weeknd", "generi": ["pop", "synthwave", "r&b"]},
    {"titolo": "Bohemian Rhapsody", "artista": "Queen", "generi": ["rock", "progressive rock"]},
    {"titolo": "Shape of You", "artista": "Ed Sheeran", "generi": ["pop", "dancehall"]},
    {"titolo": "Smells Like Teen Spirit", "artista": "Nirvana", "generi": ["grunge", "rock"]},
    {"titolo": "Rolling in the Deep", "artista": "Adele", "generi": ["pop", "soul"]},
    {"titolo": "Take On Me", "artista": "A-ha", "generi": ["synthpop", "new wave"]},
    {"titolo": "Yesterday", "artista": "The Beatles", "generi": ["pop", "rock", "ballad"]},
    {"titolo": "Bad Guy", "artista": "Billie Eilish", "generi": ["pop", "electropop"]},
    {"titolo": "Enter Sandman", "artista": "Metallica", "generi": ["metal", "heavy metal"]},
    {"titolo": "Levitating", "artista": "Dua Lipa", "generi": ["pop", "dance-pop"]},
    {"titolo": "HUMBLE.", "artista": "Kendrick Lamar", "generi": ["hip-hop", "rap"]},
    {"titolo": "Viva La Vida", "artista": "Coldplay", "generi": ["rock", "alternative rock", "pop"]},
    {"titolo": "Hips Don't Lie", "artista": "Shakira", "generi": ["reggaeton", "latin pop"]},
    {"titolo": "Highway to Hell", "artista": "AC/DC", "generi": ["rock", "hard rock"]},
    {"titolo": "Gangnam Style", "artista": "PSY", "generi": ["k-pop", "dance-pop"]},
    {"titolo": "One Dance", "artista": "Drake", "generi": ["dancehall", "afrobeat"]},
    {"titolo": "Sweet Child O' Mine", "artista": "Guns N' Roses", "generi": ["rock", "hard rock"]},
    {"titolo": "Born to Die", "artista": "Lana Del Rey", "generi": ["indie pop", "baroque pop"]},
    {"titolo": "Toxic", "artista": "Britney Spears", "generi": ["pop", "dance-pop"]},
    {"titolo": "Dance Monkey", "artista": "Tones and I", "generi": ["pop", "electropop"]},
]
# ora cerchiamo di calcolare quanto queste canzoni sono simili alla nostra. 
# useremo l'indice di Jaccard
# intersezione / unione degli insiemi dei generi musicali. 
# lista delle canzoni/indice: 
recommend = []
for canzone in canzoni:
    # unisco l'insieme dei generi della canzone test e di quella che sto valutando
    unione = set(canzone["generi"]) | set(canzone_test["generi"])
    # intersezione
    intersezione = set(canzone["generi"]) & set(canzone_test["generi"])
    # calcolo l'indice
    indice = len(intersezione)/len(unione)
    
    recommend.append({"canzone": canzone, "indice": indice})
# le canzoni sono in disordine, dobbiamo ordinarle.
# uso la chiave "indice" come chiave per il sorting dei dizionari
# reverse = ordino dalla similarità maggiore
recommend.sort(key= lambda d: d["indice"], reverse=True)

# stampiamo le prime 5 canzoni più simili!
for i in range(0,5):
    temp_canzone = recommend[i]["canzone"]
    print("potrebbe piacerti ",temp_canzone["titolo"]," di ", temp_canzone["artista"])